import email
import os
from dotenv import load_dotenv
import smtplib, ssl
import imghdr
from email.message import EmailMessage

load_dotenv()

password = os.getenv('EMAIL_PASSWORD')
email_sender = "strickland.wang@gmail.com"
email_receiver = "strickland.wang@gmail.com"

load_dotenv()

def send_email(image_path):
    print("send_email function started")
    email_message = EmailMessage()
    email_message["Subject"] = "New customer showed up!"
    email_message.set_content("Hey, we just saw a new customer!")

    with open(image_path, "rb") as file:
        content = file.read()
    email_message.add_attachment(content, maintype="image", subtype=imghdr.what(None, content))

    gmail = smtplib.SMTP("smtp.gmail.com", 587)
    gmail.ehlo()
    gmail.starttls()
    gmail.login(email_sender, password)
    gmail.sendmail(email_sender, email_receiver, email_message.as_string())
    gmail.quit()
    print("send_email function ended")

if __name__ == "__main__":
    send_email(image_path="images/image.png")
