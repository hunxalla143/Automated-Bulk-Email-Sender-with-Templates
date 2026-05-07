from email_sender import send_email
from contact_loader import load_csv, load_json
from template_manager import load_templates, render_template
from history_manager import save_history, view_history

contacts = []
templates = {}
selected_template = None


def menu():
    print("\n==== Bulk Email Sender ====")
    print("1. Load Contacts")
    print("2. Show Templates")
    print("3. Choose Template")
    print("4. Send Bulk Emails")
    print("5. View History")
    print("6. Exit")


def load_contacts():
    global contacts

    file_type = input("Load CSV or JSON? (csv/json): ").lower()

    if file_type == "csv":
        try:
            contacts = load_csv("data/contacts.csv")
            print(f" {len(contacts)} contacts loaded from CSV.")
        except Exception as e:
            print(" Error loading CSV:", e)

    elif file_type == "json":
        try:
            contacts = load_json("data/contacts.json")
            print(f" {len(contacts)} contacts loaded from JSON.")
        except FileNotFoundError:
            print(" contacts.json file not found in data folder!")
        except Exception as e:
            print(" Error loading JSON:", e)

    else:
        print(" Invalid choice! Type 'csv' or 'json'.")


def show_templates():
    global templates

    templates = load_templates()

    if not templates:
        print(" No templates found!")
        return

    print("\n Available Templates:")
    for key in templates:
        print(f"- {key}")


def choose_template():
    global selected_template, templates

    if not templates:
        templates = load_templates()

    template_name = input("Enter template name: ")

    if template_name in templates:
        selected_template = templates[template_name]
        print(" Template selected.")
    else:
        print(" Template not found!")


def send_bulk_emails():
    global contacts, selected_template

    if not contacts:
        print(" Load contacts first!")
        return

    if not selected_template:
        print(" Choose template first!")
        return

    sender = input("Enter your email: ")
    password = input("Enter app password: ")
    subject = input("Enter subject: ")

    print("\n Sending emails...\n")

    for contact in contacts:
        try:
            message = render_template(selected_template, contact)

            success, status = send_email(
                sender,
                password,
                contact['email'],
                subject,
                message
            )

            save_history(contact['email'], subject, status)

            print(f"{contact['email']}  {status}")

        except Exception as e:
            print(f"{contact.get('email', 'Unknown')}  Error: {e}")


def main():
    while True:
        menu()
        choice = input("Select option: ")

        if choice == '1':
            load_contacts()

        elif choice == '2':
            show_templates()

        elif choice == '3':
            choose_template()

        elif choice == '4':
            send_bulk_emails()

        elif choice == '5':
            view_history()

        elif choice == '6':
            print(" Exiting program...")
            break

        else:
            print(" Invalid option! Try again.")


if __name__ == "__main__":
    main()