import tkinter as tk
from tkinter import messagebox, simpledialog

# Struktur Data Stack
class Stack:
    def __init__(self, capacity=10):
        self.capacity = capacity
        self.items = []
    
    def kosong(self):
        return len(self.items) == 0
    
    def push(self, item):
        if len(self.items) >= self.capacity:
            raise OverflowError("Stack penuh")
        self.items.append(item)

    def pop(self):
        if not self.kosong():
            return self.items.pop()
        raise IndexError("Pop dari stack yang kosong")
    
    def peek(self):
        if not self.kosong():
            return self.items[-1]
        raise IndexError("Peek dari stack yang kosong")
    
    def size(self):
        return len(self.items)


# Struktur Data Queue
class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None
        
class Queue:
    def __init__(self):
        self.front = None
        self.rear = None

    def enqueue(self, data):
        new_node = Node(data)
        if self.rear is None:
            self.front = self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node

    def dequeue(self):
        if self.front is None:
            raise IndexError("Queue kosong!")
        data_keluar = self.front.data
        self.front = self.front.next
        if self.front is None:
            self.rear = None
        return data_keluar

    def tampil(self):
        current = self.front
        result = []
        while current is not None:
            result.append(current.data)
            current = current.next
        return result

    def kosong(self):
        return self.front is None


# Global Variables
users = {"admin": "admin"}  # Default login
queue_pertanyaan = Queue()  # Queue untuk soal
score_stack = Stack()  # Stack untuk skor

# Fungsi Register
def register():
    """Register function for new users"""
    new_username = simpledialog.askstring("Register", "Masukkan Username:")
    if not new_username:
        messagebox.showerror("Error", "Username tidak boleh kosong.")
        return
    elif new_username in users:
        messagebox.showerror("Error", "Username telah dipakai.")
        return

    new_password = simpledialog.askstring("Register", "Masukkan Password:")
    if not new_password:
        messagebox.showerror("Error", "Password tidak boleh kosong.")
        return

    # Menambahkan pengguna baru
    users[new_username] = new_password
    messagebox.showinfo("Sukses", f"Akun baru untuk username: {new_username}")

# Fungsi Login
def login():
    username = username_entry.get()
    password = password_entry.get()
    if username in users and users[username] == password:
        messagebox.showinfo("Sukses", "Login sukses!")
        login_window.destroy()
        show_menu()
    else:
        messagebox.showerror("Error", "Username atau Password salah!")


# Add Pertanyaan
def add_question():
    pertanyaan = simpledialog.askstring("Tambah Pertanyaan", "Masukkan pertanyaan:")
    jawaban = simpledialog.askstring("Tambah Jawaban", "Masukkan jawaban yang benar:")
    if pertanyaan and jawaban:
        queue_pertanyaan.enqueue({"pertanyaan": pertanyaan, "jawaban": jawaban})
        messagebox.showinfo("Sukses", "Pertanyaan added to the quiz!")


# Lihat Pertanyaan
def view_questions():
    if queue_pertanyaan.kosong():
        messagebox.showinfo("Pertanyaan", "Tidak ada pertanyaan yang tersedia.")
        return
    pertanyaan = queue_pertanyaan.tampil()
    list_pertanyaan = "\n".join([f"{idx + 1}. {q['pertanyaan']}" for idx, q in enumerate(pertanyaan)])
    messagebox.showinfo("Pertanyaan", list_pertanyaan)


# Edit Pertanyaan
def edit_question():
    if queue_pertanyaan.kosong():
        messagebox.showinfo("Edit Pertanyaan", "Tidak ada pertanyaan yang tersedia untuk diubah.")
        return
    pertanyaan = queue_pertanyaan.tampil()
    list_pertanyaan = "\n".join([f"{idx + 1}. {q['pertanyaan']}" for idx, q in enumerate(pertanyaan)])
    selected_idx = simpledialog.askinteger("Edit Pertanyaan", f"Select pertanyaan number untuk diubah:\n\n{list_pertanyaan}")
    
    if selected_idx is None or selected_idx < 1 or selected_idx > len(pertanyaan):
        messagebox.showerror("Error", "Invalid selection!")
        return
    
    pertanyaan_terpilih = pertanyaan[selected_idx - 1]
    pertanyaan_baru = simpledialog.askstring("Edit Pertanyaan", f"Current pertanyaan: {pertanyaan_terpilih['pertanyaan']}\n\nEnter new pertanyaan:")
    jawaban_baru = simpledialog.askstring("Edit Jawaban", f"Current jawaban: {pertanyaan_terpilih['jawaban']}\n\nEnter new jawaban:")
    
    if pertanyaan_baru and jawaban_baru:
        pertanyaan_terpilih["pertanyaan"] = pertanyaan_baru
        pertanyaan_terpilih["jawaban"] = jawaban_baru
        messagebox.showinfo("Sukses", "Pertanyaan successfully updated!")
    else:
        messagebox.showerror("Error", "Pertanyaan or jawaban cannot be empty.")


