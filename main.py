import requests
from bs4 import BeautifulSoup
import smtplib
import os
from email.mime.text import MIMEText

# URLS 
NOTICE_URL = "https://fas.wyb.ac.lk/notices/"
RESULTS_URL = "https://fas.wyb.ac.lk/results/"

# Email config
SENDER = os.getenv("SENDER_EMAIL")
PASSWORD = os.getenv("EMAIL_PASSWORD")

emails = os.getenv("RECEIVER_EMAILS", "")
RECEIVERS = [e.strip() for e in emails.split(",") if e.strip()]

# Storage files
NOTICE_FILE = "last_notice.txt"
RESULTS_FILE = "last_results.txt"

# Clean text
def clean(text):
    return " ".join(text.split())

# Send email
def send_email(subject, message):
    if not RECEIVERS:
        print("No receivers configured")
        return

    if not SENDER or not PASSWORD:
        print("Email credentials not set")
        return

    msg = MIMEText(message, "plain", "utf-8")
    msg["Subject"] = subject
    msg["From"] = SENDER
    msg["To"] = ", ".join(RECEIVERS)

    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(SENDER, PASSWORD)

    server.sendmail(SENDER, RECEIVERS, msg.as_string())
    server.quit()

# Check notices
def check_notices():
    try:
        response = requests.get(NOTICE_URL, timeout=10)
        soup = BeautifulSoup(response.text, "html.parser")

        tag = soup.find("h3")
        if not tag:
            print("Page structure changed or no notice found!")
            return

        notice = clean(tag.text)

        if os.path.exists(NOTICE_FILE):
            with open(NOTICE_FILE, "r") as f:
                last_notice = clean(f.read())
        else:
            last_notice = ""

        if notice != last_notice:
            print("New Notice:", notice)
            send_email(
                "New University Notice",
                f"{notice}\n\nCheck here: {NOTICE_URL}"
            )

            with open(NOTICE_FILE, "w") as f:
                f.write(notice)
        else:
            print("No new notice")

    except Exception as e:
        print("Error checking notices:", e)
        
# Check results
def check_results():
    try:
        response = requests.get(RESULTS_URL, timeout=10)
        soup = BeautifulSoup(response.text, "html.parser")

        results = []
        for tag in soup.find_all("h3"):
            text = clean(tag.text)
            if text:
                results.append(text)

        new_results = set(results)

        if os.path.exists(RESULTS_FILE):
            with open(RESULTS_FILE, "r") as f:
                old_results = set(clean(line) for line in f.read().splitlines())
        else:
            old_results = set()

        diff = new_results - old_results

        if diff:
            for r in diff:
                print("New Result:", r)
                send_email(
                    "New Exam Result Published",
                    f"{r}\n\nCheck here: {RESULTS_URL}"
                )

            with open(RESULTS_FILE, "w") as f:
                f.write("\n".join(new_results))
        else:
            print("No new results")

    except Exception as e:
        print("Error checking results:", e)

# Main runner
def main():
    print("Running bot...")
    check_notices()
    check_results()


if __name__ == "__main__":
    main()
