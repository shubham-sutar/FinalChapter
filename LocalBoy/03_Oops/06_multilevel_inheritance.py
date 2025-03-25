# Inheritance
# multi level Inheritance

class Manager:
    company = "Softcorp India"


class Programmer(Manager):
    programming_lang = "python"


class Coder(Programmer):
    basic_salary = 25000


obj1 = Manager()
print(obj1.company)

obj2 = Programmer()
print(obj2.company, obj2.programming_lang)

obj3 = Coder()
print(obj3.company, obj3.programming_lang, obj3.basic_salary)

