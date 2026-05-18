from fastapi import FastAPI
from pydantic import BaseModel, EmailStr
from datetime import datetime
import sqlite3
import uuid

app = FastAPI(
    title="Email Automation API",
    version="1.0"
)

# ==============================
# DATABASE CONNECTION
# ==============================

conn = sqlite3.connect(
    "database/email_system.db",
    check_same_thread=False
)

cursor = conn.cursor()

# ==============================
# CREATE TABLES
# ==============================

cursor.execute("""
CREATE TABLE IF NOT EXISTS contacts (
    id TEXT PRIMARY KEY,
    name TEXT,
    email TEXT
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS reminders (
    id TEXT PRIMARY KEY,
    name TEXT,
    email TEXT,
    reminder_type TEXT,
    reminder_date TEXT
)
""")

conn.commit()

# ==============================
# PYDANTIC MODELS
# ==============================

class Contact(BaseModel):
    name: str
    email: EmailStr

class Reminder(BaseModel):
    name: str
    email: EmailStr
    reminder_type: str
    reminder_date: str

# ==============================
# HOME ROUTE
# ==============================

@app.get("/")
def home():
    return {
        "message": "Email Automation API Running"
    }

# ==============================
# CREATE CONTACT
# ==============================

@app.post("/add-contact")
def add_contact(contact: Contact):

    contact_id = str(uuid.uuid4())

    cursor.execute("""
    INSERT INTO contacts
    VALUES (?, ?, ?)
    """, (
        contact_id,
        contact.name,
        contact.email
    ))

    conn.commit()

    return {
        "message": "Contact Added",
        "id": contact_id
    }

# ==============================
# GET CONTACTS
# ==============================

@app.get("/contacts")
def get_contacts():

    cursor.execute("""
    SELECT * FROM contacts
    """)

    data = cursor.fetchall()

    return {
        "contacts": data
    }

# ==============================
# CREATE REMINDER
# ==============================

@app.post("/add-reminder")
def add_reminder(reminder: Reminder):

    reminder_id = str(uuid.uuid4())

    cursor.execute("""
    INSERT INTO reminders
    VALUES (?, ?, ?, ?, ?)
    """, (
        reminder_id,
        reminder.name,
        reminder.email,
        reminder.reminder_type,
        reminder.reminder_date
    ))

    conn.commit()

    return {
        "message": "Reminder Added",
        "id": reminder_id
    }

# ==============================
# GET REMINDERS
# ==============================

@app.get("/reminders")
def get_reminders():

    cursor.execute("""
    SELECT * FROM reminders
    """)

    data = cursor.fetchall()

    return {
        "reminders": data
    }