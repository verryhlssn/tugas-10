class Heap:  # Definisi kelas untuk Binary Heap
    def __init__(self, size):  # Inisialisasi heap dengan kapasitas tertentu
        self.customList = (size+1) * [None]  # Membuat list kosong dengan ukuran size+1 (indeks 0 tidak digunakan)
        self.heapSize = 0  # Ukuran elemen aktif dalam heap saat ini
        self.maxSize = size + 1  # Batas maksimal kapasitas list

def peekofHeap(rootNode):  # Fungsi melihat elemen root tanpa menghapusnya
    if not rootNode or rootNode.customList is None:  # Cek apakah heap ada atau sudah dihapus
        return  # Kembali jika tidak ada heap
    return rootNode.customList[1]  # Mengembalikan elemen pada indeks pertama (root)

def sizeofHeap(rootNode):  # Fungsi melihat jumlah elemen dalam heap
    if not rootNode:  # Cek jika objek heap tidak ada
        return  # Kembali
    return rootNode.heapSize  # Mengembalikan jumlah elemen saat ini

def levelOrderTraversal(rootNode):  # Fungsi menampilkan semua elemen secara level-order
    if not rootNode or rootNode.customList is None:  # Proteksi jika heap kosong atau sudah dihapus
        return  # Berhenti jika tidak bisa diakses
    for i in range(1, rootNode.heapSize+1):  # Loop dari indeks 1 sampai jumlah elemen
        print(rootNode.customList[i])  # Cetak nilai elemen ke layar

def heapifyTreeInsert(rootNode, index, heapType):  # Fungsi mengatur ulang struktur heap setelah penyisipan (Up-Heap)
    parentIndex = int(index/2)  # Mencari indeks orang tua dari node saat ini
    if index <= 1:  # Jika sudah sampai di root
        return  # Berhenti rekursi
    if heapType == "Min":  # Jika tipe adalah Min Heap
        if rootNode.customList[index] < rootNode.customList[parentIndex]:  # Jika anak lebih kecil dari orang tua
            rootNode.customList[index], rootNode.customList[parentIndex] = rootNode.customList[parentIndex], rootNode.customList[index]  # Tukar posisi
            heapifyTreeInsert(rootNode, parentIndex, heapType)  # Rekursi ke arah atas
    elif heapType == "Max":  # Jika tipe adalah Max Heap
        if rootNode.customList[index] > rootNode.customList[parentIndex]:  # Jika anak lebih besar dari orang tua
            rootNode.customList[index], rootNode.customList[parentIndex] = rootNode.customList[parentIndex], rootNode.customList[index]  # Tukar posisi
            heapifyTreeInsert(rootNode, parentIndex, heapType)  # Rekursi ke arah atas

def insertNode(rootNode, nodeValue, heapType):  # Fungsi menambahkan elemen baru ke dalam heap
    if rootNode.heapSize + 1 == rootNode.maxSize:  # Cek apakah kapasitas heap sudah penuh
        return "The Binary Heap is Full"  # Pesan jika penuh
    rootNode.customList[rootNode.heapSize + 1] = nodeValue  # Tambah nilai di posisi terakhir yang tersedia
    rootNode.heapSize += 1  # Tambah jumlah elemen aktif
    heapifyTreeInsert(rootNode, rootNode.heapSize, heapType)  # Lakukan penyesuaian posisi ke atas
    return "The value has been successfully inserted"  # Pesan sukses

