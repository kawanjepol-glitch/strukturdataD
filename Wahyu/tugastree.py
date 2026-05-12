import streamlit as st

# =========================
# NODE BST
# =========================
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


# =========================
# BINARY SEARCH TREE
# =========================
class BST:
    def __init__(self):
        self.root = None

    # Insert Node
    def insert(self, root, value):

        if root is None:
            return Node(value)

        if value < root.value:
            root.left = self.insert(root.left, value)

        else:
            root.right = self.insert(root.right, value)

        return root

    # Preorder
    def preorder(self, root, result):

        if root:
            result.append(root.value)
            self.preorder(root.left, result)
            self.preorder(root.right, result)

    # Inorder
    def inorder(self, root, result):

        if root:
            self.inorder(root.left, result)
            result.append(root.value)
            self.inorder(root.right, result)

    # Postorder
    def postorder(self, root, result):

        if root:
            self.postorder(root.left, result)
            self.postorder(root.right, result)
            result.append(root.value)

    # Visualisasi Tree
    def display_tree(self, node, level=0, prefix="Root: "):

        result = ""

        if node is not None:
            result += " " * (level * 4) + prefix + str(node.value) + "\n"

            if node.left:
                result += self.display_tree(
                    node.left,
                    level + 1,
                    "L--- "
                )

            if node.right:
                result += self.display_tree(
                    node.right,
                    level + 1,
                    "R--- "
                )

        return result


# =========================
# STREAMLIT
# =========================
st.title("TREE DATA STRUCTURE - BST")

st.write("### Data Awal BST")

data_awal = [50, 30, 70, 20, 40, 60, 80]

st.code(data_awal)

# Membuat BST
tree = BST()

for item in data_awal:
    tree.root = tree.insert(tree.root, item)

# Traversal Awal
pre = []
ino = []
post = []

tree.preorder(tree.root, pre)
tree.inorder(tree.root, ino)
tree.postorder(tree.root, post)

st.write("## Traversal Sebelum Penambahan Node")

st.write("### Preorder")
st.success(pre)

st.write("### Inorder")
st.success(ino)

st.write("### Postorder")
st.success(post)

# Tambah Node Baru
st.write("## Menambahkan Node Baru")

node_baru = [10, 90, 65]

st.code(node_baru)

for item in node_baru:
    tree.root = tree.insert(tree.root, item)

# Traversal Setelah Penambahan
pre2 = []
ino2 = []
post2 = []

tree.preorder(tree.root, pre2)
tree.inorder(tree.root, ino2)
tree.postorder(tree.root, post2)

st.write("## Traversal Setelah Penambahan Node")

st.write("### Preorder")
st.success(pre2)

st.write("### Inorder")
st.success(ino2)

st.write("### Postorder")
st.success(post2)

# Analisis
st.write("## Analisis Perubahan")

st.info("""
1. Node 10 masuk ke kiri node 20 karena lebih kecil.
2. Node 90 masuk ke kanan node 80 karena lebih besar.
3. Node 65 masuk ke kanan node 60 karena lebih besar dari 60 tetapi lebih kecil dari 70.
4. Traversal inorder tetap menghasilkan data terurut ascending.
""")

# Visualisasi Tree
st.write("## Visualisasi BST")

tree_visual = tree.display_tree(tree.root)

st.code(tree_visual)