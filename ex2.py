import random

class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.height = 1

class AVLTree:
    def __init__(self):
        self.root = None
    
    def insert(self, key):
        """Insert a node and identify pivot cases."""
        self.root, pivot_case = self._insert_recursive(self.root, key)
        print(pivot_case)
    
    def _insert_recursive(self, node, key):
        if not node:
            return Node(key), "Case #1: Pivot not detected"
        
        if key < node.key:
            node.left, pivot_case = self._insert_recursive(node.left, key)
        else:
            node.right, pivot_case = self._insert_recursive(node.right, key)
        
        # Update height
        node.height = 1 + max(self._get_height(node.left), self._get_height(node.right))
        
        # Identify pivot node (first unbalanced node up the recursion)
        balance = self.get_balance(node)
        if abs(balance) > 1:
            return node, "Case 3 not supported"
        
        # Determine if insertion happened in the shorter subtree
        if balance == 0 or (key < node.key and balance > 0) or (key > node.key and balance < 0):
            return node, "Case #2: A pivot exists, and a node was added to the shorter subtree"
        
        return node, pivot_case
    
    def _get_height(self, node):
        return node.height if node else 0
    
    def get_balance(self, node):
        if not node:
            return 0
        return self._get_height(node.left) - self._get_height(node.right)

# Test Cases
def run_test_cases():
    tree = AVLTree()
    
    # Test Case 1: Pivot not detected
    print("Test Case 1:")
    tree.insert(10)
    print()
    
    # Test Case 2: A pivot exists, and a node was added to the shorter subtree
    print("Test Case 2:")
    tree.insert(5)
    print()
    
    # Test Case 3: Case 3 not supported (Unbalanced insert)
    print("Test Case 3:")
    tree.insert(1)
    print()

if __name__ == "__main__":
    run_test_cases()
