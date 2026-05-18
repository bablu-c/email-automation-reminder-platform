import smtplib
from email.message import EmailMessage
from src.config import *
from src.logger import logger

def send_email(to_email, subject, body):

    if DRY_RUN:
        print(f"[DRY RUN] Email to {to_email}")
        logger.info(f"DRY RUN email to {to_email}")
        return "DRY_RUN"

    try:
        msg = EmailMessage()
        msg["Subject"] = subject
        msg["From"] = EMAIL_ADDRESS
        msg["To"] = to_email
        msg.set_content(body)

        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls()
            server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
            server.send_message(msg)

        logger.info(f"Email sent to {to_email}")
        return "SENT"

    except Exception as e:
        logger.error(f"Failed to send email: {e}")
        return "FAILED"