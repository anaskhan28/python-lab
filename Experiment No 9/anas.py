class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def is_empty(self):
        len(self.items) == 0

    def pop(self):
        if self.is_empty():
            print("Stack is empty")
        else:
            return self.items.pop()

    def peek(self):
        if self.is_empty():
            print("Stack is empty")
        else:
            return self.items[-1]

    def display(self):
        if  self.is_empty():
            print("Stack is empty")
        else:
            print("Current Stack:", self.items)


def main():
    stack = Stack()

    while True:
        print("\nMenu:")
        print("1. Push")
        print("2. Pop")
        print("3. Peek")
        print("4. Display Stack")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            item = input("Enter item to push onto the stack: ")
            while item != "c" and item != "C":
                stack.push(item)
                print(item, "pushed onto the stack.\n")
                item = input("Enter item to push onto the stack: ")
        elif choice == "2":
            popped_item = stack.pop()
            if popped_item is not None:
                print("Popped item:", popped_item)
        elif choice == "3":
            peeked_item = stack.peek()
            if peeked_item is not None:
                print("Peeked item:", peeked_item)
        elif choice == "4":
            stack.display()
        elif choice == "5":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
