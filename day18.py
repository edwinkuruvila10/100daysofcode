def average(*number):
    print(type(number))
    sum = 0
    for i in number:
        sum = sum + i
    print("Average is: ", sum / len(number))

    # return sum / len(number)

# c = average(5, 6, 7, 9)
# print(c)  
       
def name(**name):
    print(type(name))
    print("hello,", name["fname"], name["mname"], 
        name["lname"])

name(mname = "edwin", fname = "pranav",
     lname = "amal")





