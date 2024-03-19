import numpy as np
def calculate_sum(arr):
    sum_arr = sum(arr)
    print("Sum of the numbers are:", sum_arr)
    return sum_arr
def print_even_or_odd_numbers(arr, sum_arr):
    if sum_arr % 2 == 0:
        even_nums = [num for num in arr if num % 2 == 0]
        print("Even numbers in the array: ", even_nums)
    else:
        odd_nums = [num for num in arr if num % 2 != 0]
        print("Odd numbers in the array: ", odd_nums)
def calculate_average(arr):
    try:
        avg = sum(arr) / len(arr)
        print("Average of the array: ", avg)
    except ZeroDivisionError:
        print("\nError: Division by zero is not allowed.")
def generate_type_error(arr):
    try:
        error = arr + "string"
    except TypeError:
        print("Error: Operation between string and integer is not allowed.")
def create_array():
    arr = [45,46,50,96,10]
    sum_arr = calculate_sum(arr)
    print_even_or_odd_numbers(arr, sum_arr)
    calculate_average(arr)
    generate_type_error(arr)

create_array()