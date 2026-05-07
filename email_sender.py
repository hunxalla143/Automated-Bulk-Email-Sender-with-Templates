import smtplib
from email.mime.text import MIMEText

def send_email(sender, password, recipient, subject, message):
    try:
        msg = MIMEText(message)
        msg['Subject'] = subject
        msg['From'] = sender
        msg['To'] = recipient

        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server:
            server.login(sender, password)
            server.send_message(msg)

        return True, "Sent"

    except Exception as e:
        return False, str(e)