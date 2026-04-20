import requests
from bs4 import BeautifulSoup
import smtplib
import os

URL = "https://fas.wyb.ac.lk/notices/"

SENDER = os.getenv("SENDER_EMAIL")
PASSWORD = os.getenv("EMAIL_PASSWORD")

RECEIVERS = [
    "lahirumadhushan566@gmail.com"
]

# Load last notice
try:
    with open("last_notice.txt", "r") as f:
        last_notice = f.read().strip()
except:
    last_notice = ""

def send_email(message):
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(SENDER, PASSWORD)

    subject = "📢 New University Notice!"
    msg = f"Subject: {subject}\n\n{message}"

    for r in RECEIVERS:
        server.sendmail(SENDER, r, msg)

    server.quit()

response = requests.get(URL, timeout=10)
soup = BeautifulSoup(response.text, "html.parser")

notice = soup.find("h3").text.strip()

if notice != last_notice:
    print("🔥 New Notice:", notice)
    send_email(notice)

    with open("last_notice.txt", "w") as f:
        f.write(notice)
else:
    print("No new notice")
