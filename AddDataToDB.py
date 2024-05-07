import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

cred = credentials.Certificate("serviceAcKEY.json")
firebase_admin.initialize_app(cred,{
    'databaseURL':"https://faceattendancesystem-705bc-default-rtdb.firebaseio.com/"
})

ref = db.reference('Students')

data = {
    "321654":
        {
            "name": "Aman",
            "major": "Computer Science",
            "starting_year": 2020,
            "total_attendance": 8,
            "grade": "G",
            "year": 4,
            "last_attendance_time": "2023-10-15 00:54:34"
        },
    "742971":
        {
            "name": "Abhiraj Anand",
            "major": "Computer Science",
            "starting_year": 2020,
            "total_attendance": 12,
            "grade": "E",
            "year": 4,
            "last_attendance_time": "2023-10-15 00:54:34"
        },
    "852741":
        {
            "name": "Mam",
            "major": "Economics",
            "starting_year": 2021,
            "total_attendance": 14,
            "grade": "B",
            "year": 1,
            "last_attendance_time": "2023-10-15 00:54:34"
        },
    "853621":
        {
            "name": "Priyanka Chopra",
            "major": "Physics",
            "starting_year": 2020,
            "total_attendance": 7,
            "grade": "G",
            "year": 2,
            "last_attendance_time": "2023-10-15 00:54:34"
        },
    "951205":
        {
            "name": "Rajnikant",
            "major": "Physics",
            "starting_year": 2018,
            "total_attendance": 12,
            "grade": "H",
            "year": 3,
            "last_attendance_time": "2023-10-15 00:54:34"
        },
    "963852":
        {
            "name": "Elon Musk",
            "major": "Physics",
            "starting_year": 2023,
            "total_attendance": 10,
            "grade": "F",
            "year": 1,
            "last_attendance_time": "2023-10-15 00:54:34"
        }
}

for key, value in data.items():
    ref.child(key).set(value)