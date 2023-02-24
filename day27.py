# # def factorial(n):
#     if(n==0 or n==1):
#         return 1
#     else:
#         return n * factorial(n-1)
    
# print(factorial(3))
# print(factorial(4))
# print(factorial(5))

#fabanocci series
a=int(input("Enter any number: "))
def fibo(n):
    if (n==0):
        return 0
    elif (n==1 or n==2):
        return 1
    else:
        return fibo(n-1)+fibo(n-2)

print(fibo(a))