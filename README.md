# 📢 University Notice & Results Bot

An automated system that monitors university notice and results pages and sends email notifications when new updates are published — eliminating the need for manual checking.

---

## 🚀 Overview

Students often miss important announcements and exam results because checking the university website regularly is inconvenient.

This bot continuously monitors:

- https://fas.wyb.ac.lk/notices/ 📢  
- https://fas.wyb.ac.lk/results/ 🎓  

and sends email alerts whenever new content appears.

---

## ⚙️ How It Works

1. Fetches the latest data from the website 🌐  
2. Extracts notices and results  
3. Compares with previously stored data 🧠  
4. Detects new updates  
5. Sends email notifications 📧  
6. Stores the latest state to prevent duplicates  

---

## ⏱️ Automation

- Runs automatically using **GitHub Actions**
- Triggered every few minutes using cron scheduling
- Can be enhanced with external triggers for higher reliability

```yaml
cron: "*/5 * * * *"
