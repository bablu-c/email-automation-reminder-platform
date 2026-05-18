import pandas as pd
from datetime import datetime
from src.email_sender import send_email
from src.report_generator import generate_report

contacts = pd.read_csv("data/contacts.csv")
reminders = pd.read_csv("data/reminders.csv")

with open("templates/reminder_template.txt", "r") as file:
    template = file.read()

report_data = []

for index, row in reminders.iterrows():

    contact = contacts[contacts["name"] == row["name"]]

    if contact.empty:
        continue

    email = contact.iloc[0]["email"]

    message = template.format(
        name=row["name"],
        reminder_type=row["reminder_type"],
        date=row["date"]
    )

    subject = f"{row['reminder_type']}"

    status = send_email(
        email,
        subject,
        message
    )

    report_data.append({
        "name": row["name"],
        "email": email,
        "reminder_type": row["reminder_type"],
        "status": status,
        "timestamp": datetime.now()
    })

generate_report(report_data)

print("Automation Completed.")