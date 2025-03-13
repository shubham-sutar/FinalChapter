# Strings

name = "Sayali"
short_name = name[0:4]
print(short_name)

last_char = name[-1]
print(f"last character of {name} is {last_char}")

name1 = "Sayali"
print(name1[-4:-1])  # printing index -4 to -1 (yali), -1 excluded -(yal) ✅

print(name1[:4])  # printing starts from 0 to 4(sayal), 4 excluded -(saya) ✅

print(name1[1:])  # printing starts from 1 to length (ayali) ✅

name2 = "sayalisutar"

#  s a y a l i s u t a r
#  0 1 2 3 4 5 6 7 8 9 10
print(name2[2:8:4])  # printing starts from 2-8(yalisu),(2,4 - ys)
print(name2[1:6:2])  # printing starts from 1-6(ayali),(1-2-2 - aai)
print(name2[1:9:4])  # printing starts from 1-9(ayalisut),(1-4 - ai)





