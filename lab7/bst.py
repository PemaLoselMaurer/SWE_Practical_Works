from collections import deque

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        if not self.root:
            self.root = Node(value)
        else:
            self._insert_recursive(self.root, value)

    def _insert_recursive(self, node, value):
        if value < node.value:
            if node.left is None:
                node.left = Node(value)
            else:
                self._insert_recursive(node.left, value)
        elif value > node.value:
            if node.right is None:
                node.right = Node(value)
            else:
                self._insert_recursive(node.right, value)

    def search(self, value):
        return self._search_recursive(self.root, value)

    def _search_recursive(self, node, value):
        if node is None or node.value == value:
            return node
        if value < node.value:
            return self._search_recursive(node.left, value)
        return self._search_recursive(node.right, value)

    def inorder_traversal(self):
        result = []
        self._inorder_recursive(self.root, result)
        return result

    def _inorder_recursive(self, node, result):
        if node:
            self._inorder_recursive(node.left, result)
            result.append(node.value)
            self._inorder_recursive(node.right, result)

    def preorder_traversal(self):
        result = []
        self._preorder_recursive(self.root, result)
        return result

    def _preorder_recursive(self, node, result):
        if node:
            result.append(node.value)
            self._preorder_recursive(node.left, result)
            self._preorder_recursive(node.right, result)

    def postorder_traversal(self):
        result = []
        self._postorder_recursive(self.root, result)
        return result

    def _postorder_recursive(self, node, result):
        if node:
            self._postorder_recursive(node.left, result)
            self._postorder_recursive(node.right, result)
            result.append(node.value)

    def delete(self, value):
        self.root = self._delete_recursive(self.root, value)

    def _delete_recursive(self, node, value):
        if node is None:
            return node

        if value < node.value:
            node.left = self._delete_recursive(node.left, value)
        elif value > node.value:
            node.right = self._delete_recursive(node.right, value)
        else:
            # Node with only one child or no child
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left

            # Node with two children
            node.value = self._min_value(node.right)
            node.right = self._delete_recursive(node.right, node.value)

        return node

    def _min_value(self, node):
        current = node
        while current.left is not None:
            current = current.left
        return current.value

    def find_max(self):
        if not self.root:
            return None  # Tree is empty, so there's no maximum value.
        
        current = self.root
        while current.right:
            current = current.right
        
        return current.value
    
    def count_nodes(self):
        return self._count_nodes_recursive(self.root)

    def _count_nodes_recursive(self, node):
        if node is None:
            return 0 
        else:
            return 1 + self._count_nodes_recursive(node.left) + self._count_nodes_recursive(node.right)
        
    def level_order_traversal(self):
        if not self.root:
            return []  # Return an empty list if the tree is empty
        
        result = []
        queue = deque([self.root])  # Initialize the queue with the root node
        
        while queue:
            current = queue.popleft()  # Dequeue the front node
            result.append(current.value)  # Process the current node
            
            # Enqueue left and right children if they exist
            if current.left:
                queue.append(current.left)
            if current.right:
                queue.append(current.right)
        
        return result
        
    def height(self):
        return self._height_recursive(self.root)

    def _height_recursive(self, node):
        if node is None:
            return -1  # Base case: height of an empty tree is -1
        else:
            # Recursively find the height of left and right subtrees
            left_height = self._height_recursive(node.left)
            right_height = self._height_recursive(node.right)
            return 1 + max(left_height, right_height)  # Height of current node
        
    def is_valid_bst(self):
        def validate(node, low=float('-inf'), high=float('inf')):
            if node is None:
                return True
            val = node.value
            if val <= low or val >= high:
                return False
            return (validate(node.left, low, val) and 
                    validate(node.right, val, high))

        return validate(self.root)
    
# Test insertion
bst = BinarySearchTree()
for value in [5, 3, 7, 2, 4, 6, 8]:
    bst.insert(value)

# Test search
print(bst.search(4))  # Should return a Node
print(bst.search(9))  # Should return None

# Test traversals
print("In-order:", bst.inorder_traversal())
print("Pre-order:", bst.preorder_traversal())
print("Post-order:", bst.postorder_traversal())

# max value
max_value = bst.find_max()
print("Max value:", max_value) 

# count nodes
total_nodes = bst.count_nodes()
print("Total nodes:", total_nodes)

# traversal
level_order = bst.level_order_traversal()
print("Level-order Traversal:", level_order)

#tree
tree_height = bst.height()
print("Height of the BST:", tree_height)

# valid
print("Is valid BST:", bst.is_valid_bst()) 

# Test deletion
bst.delete(3)
print("After deleting 3:", bst.inorder_traversal())


