filename = input("Enter the filename: ")

try:
    with open(filename, 'r') as f:
        lines = f.readlines()

    letter_count = sum(len(word) for line in lines for word in line.split())
    word_count = sum(len(line.split()) for line in lines)
    line_count = len(lines)

    print(f"Number of letters: {letter_count}")
    print(f"Number of words: {word_count}")
    print(f"Number of lines: {line_count}")
except IOError:
    print(f"An error occurred while trying to read {filename}.")
except Exception as e:
    print(f"An unexpected error occurred: {str(e)}")