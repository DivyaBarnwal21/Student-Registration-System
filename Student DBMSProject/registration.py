import tkinter as tk
from tkinter import ttk, messagebox
from PIL import Image, ImageTk
import backend  # This connects to backend.py

def set_background(window, image_path):
    image = Image.open(image_path)
    image = image.resize((window.winfo_screenwidth(), window.winfo_screenheight()), Image.LANCZOS)
    bg_image = ImageTk.PhotoImage(image)
    bg_label = tk.Label(window, image=bg_image)
    bg_label.image = bg_image
    bg_label.place(relwidth=1, relheight=1)

class LoginPage:
    def __init__(self, root):
        self.root = root
        self.root.title("Login - Student Result System")
        self.root.geometry(f"{self.root.winfo_screenwidth()}x{self.root.winfo_screenheight()}")

        left_frame = tk.Frame(root, width=self.root.winfo_screenwidth() // 2, height=self.root.winfo_screenheight())
        left_frame.pack(side="left", fill="both", expand=False)

        image = Image.open("bg.jpeg")
        image = image.resize((self.root.winfo_screenwidth() // 2, self.root.winfo_screenheight()), Image.LANCZOS)
        self.bg_image = ImageTk.PhotoImage(image)

        bg_label = tk.Label(left_frame, image=self.bg_image)
        bg_label.place(relwidth=1, relheight=1)

        right_frame = tk.Frame(root, width=self.root.winfo_screenwidth() // 2, height=self.root.winfo_screenheight(), bg="white")
        right_frame.pack(side="right", fill="both", expand=True)

        login_frame = tk.Frame(right_frame, bg="white", padx=20, pady=20)
        login_frame.place(relx=0.5, rely=0.5, anchor="center")

        tk.Label(login_frame, text="Login", font=("Arial", 22, "bold"), bg="white", fg="Red").pack(pady=16)

        tk.Label(login_frame, text="Username:", font=("Arial", 14), bg="white").pack(pady=5)
        self.username_entry = tk.Entry(login_frame, font=("Arial", 14), width=30)
        self.username_entry.pack(pady=5, ipady=7)

        tk.Label(login_frame, text="Password:", font=("Arial", 14), bg="white").pack(pady=5)
        self.password_entry = tk.Entry(login_frame, show='*', font=("Arial", 14), width=30)
        self.password_entry.pack(pady=5, ipady=7)

        tk.Button(login_frame, text="Login", font=("Arial", 14), width=15, command=self.login).pack(pady=20)

    def login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()
        if backend.verify_login(username, password):
            messagebox.showinfo("Login", "Login Successful!")
            self.root.destroy()
            open_dashboard()
        else:
            messagebox.showerror("Login Failed", "Invalid credentials.")

def open_dashboard():
    dashboard = tk.Tk()
    dashboard.title("Dashboard - Student Result System")
    screen_width = dashboard.winfo_screenwidth()
    screen_height = dashboard.winfo_screenheight()
    dashboard.geometry(f"{screen_width}x{screen_height}")

    main_frame = tk.Frame(dashboard)
    main_frame.pack(fill="both", expand=True)

    left_frame = tk.Frame(main_frame, width=screen_width // 2, height=screen_height)
    left_frame.pack(side="left", fill="both", expand=True)

    bg_image = Image.open("dashboard.jpg")
    bg_image = bg_image.resize((screen_width // 2, screen_height), Image.LANCZOS)
    bg_photo = ImageTk.PhotoImage(bg_image)
    dashboard.bg_photo = bg_photo
    bg_label = tk.Label(left_frame, image=dashboard.bg_photo)
    bg_label.place(x=0, y=0, width=screen_width // 2, height=screen_height)

    right_frame = tk.Frame(main_frame, width=screen_width // 2, height=screen_height, bg="#f5f5f5")
    right_frame.pack(side="right", fill="both", expand=True)

    content_frame = tk.Frame(right_frame, bg="#f5f5f5")
    content_frame.place(relx=0.5, rely=0.5, anchor="center")

    tk.Label(content_frame, text="Welcome to Dashboard!", font=("Arial", 24, "bold"), bg="#f5f5f5", fg="Red").pack(pady=40)

    tk.Button(content_frame, text="Manage Data", width=30, height=3, font=("Arial", 14, "bold"), command=open_management_page).pack(pady=20)
    tk.Button(content_frame, text="View Results", width=30, height=3, font=("Arial", 14, "bold"), command=open_view_results).pack(pady=20)

    dashboard.mainloop()

def open_management_page():
    mgmt = tk.Toplevel()
    mgmt.title("Management - Student Result System")
    mgmt.geometry(f"{mgmt.winfo_screenwidth()}x{mgmt.winfo_screenheight()}")
    mgmt.configure(bg="#ADD8E6")

    tab_control = ttk.Notebook(mgmt)
    student_tab = tk.Frame(tab_control, bg="#ADD8E6")
    exam_tab = tk.Frame(tab_control, bg="#ADD8E6")
    result_tab = tk.Frame(tab_control, bg="#ADD8E6")

    tab_control.add(student_tab, text="Students")
    tab_control.add(exam_tab, text="Exams")
    tab_control.add(result_tab, text="Results")
    tab_control.pack(expand=1, fill="both")

    def create_centered_form(parent, fields, button_text, callback):
        form_frame = tk.Frame(parent, bg="#ADD8E6")
        form_frame.place(relx=0.5, rely=0.4, anchor="center")

        entries = {}
        for i, field in enumerate(fields):
            tk.Label(form_frame, text=field, font=("Arial", 16, "bold"), bg="#ADD8E6").grid(row=i, column=0, padx=20, pady=10, sticky="e")
            entry = tk.Entry(form_frame, font=("Arial", 16), width=30)
            entry.grid(row=i, column=1, padx=20, pady=10, sticky="w")
            entries[field] = entry

        def handle_submit():
            try:
                values = [entry.get() for entry in entries.values()]
                callback(*values)
                messagebox.showinfo("Success", f"{button_text} successful!")
                for entry in entries.values():
                    entry.delete(0, tk.END)
            except Exception as e:
                messagebox.showerror("Error", str(e))

        tk.Button(form_frame, text=button_text, font=("Arial", 16, "bold"),
                  bg="#007ACC", fg="white", width=20, command=handle_submit).grid(row=len(fields), column=0, columnspan=2, pady=20)

    # Student Form
    create_centered_form(
        student_tab,
        ["Student ID:", "Name:", "Email:", "Address:", "Mobile No:"],
        "Add Student",
        lambda sid, name, email, addr, mobile: backend.add_student(int(sid), name, email, addr, mobile)
    )

    # Exam Form
    create_centered_form(
        exam_tab,
        ["Exam ID:", "Exam Name:", "Subject:", "Date:"],
        "Add Exam",
        lambda eid, ename, subject, date: backend.add_exam(int(eid), ename, subject, date)
    )

    # Result Form
    create_centered_form(
        result_tab,
        ["Student ID:", "Exam ID:", "Marks:"],
        "Save Result",
        lambda sid, eid, marks: backend.save_result(int(sid), int(eid), float(marks))
    )

    mgmt.mainloop()

def open_view_results():
    view_results = tk.Toplevel()
    view_results.title("View Results - Student Result System")
    view_results.geometry(f"{view_results.winfo_screenwidth()}x{view_results.winfo_screenheight()}")
    view_results.configure(bg="#ADD8E6")

    frame = tk.Frame(view_results, padx=20, pady=20, bg="#ADD8E6")
    frame.place(relx=0.5, rely=0.5, anchor="center")

    tk.Label(frame, text="Enter Student ID:", font=("Arial", 16, "bold"), bg="#ADD8E6").pack(pady=5)
    student_id_entry = tk.Entry(frame, font=("Arial", 14), width=30)
    student_id_entry.pack(pady=5)

    def view_student_result():
        student_id = student_id_entry.get()
        if not student_id.isdigit():
            messagebox.showerror("Error", "Please enter a valid Student ID")
            return
        results = backend.get_result(int(student_id))
        if not results:
            messagebox.showinfo("Result", "No results found for this student.")
            return

        result_window = tk.Toplevel(view_results)
        result_window.title("Results")
        result_window.geometry("600x400")

        tree = ttk.Treeview(result_window, columns=("Exam", "Subject", "Marks"), show="headings")
        tree.heading("Exam", text="Exam")
        tree.heading("Subject", text="Subject")
        tree.heading("Marks", text="Marks")
        tree.pack(fill="both", expand=True)

        for row in results:
            tree.insert("", "end", values=(row[1], row[2], row[3]))

    tk.Button(frame, text="View Result", font=("Arial", 16, "bold"), bg="#007ACC", fg="white",
              width=20, command=view_student_result).pack(pady=10)

    view_results.mainloop()

# ================= Run App ==================
if __name__ == "__main__":
    root = tk.Tk()
    app = LoginPage(root)
    root.mainloop()
