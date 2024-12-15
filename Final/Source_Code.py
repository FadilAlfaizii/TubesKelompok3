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

q_pertanyaan = Queue()

# Tambah Pertanyaan
def tambah_pertanyaan():
    pertanyaan = input("Masukkan pertanyaan: ")
    jawaban = input("Masukkan jawaban: ")
    if pertanyaan and jawaban:
        q_pertanyaan.enqueue({"pertanyaan": pertanyaan, "jawaban": jawaban})

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
        print("Pertanyaan deleted from the quiz!")
    except IndexError as e:
        print(str(e))