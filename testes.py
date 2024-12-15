# Import necessary libraries
import tkinter as tk
from tkinter import messagebox, simpledialog

# Global Variables
users = {"admin": "admin"}  # Default login credentials


def register():
    """Register function for new users"""
    new_username = simpledialog.askstring("Register", "Enter a new username:")
    if not new_username:
        messagebox.showerror("Error", "Username cannot be empty.")
        return
    elif new_username in users:
        messagebox.showerror("Error", "Username already exists.")
        return

    new_password = simpledialog.askstring("Register", "Enter a new password:")
    if not new_password:
        messagebox.showerror("Error", "Password cannot be empty.")
        return

    # Add new user to the system
    users[new_username] = new_password
    messagebox.showinfo("Success", f"Account created for username: {new_username}")


def login():
    """Login function"""
    username = username_entry.get()
    password = password_entry.get()
    if username in users and users[username] == password:
        messagebox.showinfo("Success", "Login successful!")
        login_window.destroy()
        show_menu()
    else:
        messagebox.showerror("Error", "Invalid username or password!")


def show_menu():
    """Dummy menu window for demonstration"""
    menu_window = tk.Tk()
    menu_window.title("Quiz Menu")
    tk.Label(menu_window, text="Welcome to the Quiz Menu!", font=("Helvetica", 16)).pack(pady=10)
    menu_window.mainloop()


# Login GUI
login_window = tk.Tk()
login_window.title("Login System")
login_window.configure(bg="#f5f5f5")

tk.Label(login_window, text="Welcome to Quiz System", font=("Helvetica", 16, "bold"), bg="#f5f5f5", fg="#333").grid(row=0, column=0, columnspan=2, pady=10)

tk.Label(login_window, text="Username:", font=("Arial", 12), bg="#f5f5f5").grid(row=1, column=0, padx=10, pady=5, sticky="w")
username_entry = tk.Entry(login_window, font=("Arial", 12))
username_entry.grid(row=1, column=1, padx=10, pady=5)

tk.Label(login_window, text="Password:", font=("Arial", 12), bg="#f5f5f5").grid(row=2, column=0, padx=10, pady=5, sticky="w")
password_entry = tk.Entry(login_window, show="*", font=("Arial", 12))
password_entry.grid(row=2, column=1, padx=10, pady=5)

tk.Button(login_window, text="Login", command=login, font=("Arial", 12), bg="#4caf50", fg="white", width=15).grid(row=3, column=0, columnspan=2, pady=10)

# Adding "No account? Register now" text
tk.Label(login_window, text="Belum ada akun?", font=("Arial", 10), bg="#f5f5f5", fg="#333").grid(row=4, column=0, padx=10, pady=5, sticky="e")
register_label = tk.Label(login_window, text="buat sekarang", font=("Arial", 10, "underline"), fg="blue", bg="#f5f5f5", cursor="hand2")
register_label.grid(row=4, column=1, sticky="w")

# Bind the clickable text to the `register` function
register_label.bind("<Button-1>", lambda e: register())

login_window.geometry("400x250")
login_window.mainloop()
