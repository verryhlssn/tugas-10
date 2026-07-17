# Soal 3 (Sedang)
# Implementasi Priority Queue Menggunakan Binary Heap
# Deskripsi

# Buat program Priority Queue menggunakan Max Heap.

# Program harus mendukung:

# Operasi	Keterangan
# INSERT x	Menambah elemen
# EXTRACT	Menghapus elemen terbesar
# DISPLAY	Menampilkan isi heap
# Contoh Input
# INSERT 20
# INSERT 15
# INSERT 40
# INSERT 10
# DISPLAY
# EXTRACT
# DISPLAY
# Output
# 40 15 20 10
# Data terbesar: 40
# 20 15 10
# Ketentuan

# Implementasikan:

# HeapifyUp()
# HeapifyDown()
# Insert()
# ExtractMax()
# Tujuan Pembelajaran

# Mahasiswa memahami:

# Representasi heap dalam array
# Priority Queue
# Heapify Process


class MaxHeap:

    def __init__(self):
        self.heap = []

    def insert(self, value):

        self.heap.append(value)

        idx = len(self.heap) - 1

        while idx > 0:

            parent = (idx - 1) // 2

            if self.heap[parent] < self.heap[idx]:

                self.heap[parent], self.heap[idx] = (
                    self.heap[idx],
                    self.heap[parent]
                )

                idx = parent
            else:
                break

    def extract_max(self):

        if not self.heap:
            return None

        maximum = self.heap[0]

        self.heap[0] = self.heap[-1]
        self.heap.pop()

        idx = 0

        while True:

            left = 2 * idx + 1
            right = 2 * idx + 2
            largest = idx

            if (
                left < len(self.heap)
                and self.heap[left] > self.heap[largest]
            ):
                largest = left

            if (
                right < len(self.heap)
                and self.heap[right] > self.heap[largest]
            ):
                largest = right

            if largest != idx:
                self.heap[idx], self.heap[largest] = (
                    self.heap[largest],
                    self.heap[idx]
                )
                idx = largest
            else:
                break

        return maximum

    def display(self):
        print(self.heap)


heap = MaxHeap()

heap.insert(20)
heap.insert(15)
heap.insert(40)
heap.insert(10)

heap.display()

print("Data terbesar =", heap.extract_max())

heap.display()

# jawaban/output :

# [40, 15, 20, 10]
# Data terbesar = 40
# [20, 15, 10]