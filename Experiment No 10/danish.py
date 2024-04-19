class Queue:
    def __init__(self):
        self.items = []

    def add(self, item):
        self.items.append(item)

    def remove(self):
        if not self.is_empty():
            return self.items.pop(0)
        else:
            print("Queue is empty")

    def search(self, item):
        if item in self.items:
            print("Item found in the queue")
        else:
            print("Item not found in the queue")

    def is_empty(self):
        return len(self.items) == 0

    def display(self):
        if not self.is_empty():
            print("Current Queue:", self.items)
        else:
            print("Queue is empty")


def main():
    queue = Queue()

    while True:
        print("\nMenu:")
        print("1. Add")
        print("2. Remove")
        print("3. Search")
        print("4. Display Queue")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            item = input("Enter item to add to the queue: ")
            queue.add(item)
            print(item, "added to the queue.")
        elif choice == "2":
            removed_item = queue.remove()
            if removed_item is not None:
                print("Removed item:", removed_item)
        elif choice == "3":
            item = input("Enter item to search in the queue: ")
            queue.search(item)
        elif choice == "4":
            queue.display()
        elif choice == "5":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
