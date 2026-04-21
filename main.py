import requests
from bs4 import BeautifulSoup
import smtplib
import os
from email.mime.text import MIMEText

URL = "https://fas.wyb.ac.lk/notices/"

SENDER = os.getenv("SENDER_EMAIL")
PASSWORD = os.getenv("EMAIL_PASSWORD")

emails = os.getenv("RECEIVER_EMAILS", "")
RECEIVERS = [e.strip() for e in emails.split(",") if e.strip()]

CACHE_FILE = "last_notice.txt"

def clean(text):
    return " ".join(text.split())

# Load last notice
if os.path.exists(CACHE_FILE):
    with open(CACHE_FILE, "r") as f:
        last_notice = clean(f.read())
else:
    last_notice = ""

def send_email(message):
    msg = MIMEText(message, "plain", "utf-8")
    msg["Subject"] = "New University Notice"
    msg["From"] = SENDER
    msg["To"] = ", ".join(RECEIVERS)

    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(SENDER, PASSWORD)

    server.sendmail(SENDER, RECEIVERS, msg.as_string())
    server.quit()

response = requests.get(URL, timeout=10)
soup = BeautifulSoup(response.text, "html.parser")

tag = soup.find("h3")
if not tag:
    print("No notice found")
    exit()

notice = clean(tag.text)

if notice != last_notice:
    print("🔥 New Notice:", notice)
    send_email(notice)

    with open(CACHE_FILE, "w") as f:
        f.write(notice)
else:
    print("No new notice")