# Hapus Pertanyaan
def delete_question():
    try:
        if queue_pertanyaan.kosong():
            raise IndexError("Tidak ada pertanyaan to delete.")
        queue_pertanyaan.dequeue()
        messagebox.showinfo("Sukses", "Pertanyaan deleted from the quiz!")
    except IndexError as e:
        messagebox.showerror("Error", str(e))


# Mulai Kuis
def take_quiz():
    if queue_pertanyaan.kosong():
        messagebox.showerror("Error", "Tidak ada pertanyaan yang tersedia for the quiz.")
        return
    pertanyaan = queue_pertanyaan.tampil()
    skor = 0
    for q in pertanyaan:
        jawaban = simpledialog.askstring("Kuis", q["pertanyaan"])
        if jawaban and jawaban.lower() == q["jawaban"].lower():
            skor += 1
    score_stack.push(skor)  # Simpan skor ke Stack
    messagebox.showinfo("Kuis Selesai", f"Skor Anda: {skor}/{len(pertanyaan)}")


# Lihat Total Skor
def view_total_score():
    if score_stack.kosong():
        messagebox.showinfo("Total Skor", "Belum ada skor yang tersedia.")
        return
    total_score = sum(score_stack.items)
    latest_score = score_stack.peek()
    messagebox.showinfo("Total Skor", f"Total skor: {total_score}\nSkor terbaru: {latest_score}")


# Show Menu
def show_menu():
    """Show menu after login"""
    menu_window = tk.Tk()
    menu_window.title("Kuis Menu")
    menu_window.configure(bg="#f0f8ff")

    tk.Label(menu_window, text="Kuis Management System", font=("Helvetica", 16, "bold"), bg="#4682b4", fg="white", padx=10, pady=10).pack(fill=tk.X)

    tk.Button(menu_window, text="Tambah Pertanyaan", command=add_question, font=("Arial", 12), bg="#add8e6", fg="black", width=20).pack(pady=10)
    tk.Button(menu_window, text="Lihat Pertanyaan", command=view_questions, font=("Arial", 12), bg="#add8e6", fg="black", width=20).pack(pady=10)
    tk.Button(menu_window, text="Edit Pertanyaan", command=edit_question, font=("Arial", 12), bg="#add8e6", fg="black", width=20).pack(pady=10)
    tk.Button(menu_window, text="Hapus Pertanyaan", command=delete_question, font=("Arial", 12), bg="#add8e6", fg="black", width=20).pack(pady=10)
    tk.Button(menu_window, text="Mulai Kuis", command=take_quiz, font=("Arial", 12), bg="#add8e6", fg="black", width=20).pack(pady=10)
    tk.Button(menu_window, text="Lihat Total Skor", command=view_total_score, font=("Arial", 12), bg="#add8e6", fg="black", width=20).pack(pady=10)
    tk.Button(menu_window, text="Exit", command=menu_window.destroy, font=("Arial", 12), bg="#ff7f7f", fg="black", width=20).pack(pady=10)

    menu_window.geometry("400x400")
    menu_window.mainloop()


# Login GUI
login_window = tk.Tk()
login_window.title("Login System")
login_window.configure(bg="#f5f5f5")

tk.Label(login_window, text="Welcome to Kuis System", font=("Helvetica", 16, "bold"), bg="#f5f5f5", fg="#333").grid(row=0, column=0, columnspan=2, pady=10)

tk.Label(login_window, text="Username:", font=("Arial", 12), bg="#f5f5f5").grid(row=1, column=0, padx=10, pady=5, sticky="w")
username_entry = tk.Entry(login_window, font=("Arial", 12))
username_entry.grid(row=1, column=1, padx=10, pady=5)

tk.Label(login_window, text="Password:", font=("Arial", 12), bg="#f5f5f5").grid(row=2, column=0, padx=10, pady=5, sticky="w")
password_entry = tk.Entry(login_window, show="*", font=("Arial", 12))
password_entry.grid(row=2, column=1, padx=10, pady=5)

tk.Button(login_window, text="Login", command=login, font=("Arial", 12), bg="#4caf50", fg="white", width=15).grid(row=3, column=0, columnspan=2, pady=10)

# Adding "Tidak ada account? Register now" text
tk.Label(login_window, text="Belum ada akun?", font=("Arial", 10), bg="#f5f5f5", fg="#333").grid(row=4, column=0, padx=10, pady=5, sticky="e")
register_label = tk.Label(login_window, text="Buat Sekarang", font=("Arial", 10, "underline"), fg="blue", bg="#f5f5f5", cursor="hand2")
register_label.grid(row=4, column=1, sticky="w")

# Bind the clickable text to the `register` function
register_label.bind("<Button-1>", lambda e: register())

login_window.geometry("400x250")
login_window.mainloop()