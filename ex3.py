import random

class Node:
    def __init__(self, key):
        # Initialize a new node with the given key
        self.key = key
        self.left = None  # Left child
        self.right = None  # Right child
        self.height = 1  # Height of the node (used for balance factor calculation)

class AVLTree:
    def __init__(self):
        # Initialize an empty AVL tree
        self.root = None

    def insert(self, key):
        """Insert a node with the given key and identify pivot cases."""
        # Perform recursive insertion and capture the pivot case
        self.root, pivot_case = self._insert_recursive(self.root, key)
        print(pivot_case)  # Print the detected pivot case

    def _insert_recursive(self, node, key):
        # Base case: if the current node is None, insert a new node here
        if not node:
            return Node(key), "Case #1: Pivot not detected"

        # Recursively insert the key in the left or right subtree
        if key < node.key:
            node.left, pivot_case = self._insert_recursive(node.left, key)
        else:
            node.right, pivot_case = self._insert_recursive(node.right, key)

        # Update the height of the current node
        node.height = 1 + max(self._get_height(node.left), self._get_height(node.right))

        # Calculate the balance factor of the current node after updating the height
        balance = self.get_balance(node)
        print(balance)
        # If the node is unbalanced (balance factor > 1 or < -1), perform rotations
        if abs(balance) > 1:
            node, pivot_case = self.single_double_rotations(node, key)
            return node, pivot_case

        # Identify if insertion happened in the shorter subtree
        # Case #2 occurs if:
        # - Balance is 0 (tree was perfectly balanced before insertion)
        # - Insertion occurs on the left when balance > 0 (left-heavy tree)
        # - Insertion occurs on the right when balance < 0 (right-heavy tree)
        if balance == 0 or (key < node.key and balance > 0) or (key > node.key and balance < 0):
            return node, "Case #2: A pivot exists, and a node was added to the shorter subtree"

        # Otherwise, propagate the previous pivot case
        return node, pivot_case

    def _get_height(self, node):
        # Helper function to get the height of a node (returns 0 for None)
        return node.height if node else 0

    def get_balance(self, node):
        # Calculate the balance factor (height difference between left and right subtrees)
        if not node:
            return 0
        return self._get_height(node.left) - self._get_height(node.right)

    def single_double_rotations(self, node, key):
        # Perform appropriate rotation based on the balance factor.
        balance = self.get_balance(node)

        # Left-Left (LL) Case - Right rotation
        if balance > 1 and key < node.left.key:
            return self._right_rotate(node), "Case #3a: adding a node to an outside subtree"

        # Right-Right (RR) Case - Left rotation
        if balance < -1 and key > node.right.key:
            return self._left_rotate(node), "Case #3a: adding a node to an outside subtree"

        # Left-Right (LR) Case - Left rotation on left child, then right rotation on node
        if balance > 1 and key > node.left.key:
            print("DEBUG1")
            return node, "Case 3b not supported"

        # Right-Left (RL) Case - Right rotation on right child, then left rotation on node
        if balance < -1 and key < node.right.key:
            print("DEBUG2")
            return node, "Case 3b not supported"

        return node, "Case #3: Rotation not required"

    def _left_rotate(self, node):
        new_root = node.right
        node.right = new_root.left
        new_root.left = node

        # Update heights
        node.height = 1 + max(self._get_height(node.left), self._get_height(node.right))
        new_root.height = 1 + max(self._get_height(new_root.left), self._get_height(new_root.right))

        return new_root

    def _right_rotate(self, node):
        new_root = node.left
        node.left = new_root.right
        new_root.right = node

        # Update heights
        node.height = 1 + max(self._get_height(node.left), self._get_height(node.right))
        new_root.height = 1 + max(self._get_height(new_root.left), self._get_height(new_root.right))

        return new_root

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

    # Test Case 3a: Adding a node to an outside subtree
    print("Test Case 3:")
    tree.insert(1)
    print()

    # Test Case 4: Double Rotation (Left-Right case)
    print("Test Case 4:")
    tree.insert(2)
    print()

if __name__ == "__main__":
    run_test_cases()