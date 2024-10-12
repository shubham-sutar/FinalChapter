"""
class Person:
    name = "amit"  # instance variable
    age = None

    def walk(self):
        id = 1001  # local variable
        print("I am a simple method")
        print("Hi", self.age)


obj = Person()
amit.walk()
"""

"""
class Car:
    name = None
    model = None
    make = None

    def __init__(self, o_name, o_model, o_make):
        self.name = o_name
        self.model = o_model
        self.make = o_make

    def new_audi(self):
        print("launching a with name", self.name)
        print("launched car model is", self.model)
        print("launched car make in", self.make)


obj = Car("Audi", 2022, "india")
obj.new_audi()
"""

"""
class Employee:
    name = None
    id = None
    salary = None

    def __init__(self, f_name, f_id, f_salary):
        self.name = f_name
        self.id = f_id
        self.salary = f_salary

    def emp_info(self):
        print("Employee name is", self.name)
        print("Employee id is", self.id)
        print("Employee salary is", self.salary)


obj = Employee("sabrina", 1001, 20000)
obj.emp_info()
"""

"""
class VwoLogin:
    email = None
    password = None

    def __init__(self, o_email, o_password):
        self.email = o_email
        self.password = o_password

    def login(self):
        if self.email == "shubhamsutar@gmail.com" and self.password == "shubh123":
            print("logged in seccessfully")
        else:
            print("failed to login")


user1 = VwoLogin("shubhamsutar@gmail.com", "shubh123")
user1.login()  # login

user2 = VwoLogin("sayalisutar@gmail.com", "sayali123")
user2.login()
"""

# Encapsulation
# bind the data variable with the methods
# Data Member - / class Variables
# Methods - Def function within the class
# Wrapping or binding the data variable with the methods - Encapsulation.
# Hide the data members(class variables, instance variables) by using only the methods.
"""
class MyClass:

    def __init__(self):
        self.name = "Sayali"
        print(self.name)

    def public_func(self):
        print("public function")

    def __private_func(self):
        print("This is private")

    def public_fn_privat(self):
        self.__private_func()


# security --> Not everyone can access your variables/methods

obj1 = MyClass()  # Object creation

obj1.public_func()  # public method call

obj1.public_fn_privat()  # make private callable

obj1.__init__()  # constructor call

# obj1.__private_func() error
"""

# email and password changed because its Public
"""
class VwoLogin:

    def __init__(self, email, password):
        self.email = email
        self.password = password

    def person_login(self):
        if self.email == "sayalisutar@gmail.com" and self.password == "sayali@123":
            print("login successfully")
        else:
            print("login failed..")


obj1 = VwoLogin("sayalisutar@gmail.com", "sayali@123")

obj1.email = "??"  # email = email changed
obj1.password = "??"  # password = password changed
obj1.person_login()  # Output = login failed because email, pass changed.
"""

# email and password Not changed because its Private
"""
class VwoLogin:
    def __init__(self, email, password, name):
        self.__email = email
        self.__password = password
        self.name = name

    def person_login(self):
        if self.__email == "sayu@gmail.com" and self.__password == "sayu123":
            print("login successfully")
        else:
            print("login failed")


obj1 = VwoLogin("sayu@gmail.com", "sayu123", "sayali")
obj1.__email = "shubham@gmail.com"  # Not changed not access by outsider
obj1.__password = "shubham123"  # # Not changed not access by outsider

"""
# print(obj1.name)  accessible because its public. // sayali
# print(obj1.__email) Not accessible because its private. // error
"""

obj1.person_login()  # Output = login successfully
"""

"""
class BankAccount:
    def __init__(self):
        self.balance = 0
        self.__private_var = 100

    def public_fn(self):
        print(self.__private_var)

    def deposit(self, balance):
        self.balance += balance

    def __withdraw(self, balance):
        self.balance -= balance

    def __show_balance(self):
        print("Your Balance is ", self.balance)

    def if_you_are_auth(self, flag):
        if flag:
            self.__show_balance()
        else:
            print("Not Allowed")

    def if_you_are_auth_user(self, auth, balance):
        if auth:
            self.__withdraw(balance=balance)
        else:
            print("Not Allowed")


jp_chase = BankAccount()
jp_chase.deposit(200)

secret_pass = input("Enter your PIN to see Balance")
if secret_pass == "1234":
    jp_chase.if_you_are_auth(True)
else:
    jp_chase.if_you_are_auth(False)

secret_pass = input("Enter your PIN to Withdraw: ")
your_amount = int(input("Enter your amount to Withdraw: "))
if secret_pass == "1234":
    jp_chase.if_you_are_auth_user(True, balance=your_amount)
    jp_chase.if_you_are_auth(True)
else:
    jp_chase.if_you_are_auth_user(False)
"""
"""
class Password:
    def __init__(self, password):
        self.__password = password
        self.public_var = 10

    def get_pwd(self, is_auth):
        if is_auth:
            print(self.__password)
        else:
            print("Invalid password")

    def set_pwd(self, password):
        if password.endswith("9"):
            if len(password) > 10:
                self.__password = password
                print("Set to correct", self.__password)
            else:
                print("Not allowed, weak password")


pwd = Password("Hacker123")
pwd.get_pwd(True)
pwd.set_pwd("piuytrewqfghj9")
"""