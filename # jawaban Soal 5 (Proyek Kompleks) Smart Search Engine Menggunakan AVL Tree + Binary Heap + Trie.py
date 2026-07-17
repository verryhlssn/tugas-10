# Soal 5 (Proyek Kompleks)
# Smart Search Engine Menggunakan AVL Tree + Binary Heap + Trie
# Deskripsi

# Buat sistem pencarian dokumen mini seperti Google Search sederhana.

# Struktur Data yang Digunakan
# Trie

# Digunakan untuk:

# Menyimpan kata-kata
# Autocomplete keyword

# Contoh:

# programming
# program
# project
# python

# Jika user mengetik:

# pro

# Maka sistem menampilkan:

# program
# programming
# project
# AVL Tree

# Digunakan untuk menyimpan dokumen.

# Setiap dokumen memiliki:

# Document
# {
#     int id;
#     string title;
#     int score;
# }

# AVL Tree digunakan agar:

# Insert cepat
# Search cepat
# Data selalu seimbang
# Binary Max Heap

# Digunakan untuk ranking hasil pencarian.

# Misalnya:

# Dokumen	Relevansi
# AI Research	95
# AI for Healthcare	87
# Machine Learning	70

# Heap akan mengurutkan:

# 95
# 87
# 70
# Fitur Sistem
# Menu 1

# Tambah Dokumen

# Input:

# ID
# Judul
# Score

# Simpan ke AVL Tree.

# Menu 2

# Cari Dokumen

# Input:

# ID

# Cari menggunakan AVL Tree.

# Menu 3

# Autocomplete

# Input:

# Prefix

# Gunakan Trie.

# Menu 4

# Top K Dokumen

# Input:

# K

# Tampilkan K dokumen dengan score tertinggi menggunakan Max Heap.

# Menu 5

# Tampilkan Semua Dokumen

# Traversal AVL Tree secara Inorder.

# Contoh Skenario

# Tambah:

# ID	Judul	Score
# 101	AI Research	95
# 102	Data Mining	70
# 103	AI Healthcare	87

# Autocomplete:

# AI

# Output:

# AI Research
# AI Healthcare

# Top 2:

# AI Research (95)
# AI Healthcare (87)
# Tingkat Kesulitan
# Soal	Struktur Data	Level
# 1	AVL Insert	Mudah
# 2	AVL Search & Statistik	Mudah-Sedang
# 3	Binary Heap Priority Queue	Sedang
# 4	Trie Dictionary	Sedang
# 5	AVL + Heap + Trie Search Engine	Proyek Akhir
# Capaian Pembelajaran (CPMK)

# Setelah menyelesaikan kelima soal ini, mahasiswa diharapkan mampu:

# Mengimplementasikan AVL Tree beserta rotasi keseimbangan.
# Mengimplementasikan Binary Heap sebagai Priority Queue.
# Mengimplementasikan Trie untuk pencarian prefix.
# Memilih struktur data yang sesuai dengan kebutuhan aplikasi.
# Mengintegrasikan beberapa struktur data dalam sebuah sistem nyata yang lebih kompleks.


import heapq

# =====================
# DOCUMENT
# =====================

class Document:

    def __init__(self, doc_id, title, score):

        self.id = doc_id
        self.title = title
        self.score = score


# =====================
# AVL TREE
# =====================

class AVLNode:

    def __init__(self, document):

        self.doc = document
        self.left = None
        self.right = None
        self.height = 1


class AVLTree:

    def height(self, node):
        return node.height if node else 0

    def balance(self, node):

        if not node:
            return 0

        return (
            self.height(node.left)
            - self.height(node.right)
        )

    def right_rotate(self, y):

        x = y.left
        t2 = x.right

        x.right = y
        y.left = t2

        y.height = max(
            self.height(y.left),
            self.height(y.right)
        ) + 1

        x.height = max(
            self.height(x.left),
            self.height(x.right)
        ) + 1

        return x

    def left_rotate(self, x):

        y = x.right
        t2 = y.left

        y.left = x
        x.right = t2

        x.height = max(
            self.height(x.left),
            self.height(x.right)
        ) + 1

        y.height = max(
            self.height(y.left),
            self.height(y.right)
        ) + 1

        return y

    def insert(self, root, document):

        if root is None:
            return AVLNode(document)

        if document.id < root.doc.id:
            root.left = self.insert(root.left, document)

        elif document.id > root.doc.id:
            root.right = self.insert(root.right, document)

        else:
            return root

        root.height = max(
            self.height(root.left),
            self.height(root.right)
        ) + 1

        bf = self.balance(root)

        if bf > 1 and document.id < root.left.doc.id:
            return self.right_rotate(root)

        if bf < -1 and document.id > root.right.doc.id:
            return self.left_rotate(root)

        if bf > 1 and document.id > root.left.doc.id:
            root.left = self.left_rotate(root.left)
            return self.right_rotate(root)

        if bf < -1 and document.id < root.right.doc.id:
            root.right = self.right_rotate(root.right)
            return self.left_rotate(root)

        return root

    def search(self, root, doc_id):

        if root is None:
            return None

        if root.doc.id == doc_id:
            return root.doc

        if doc_id < root.doc.id:
            return self.search(root.left, doc_id)

        return self.search(root.right, doc_id)

    def inorder(self, root):

        if root:

            self.inorder(root.left)

            print(
                root.doc.id,
                root.doc.title,
                root.doc.score
            )

            self.inorder(root.right)


