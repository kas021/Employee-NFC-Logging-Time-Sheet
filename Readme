# Employee NFC Logging Time Sheet

An ACR122U card reader and Raspberry Pi are used in this straightforward Python-based NFC attendance system.  Employees can tap their cards to check in and out, and the information is subsequently logged into a shared Google Sheet.  Each scan is accompanied by audio feedback to let the user know it was successful.

---------------------------

## 🧰 What You’ll Need

- Raspberry Pi (any model with internet access)
- ACR122U NFC Reader
- Blank NFC cards/tags
- External speaker (optional but recommended)
- Google account (for Google Sheets access)
- Python 3 installed on the Pi
- Internet connection (for syncing logs)

---------------------------

## 🔧 Initial Setup

### 1. Clone This Repo

```bash
git clone https://github.com/your-username/Employee-NFC-Logging-Time-Sheet.git
cd Employee-NFC-Logging-Time-Sheet

---------------------------
Install the required packages:

sudo apt update
sudo apt install python3-pip libnfc-bin mpg123
pip3 install gspread oauth2client

---------------------------

Start the NFC reader service (also useful to enable it permanently):

sudo systemctl enable pcscd
sudo systemctl start pcscd

---------------------------
Setting Up Google Sheets Integration:

Go to Google Developers Console (https://console.developers.google.com/).
Create a new project.
Enable both Google Sheets API and Google Drive API for that project.
Under the “Credentials” section, create a Service Account Key and choose the JSON format.
Download the JSON file and place it inside your project folder.
Rename it to: credentials.json
Share your Google Sheet with the email from the client_email field inside that JSON file.

---------------------------
Folder Structure (make sure this is exactly right):

Employee-NFC-Logging-Time-Sheet/
├── audio/
│ ├── checkin/ → contains Checkedin.mp3
│ ├── checkout/ → contains Checkedout.mp3
│ └── error/ → contains error.mp3
├── main.py
├── credentials.json

You can change the audio files, but the names and folder structure must match exactly.
---------------------------
Running the Program:

To start the NFC logger: python3 main.py
The system will:

Wait for card scan
Log check-in or check-out based on previous activity
Play a sound to confirm action
Print UID, employee name, action, and timestamp in the terminal
Send the log to your Google Sheet
---------------------------

Troubleshooting:
If you get No such file or directory, check your MP3 paths and names.
If the sheet doesn’t update, make sure you’ve shared it properly with the correct service account email.
To test if the NFC reader is working, run: sudo pcsc_scan

---------------------------



