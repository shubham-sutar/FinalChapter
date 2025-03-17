# problem 02
# 2. write a python program using function to convert Celsius to fahreinheit.


def convo(celsius):
    return (celsius * 9 / 5) + 32


celsius = float(input("Enter Celsius temp: "))
conversion = convo(celsius)

print(f"conversion of celsius : {celsius}°C to fahrenheit : {conversion}°F✅")
