# import numpy as np
# def create_array():
#     arr = np.array([5])
#     sum_arr = np.sum(arr)
#     print("Sum of the numbers are:", sum_arr);
#     if sum_arr % 2 == 0:
#         even_nums = list(filter(lambda x: x % 2 == 0, arr))
#         print("Even numbers in the array: ", even_nums)
#     else:
#         odd_nums = list(filter(lambda x: x % 2 != 0, arr))
#         print("Odd numbers in the array: ", odd_nums);
#     if arr.size != 0:
#         avg = np.mean(arr)
#         print("Average of the array: ", avg)
#     else:
#         print("Error: Cannot calculate the mean of an empty array.")
#     try:
#         error = arr + '2'
#     except TypeError:
#         print("Error: Operation between string and integer is not allowed.")
# create_array()



import numpy as np
def calculate_sum(arr):
    sum_arr = np.sum(arr)
    print("Sum of the numbers are:", sum_arr)
    return sum_arr

def print_even_or_odd_numbers(arr, sum_arr):
    if sum_arr % 2 == 0:
        even_nums = list(filter(lambda result: result % 2 == 0, arr))
        print("Even numbers in the array: ", even_nums)
    else:
        odd_nums = list(filter(lambda y: y % 2 != 0, arr))
        print("Odd numbers in the array: ", odd_nums)
def calculate_average(arr):
    if arr.size != 0:
        avg = np.mean(arr)
        print("Average of the array: ", avg)
    else:
        print("\nError: Division by zero is not allowed.");
def generate_type_error(arr):
    try:
        error = arr 
    except TypeError:
        print("Error: Operation between string and integer is not allowed.");


def create_array():
    arr = np.array([45,46,50,96,10])
    sum_arr = calculate_sum(arr)
    print_even_or_odd_numbers(arr, sum_arr)
    calculate_average(arr)
    generate_type_error(arr)

create_array()



