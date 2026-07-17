# Soal 2 (Mudah-Sedang)
# AVL Tree: Pencarian dan Statistik Tree
# Deskripsi

# Lanjutkan AVL Tree dari soal sebelumnya.

# Tambahkan fitur:

# Search data
# Menampilkan:
# Tinggi tree
# Jumlah node
# Nilai minimum
# Nilai maksimum
# Contoh Input
# 8
# 50 30 70 20 40 60 80 35
# 35
# Output
# Data ditemukan
# Jumlah node : 8
# Tinggi tree : 4
# Minimum : 20
# Maximum : 80
# Tujuan Pembelajaran

# Mahasiswa memahami:

# Operasi Search pada AVL
# Perhitungan tinggi pohon
# Traversal untuk statistik data


class AVLNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.height = 1


class AVLTree:

    def height(self, node):
        return node.height if node else 0

    def get_balance(self, node):
        return self.height(node.left) - self.height(node.right) if node else 0

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

    def insert(self, root, key):

        if root is None:
            return AVLNode(key)

        if key < root.data:
            root.left = self.insert(root.left, key)

        elif key > root.data:
            root.right = self.insert(root.right, key)

        else:
            return root

        root.height = max(
            self.height(root.left),
            self.height(root.right)
        ) + 1

        balance = self.get_balance(root)

        if balance > 1 and key < root.left.data:
            return self.right_rotate(root)

        if balance < -1 and key > root.right.data:
            return self.left_rotate(root)

        if balance > 1 and key > root.left.data:
            root.left = self.left_rotate(root.left)
            return self.right_rotate(root)

        if balance < -1 and key < root.right.data:
            root.right = self.right_rotate(root.right)
            return self.left_rotate(root)

        return root

    def search(self, root, key):

        if root is None:
            return False

        if root.data == key:
            return True

        if key < root.data:
            return self.search(root.left, key)

        return self.search(root.right, key)

    def count_nodes(self, root):

        if root is None:
            return 0

        return (
            1
            + self.count_nodes(root.left)
            + self.count_nodes(root.right)
        )

    def minimum(self, root):

        current = root

        while current.left:
            current = current.left

        return current.data

    def maximum(self, root):

        current = root

        while current.right:
            current = current.right

        return current.data


avl = AVLTree()
root = None

data = [50, 30, 70, 20, 40, 60, 80, 35]

for x in data:
    root = avl.insert(root, x)

key = 35

if avl.search(root, key):
    print("Data ditemukan")
else:
    print("Data tidak ditemukan")

print("Jumlah Node :", avl.count_nodes(root))
print("Tinggi Tree :", avl.height(root))
print("Minimum :", avl.minimum(root))
print("Maximum :", avl.maximum(root))

# jawaban/output:

# Data ditemukan
# Jumlah Node : 8
# Tinggi Tree : 4
# Minimum : 20
# Maximum : 80