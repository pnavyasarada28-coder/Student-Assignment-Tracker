# Student-Assignment-Tracker
A Flask-based Student Assignment Tracker using SQLAlchemy that allows users to add, track, and manage assignment submissions with deadline tracking and status updates.

# 📚 Student Assignment Tracker

## 🔹 Description

This is a Flask-based web application designed to help students manage their assignments efficiently. The system allows users to add assignments, track pending tasks, mark them as completed, and view submitted assignments.

The application uses SQLAlchemy Core for database interaction and follows a structured backend approach.

---

## 🔹 Features

* Add new assignments with title, subject, description, and due date
* View all pending assignments
* Mark assignments as submitted
* View completed assignments separately
* Simple and clean UI using HTML templates

---

## 🔹 Technologies Used

* Python
* Flask (Web Framework)
* SQLAlchemy Core (Database handling)
* SQLite
* HTML, CSS

---

## 🔹 Database Design

Table: `tasks_asgmt`

Fields:

* assignment_id (Primary Key)
* title
* subject
* descr (Description)
* due_date
* is_submitted (Boolean)
* submitted_at (Auto updated timestamp)

---

## 🔹 Project Structure

stud_asgmt_tracker/
│── app.py
│── conn_pool.py
│── templates/
│── static/
│── .gitignore
│── README.md

---

## 🔹 How It Works

1. User adds an assignment
2. Data is stored in the database using SQLAlchemy
3. Pending assignments are displayed
4. User can mark assignments as completed
5. Completed assignments are moved to a separate view

---

## 🔹 How to Run the Project

1. Clone the repository

2. Navigate to project folder:
   cd stud_asgmt_tracker

3. Create virtual environment:
   python -m venv .venv

4. Activate virtual environment:
   .venv\Scripts\activate

5. Install dependencies:
   pip install flask sqlalchemy

6. Run the application:
   python app.py

7. Open browser:
   http://127.0.0.1:5000/

---

## 🔹 Future Enhancements

* User authentication (login/signup)
* Assignment reminders & notifications
* Priority-based task sorting
* REST API integration
* Deployment on cloud (Render/Heroku)

---

## 🔹 Author

Panyam Navya Sarada
