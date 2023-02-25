a = input("enter the number:")
print(f"Multiplication table of {a} is: ")

try:
    for i in range(1, 11):
        print(f"{a} x {i} = {a*i}")
except Exception as e:
    print(e)


print("some line if code")
print("end the program")


try:
    num = int(input("Enter an integer: "))
    a = [6, 3]
    print(a[num])
except ValueError:
    print("number entered is not an integer.")
except IndexError:
    print("Index Error")