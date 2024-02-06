import numpy as np

# Function to calculate and print the sum of the array
def calculate_sum(arr):
    sum_arr = np.sum(arr)
    print("Sum of the numbers are:", sum_arr)
    return sum_arr

# Function to print even or odd numbers based on the sum
def print_even_or_odd_numbers(arr, sum_arr):
    if sum_arr % 2 == 0:
        even_nums = list(filter(lambda result: result % 2 == 0, arr))
        print("Even numbers in the array: ", even_nums)
    else:
        odd_nums = list(filter(lambda y: y % 2 != 0, arr))
        print("Odd numbers in the array: ", odd_nums)

# Function to calculate and print the average of the array
def calculate_average(arr):
     # Calculate the average of the array
    if arr.size != 0:
        avg = np.mean(arr)
        print("Average of the array: ", avg)
    else:
        print("\nError: Division by zero is not allowed.")

# Function to generate a TypeError
def generate_type_error():
    try:
        error = '2' + 2
    except TypeError:
        print("Error: Operation between string and integer is not allowed.")

# Main function to create the array and call the other functions
def create_array():
    arr = np.array([])
    sum_arr = calculate_sum(arr)
    print_even_or_odd_numbers(arr, sum_arr)
    calculate_average(arr)
    generate_type_error()

create_array()