def heapifyTreeExtract(rootNode, index, heapType):  # Fungsi mengatur ulang struktur heap setelah penghapusan (Down-Heap)
    leftIndex = index * 2  # Indeks anak kiri
    rightIndex = index * 2 + 1  # Indeks anak kanan
    swapChild = 0  # Variabel bantu untuk menentukan node mana yang akan ditukar

    if rootNode.heapSize < leftIndex:  # Jika node tidak punya anak sama sekali
        return  # Selesai
    elif rootNode.heapSize == leftIndex:  # Jika hanya punya anak kiri saja
        if heapType == "Min":  # Logika Min Heap
            if rootNode.customList[index] > rootNode.customList[leftIndex]:  # Jika parent lebih besar
                rootNode.customList[index], rootNode.customList[leftIndex] = rootNode.customList[leftIndex], rootNode.customList[index]  # Tukar
        else:  # Logika Max Heap
            if rootNode.customList[index] < rootNode.customList[leftIndex]:  # Jika parent lebih kecil
                rootNode.customList[index], rootNode.customList[leftIndex] = rootNode.customList[leftIndex], rootNode.customList[index]  # Tukar
        return  # Selesai setelah penanganan anak tunggal

    else:  # Jika punya dua anak (kiri dan kanan)
        if heapType == "Min":  # Penentuan anak terkecil untuk Min Heap
            swapChild = leftIndex if rootNode.customList[leftIndex] < rootNode.customList[rightIndex] else rightIndex  # Pilih anak terkecil
            if rootNode.customList[index] > rootNode.customList[swapChild]:  # Jika parent lebih besar dari anak terkecil
                rootNode.customList[index], rootNode.customList[swapChild] = rootNode.customList[swapChild], rootNode.customList[index]  # Tukar
                heapifyTreeExtract(rootNode, swapChild, heapType)  # Rekursi hanya jika terjadi pertukaran
        else:  # Penentuan anak terbesar untuk Max Heap
            swapChild = leftIndex if rootNode.customList[leftIndex] > rootNode.customList[rightIndex] else rightIndex  # Pilih anak terbesar
            if rootNode.customList[index] < rootNode.customList[swapChild]:  # Jika parent lebih kecil dari anak terbesar
                rootNode.customList[index], rootNode.customList[swapChild] = rootNode.customList[swapChild], rootNode.customList[index]  # Tukar
                heapifyTreeExtract(rootNode, swapChild, heapType)  # Rekursi hanya jika terjadi pertukaran

def extractNode(rootNode, heapType):  # Fungsi mengambil dan menghapus elemen root (prioritas utama)
    if rootNode.heapSize == 0:  # Cek jika heap kosong
        return  # Tidak ada yang bisa diambil
    extractedNode = rootNode.customList[1]  # Simpan nilai root yang akan dikembalikan
    rootNode.customList[1] = rootNode.customList[rootNode.heapSize]  # Pindahkan elemen terakhir ke root
    rootNode.customList[rootNode.heapSize] = None  # Hapus elemen terakhir yang sudah dipindah
    rootNode.heapSize -= 1  # Kurangi jumlah elemen aktif
    heapifyTreeExtract(rootNode, 1, heapType)  # Lakukan penyesuaian posisi ke bawah dari root
    return extractedNode  # Kembalikan nilai yang diekstrak

def deleteEntireBP(rootNode):  # Fungsi menghapus seluruh struktur heap
    rootNode.customList = None  # Melepaskan referensi list agar dihapus memori
    rootNode.heapSize = 0  # Reset ukuran menjadi nol

if __name__ == "__main__":  # Blok eksekusi utama
    newHeap = Heap(5)  # Membuat heap baru kapasitas 5
    insertNode(newHeap, 4, "Max")  # Masukkan nilai 4
    insertNode(newHeap, 5, "Max")  # Masukkan nilai 5
    insertNode(newHeap, 2, "Max")  # Masukkan nilai 2
    insertNode(newHeap, 1, "Max")  # Masukkan nilai 1
    print("Heap sebelum dihapus:")  # Informasi status
    levelOrderTraversal(newHeap)  # Tampilkan isi heap
    print("Ekstrak elemen terbesar:", extractNode(newHeap, "Max"))  # Harusnya 5
    levelOrderTraversal(newHeap)  # Tampilkan sisa heap
    deleteEntireBP(newHeap)  # Hapus seluruh heap
    levelOrderTraversal(newHeap)  # Tidak akan mencetak apa pun karena sudah dihapus

# jawaban/output:

# Heap sebelum dihapus:
# 5
# 4
# 2
# 1
# Ekstrak elemen terbesar: 5
# 4
# 1
# 2