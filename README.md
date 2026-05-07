# Automated-Bulk-Email-Sender-with-Templates
## Project Overview

This project is a Python-based Bulk Email Sender that allows users to send personalized emails to multiple recipients automatically using templates.

The system supports:
- Bulk email sending
- Email templates
- Personalization
- CSV/JSON contact loading
- Email history tracking
- Error handling
- Retry mechanism

---

# Features

## Email Sending
- Send emails using SMTP
- Secure login with Gmail App Password

## Bulk Sending
- Send emails to multiple recipients automatically

## Templates
- Reusable email templates
- Dynamic placeholders:
  - `{name}`
  - `{company}`

## Personalization
Example:
```text
Hello Ali, welcome to HK Academy!
```

## Contact Loading
Supports:
- CSV files
- JSON files

## Email History
Stores:
- Recipient email
- Subject
- Status
- Timestamp

## Error Handling
Handles:
- Invalid files
- Connection errors
- Missing templates
- SMTP issues

## Retry Mechanism
Automatically retries failed emails.

---

# Project Structure

```text
bulk_email_sender/
│
├── main.py
├── email_sender.py
├── contact_loader.py
├── template_manager.py
├── history_manager.py
│
└── data/
    ├── contacts.csv
    ├── contacts.json
    ├── templates.json
    ├── history.json
```

---

# Requirements

Install Python 3.x

Check version:
```bash
python --version
```

---

# How to Run

Open terminal inside project folder:

```bash
python main.py
```

---

# Gmail SMTP Setup

This project uses Gmail SMTP.

## Important:
You MUST use a Gmail App Password.

### Steps:
1. Enable 2-Step Verification
2. Go to Google Account Settings
3. Open:
   Security → App Passwords
4. Generate App Password
5. Use that password in program

 Do NOT use your normal Gmail password.

---

# Sample CSV Format

## contacts.csv

```csv
name,email,company
Ali,ali@example.com,HK Academy
Sara,sara@example.com,TechSoft
```

---

# Sample JSON Format

## contacts.json

```json
[
  {
    "name": "Ali",
    "email": "ali@example.com",
    "company": "HK Academy"
  },
  {
    "name": "Sara",
    "email": "sara@example.com",
    "company": "TechSoft"
  }
]
```

---

# Sample Templates

## templates.json

```json
{
  "welcome": "Hello {name}, welcome to {company}!",
  "offer": "Hi {name}, we have an exclusive offer for {company}."
}
```

---

# Program Workflow

1. Load Contacts
2. Show Templates
3. Choose Template
4. Send Bulk Emails
5. View History

---

# Deliverables

- Source Code
- README.md
- contacts.csv
- templates.json
- history.json
- GitHub Repository

---

# Technologies Used

- Python
- JSON
- CSV

---

# HUNZALLA AJAB

Automated Bulk Email Sender Project
