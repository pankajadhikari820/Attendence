import firebase_admin
from firebase_admin import credentials, db
import pandas as pd

# Initialize Firebase Admin
cred = credentials.Certificate("serviceAccountKey.json")  # Download from Firebase > Project Settings > Service Accounts
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://attendence-system-b6eb9-default-rtdb.firebaseio.com/'
})

def export_data():
    ref_users = db.reference('users')
    ref_attendance = db.reference('attendance')

    users_data = ref_users.get()
    attendance_data = ref_attendance.get()

    # Users data
    if users_data:
        df_users = pd.DataFrame(users_data).T
        df_users.to_excel('users_data.xlsx', index=False)
        print("✅ users_data.xlsx exported!")

    # Attendance data
    if attendance_data:
        records = []
        for user, dates in attendance_data.items():
            for date, info in dates.items():
                records.append({
                    'UserID': user,
                    'Date': info.get('date', ''),
                    'Time': info.get('time', '')
                })
        df_att = pd.DataFrame(records)
        df_att.to_excel('attendance_data.xlsx', index=False)
        print("✅ attendance_data.xlsx exported!")

if __name__ == "__main__":
    export_data()
