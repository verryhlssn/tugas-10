import QueueLinkedList as queue  # Mengimpor modul Queue berbasis Linked List

class AVLNode:  # Definisi kelas untuk node pohon AVL
    def __init__(self, data):  # Konstruktor untuk membuat node baru
        self.data = data  # Menyimpan nilai data pada node
        self.leftChild = None  # Pointer ke anak kiri (awalnya kosong)
        self.rightChild = None  # Pointer ke anak kanan (awalnya kosong)
        self.height = 1  # Tinggi awal node adalah 1

def preOrderTraversal(rootNode):  # Fungsi traversal Pre-order (Root, Kiri, Kanan)
    if not rootNode:  # Jika node kosong (None)
        return  # Berhenti/kembali
    print(rootNode.data)  # Cetak data node saat ini
    preOrderTraversal(rootNode.leftChild)  # Rekursi ke anak kiri
    preOrderTraversal(rootNode.rightChild)  # Rekursi ke anak kanan

def inOrderTraversal(rootNode):  # Fungsi traversal In-order (Kiri, Root, Kanan)
    if not rootNode:  # Jika node kosong
        return  # Berhenti
    inOrderTraversal(rootNode.leftChild)  # Rekursi ke anak kiri
    print(rootNode.data)  # Cetak data node saat ini
    inOrderTraversal(rootNode.rightChild)  # Rekursi ke anak kanan

def postOrderTraversal(rootNode):  # Fungsi traversal Post-order (Kiri, Kanan, Root)
    if not rootNode:  # Jika node kosong
        return  # Berhenti
    postOrderTraversal(rootNode.leftChild)  # Rekursi ke anak kiri
    postOrderTraversal(rootNode.rightChild)  # Rekursi ke anak kanan
    print(rootNode.data)  # Cetak data node saat ini

def levelOrderTraversal(rootNode):  # Fungsi traversal Level-order (per tingkat)
    if not rootNode:  # Jika pohon kosong
        return  # Berhenti
    else:  # Jika pohon tidak kosong
        customQueue = queue.Queue()  # Inisialisasi antrean (queue) baru
        customQueue.enqueue(rootNode)  # Masukkan root ke antrean
        while not(customQueue.isEmpty()):  # Selama antrean tidak kosong
            root = customQueue.dequeue()  # Keluarkan elemen dari antrean (mengembalikan node LL)
            print(root.value.data)  # Cetak data dari AVLNode di dalam node LL
            if root.value.leftChild is not None:  # Jika anak kiri ada
                customQueue.enqueue(root.value.leftChild)  # Masukkan anak kiri ke antrean
            if root.value.rightChild is not None:  # Jika anak kanan ada
                customQueue.enqueue(root.value.rightChild)  # Masukkan anak kanan ke antrean

def searchNode(rootNode, nodeValue):  # Fungsi mencari nilai dalam AVL Tree
    if not rootNode:  # Jika node kosong atau nilai tidak ditemukan
        print("The value is not found")  # Beri tahu pengguna tidak ketemu
        return  # Keluar dari fungsi
    if rootNode.data == nodeValue:  # Jika nilai ditemukan di node saat ini
        print("The value is found")  # Beri tahu pengguna ketemu
    elif nodeValue < rootNode.data:  # Jika nilai yang dicari lebih kecil
        searchNode(rootNode.leftChild, nodeValue)  # Cari rekursif ke kiri
    else:  # Jika nilai yang dicari lebih besar
        searchNode(rootNode.rightChild, nodeValue)  # Cari rekursif ke kanan

def getHeight(rootNode):  # Fungsi mendapatkan tinggi sebuah node
    if not rootNode:  # Jika node kosong
        return 0  # Tinggi adalah 0
    return rootNode.height  # Kembalikan atribut height node

