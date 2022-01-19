import smtplib
import datetime as dt
import random

my_email = "hutao77D@gmail.com"
my_password = "Amaan@180501"


now = dt.datetime.now()
weekday = now.weekday()
if weekday == 0:
    with open("quotes.txt") as quote_file:
        all_quotes = quote_file.readlines()
        quote = random.choice(all_quotes)

    with smtplib.SMTP("smtp.gmail.com") as connection:
                connection.starttls()
                connection.login(user=my_email, password=my_password)
                connection.sendmail(from_addr=my_email,
                                    to_addrs=my_email,
                                    msg=f"Subject:MONDAY MOTIVATION!!!\n\n{quote}")
