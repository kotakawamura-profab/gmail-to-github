from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build
from email import message_from_bytes
import base64
from datetime import datetime
import os
import json


def save_markdown(subject, body):
    today = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    filename = f"gmail_{today}.md"
    filepath = os.path.join("gmail", filename)

    os.makedirs("gmail", exist_ok=True)

    with open(filepath, "w") as f:
        f.write(f"# {subject}\n\n")
        f.write(body)


def main():
    creds = Credentials.from_authorized_user_info(json.loads(open("token.json").read()))
    
    service = build("gmail", "v1", credentials=creds)
    results = service.users().messages().list(userId="me", maxResults=1).execute()
    messages = results.get("messages", [])

    if not messages:
        print("No messages found.")
        return

    msg_id = messages[0]["id"]
    msg = service.users().messages().get(userId="me", id=msg_id, format="raw").execute()

    raw_msg = base64.urlsafe_b64decode(msg["raw"])
    parsed = message_from_bytes(raw_msg)

    subject = parsed["Subject"] or "No Subject"
    body = parsed.get_payload()

    save_markdown(subject, body)
    print(f"Saved: {subject}")


if __name__ == "__main__":
    main()