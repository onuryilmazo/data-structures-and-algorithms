class TreeNode:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key 

    
class BinarySearchTree:
    def __init__(self) -> None:
        self.root = None

    def insert(self, root, key):
        if root is None:
            return TreeNode(key)
        if key < root.val:
            root.left = self.insert(root.left ,key)
        else:
            root.right = self.insert(root.right, key)
        return root

    def search(self, root, key):
        if root is None or root.val == key:
            return root
        if root.val < key:
            return self.search(root.right, key)
        else: 
            return self.search(root.left, key)
    
    def delete(self, root, key):
        if root is None:
            return root
        
        if key < root.val:
            root.left = self.delete(root.left, key)
        elif key > root.val:
            root.right = self.delete(root.right, key)
        else:
            if root.left is None:
                return root.right
            elif root.right is None:
                return root.left
            
            root.val = self.minimum_value_node(root.right).val
            root.right = self.delete(root.right, root.val)

        return root

    def minimum_value_node(self, node):
        current = node
        while(current.left is not None):
            current = current.left
        return current

    def inorder_traversal(self, root):
        result = []
        if root:
            result = self.inorder_traversal(root.left)
            result.append(root.val)
            result = result + self.inorder_traversal(root.right)
        return result

    # BST oluştur
bst = BinarySearchTree()
root = None
keys = [50, 30, 70, 20, 40, 60, 80]

for key in keys:
    root = bst.insert(root, key)

# Düğümleri sırayla ekrana yazdır
print("Inorder traversal:")
result = bst.inorder_traversal(root)
print(result)

# Bir öğeyi ara
search_key = 60
result_node = bst.search(root, search_key)
if result_node:
    print(f"{search_key} bulundu.")
else:
    print(f"{search_key} bulunamadı.")

# Bir öğeyi sil
delete_key = 30
root = bst.delete(root, delete_key)
print(f"{delete_key} silindi.")

# Güncellenmiş ağacı tekrar yazdır
print("Inorder traversal (güncellenmiş):")
result = bst.inorder_traversal(root)
print(result)
