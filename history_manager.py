import json
from datetime import datetime

HISTORY_FILE = 'data/history.json'


def save_history(email, subject, status):
    record = {
        "email": email,
        "subject": subject,
        "status": status,
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }

    try:
        with open(HISTORY_FILE, 'r', encoding='utf-8') as f:
            history = json.load(f)
    except:
        history = []

    history.append(record)

    with open(HISTORY_FILE, 'w', encoding='utf-8') as f:
        json.dump(history, f, indent=4)


def view_history():
    try:
        with open(HISTORY_FILE, encoding='utf-8') as f:
            history = json.load(f)

            if not history:
                print("No history found.")
                return

            print("\n==== Email History ====")
            for h in history:
                print(f"{h['timestamp']} | {h['email']} | {h['status']}")

    except:
        print("No history file found.")