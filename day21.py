#Tuples
tup1 = (1, 2, 3, 55, 5, 6, 7)
tup2 = ("red", "green", "blue")
print(type(tup1), tup1)
print(type(tup2), tup2)

print(tup1[0])
print(tup1[1])
print(tup1[2])

if 55 in tup1:
    print("yes 55 is present in this tuple")
tup2 = tup1[1:4]
print(tup2)