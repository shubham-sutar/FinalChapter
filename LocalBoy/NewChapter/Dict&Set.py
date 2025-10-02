# Dictionary and sets
"""
marks = {
    "shubham": 120,
    "sayali": 110,
    "rajeah": 125
}

print(marks, type(marks))
print(marks["shubham"])

marks["shubham"] = 99
print(marks)

# methods
print("------ Methods ------")
print(marks.items())
print(marks.keys(), marks.values())
marks.update({"shubham": 200, "renuka": 150})
print(marks)
marks.update({"rajesh": 125})
marks.pop("rajeah")
print(marks)
print(marks.get("shubham"))



s = {10, 500, 77, 81, 500, 77, 500}
print(s, type(s))

s.add(80)
print(s)

num = {22, 56, 78, "riya"}
names = {"leela", "riya", "madhuri", 56}

union_set = num.union(names)
print(f"union of set is {union_set}")

intersection_set = num.intersection(names)
print(f"intersection of set is {intersection_set}")
"""
