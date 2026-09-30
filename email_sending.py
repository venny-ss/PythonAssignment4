import smtplib
from email.message import EmailMessage

sender_email = "your_email@gmail.com"
receiver_email = "receiver@gmail.com"
app_password = "your_app_password"

message = EmailMessage()

message["Subject"] = "Test Email"
message["From"] = sender_email
message["To"] = receiver_email

message.set_content("Hello! This email was sent using Python.")

with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
    smtp.login(sender_email, app_password)
    smtp.send_message(message)

print("Email sent successfully!")