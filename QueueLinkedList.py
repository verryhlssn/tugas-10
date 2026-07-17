class Node:  # Definisi kelas Node untuk menyimpan data
    def __init__(self, value=None):  # Konstruktor node dengan nilai awal
        self.value = value  # Menyimpan nilai pada node
        self.next = None  # Pointer ke node selanjutnya
    
    def __str__(self):  # Mengembalikan representasi string dari node
        return str(self.value)  # Mengonversi nilai ke string

class LinkedList:  # Definisi kelas LinkedList sebagai dasar Queue
    def __init__(self):  # Konstruktor untuk inisialisasi list kosong
        self.head = None  # Head menunjuk ke awal list
        self.tail = None  # Tail menunjuk ke akhir list
    
    def __iter__(self):  # Agar objek linked list bisa di-loop (iterable)
        node = self.head  # Mulai dari elemen pertama
        while node:  # Selama node tidak None
            yield node  # Mengembalikan node satu per satu
            node = node.next  # Pindah ke node berikutnya

class Queue:  # Definisi kelas Queue (First In First Out)
    def __init__(self):  # Konstruktor queue
        self.linkedList = LinkedList()  # Inisialisasi queue dengan linked list
    
    def __str__(self):  # Representasi string untuk mencetak isi queue
        values = [str(x) for x in self.linkedList]  # Mengambil semua nilai node
        return ' '.join(values)  # Menggabungkan nilai dengan spasi
    
    def enqueue(self, value):  # Fungsi menambah elemen di akhir antrean
        newNode = Node(value)  # Membuat node baru
        if self.linkedList.head == None:  # Cek jika antrean kosong
            self.linkedList.head = newNode  # Set head ke node baru
            self.linkedList.tail = newNode  # Set tail ke node baru
        else:  # Jika antrean tidak kosong
            self.linkedList.tail.next = newNode  # Sambungkan tail lama ke node baru
            self.linkedList.tail = newNode  # Perbarui tail ke node baru
    
    def isEmpty(self):  # Fungsi mengecek apakah antrean kosong
        if self.linkedList.head == None:  # Jika tidak ada head
            return True  # Kembalikan True
        else:  # Jika ada head
            return False  # Kembalikan False
    
    def dequeue(self):  # Fungsi menghapus elemen dari depan antrean
        if self.isEmpty():  # Jika antrean kosong
            return "There is not any node in the Queue"  # Pesan jika kosong
        else:  # Jika antrean berisi
            tempNode = self.linkedList.head  # Simpan node yang akan dihapus
            if self.linkedList.head == self.linkedList.tail:  # Jika hanya ada satu node
                self.linkedList.head = None  # Set head ke None
                self.linkedList.tail = None  # Set tail ke None
            else:  # Jika ada lebih dari satu node
                self.linkedList.head = self.linkedList.head.next  # Pindahkan head ke node selanjutnya
            return tempNode  # Kembalikan node yang dihapus
    
    def peek(self):  # Fungsi melihat elemen terdepan
        if self.isEmpty():  # Jika antrean kosong
            return "There is not any node in the Queue"  # Pesan jika kosong
        else:  # Jika berisi
            return self.linkedList.head  # Kembalikan node di posisi head
    
    def delete(self):  # Fungsi menghapus seluruh antrean
        self.linkedList.head = None  # Kosongkan head
        self.linkedList.tail = None  # Kosongkan tail

if __name__ == "__main__":  # Kode di bawah ini hanya jalan jika file dijalankan langsung
    custQueue = Queue()  # Membuat objek antrean baru
    custQueue.enqueue(1)  # Menambah angka 1 ke antrean
    custQueue.enqueue(2)  # Menambah angka 2 ke antrean
    custQueue.enqueue(3)  # Menambah angka 3 ke antrean
    print(custQueue)  # Mencetak isi antrean: 1 2 3
    print(custQueue.peek())  # Melihat elemen pertama: 1
    print(custQueue)  # Memastikan elemen tidak terhapus setelah peek

# Jawaban/Output:

# 1 2 3
# 1
# 1 2 3