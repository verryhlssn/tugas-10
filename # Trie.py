class TrieNode:  # Definisi kelas untuk node dalam struktur data Trie
    def __init__(self):  # Inisialisasi node baru
        self.children = {}  # Dictionary untuk menyimpan anak-anak node (karakter)
        self.endOfString = False  # Penanda apakah node ini adalah akhir dari sebuah kata

class Trie:  # Definisi kelas utama untuk Trie
    def __init__(self):  # Inisialisasi Trie baru
        self.root = TrieNode()  # Root node kosong sebagai titik awal
    
    def insertString(self, word):  # Fungsi untuk memasukkan kata ke dalam Trie
        current = self.root  # Mulai penelusuran dari root
        for i in word:  # Loop untuk setiap karakter dalam kata
            ch = i  # Ambil karakter saat ini
            node = current.children.get(ch)  # Cek apakah karakter sudah ada sebagai anak
            if node == None:  # Jika karakter belum ada
                node = TrieNode()  # Buat node baru untuk karakter tersebut
                current.children.update({ch:node})  # Tambahkan ke dictionary anak-anak
            current = node  # Pindah ke node karakter selanjutnya
        current.endOfString = True  # Tandai node terakhir sebagai akhir dari kata
        print("Successfully inserted")  # Cetak pesan sukses
    
    def searchString(self, word):  # Fungsi untuk mencari keberadaan kata dalam Trie
        currentNode = self.root  # Mulai pencarian dari root
        for i in word:  # Loop setiap karakter dalam kata yang dicari
            node = currentNode.children.get(i)  # Ambil node untuk karakter saat ini
            if node == None:  # Jika karakter tidak ditemukan di jalur yang ada
                return False  # Kata tidak ada dalam Trie
            currentNode = node  # Lanjut ke node karakter berikutnya

        if currentNode.endOfString == True:  # Cek jika karakter terakhir ditandai sebagai akhir kata
            return True  # Kata ditemukan sepenuhnya
        else:  # Jika hanya prefix (awalan) dari kata lain
            return False  # Kata tidak ditemukan sebagai entitas utuh
        

def deleteString(root, word, index):  # Fungsi rekursif untuk menghapus kata dari Trie
    if index >= len(word):  # Cek batas index untuk mencegah error
        return False  # Berhenti jika index melebihi panjang kata
    ch = word[index]  # Ambil karakter kata pada index saat ini
    currentNode = root.children.get(ch)  # Ambil node anak yang sesuai dengan karakter
    if currentNode == None:  # Jika jalur kata tidak ditemukan (proteksi error)
        return False  # Penghapusan gagal karena kata tidak ada
    canThisNodeBeDeleted = False  # Variabel untuk menandai status penghapusan

    if len(currentNode.children) > 1:  # Jika node ini memiliki lebih dari satu jalur (bercabang)
        deleteString(currentNode, word, index+1)  # Lanjutkan ke karakter berikutnya tanpa menghapus node ini
        return False  # Node ini tidak boleh dihapus karena digunakan kata lain
    
    if index == len(word) - 1:  # Jika sudah sampai pada karakter terakhir dari kata yang ingin dihapus
        if len(currentNode.children) >= 1:  # Jika karakter terakhir ini punya anak (prefix kata lain)
            currentNode.endOfString = False  # Cukup hapus tanda akhir katanya saja
            return False  # Node fisiknya jangan dihapus
        else:  # Jika benar-benar node daun (leaf node)
            root.children.pop(ch)  # Hapus node ini dari parent-nya
            return True  # Beritahu parent bahwa node ini berhasil dihapus
    
    if currentNode.endOfString == True:  # Jika di tengah proses ketemu node yang juga akhir kata lain
        deleteString(currentNode, word, index+1)  # Lanjutkan rekursi untuk sisa karakter kata target
        return False  # Jangan hapus node ini karena merupakan bagian kata lain

    canThisNodeBeDeleted = deleteString(currentNode, word, index+1)  # Rekursi dan simpan status penghapusan di bawahnya
    if canThisNodeBeDeleted == True:  # Jika node di bawahnya sukses dihapus dan tidak bercabang
        root.children.pop(ch)  # Hapus node saat ini dari parent-nya
        return True  # Beritahu parent di atasnya untuk mencoba menghapus juga
    else:  # Jika node di bawah tidak bisa dihapus
        return False  # Jangan hapus node di level ini

if __name__ == "__main__":  # Memastikan pengujian hanya berjalan saat file dieksekusi langsung
    newTrie = Trie()  # Membuat instance Trie baru
    newTrie.insertString("App")  # Memasukkan kata "App"
    newTrie.insertString("Appl")  # Memasukkan kata "Appl"
    deleteString(newTrie.root, "App", 0)  # Mencoba menghapus "App"
    print(newTrie.searchString("App"))  # Harus menghasilkan False (karena sudah dihapus)
    print(newTrie.searchString("Appl"))  # Harus tetap True (karena tidak ikut terhapus)

# jawaban/output :

# Successfully inserted
# Successfully inserted
# False
# True