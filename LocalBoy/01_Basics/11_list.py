# List

friends = ["shubham", "sayali", "Orange", "False", "integer"]

print(friends[0])
friends[2] = "loves"
print(friends)
print(friends[1:3])

# Methods

# Insertion [.append]

friends.append("bheem")
print(friends)  # add bheem to end of the list(at the end)

# insertion [.insert]
digits = [13, 11, 1, 5, 8]
digits.insert(3, 99)
print(digits)  # added 99 at 3 index

# Sort

friends.sort()
print(friends)

friends[0] = "false"
print(friends)

friends.sort()
print(friends)

# reverse
cars = ["mustang", "pagani", "ds", "dart", "vulcan"]
cars.reverse()
print(cars)



