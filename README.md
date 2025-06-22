# 🎓 Student Registration System

A desktop application built with Python’s Tkinter GUI and MySQL backend to manage student data, exams, and results.

---

⚙️ Features

- Secure login integration with MySQL users table  
- Add student, exam, and result entries  
- View student results in a tabular format  
- Visually appealing UI with background images (login & dashboard)

---

## Tech Stack

| Layer        | Technology                          |
|-------------|-------------------------------------|
| Backend     | `mysql-connector-python`           |
| GUI         | `Tkinter`, `ttk` widgets, `PIL` (Image) |
| Database    | MySQL (`student_results` schema)   |

---

## 🔧 Installation & Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/DivyaBarnwal21/student-registration-system.git
   cd student-registration-system


2. Install required Python Packages:
   
   pip install mysql-connector-python Pillow

   
3. setup MySql Database:
   
   CREATE DATABASE student_results;
   
   CREATE TABLE users(username VARCHAR(50), password VARCHAR(50));
   
   CREATE TABLE students(...);
   
   CREATE TABLE exams(...);
   
   CREATE TABLE results(...);
   
5. Update backend.py db_config with your MySQL credentials:

   db_config = {
  'host': '127.0.0.1',
  'user': 'root',
  'password': 'Divya.21',
  'database': 'student_results'
}

6. Ensure images bg.jpeg and dashboard.jpg are in the project folder.

# Usage:

  Launch the application:
  
  python main.py


- Login with valid credentials stored in users table.

- After login, access Management or View Results pages.

- Use the Management tab to add students, exams, and results.

- Use View Results to fetch and display student exam records.


# Screenshots:
1.Login Page:
  ![image](https://github.com/user-attachments/assets/953347bd-a415-4ece-b79e-3b0f8afe3d30)
2.Dashboard:
  ![image](https://github.com/user-attachments/assets/f17d2743-cf63-4eba-95be-ed54e1ecf837)
3.Student Page:
  ![image](https://github.com/user-attachments/assets/26f85422-e8bc-41b0-a697-7b746f9deac7)
4.Exam Page:
  ![image](https://github.com/user-attachments/assets/cdcf9d10-327e-4e37-9747-d019da89a6f4)
5.Mark Information Page:
  ![image](https://github.com/user-attachments/assets/3ea987ea-3158-4e71-b2a3-ba71a9772a19)
6.Result Page:
  ![image](https://github.com/user-attachments/assets/f192c724-16fe-4c65-b4ef-efc131a20f45)



# How It Works
backend.py:

- Uses mysql.connector.connect(**db_config) to connect 

- Contains functions to verify login, add students/exams/results, and retrieve results.

main.py (or GUI script):

- Creates multi-page UI: login, dashboard, management, and view results.

- Uses tkinter.Label, tk.Entry, ttk.Notebook, ttk.Treeview, messagebox—standard Tkinter widgets .

- Uses PIL.ImageTk for background image handling.

# Notes & Tips:
- Store passwords securely in production (use hashing and salting).

- Use parameterized queries (%s) to prevent SQL injection.

- Add error handling around database operations for robustness.

# License
  This project is licensed under the MIT License.

# Contact
  Created by Divya Barnwal
  
  Contact:db8123@srmist.edu.in








  










