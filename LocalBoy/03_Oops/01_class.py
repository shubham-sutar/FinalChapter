# class

class Employee:
    name = "shubham"  # variables/ class attributes
    language = "python"
    salary = 50000


obj = Employee()
# obj.name = "sayali"  # instance attribute01_class.py
new_user = obj.name, obj.language, obj.salary
print(f"--------- New Employee Informaion ---------\n{new_user}")
