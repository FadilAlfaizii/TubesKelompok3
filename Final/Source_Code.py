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


q_pertanyaan = Queue() # Queue untuk soal
score_stack = Stack()  # Stack untuk skor

# Tambah Pertanyaan
def tambah_pertanyaan():
    pertanyaan = input("Masukkan pertanyaan: ")
    jawaban = input("Masukkan jawaban: ")
    if pertanyaan and jawaban:
        q_pertanyaan.enqueue({"pertanyaan": pertanyaan, "jawaban": jawaban})
        simpan_pertanyaan()

# Lihat Pertanyaan
def lihat_pertanyaan():
    if q_pertanyaan.kosong():
        print("Tidak ada pertanyaan yang tersedia.")
    else:
        pertanyaan = q_pertanyaan.tampil()
        for idx, q in enumerate(pertanyaan):
            print(f"{idx + 1}. {q['pertanyaan']}")

# Hapus Pertanyaan
def hapus_pertanyaan():
    try:
        if q_pertanyaan.kosong():
            raise IndexError("Tidak ada pertanyaan to delete.")
        q_pertanyaan.dequeue()
        simpan_pertanyaan()
        print("Pertanyaan deleted from the quiz!")
    except IndexError as e:
        print(str(e))

# Edit Pertanyaan
def edit_pertanyaan():
    if q_pertanyaan.kosong():
        print("Tidak ada pertanyaan yang tersedia untuk diubah.")
        return
    pertanyaan = q_pertanyaan.tampil()
    list_pertanyaan = "\n".join([f"{idx + 1}. {q['pertanyaan']}" for idx, q in enumerate(pertanyaan)])
    index_terpilih = int(input(f"Pilih nomor pertanyaan yang ingin diubah:\n\n{list_pertanyaan}")) - 1
    if index_terpilih < 0 or index_terpilih >= len(pertanyaan):
        print("Nomor tersebut tidak ada!")
        return
    pertanyaan_terpilih = pertanyaan[index_terpilih]
    pertanyaan_baru = input(f"Pertanyaan Sebelum: {pertanyaan_terpilih['pertanyaan']}\n\nEnter new pertanyaan:")
    jawaban_baru = input(f"Jawaban Sebelum: {pertanyaan_terpilih['jawaban']}\n\nEnter new jawaban:")
    if pertanyaan_baru and jawaban_baru:
        pertanyaan_terpilih["pertanyaan"] = pertanyaan_baru
        pertanyaan_terpilih["jawaban"] = jawaban_baru
        print("Pertanyaan berhasil diupdate!")
    else:
        print("Pertanyaan atau jawaban tidak boleh kosong!")


def simpan_pertanyaan():
    with open("pertanyaan.txt", "w") as file:
        pertanyaan = q_pertanyaan.tampil()
        for q in pertanyaan:
            file.write(f"{q['pertanyaan']}\n{q['jawaban']}\n\n")


def load_pertanyaan():
    try:
        with open("pertanyaan.txt", "r") as file:
            for line in file:
                pertanyaan = line.strip()
                jawaban = file.readline().strip()
                q_pertanyaan.enqueue({"pertanyaan": pertanyaan, "jawaban": jawaban})
    except FileNotFoundError:
        pass


# Mulai Kuis
def take_quiz():
    if q_pertanyaan.kosong():
        print("Error", "Tidak ada pertanyaan yang tersedia for the quiz.")
        return
    pertanyaan = q_pertanyaan.tampil()
    skor = 0
    for q in pertanyaan:
        jawaban = input("Kuis", q["pertanyaan"])
        if jawaban and jawaban.lower() == q["jawaban"].lower():
            skor += 1
    score_stack.push(skor)  # Simpan skor ke Stack
    print("Kuis Selesai", f"Skor Anda: {skor}/{len(pertanyaan)}")


# Lihat Total Skor 
def view_total_score():
    if score_stack.kosong():
        print("Total Skor", "Belum ada skor yang tersedia.")
        return
    total_score = sum(score_stack.items)
    latest_score = score_stack.peek()
    print("Total Skor", f"Total skor: {total_score}\nSkor terbaru: {latest_score}")






