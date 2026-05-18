# Email Automation & Reminder Platform

## Overview

Email Automation & Reminder Platform is a Python-based automation system that helps users schedule and send automated emails, reminders, and notifications using FastAPI, SQLite, SMTP, and CSV datasets.

This project simulates a real-world automation workflow used by startups, HR teams, educators, operations teams, and support teams for handling repetitive communication tasks efficiently.

---

# Features

* Automated email reminders
* FastAPI backend APIs
* SQLite database integration
* SMTP email sending
* Personalized email templates
* CSV contact management
* Reminder scheduling
* Logging system
* CSV report generation
* Dry-run testing mode
* Swagger API documentation
* Modular project structure

---

# Tech Stack

| Category              | Technology    |
| --------------------- | ------------- |
| Language              | Python        |
| Backend               | FastAPI       |
| Database              | SQLite        |
| Email Service         | SMTP          |
| Data Handling         | Pandas        |
| Scheduling            | APScheduler   |
| API Testing           | Swagger UI    |
| Environment Variables | python-dotenv |

---

# Project Architecture

```text
Dashboard / API
        ↓
FastAPI Backend
        ↓
Scheduler Engine
        ↓
SMTP Email Sender
        ↓
SQLite Database
        ↓
Reports & Logs
```

---

# Folder Structure

```text
Email-Automation-Reminder-System/
│
├── api/
├── database/
├── dashboard/
├── data/
├── templates/
├── src/
├── outputs/
├── logs/
├── docs/
├── tests/
├── images/
├── .env.example
├── requirements.txt
├── README.md
└── main.py
```

---

# Installation

## Clone Repository

```bash
git clone https://github.com/yourusername/email-automation-reminder-platform.git
```

---

## Create Virtual Environment

### Windows

```bash
python -m venv venv
venv\Scripts\activate
```

### Mac/Linux

```bash
python3 -m venv venv
source venv/bin/activate
```

---

# Install Dependencies

```bash
pip install -r requirements.txt
```

---

# Environment Variables

Create `.env` file:

```env
EMAIL_ADDRESS=your_email@gmail.com
EMAIL_PASSWORD=your_app_password
SMTP_SERVER=smtp.gmail.com
SMTP_PORT=587
DRY_RUN=True
```

---

# Run Main Automation System

```bash
python main.py
```

---

# Run FastAPI Server

```bash
uvicorn api.app:app --reload
```

---

# Open Swagger API Docs

```text
http://127.0.0.1:8000/docs
```

---

# API Endpoints

| Method | Endpoint      | Description   |
| ------ | ------------- | ------------- |
| GET    | /             | Home Route    |
| POST   | /add-contact  | Add Contact   |
| GET    | /contacts     | Get Contacts  |
| POST   | /add-reminder | Add Reminder  |
| GET    | /reminders    | Get Reminders |

---

# Sample Contact JSON

```json
{
  "name": "Rahul",
  "email": "rahul@example.com"
}
```

---

# Sample Reminder JSON

```json
{
  "name": "Rahul",
  "email": "rahul@example.com",
  "reminder_type": "Meeting Reminder",
  "reminder_date": "2026-05-20"
}
```

---

# Sample Terminal Output

```text
[DRY RUN] Email to rahul@example.com
[DRY RUN] Email to priya@example.com

Report generated successfully.
Automation Completed.
```

---

# Generated Outputs

* email_report.csv
* app.log
* reminder reports
* API responses

---

# Security Notes

* Never upload `.env`
* Never upload real passwords
* Use `.env.example`
* Use fake emails for demo/testing

---

# Learning Outcomes

This project helped in learning:

* Python automation
* FastAPI backend development
* SMTP integration
* SQLite database handling
* REST API development
* Logging systems
* CSV processing
* Scheduling workflows
* Backend architecture design

---

# Future Improvements

* Streamlit Dashboard
* Next.js Frontend
* Redis Queue
* Celery Workers
* Email Analytics
* Docker Deployment
* SendGrid Integration

---

# Author

Bablu kumar

---

# License

This project is created for educational and portfolio purposes.
