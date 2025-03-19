import random
import time
import matplotlib.pyplot as plt

class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.height = 1  # Track height for balance calculation

class BST:
    def __init__(self):
        self.root = None
    
    def insert(self, key):
        """Insert a key into the BST."""
        if not self.root:
            self.root = Node(key)
        else:
            self.root = self._insert_recursive(self.root, key)
    
    def _insert_recursive(self, node, key):
        if not node:
            return Node(key)
        if key < node.key:
            node.left = self._insert_recursive(node.left, key)
        else:
            node.right = self._insert_recursive(node.right, key)
        node.height = 1 + max(self._get_height(node.left), self._get_height(node.right))
        return node
    
    def search(self, key):
        """Search for a key in the BST."""
        return self._search_recursive(self.root, key)
    
    def _search_recursive(self, node, key):
        if not node or node.key == key:
            return node
        if key < node.key:
            return self._search_recursive(node.left, key)
        return self._search_recursive(node.right, key)
    
    def _get_height(self, node):
        """Return the height of a node."""
        return node.height if node else 0
    
    def get_balance(self, node):
        """Return the balance factor of a node."""
        if not node:
            return 0
        return self._get_height(node.left) - self._get_height(node.right)
    
    def get_max_absolute_balance(self):
        """Compute the maximum absolute balance factor in the BST."""
        return self._max_absolute_balance(self.root)
    
    def _max_absolute_balance(self, node):
        if not node:
            return 0
        left_balance = self._max_absolute_balance(node.left)
        right_balance = self._max_absolute_balance(node.right)
        return max(abs(self.get_balance(node)), left_balance, right_balance)

def generate_search_tasks():
    """Generate 1000 search tasks by shuffling a list of integers (0-999) 1000 times."""
    numbers = list(range(1000))
    tasks = []
    for _ in range(1000):
        random.shuffle(numbers)
        tasks.append(list(numbers))
    return tasks

def measure_performance(bst, search_tasks):
    """Measure search performance and max absolute balance for each task."""
    performance_results = []
    
    for task in search_tasks:
        start_time = time.time()
        for key in task:
            bst.search(key)
        end_time = time.time()
        search_time = (end_time - start_time) / len(task)  # Average search time
        max_balance = bst.get_max_absolute_balance()
        performance_results.append((max_balance, search_time))
    
    return performance_results

def plot_results(performance_results):
    """Generate a scatter plot of absolute balance vs. search time."""
    balances, search_times = zip(*performance_results)
    
    plt.figure(figsize=(8, 6))
    plt.scatter(balances, search_times, alpha=0.5)
    plt.xlabel("Absolute Balance")
    plt.ylabel("Average Search Time (seconds)")
    plt.title("Scatter Plot of Balance vs. Search Performance")
    plt.show()

# Main execution
bst = BST()
values = list(range(1000))  # Insert values 0-999 in order
random.shuffle(values)  # Randomize insertion order
for value in values:
    bst.insert(value)

search_tasks = generate_search_tasks()
performance_results = measure_performance(bst, search_tasks)
plot_results(performance_results)
