# Dictionary = key value pair
# 1. It is unordered
# 2. It is mutable
# 3. It is indexed
# 4. cannot contain duplicate keys.


marks = {
    "harry": 76,
    "shubham": 84,
    "sayali": 44
}

print(marks, type(marks))
print(marks["harry"])

# Dictionary Methods

print(marks.items())
print(marks.keys())
marks.update({"sasuke": 74, "sakura": 80})
print(marks)
print(marks.get("shubham"))
print(marks["sayali"])
print(marks.pop("sasuke"))
print(marks)