# =====================
# TRIE
# =====================

class TrieNode:

    def __init__(self):
        self.children = {}
        self.words = []


class Trie:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):

        node = self.root

        for char in word.lower():

            if char not in node.children:
                node.children[char] = TrieNode()

            node = node.children[char]
            node.words.append(word)

    def autocomplete(self, prefix):

        node = self.root

        for char in prefix.lower():

            if char not in node.children:
                return []

            node = node.children[char]

        return node.words


# =====================
# SEARCH ENGINE
# =====================

avl = AVLTree()
trie = Trie()

root = None

maxheap = []

while True:

    print("\n===== MENU =====")
    print("1. Tambah Dokumen")
    print("2. Cari Dokumen")
    print("3. Autocomplete")
    print("4. Top K Dokumen")
    print("5. Tampilkan Semua")
    print("6. Keluar")

    pilihan = input("Pilih : ")

    if pilihan == "1":

        doc_id = int(input("ID : "))
        title = input("Judul : ")
        score = int(input("Score : "))

        doc = Document(
            doc_id,
            title,
            score
        )

        root = avl.insert(root, doc)

        trie.insert(title)

        heapq.heappush(
            maxheap,
            (-score, title)
        )

        print("Dokumen ditambahkan")

    elif pilihan == "2":

        doc_id = int(input("Cari ID : "))

        hasil = avl.search(
            root,
            doc_id
        )

        if hasil:
            print(
                hasil.id,
                hasil.title,
                hasil.score
            )
        else:
            print("Tidak ditemukan")

    elif pilihan == "3":

        prefix = input("Prefix : ")

        hasil = trie.autocomplete(prefix)

        if hasil:
            for h in hasil:
                print(h)
        else:
            print("Tidak ada")

    elif pilihan == "4":

        k = int(input("Top K = "))

        temp = sorted(maxheap)

        for i in range(
            min(k, len(temp))
        ):
            score, title = temp[i]

            print(
                title,
                "Score =",
                -score
            )

    elif pilihan == "5":

        avl.inorder(root)

    elif pilihan == "6":

        print("Program selesai")
        break

    else:
        print("Menu tidak valid")

# jawaban/output:

# ===== MENU =====
# 1. Tambah Dokumen
# 2. Cari Dokumen
# 3. Autocomplete
# 4. Top K Dokumen
# 5. Tampilkan Semua
# 6. Keluar

# Pilih : 1
# ID : 101
# Judul : AI Research
# Score : 95
# Dokumen ditambahkan

# ===== MENU =====
# 1. Tambah Dokumen
# 2. Cari Dokumen
# 3. Autocomplete
# 4. Top K Dokumen
# 5. Tampilkan Semua
# 6. Keluar

# Pilih : 1
# ID : 102
# Judul : Data Mining
# Score : 70
# Dokumen ditambahkan

# ===== MENU =====
# 1. Tambah Dokumen
# 2. Cari Dokumen
# 3. Autocomplete
# 4. Top K Dokumen
# 5. Tampilkan Semua
# 6. Keluar

# Pilih : 1
# ID : 103
# Judul : AI Healthcare
# Score : 87
# Dokumen ditambahkan

# ===== MENU =====
# 1. Tambah Dokumen
# 2. Cari Dokumen
# 3. Autocomplete
# 4. Top K Dokumen
# 5. Tampilkan Semua
# 6. Keluar

# Pilih : 3
# Prefix : AI
# AI Research
# AI Healthcare

# ===== MENU =====
# 1. Tambah Dokumen
# 2. Cari Dokumen
# 3. Autocomplete
# 4. Top K Dokumen
# 5. Tampilkan Semua
# 6. Keluar

# Pilih : 4
# Top K = 2
# AI Research Score = 95
# AI Healthcare Score = 87

# ===== MENU =====
# 1. Tambah Dokumen
# 2. Cari Dokumen
# 3. Autocomplete
# 4. Top K Dokumen
# 5. Tampilkan Semua
# 6. Keluar

# Pilih : 5
# 101 AI Research 95
# 102 Data Mining 70
# 103 AI Healthcare 87

# ===== MENU =====
# 1. Tambah Dokumen
# 2. Cari Dokumen
# 3. Autocomplete
# 4. Top K Dokumen
# 5. Tampilkan Semua
# 6. Keluar

# Pilih : 6
# Program selesai