def rightRotate(disbalanceNode): # Fungsi melakukan rotasi kanan untuk menyeimbangkan pohon
    newRoot = disbalanceNode.leftChild  # Anak kiri menjadi root baru
    disbalanceNode.leftChild = disbalanceNode.leftChild.rightChild  # Geser anak kanan newRoot ke kiri disbalanceNode
    newRoot.rightChild = disbalanceNode  # Letakkan disbalanceNode di kanan root baru
    disbalanceNode.height = 1 + max(getHeight(disbalanceNode.leftChild), getHeight(disbalanceNode.rightChild))  # Update tinggi node lama
    newRoot.height = 1 + max(getHeight(newRoot.leftChild), getHeight(newRoot.rightChild))  # Update tinggi root baru
    return newRoot  # Kembalikan root baru hasil rotasi

def leftRotate(disbalanceNode): # Fungsi melakukan rotasi kiri untuk menyeimbangkan pohon
    newRoot = disbalanceNode.rightChild  # Anak kanan menjadi root baru
    disbalanceNode.rightChild = disbalanceNode.rightChild.leftChild  # Geser anak kiri newRoot ke kanan disbalanceNode
    newRoot.leftChild = disbalanceNode  # Letakkan disbalanceNode di kiri root baru
    disbalanceNode.height = 1 + max(getHeight(disbalanceNode.leftChild), getHeight(disbalanceNode.rightChild))  # Update tinggi node lama
    newRoot.height = 1 + max(getHeight(newRoot.leftChild), getHeight(newRoot.rightChild))  # Update tinggi root baru
    return newRoot  # Kembalikan root baru hasil rotasi

def getBalance(rootNode):  # Fungsi menghitung selisih tinggi anak kiri dan kanan
    if not rootNode:  # Jika node kosong
        return 0  # Keseimbangan adalah 0
    return getHeight(rootNode.leftChild) - getHeight(rootNode.rightChild)  # Selisih tinggi kiri dikurangi kanan

def insertNode(rootNode, nodeValue):  # Fungsi menyisipkan node baru ke AVL Tree
    if not rootNode:  # Jika mencapai posisi kosong
        return AVLNode(nodeValue)  # Buat node baru di posisi tersebut
    elif nodeValue < rootNode.data:  # Jika nilai baru lebih kecil dari root saat ini
        rootNode.leftChild = insertNode(rootNode.leftChild, nodeValue)  # Sisipkan ke sub-tree kiri
    else:  # Jika nilai baru lebih besar atau sama
        rootNode.rightChild = insertNode(rootNode.rightChild, nodeValue)  # Sisipkan ke sub-tree kanan
    
    rootNode.height = 1 + max(getHeight(rootNode.leftChild), getHeight(rootNode.rightChild))  # Perbarui tinggi root saat ini
    balance = getBalance(rootNode)  # Dapatkan faktor keseimbangan
    if balance > 1 and nodeValue < rootNode.leftChild.data:  # Kondisi Left Left (LL)
        return rightRotate(rootNode)  # Lakukan rotasi kanan
    if balance > 1 and nodeValue > rootNode.leftChild.data:  # Kondisi Left Right (LR)
        rootNode.leftChild = leftRotate(rootNode.leftChild)  # Rotasi kiri pada anak
        return rightRotate(rootNode)  # Rotasi kanan pada root
    if balance < -1 and nodeValue > rootNode.rightChild.data:  # Kondisi Right Right (RR)
        return leftRotate(rootNode)  # Lakukan rotasi kiri
    if balance < -1 and nodeValue < rootNode.rightChild.data:  # Kondisi Right Left (RL)
        rootNode.rightChild = rightRotate(rootNode.rightChild)  # Rotasi kanan pada anak
        return leftRotate(rootNode)  # Rotasi kiri pada root
    return rootNode  # Kembalikan root yang sudah seimbang

def getMinValueNode(rootNode):  # Fungsi mendapatkan node dengan nilai terkecil
    if rootNode is None or rootNode.leftChild is None:  # Jika tidak ada anak kiri lagi
        return rootNode  # Node ini adalah nilai terkecil
    return getMinValueNode(rootNode.leftChild)  # Rekursi terus ke arah kiri

