import smtplib 
from account import *
from email.message import EmailMessage
import datetime
from project import *

msg = EmailMessage()
today_date = str(datetime.date.today())
msg["Subject"] = today_date + " Carpe Diem!"
msg["From"] = EMAIL_ADDRESS
msg["To"] = "ysy011600@gmail.com"
msg.set_content(scrape_weather() + "\n" + scrape_news() + "\n" + scrape_quotes())


with smtplib.SMTP("smtp.gmail.com", 587) as smtp:
  # Connection Check
  smtp.ehlo() 
  # Encoding
  smtp.starttls()
  # Login
  smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
  
  smtp.send_message(msg)