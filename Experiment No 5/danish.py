def append_to_file(filename, data):
    if not filename.endswith('.txt'):
        raise ValueError("The file must be a .txt file.")

    with open(filename, 'a') as file:
        file.write(data + '\n')

def main():
    filename = input("Enter the filename: ")
    data = input("Enter the data you want to append to the file: ")

    try:
        append_to_file(filename, data)
        print("Data has been appended to the file.")
    except IOError:
        print(f"An error occurred while trying to write to {filename}.")
    except ValueError as ve:
        print(f"An error occurred: {str(ve)}")
    except Exception as e:
        print(f"An unexpected error occurred: {str(e)}")

if __name__ == "__main__":
    main()