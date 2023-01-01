--Identify the crime

SELECT description
FROM crime_scene_reports
WHERE year = 2021
AND month = 7
AND day = 28
AND street = 'Humphrey Street';

-- Not the duck! This warrants a full scale cyber investigation immediately!!

--Check the transcripts of the interviews about the crime.

SELECT name, transcript
FROM interviews
WHERE day = '28'
AND month = '7'
AND year = '2021';

--Filter the data to only show bakery-related crime reports.

SELECT name, transcript
FROM interviews
WHERE year = 2021
AND month = 7
AND day = 28
AND transcript LIKE '%bakery%'
ORDER BY name;

--Eugene, Raymond, Ruth have testimony.

--Eugene says thief withdrew money from ATM on Leggett Street earlier this morning.

--Raymond says thief called someone while leaving the scene. For less than a minute, Raymond heard the thief say that
--"they were planning to take the earliest flight out of Fiftyville tomorrow", and that "they asked the person on the
--line to buy a ticket."

--Ruth says the thief left the bakery in a car within 10 minutes.

--Start following Eugene's lead regarding the ATM on Leggett Street, gathering details about the ATM withdrawal records first

SELECT account_number, amount
FROM atm_transactions
WHERE year = 2021
AND month = 7
AND day = 28
AND atm_location = 'Leggett Street'
AND transaction_type = 'withdraw';

--Find the account holder names from the ATM transactions via asking the bank, providing the account_number from the ATM.

SELECT name, atm_transactions.amount, atm_transactions.account_number
FROM people
JOIN bank_accounts ON people.id = bank_accounts.person_id
JOIN atm_transactions ON bank_accounts.account_number = atm_transactions.account_number
WHERE atm_transactions.year = 2021
AND atm_transactions.month = 7
AND atm_transactions.day = 28
AND atm_transactions.atm_location = 'Leggett Street'
AND atm_transactions.transaction_type = 'withdraw';

--Update Suspect list based on above results:

--Bruce, Diana, Brooke, Kenny, Iman, Luca, Taylor, Benista, and technically Eugene, Raymond, Ruth as well.

--Follow Raymond's lead by finding all airports

SELECT abbreviation, full_name, city
FROM airports
WHERE city = 'Fiftyville';

---There's only one... HA, plebians.

--Find all the flights on the 29th and order them by time

SELECT flights.id, full_name, city, flights.hour, flights.minute
FROM airports
JOIN flights ON airports.id = flights.destination_airport_id
WHERE flights.origin_airport_id = (
    SELECT id
    FROM airports
    WHERE city = 'Fiftyville'
)
AND flights.year = 2021
AND flights.month = 7
AND flights.day = 29
ORDER BY flights.hour, flights.minute;

--Investigate flight ID 36, the first flight out on the 29th, 8:20 AM
--List the passengers by their passport_number

SELECT passengers.flight_id, name, passengers.passport_number, passengers.seat
FROM people
JOIN passengers ON people.passport_number = passengers.passport_number
JOIN flights ON passengers.flight_id = flights.id
WHERE flights.year = 2021
AND flights.month = 7
AND flights.day = 29
AND flights.hour = 8
AND flights.minute = 20
ORDER BY passengers.passport_number;

--Suspect list based on all above criteria: Taylor, Bruce, Luca, Kenny

--Time to investigate the call records for the 28th
SELECT name, phone_calls.duration
FROM people
JOIN phone_calls ON people.phone_number = phone_calls.caller
WHERE phone_calls.year = 2021
AND phone_calls.month = 7
AND phone_calls.day = 28
AND phone_calls.duration <= 60
ORDER BY phone_calls.duration;

--Suspect list based on all above criteria: Taylor, Bruce, Kenny
--Investigate the calls received

SELECT name, phone_calls.duration
FROM people
JOIN phone_calls ON people.phone_number = phone_calls.receiver
WHERE phone_calls.year = 2021
AND phone_calls.month = 7
AND phone_calls.day = 28
AND phone_calls.duration <= 60
ORDER BY phone_calls.duration;

--Suspects for accomplice: Larry, Jacquelin, James, Robin, Phillip, Melissa, Jack, Anna, Doris, Luca

--Use the last clue, from Ruth, to decide to list the exits from the bakery between 10:15AM and 10:25AM

SELECT name, bakery_security_logs.hour, bakery_security_logs.minute
FROM people
JOIN bakery_security_logs ON people.license_plate = bakery_security_logs.license_plate
WHERE bakery_security_logs.year = 2021
AND bakery_security_logs.month = 7
AND bakery_security_logs.day = 28
AND bakery_security_logs.activity = 'exit'
AND bakery_security_logs.minute >= 15
AND bakery_security_logs.minute <= 25
ORDER BY bakery_security_logs.minute;

--List of suspects: Bruce is the only potential suspect left, everyone else has failed to satisfy all 3 major clues' criteria.
--Find Bruce's Phone number

SELECT phone_number FROM people
WHERE name = 'Bruce'
LIMIT 1;

-- Bruce: (367) 555-5533

--Who did Bruce talk to on that date?

SELECT receiver, duration FROM phone_calls
WHERE caller = '(367) 555-5533'
AND year = 2021
AND month = 7
AND day = 28;

--There is only one call less than a minute that day, and it was to (375)-555-8161.
--Look up who '(375) 555-8161' is.

SELECT name FROM people
WHERE phone_number = '(375) 555-8161';

-- It's Robin. They are so busted.

--The Ducknapper himself: Bruce
--Destination where he escaped to: New York City
--His partner in crime: Robin

--Thanks for playing!