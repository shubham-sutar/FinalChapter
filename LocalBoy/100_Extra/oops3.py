# Inheritance

# Single Inheritance

class Father:
    key = "abc@123"

    def father_method(self):
        return "father method"


class Child(Father):

    def child_method(self):
        return "child_methid"


obj = Child()
output = obj.child_method()
print(output)

output1 = obj.father_method()
print(output1)
