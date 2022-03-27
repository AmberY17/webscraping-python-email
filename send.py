import smtplib 
from account import *

with smtplib.SMTP("smtp.gmail.com", 587) as smtp:
  # Connection Check
  smtp.ehlo() 
  # Encoding
  smtp.starttls()
  # Login
  smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)

  subject = "Email Subject"
  body = "Email Body"
  msg = f"Subject: {subject}\n{body}"
  
  smtp.sendmail(EMAIL_ADDRESS, "ysy011600@gmail.com", msg)