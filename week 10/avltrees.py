# MADHU SATYA KUMAR KATTA
#AV.SC.U4CSE25118


class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.height = 1


class AVLTree:
    # Get height of a node
    def height(self, node):
        if node is None:
            return 0
        return node.height

    # Calculate balance factor
    def get_balance(self, node):
        if node is None:
            return 0
        return self.height(node.left) - self.height(node.right)

    # Update height of a node
    def update_height(self, node):
        node.height = 1 + max(
            self.height(node.left),
            self.height(node.right)
        )

    # Right rotation
    def right_rotate(self, y):
        x = y.left
        T2 = x.right

        x.right = y
        y.left = T2

        self.update_height(y)
        self.update_height(x)

        return x

    # Left rotation
    def left_rotate(self, x):
        y = x.right
        T2 = y.left

        y.left = x
        x.right = T2

        self.update_height(x)
        self.update_height(y)

        return y

    # Insert a key
    def insert(self, root, key):
        if root is None:
            return Node(key)

        if key < root.key:
            root.left = self.insert(root.left, key)
        elif key > root.key:
            root.right = self.insert(root.right, key)
        else:
            return root  # Duplicate keys are not allowed

        self.update_height(root)
        balance = self.get_balance(root)

        # LL Case
        if balance > 1 and key < root.left.key:
            return self.right_rotate(root)

        # RR Case
        if balance < -1 and key > root.right.key:
            return self.left_rotate(root)

        # LR Case
        if balance > 1 and key > root.left.key:
            root.left = self.left_rotate(root.left)
            return self.right_rotate(root)

        # RL Case
        if balance < -1 and key < root.right.key:
            root.right = self.right_rotate(root.right)
            return self.left_rotate(root)

        return root

    # Find the node with minimum key
    def min_value_node(self, root):
        current = root
        while current.left is not None:
            current = current.left
        return current

    # Delete a key
    def delete(self, root, key):
        if root is None:
            return None

        if key < root.key:
            root.left = self.delete(root.left, key)
        elif key > root.key:
            root.right = self.delete(root.right, key)
        else:
            # Node with one child or no child
            if root.left is None:
                return root.right
            elif root.right is None:
                return root.left

            # Node with two children
            temp = self.min_value_node(root.right)
            root.key = temp.key
            root.right = self.delete(root.right, temp.key)

        self.update_height(root)
        balance = self.get_balance(root)

        # LL Case
        if balance > 1 and self.get_balance(root.left) >= 0:
            return self.right_rotate(root)

        # LR Case
        if balance > 1 and self.get_balance(root.left) < 0:
            root.left = self.left_rotate(root.left)
            return self.right_rotate(root)

        # RR Case
        if balance < -1 and self.get_balance(root.right) <= 0:
            return self.left_rotate(root)

        # RL Case
        if balance < -1 and self.get_balance(root.right) > 0:
            root.right = self.right_rotate(root.right)
            return self.left_rotate(root)

        return root

    # Search for a key
    def search(self, root, key):
        if root is None or root.key == key:
            return root

        if key < root.key:
            return self.search(root.left, key)

        return self.search(root.right, key)

    # Inorder traversal: Left, Root, Right
    def inorder(self, root):
        if root:
            self.inorder(root.left)
            print(root.key, end=" ")
            self.inorder(root.right)

    # Preorder traversal: Root, Left, Right
    def preorder(self, root):
        if root:
            print(root.key, end=" ")
            self.preorder(root.left)
            self.preorder(root.right)

    # Postorder traversal: Left, Right, Root
    def postorder(self, root):
        if root:
            self.postorder(root.left)
            self.postorder(root.right)
            print(root.key, end=" ")

    # Find minimum key
    def find_min(self, root):
        if root is None:
            return None
        return self.min_value_node(root).key

    # Find maximum key
    def find_max(self, root):
        if root is None:
            return None

        while root.right is not None:
            root = root.right
        return root.key

    # Count total nodes
    def count_nodes(self, root):
        if root is None:
            return 0
        return 1 + self.count_nodes(root.left) + \
            self.count_nodes(root.right)

    # Display tree structure
    def display(self, root, level=0, prefix="Root: "):
        if root is not None:
            print(" " * (level * 4) + prefix + str(root.key))
            self.display(root.left, level + 1, "L--- ")
            self.display(root.right, level + 1, "R--- ")


# Main program
tree = AVLTree()
root = None

while True:
    print("\n\n--- AVL TREE MENU ---")
    print("1. Insert")
    print("2. Delete")
    print("3. Search")
    print("4. Inorder Traversal")
    print("5. Preorder Traversal")
    print("6. Postorder Traversal")
    print("7. Find Minimum")
    print("8. Find Maximum")
    print("9. Count Nodes")
    print("10. Display Tree")
    print("11. Height of Tree")
    print("12. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        key = int(input("Enter value to insert: "))
        root = tree.insert(root, key)
        print("Insertion completed.")

    elif choice == "2":
        key = int(input("Enter value to delete: "))
        if tree.search(root, key):
            root = tree.delete(root, key)
            print("Deletion completed.")
        else:
            print("Value not found.")

    elif choice == "3":
        key = int(input("Enter value to search: "))
        if tree.search(root, key):
            print("Value found.")
        else:
            print("Value not found.")

    elif choice == "4":
        print("Inorder:", end=" ")
        tree.inorder(root)
        print()

    elif choice == "5":
        print("Preorder:", end=" ")
        tree.preorder(root)
        print()

    elif choice == "6":
        print("Postorder:", end=" ")
        tree.postorder(root)
        print()

    elif choice == "7":
        result = tree.find_min(root)
        print("Minimum:", result if result is not None
              else "Tree is empty")

    elif choice == "8":
        result = tree.find_max(root)
        print("Maximum:", result if result is not None
              else "Tree is empty")

    elif choice == "9":
        print("Total nodes:", tree.count_nodes(root))

    elif choice == "10":
        if root is None:
            print("Tree is empty.")
        else:
            tree.display(root)

    elif choice == "11":
        print("Height:", tree.height(root))

    elif choice == "12":
        print("Exiting program.")
        break

    else:
        print("Invalid choice. Try again.")
