# 📢 University Notice Bot

An automated system that monitors the university notice page and sends email notifications when new notices are published — removing the need for manual checking.

---

## 🚀 Overview

Students often miss important notices because checking the university website regularly is inconvenient.

This project solves that problem by automatically monitoring:

https://fas.wyb.ac.lk/notices/

and sending alerts whenever a new notice appears.

---

## ⚙️ How It Works

1. Fetches the latest notice from the website 🌐  
2. Extracts and reads the notice content  
3. Compares it with the previously stored notice 🧠  
4. If a new notice is detected:
   - Sends email notifications 📧  
5. Updates stored data to prevent duplicate alerts  

---

## ⏱️ Automation System

The system runs automatically using:

- GitHub Actions (execution environment)  
- External cron trigger (for reliable scheduling)  

```yaml
cron: "*/3 * * * *"
