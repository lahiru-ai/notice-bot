import requests
from bs4 import BeautifulSoup
import smtplib
import os
from email.mime.text import MIMEText

URL = "https://fas.wyb.ac.lk/notices/"

SENDER = os.getenv("SENDER_EMAIL")
PASSWORD = os.getenv("EMAIL_PASSWORD")

RECEIVERS = os.getenv("RECEIVER_EMAILS").split(",")

CACHE_FILE = "last_notice.txt"

# Load last notice
if os.path.exists(CACHE_FILE):
    with open(CACHE_FILE, "r") as f:
        last_notice = f.read().strip()
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

notice = soup.find("h3").text.strip()

if notice != last_notice:
    print("🔥 New Notice:", notice)
    send_email(notice)

    with open(CACHE_FILE, "w") as f:
        f.write(notice)
else:
    print("No new notice")
