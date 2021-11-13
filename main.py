import smtplib
import datetime as dt
import random

my_email = "annakowalska2823@gmail.com"
password = "Habababa123!@#"

with open("quotes.txt", "r") as quotes_file:
    quotes = quotes_file.readlines()


random_quote = random.choice(quotes)

now = dt.datetime.now()

if now.weekday() == 5:
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs="annakowalska2526@yahoo.com",
            msg=random_quote)








