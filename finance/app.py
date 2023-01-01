import os

from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, session, url_for
from flask_session import Session
from tempfile import mkdtemp
from werkzeug.security import check_password_hash, generate_password_hash
from requests import get
from helpers import apology, login_required, lookup, usd

# Configure application
app = Flask(__name__)

# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True

# Custom filter
app.jinja_env.filters["usd"] = usd

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///finance.db")

# Make sure API key is set
if not os.environ.get("API_KEY"):
    raise RuntimeError("API_KEY not set")


@app.after_request
def after_request(response):
    """Ensure responses aren't cached"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response


@app.route("/")
@login_required
def index():
    # User must be logged in to access this route
    if session.get("user_id") is None:
        return redirect("/login")

    # Get portfolio data from database
    rows = db.execute(
        "SELECT symbol, SUM(shares) as total_shares, price FROM transactions WHERE user_id = :user_id GROUP BY symbol HAVING SUM(shares) > 0",
        user_id=session["user_id"],
    )
    portfolio = []
    for row in rows:
        quote = lookup(row["symbol"])
        portfolio.append({
            "symbol": quote["symbol"],
            "name": quote["name"],
            "total_shares": row["total_shares"],
            "price": usd(quote["price"]),
            "value": usd(row["total_shares"] * quote["price"]),
        })

    # Get user's cash balance from database
    rows = db.execute("SELECT cash FROM users WHERE id = :user_id", user_id=session["user_id"])
    if not rows:
        return apology("user's cash balance not found", 400)
    cash = usd(rows[0]["cash"])

    # Render template
    return render_template("index.html", portfolio=portfolio, cash=cash)


@app.route("/buy", methods=["GET", "POST"])
@login_required
def buy():
    # User must be logged in to access this route
    if session.get("user_id") is None:
        return redirect("/login")

    if request.method == "POST":
        # Get symbol and shares from form
        symbol = request.form.get("symbol").upper()
        shares = request.form.get("shares")

        # Validate input
        if not symbol:
            return apology("must provide symbol", 400)
        if not shares:
            return apology("must provide shares", 400)
        if not shares.isdigit():
            return apology("shares must be a positive integer", 400)
        shares = int(shares)
        if shares <= 0:
            return apology("shares must be a positive integer", 400)

        # Look up quote data from IEX
        quote = lookup(symbol)
        if quote is None:
            return apology("invalid symbol", 400)

        # Calculate total cost of purchase
        cost = quote["price"] * shares

        # Check if user has sufficient funds
        rows = db.execute(
            "SELECT cash FROM users WHERE id = :user_id", user_id=session["user_id"]
        )
        cash = rows[0]["cash"]
        if cost > cash:
            return apology("not enough funds", 400)

        # Update user's cash balance and add transaction to database
        db.execute(
            "UPDATE users SET cash = cash - :cost WHERE id = :user_id",
            cost=cost,
            user_id=session["user_id"],
        )
        db.execute(
            "INSERT INTO transactions (user_id, symbol, shares, price) VALUES (:user_id, :symbol, :shares, :price)",
            user_id=session["user_id"],
            symbol=symbol,
            shares=shares,
            price=quote["price"],
        )

        # Redirect to homepage
        return redirect("/")

    else:
        return render_template("buy.html")


@app.route("/history", methods=["GET", "POST"])
@login_required
def history():
    if request.method == "POST":
        # Get symbol and shares from form
        symbol = request.form.get("symbol")
        shares = request.form.get("shares")

        # Convert symbol to uppercase
        symbol = symbol.upper()

        # Insert new transaction into the transactions table
        db.execute(
            "INSERT INTO transactions (user_id, symbol, shares, price) VALUES (:user_id, :symbol, :shares, :price)",
            user_id=session["user_id"],
            symbol=symbol,
            shares=shares,
            price=quote["price"],
        )

    # Query database for transactions made by the current user
    transactions = db.execute("SELECT * FROM transactions WHERE user_id = :user_id", user_id=session["user_id"])

    # Render the history template, passing in the transactions data
    return render_template("history.html", transactions=transactions)


@app.route("/login", methods=["GET", "POST"])
def login():
    """Log user in"""

    # Forget any user_id
    session.clear()

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":

        # Ensure username was submitted
        if not request.form.get("username"):
            return apology("must provide username", 403)

        # Ensure password was submitted
        elif not request.form.get("password"):
            return apology("must provide password", 403)

        # Query database for username
        rows = db.execute("SELECT * FROM users WHERE username = ?", request.form.get("username"))

        # Ensure username exists and password is correct
        if len(rows) != 1 or not check_password_hash(rows[0]["hash"], request.form.get("password")):
            return apology("invalid username and/or password", 403)

        # Remember which user has logged in
        session["user_id"] = rows[0]["id"]

        # Redirect user to home page
        return redirect("/")

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("login.html")


@app.route("/logout")
def logout():
    """Log user out"""

    # Forget any user_id
    session.clear()

    # Redirect user to login form
    return redirect("/")


@app.route("/quote", methods=["GET", "POST"])
@login_required
def quote():
    if request.method == "POST":
        # Get symbol from form
        symbol = request.form.get("symbol")

        # Validate input
        if not symbol:
            return apology("must provide symbol", 400)

        # Look up quote data from IEX
        quote = lookup(symbol)

        if quote is None:
            return apology("invalid symbol", 400)

        # Render quoted template
        return render_template("quoted.html", quote=quote)

    else:
        return render_template("quote.html")


@app.route("/register", methods=["GET", "POST"])
def register():
    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":
        # Get form data
        username = request.form.get("username")
        password = request.form.get("password")
        confirmation = request.form.get("confirmation")

        # Validate form data
        if not username:
            return apology("must provide username", 400)
        elif not password:
            return apology("must provide password", 400)
        elif password != confirmation:
            return apology("passwords must match", 400)

        # Check if user already exists in database
        rows = db.execute("SELECT * FROM users WHERE username = :username", username=username)
        if len(rows) > 0:
            return apology("username already exists", 400)

        # Hash password
        hash = generate_password_hash(password)

        # Insert new user into database
        db.execute("INSERT INTO users (username, hash) VALUES (:username, :hash)", username=username, hash=hash)

        # Redirect user to login page
        return redirect("/login")

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("register.html")


@app.route("/sell", methods=["GET", "POST"])
@login_required
def sell():
    if request.method == "POST":
        # Query database for symbols that the user owns
        rows = db.execute(
            "SELECT symbol FROM transactions WHERE user_id = :user_id GROUP BY symbol HAVING SUM(shares) > 0", user_id=session["user_id"])

        # Create a list of symbols
        symbols = [row["symbol"] for row in rows]

        # Get symbol and shares from form
        symbol = request.form.get("symbol")
        shares = request.form.get("shares")

        # Validate input
        if not symbol:
            return apology("must provide symbol", 400)
        if symbol not in symbols:
            return apology("you do not own any shares of this stock", 400)
        if not shares:
            return apology("must provide shares", 400)
        if not shares.isdigit():
            return apology("shares must be a positive integer", 400)
        shares = int(shares)
        if shares <= 0:
            return apology("shares must be a positive integer", 400)

        # Look up quote data from IEX
        try:
            quote = lookup(symbol)
        except ValueError:
            return apology("invalid symbol", 400)
        price = quote["price"]

        # Check if user owns enough shares to sell
        rows = db.execute(
            "SELECT SUM(shares) AS total_shares FROM transactions WHERE user_id = :user_id AND symbol = :symbol",
            user_id=session["user_id"],
            symbol=symbol,
        )

        # Check if there are any results returned
        if not rows:
            return apology("you do not own any shares of this stock", 400)

        total_shares = rows[0]["total_shares"]
        if total_shares is None:
            total_shares = 0
        if total_shares < shares:
            return apology("not enough shares", 400)

        # Calculate sale price and update user's cash balance
        sale_price = shares * price
        db.execute("UPDATE users SET cash = cash + :sale_price WHERE id = :user_id",
                   sale_price=sale_price, user_id=session["user_id"])

        # Add transaction to database
        db.execute("INSERT INTO transactions (user_id, symbol, shares, price) VALUES (:user_id, UPPER(:symbol), :shares, :price)",
                   user_id=session["user_id"],
                   symbol=symbol,
                   shares=-shares,
                   price=price
                   )

        # Redirect to homepage
        return redirect("/")
    else:
        # Query database for symbols that the user owns
        rows = db.execute(
            "SELECT symbol FROM transactions WHERE user_id = :user_id GROUP BY symbol HAVING SUM(shares) > 0", user_id=session["user_id"])

        # Create a list of symbols
        symbols = [row["symbol"] for row in rows]

        # Render the sell template, passing in the symbols data
        return render_template("sell.html", symbols=symbols)


@app.route("/add_cash", methods=["GET", "POST"])
@login_required
def add_cash():
    # User must be logged in to access this route
    if session.get("user_id") is None:
        return redirect("/login")

    if request.method == "POST":
        # Get amount to add from form
        amount = request.form.get("amount")

        # Validate input
        if not amount:
            return apology("must provide amount", 400)
        if not amount.isdigit():
            return apology("amount must be a positive integer", 400)
        amount = int(amount)
        if amount <= 0:
            return apology("amount must be a positive integer", 400)

        # Update user's cash balance
        db.execute("UPDATE users SET cash = cash + :amount WHERE id = :user_id", amount=amount, user_id=session["user_id"])

        # Redirect to homepage
        return redirect("/")

    else:
        return render_template("add_cash.html")