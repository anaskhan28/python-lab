import numpy as np

def create_array():
    # Create a numpy array
    arr = np.array([45,6,88,99,100])

    # Calculate the sum of the array
    sum_arr = np.sum(arr)
    print("Sum of the numbers are:", sum_arr);

    # Check if the sum is even or odd
    if sum_arr % 2 == 0:
        # If even, print all even numbers in the array
        even_nums = list(filter(lambda x: x % 2 == 0, arr))
        print("Even numbers in the array: ", even_nums)
    else:
        # If odd, print all odd numbers in the array
        odd_nums = list(filter(lambda x: x % 2 != 0, arr))
        print("Odd numbers in the array: ", odd_nums);
    
      # Calculate the average of the array
    if arr.size != 0:
        avg = np.mean(arr)
        print("Average of the array: ", avg)
    else:
        print("Error: Cannot calculate the mean of an empty array.")

    try:
        error = arr + '2'
    except TypeError:
        print("Error: Operation between string and integer is not allowed.")

create_array()