def deleteNode(rootNode, nodeValue):  # Fungsi menghapus node berdasarkan nilai
    if not rootNode:  # Jika nilai tidak ditemukan
        return rootNode  # Kembalikan None
    elif nodeValue < rootNode.data:  # Jika nilai yang dicari lebih kecil
        rootNode.leftChild = deleteNode(rootNode.leftChild, nodeValue)  # Cari di kiri
    elif nodeValue > rootNode.data:  # Jika nilai yang dicari lebih besar
        rootNode.rightChild = deleteNode(rootNode.rightChild, nodeValue)  # Cari di kanan
    else:  # Jika nilai ditemukan
        if rootNode.leftChild is None:  # Jika hanya punya anak kanan (atau tidak punya anak)
            temp = rootNode.rightChild  # Simpan anak kanan
            rootNode = None  # Hapus node saat ini
            return temp  # Kembalikan anak sebagai pengganti
        elif rootNode.rightChild is None:  # Jika hanya punya anak kiri
            temp = rootNode.leftChild  # Simpan anak kiri
            rootNode = None  # Hapus node saat ini
            return temp  # Kembalikan anak sebagai pengganti
        temp = getMinValueNode(rootNode.rightChild)  # Jika punya dua anak, cari penerus di kanan
        rootNode.data = temp.data  # Salin data penerus ke node ini
        rootNode.rightChild = deleteNode(rootNode.rightChild, temp.data)  # Hapus node penerus yang asli
    balance = getBalance(rootNode)  # Cek keseimbangan setelah penghapusan
    if balance > 1 and getBalance(rootNode.leftChild) >= 0:  # Kasus LL
        return rightRotate(rootNode)  # Rotasi kanan
    if balance < -1 and getBalance(rootNode.rightChild) <= 0:  # Kasus RR
        return leftRotate(rootNode)  # Rotasi kiri
    if balance > 1 and getBalance(rootNode.leftChild) < 0:  # Kasus LR
        rootNode.leftChild = leftRotate(rootNode.leftChild)  # Rotasi kiri pada anak
        return rightRotate(rootNode)  # Rotasi kanan pada root
    if balance < -1 and getBalance(rootNode.rightChild) > 0:  # Kasus RL
        rootNode.rightChild = rightRotate(rootNode.rightChild)  # Rotasi kanan pada anak
        return leftRotate(rootNode)  # Rotasi kiri pada root
    
    return rootNode  # Kembalikan root yang sudah seimbang

def deleteAVL(rootNode):  # Fungsi menghapus seluruh pohon AVL
    rootNode.data = None  # Hapus data pada root
    rootNode.leftChild = None  # Putus hubungan ke anak kiri
    rootNode.rightChild = None  # Putus hubungan ke anak kanan
    return "The AVL has been successfully deleted"  # Kembalikan pesan sukses

if __name__ == "__main__":  # Memastikan kode di bawah hanya berjalan jika file ini dijalankan langsung
    newAVL = AVLNode(5)  # Membuat root awal dengan nilai 5
    newAVL = insertNode(newAVL, 10)  # Menyisipkan nilai 10
    newAVL = insertNode(newAVL, 15)  # Menyisipkan nilai 15
    newAVL = insertNode(newAVL, 20)  # Menyisipkan nilai 20
    levelOrderTraversal(newAVL)  # Menampilkan struktur pohon saat ini
    searchNode(newAVL, 15)  # Mencoba mencari nilai 15
    newAVL = deleteNode(newAVL, 10)  # Mencoba menghapus nilai 10
    levelOrderTraversal(newAVL)  # Menampilkan struktur pohon setelah dihapus

# jawaban/output :

# 10
# 5
# 15
# 20
# The value is found
# 15
# 5
# 20