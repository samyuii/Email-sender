import smtplib, ssl

port = 465  # For SSL
smtp_server = "smtp.gmail.com"
sender_email = "jainsamyak170@gmail.com"  # Enter your address
receiver_email = input("Enter receiver Email: ")  # Enter receiver address
password = "gkon xpwm dcjz gsiu"  # Replace this with the actual password for sender_email
message = input("Write mail here: ")
Subject: input("Write subject here: ")

# This message is sent from Python.
# IM SAMYAK

context = ssl.create_default_context()

with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_email, message, subject)