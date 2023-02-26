a = int (input("Enter any value between 5 and 9"))

if(a<5 or a>9): 
    raise ValueError("Value should be between 5 and 9")

#quit ex
val = input('Enter your value: \n')
if val == 'quit':
    print('ok')
elif (int(val) < 5 or int(val)> 9):
    raise ValueError('Val should be between 5 and 9')