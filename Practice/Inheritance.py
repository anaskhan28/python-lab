
class Employee:
    def __init__(self, name, age, salary) -> None:
        self.name = name
        self.age = age
        self.salary = salary

    def __str__(self) -> str:
        info = f'name = {self.name}, age = {self.age}, salary = {self.salary}'
        return info
    
    def work(self):
        print(f"{self.name} is working...")


class Developer(Employee):
    
    def __init__(self, name, age, salary, level) -> None:
        super().__init__(name, age, salary)
        self.level = level


    def __str__(self) -> str:
        info = super().__str__()
        info += f', level = {self.level}'
        return info
    
    def work(self):
       print(f"{self.name} is coding...")

class Designer(Employee):
     def work(self):
       print(f"{self.name} is designing...")


se1 = Developer("Anas", 21, 5312, "SDE1")
# print(se1)
# se1.work()

d1 = Designer("Arshad", 22, 4527)
# print(d1)
# d1.work()


employees = [
    Developer("Anas", 21, 5312, "SDE1"),
    Designer("Arshad", 22, 4527)
]


def motivate_employee(employees):
    for employee in employees:
        employee.work()

motivate_employee(employees)