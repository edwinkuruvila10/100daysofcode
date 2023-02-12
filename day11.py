a=int(input("Enter your age  "))
print("your age is:",a)

#Conditional operation
# >, <, >=, <=, ==, !=

if(a>18):
    print("You can drive")
else:
    print("You cannot drive")    

#elif
num=int(input("Enter the value of num: "))
if (num < 0):
    print("The number is negative")
elif (num == 0):
    print("The number is zero")
else:
    print("The number is positive")     

#Nested if Statements
num=18
if(num < 0):
    print("The number is negative.")
elif (num > 0):
    if (num <= 10):
        print("The number is between 1-10")
    elif (num > 10 and num <= 20):
        print("The number is between 11-20")
    else:
        print("The number is greater than 20")
else:
    print("The number is zero") 
           
