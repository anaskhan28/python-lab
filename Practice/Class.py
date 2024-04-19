se1 = ["Software Engineer", "Anas", "senior", "21", "80000"]
se2 = ["Software Engineer", "Arshad", "20", "70000"]

class SoftwareEngineers:
    

    def __init__(self, name, age, level, salary):
        self.name = name
        self.age = age
        self.level = level
        self.salary = salary
    
    def code(self):
        print(f"{self.name} is writig code..")
    
    def code_in_language(self, language) -> code:
        print(f"{self.name} is writing code in {language}")



    #  dunder method
    def __str__(self) -> str:
        information = f'name = {self.name}, age = {self.age}, level = {self.level}'
        return information
    
    def __eq__(self, value: object) -> bool:
        return self.name == value.name and self.age == value.age
    
    @staticmethod
    def entry_salary( age):
        if age <25:
            return 35353
        if age < 30:
            return 24000
        return 852000
   

se1 = SoftwareEngineers("Anas", 21, "Senior", 90000);
se2 = SoftwareEngineers("Anas", 21, "Senior", 90000);


se1.code()
print(se1)
se1.code_in_language("python")

print(se1 != se2)

print(se1.entry_salary(23))