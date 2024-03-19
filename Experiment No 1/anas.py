# Create an empty list
my_list = []

# Take input from the user
n = int(input("Enter the number of elements: "))

# Add elements to the list
for i in range(n):
    element = int(input("Enter element {}: ".format(i+1)))
    my_list.append(element)

# Check if each element is odd or even
for element in my_list:
    if element % 2 == 0:
        print("{} is even".format(element))
    else:
        print("{} is odd".format(element))