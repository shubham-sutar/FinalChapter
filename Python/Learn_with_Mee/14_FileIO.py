# File Input Output Operation
"""
with open('sample.txt', 'r') as file:
    print(file.read())
    file.close()

fp = open('sample.txt', 'r')
print(fp.read())
file.close()
"""

"""
try:
    with open('smple.txt', 'r') as file:
        print(file.read())
except FileNotFoundError as fnfe:
    print("I'm not able to find the file, check file name or path")
finally:
    print("file closed")
    file.close()
"""
"""
try:
    file = open('sample.txt', 'r')
    print(file.read())
except FileNotFoundError as fnfe:
    print("File not found, please check path of file")
finally:
    file.close()
    print("file closed!")
"""

"""
try:
    file = open('smple.txt', 'r')
    print(file.read())

except FileNotFoundError as fnfe:
    print("File not found, please check the path of file")

finally:
    try:
        file.close()
    except NameError as ne:
        print(ne)
"""

"""
class MyCustomException(Exception):
    def __init__(self, msg):
        self.msg = msg
        super().__init__(msg)


balance = 200
withdraw = int(input("Enter the amount to withdraw cash="))
if withdraw > balance:
    raise MyCustomException("Balance is low")
else:
    print("remaining Bal", (balance - withdraw))
"""
