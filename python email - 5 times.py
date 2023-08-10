import smtplib
import ssl
import time

def send_email(subject, message, sender_email, receiver_email, password):
    port = 465  # For SSL
    smtp_server = "smtp.gmail.com"

    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, message)

def main():
    sender_email = "jainsamyak170@gmail.com"
    receiver_email = "nikitasharma907918@gmail.com"
    password = "rjtr dejn drrl ggfp"
    subject = "Hi there"
    message = "Test mail"

    for _ in range(5):
        send_email(subject, message, sender_email, receiver_email, password)
        print("Email sent.")
        time.sleep(5)  # Sleep for 5 seconds

if __name__ == "__main__":
    main()
