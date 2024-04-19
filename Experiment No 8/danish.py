class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def add(self):
        data = input("\n(type 'c': to cancel adding elements.)\nEnter the element to add:")
        while data != "C" and data != "c":
            new_node = Node(data)
            if self.head is None:
                self.head = new_node
            else:
                current = self.head
                while current.next:
                    current = current.next
                current.next = new_node
            data = input("Enter the element to add:")

    def remove(self):
        data = input("Enter the element to remove: ")
        current = self.head
        if current is not None and current.data == data:
            self.head = current.next
            return
        prev = None
        while current is not None and current.data != data:
            prev = current
            current = current.next
        if current is None:
            print("Element not found in the list.")
            return
        prev.next = current.next

    def replace(self):
        old_data = input("Enter the element to replace: ")
        new_data = input("Enter the new element: ")
        current = self.head
        while current is not None:
            if current.data == old_data:
                current.data = new_data
                return
            current = current.next
        print("Element to replace not found in the list.")

    def search(self):
        data = input("Enter the element to search: ")
        current = self.head
        while current is not None:
            if current.data == data:
                print("Element found in the list.")
                return
            current = current.next
        print("Element not found in the list.")

    def display(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

    def exit(self):
        print("Exiting the program.")
        exit(0)


def menu():
    print("\nMenu:")
    print("1. Add element")
    print("2. Remove element")
    print("3. Replace element")
    print("4. Search element")
    print("5. Display list")
    print("6. Exit")


if __name__ == "__main__":
    linked_list = LinkedList()
    options = {
        "1": linked_list.add,
        "2": linked_list.remove,
        "3": linked_list.replace,
        "4": linked_list.search,
        "5": linked_list.display,
        "6": linked_list.exit,
    }
    while True:
        menu()
        choice = input("Enter your choice: ")
        if choice in options:
            options[choice]()
        else:
            print("Invalid choice. Please enter a valid option.")