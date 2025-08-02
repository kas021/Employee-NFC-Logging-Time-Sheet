# Employee NFC Logging Time Sheet

An ACR122U card reader and Raspberry Pi are used in this straightforward Python-based NFC attendance system.  Employees can tap their cards to check in and out, and the information is subsequently logged into a shared Google Sheet.  Each scan is accompanied by audio feedback to let the user know it was successful.

---

## 🧰 What You’ll Need

- Raspberry Pi (any model with internet access)
- ACR122U NFC Reader
- Blank NFC cards/tags
- External speaker (optional but recommended)
- Google account (for Google Sheets access)
- Python 3 installed on the Pi
- Internet connection (for syncing logs)

---

## 🔧 Initial Setup

### 1. Clone This Repo

```bash
git clone https://github.com/your-username/Employee-NFC-Logging-Time-Sheet.git
cd Employee-NFC-Logging-Time-Sheet


