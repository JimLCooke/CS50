import os

from cs50 import SQL
from flask import Flask, flash, jsonify, redirect, render_template, request, session

# Configure application
app = Flask(__name__)

# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///birthdays.db")


@app.after_request
def after_request(response):
    """Ensure responses aren't cached"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        if "delete" in request.form:
            # Delete the entry from the database
            db.execute("DELETE FROM birthdays WHERE id = :id", id=request.form.get("delete"))
        elif "edit" in request.form:
            # Update the entry in the database
            db.execute("UPDATE birthdays SET name = :name, month = :month, day = :day WHERE id = :id", id=request.form.get("edit"), name=request.form.get("name"), month=request.form.get("month"), day=request.form.get("day"))
        else:
            # Insert the user's entry into the database
            db.execute("INSERT INTO birthdays (name, month, day) VALUES (:name, :month, :day)", name=request.form.get("name"), month=request.form.get("month"), day=request.form.get("day"))

        return redirect("/")

    else:
        # Retrieve the entries from the database
        entries = db.execute("SELECT * FROM birthdays")

        # Render the index.html template and pass the entries to the template
        return render_template("index.html", entries=entries)


if __name__ == "__main__":
    app.run()