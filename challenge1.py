from smtplib import SMTP
from datetime import datetime
from random import choice

# replace the credentials below with authentic credentials
SENDERS_EMAIL="senders_email"
SENDERS_PASSWORD="senders password"
RECIEVERS_EMAIL="recievers email"

day_of_week=datetime.now().weekday()
print(day_of_week)

if day_of_week==0:
    with open('quotes.txt', mode='r', encoding='utf-8') as quotes_file:
        all_quote=quotes_file.readlines()
        quote=choice(all_quote)
    print(quote)
    with SMTP('smtp.gmail.com', port=587) as connection:
        connection.starttls()
        connection.login(user=SENDERS_EMAIL, password=SENDERS_PASSWORD)
        connection.sendmail(from_addr=SENDERS_EMAIL, to_addrs=RECIEVERS_EMAIL, msg=f"subject: good morning\n\n{quote}")

