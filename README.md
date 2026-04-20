# 📢 University Notice Bot

A simple automation tool that monitors the university notice page and sends an email when a new notice is published.

---

## 🚀 Overview

This bot automatically checks:
https://fas.wyb.ac.lk/notices/

Every few minutes, it:
- Fetches the latest notice 🌐  
- Compares with previous data 🧠  
- Sends an email if a new notice is detected 📧  

---

## 🎯 Purpose

Manually checking the website is inefficient.  
This project automates the process to ensure no important notice is missed.

---

## ⚙️ Tech Stack

- Python 🐍  
- BeautifulSoup (Web Scraping)  
- SMTP (Email Notifications)  
- GitHub Actions (Automation)

---

## ⏱️ Automation

Runs automatically using GitHub Actions:

```yaml
cron: "*/3 * * * *"