import nfc
import os
import time
import gspread
from oauth2client.service_account import ServiceAccountCredentials
from datetime import datetime

# Google Sheets setup
scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
creds = ServiceAccountCredentials.from_json_keyfile_name("credentials.json", scope)
client = gspread.authorize(creds)
sheet = client.open("Employee Logging Sheet").worksheet("Log")
employee_sheet = client.open("Employee Logging Sheet").worksheet("Employees")

# Keep track of last scanned UID and action
last_uid = None
last_action = None
cooldown = 5  # seconds

# Audio file paths – user can replace these with their actual .mp3 files
checkin_audio = "/home/pi/Employee-NFC-Logging-Time-Sheet/audio/checkin/Checkedin.mp3"     # 🔁 Replace this with your actual check-in audio path
checkout_audio = "/home/pi/Employee-NFC-Logging-Time-Sheet/audio/checkout/Checkedout.mp3"  # 🔁 Replace this with your actual check-out audio path
error_audio = "/home/pi/Employee-NFC-Logging-Time-Sheet/audio/error/error.mp3"             # 🔁 Replace this with your actual error audio path

def play_audio(file_path):
    os.system(f"mpg123 '{file_path}'")

def get_employee_name(uid):
    try:
        records = employee_sheet.get_all_records()
        for row in records:
            if str(row['UID']) == uid:
                return row['Employee Name']
        return None
    except Exception as e:
        print(f"Failed to fetch employee name: {e}")
        return None

def log_to_sheet(uid, name, action):
    try:
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        sheet.append_row([timestamp, uid, name, action])
    except Exception as e:
        print(f"Failed to log to sheet: {e}")
        play_audio(error_audio)

def on_connect(tag):
    global last_uid, last_action

    uid = str(tag.identifier.hex().upper())
    current_time = time.time()

    # Avoid duplicate scans
    if uid == last_uid and (current_time - last_action) < cooldown:
        return True

    name = get_employee_name(uid)
    if not name:
        print(f"Unregistered UID: {uid}")
        play_audio(error_audio)
        return True

    # Toggle action: check in/out
    action = "Check-in" if last_action != "Check-in" else "Check-out"
    print(f"{action} - {name} ({uid})")
    log_to_sheet(uid, name, action)

    # Play appropriate audio
    if action == "Check-in":
        play_audio(checkin_audio)
    else:
        play_audio(checkout_audio)

    # Update state
    last_uid = uid
    last_action = action
    last_action_time = current_time
    return True

def main():
    print("NFC Logger started. Tap a card to begin...")
    clf = nfc.ContactlessFrontend('usb')
    while True:
        try:
            clf.connect(rdwr={'on-connect': on_connect})
        except Exception as e:
            print(f"Error reading tag: {e}")
            play_audio(error_audio)

if __name__ == "__main__":
    main()
