# Import necessary libraries
import tkinter as tk
from tkinter import messagebox, simpledialog

# Global Variables
users = {"admin": "admin"}  # Default login credentials
questions = []  # List to store questions
scores = []  # List to store quiz scores


def login():
    """Login function"""
    username = username_entry.get()
    password = password_entry.get()
    try:
        if username in users and users[username] == password:
            messagebox.showinfo("Success", "Login successful!")
            show_menu()
            login_window.destroy()
        else:
            raise ValueError("Invalid username or password")
    except ValueError as e:
        messagebox.showerror("Error", str(e))


def add_question():
    """Add question function"""
    question = simpledialog.askstring("Add Question", "Enter the question:")
    answer = simpledialog.askstring("Add Answer", "Enter the answer:")
    if question and answer:
        questions.append({"question": question, "answer": answer})
        messagebox.showinfo("Success", "Question added successfully!")


def view_questions():
    """View all questions"""
    question_list = "\n".join([f"{idx + 1}. {q['question']}" for idx, q in enumerate(questions)])
    if not question_list:
        question_list = "No questions available."
    messagebox.showinfo("Questions", question_list)


def delete_question():
    """Delete question by index"""
    try:
        if not questions:
            raise IndexError("No questions available!")
        index = simpledialog.askinteger("Input", "Enter the question number to delete:") - 1
        if index < 0 or index >= len(questions):
            raise ValueError("Invalid question number!")
        questions.pop(index)
        messagebox.showinfo("Success", "Question deleted!")
    except ValueError as e:
        messagebox.showerror("Error", str(e))
    except IndexError as e:
        messagebox.showerror("Error", str(e))


def take_quiz():
    """Take quiz and calculate score"""
    if not questions:
        messagebox.showerror("Error", "No questions available for the quiz.")
        return
    score = 0
    for q in questions:
        answer = simpledialog.askstring("Quiz", q["question"])
        if answer and answer.lower() == q["answer"].lower():
            score += 1
    scores.append(score)
    messagebox.showinfo("Quiz Completed", f"Your score: {score}/{len(questions)}")


def calculate_total_score_recursively(score_list):
    """Recursive function to calculate the total score"""
    if not score_list:
        return 0
    return score_list[0] + calculate_total_score_recursively(score_list[1:])


def view_total_score():
    """View total score using recursion"""
    if not scores:
        messagebox.showinfo("Total Score", "No scores available yet.")
    else:
        total_score = calculate_total_score_recursively(scores)
        messagebox.showinfo("Total Score", f"Your total score from all quizzes is: {total_score}")


def show_menu():
    """Show menu after login"""
    menu_window = tk.Tk()
    menu_window.title("Quiz Menu")
    menu_window.configure(bg="#f0f8ff")

    tk.Label(menu_window, text="Quiz Management System", font=("Helvetica", 16, "bold"), bg="#4682b4", fg="white", padx=10, pady=10).pack(fill=tk.X)

    tk.Button(menu_window, text="Add Question", command=add_question, font=("Arial", 12), bg="#add8e6", fg="black", width=20).pack(pady=10)
    tk.Button(menu_window, text="View Questions", command=view_questions, font=("Arial", 12), bg="#add8e6", fg="black", width=20).pack(pady=10)
    tk.Button(menu_window, text="Delete Question", command=delete_question, font=("Arial", 12), bg="#add8e6", fg="black", width=20).pack(pady=10)
    tk.Button(menu_window, text="Take Quiz", command=take_quiz, font=("Arial", 12), bg="#add8e6", fg="black", width=20).pack(pady=10)
    tk.Button(menu_window, text="View Total Score", command=view_total_score, font=("Arial", 12), bg="#add8e6", fg="black", width=20).pack(pady=10)
    tk.Button(menu_window, text="Exit", command=menu_window.destroy, font=("Arial", 12), bg="#ff7f7f", fg="black", width=20).pack(pady=10)

    menu_window.geometry("400x400")
    menu_window.mainloop()


# Login GUI
login_window = tk.Tk()
login_window.title("Login System")
login_window.configure(bg="#f5f5f5")

tk.Label(login_window, text="Welcome to Quiz System", font=("Helvetica", 16, "bold"), bg="#f5f5f5", fg="#333").grid(row=0, column=0, columnspan=2, pady=10)

tk.Label(login_window, text="Username:", font=("Arial", 12), bg="#f5f5f5").grid(row=1, column=0, padx=10, pady=5)
username_entry = tk.Entry(login_window, font=("Arial", 12))
username_entry.grid(row=1, column=1, padx=10, pady=5)

tk.Label(login_window, text="Password:", font=("Arial", 12), bg="#f5f5f5").grid(row=2, column=0, padx=10, pady=5)
password_entry = tk.Entry(login_window, show="*", font=("Arial", 12))
password_entry.grid(row=2, column=1, padx=10, pady=5)

tk.Button(login_window, text="Login", command=login, font=("Arial", 12), bg="#4caf50", fg="white", width=15).grid(row=3, column=0, columnspan=2, pady=10)

login_window.geometry("400x250")
login_window.mainloop()