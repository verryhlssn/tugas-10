# Soal 4 (Sedang)
# Implementasi Trie Dictionary
# Deskripsi

# Buat aplikasi kamus sederhana menggunakan Trie.

# Fitur:

# Insert kata
# Search kata
# Menampilkan semua kata yang memiliki prefix tertentu
# Contoh Data
# apple
# application
# apply
# banana
# band
# bank
# Input
# app

# Output

# apple
# application
# apply

# Ketentuan

# Implementasikan:

# InsertWord()
# SearchWord()
# FindPrefix()
# Tujuan Pembelajaran

# Mahasiswa memahami:

# Trie Node
# Prefix Searching
# Autocomplete sederhana

class TrieNode:

    def __init__(self):
        self.children = {}
        self.end_word = False


class Trie:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):

        node = self.root

        for char in word:

            if char not in node.children:
                node.children[char] = TrieNode()

            node = node.children[char]

        node.end_word = True

    def search(self, word):

        node = self.root

        for char in word:

            if char not in node.children:
                return False

            node = node.children[char]

        return node.end_word

    def collect_words(self, node, prefix, result):

        if node.end_word:
            result.append(prefix)

        for char, child in node.children.items():
            self.collect_words(
                child,
                prefix + char,
                result
            )

    def find_prefix(self, prefix):

        node = self.root

        for char in prefix:

            if char not in node.children:
                return []

            node = node.children[char]

        result = []

        self.collect_words(
            node,
            prefix,
            result
        )

        return result


trie = Trie()

words = [
    "apple",
    "application",
    "apply",
    "banana",
    "band",
    "bank"
]

for word in words:
    trie.insert(word)

hasil = trie.find_prefix("app")

for kata in hasil:
    print(kata)

# jawaban/output :

# apple
# application
# apply