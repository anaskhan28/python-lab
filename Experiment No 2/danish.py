my_dict = {}
n = int(input("Enter the number of people: "))
for _ in range(n):
    name = input("Enter the name: ")
    age = int(input("Enter the age: "))
    my_dict[name] = age
all_people = [f'{name}:{age}' for name, age in my_dict.items()]
senior_citizens = [f'{name}:{age}' for name, age in my_dict.items() if age > 60]
no_license = [f'{name}:{age}' for name, age in my_dict.items() if age < 18]
eligible_15g = [f'{name}:{age}' for name, age in my_dict.items() if age > 15 and age > 80]
print("Name of all human")
print(all_people)
print("Name of senior citizens")
print(senior_citizens)
print("Name of no license")
print(no_license)
print("Name of eligible 15g")
print(eligible_15g)