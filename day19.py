#PY Lists
marks = [3, 5, 6, "harry", True]
# print(marks)
# print(type(marks))
# print(marks[0])
# print(marks[1])
# print(marks[2])

# print(marks[-3])  #neagtive index
# print(marks[len(marks)-3]) #positve index
# print(marks[5-3]) #positive index 
# print(marks[2])

# if "6" in marks:
#     print("yes")
# else:
#     print("no")    

#same things applies for strings
# if "arry" in "harry":
#     print("yes")

# print(marks)
# print(marks[1:-1])
# print(marks[1:4:2])

lst = [i*i for i in range(10)]
print(lst)
lst = [i*i for i in range(10) if i%2==0]
print(lst)