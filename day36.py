questions = [
    [
    "Which language is used to create fb?", "python", "french", "java", "phd", "none", 4
    ], 
    [
    "Which language is used to create fb?", "python", "french", "java", "phd", "none", 4
    ],
    [
    "Which language is used to create fb?", "python", "french", "java", "phd", "none", 4
    ],
    [
    "Which language is used to create fb?", "python", "french", "java", "phd", "none", 4
    ],
    [
    "Which language is used to create fb?", "python", "french", "java", "phd", "none", 4
    ],
    [
    "Which language is used to create fb?", "python", "french", "java", "phd", "none", 4
    ],
    [
    "Which language is used to create fb?", "python", "french", "java", "phd", "none", 4
    ],
    [
    "Which language is used to create fb?", "python", "french", "java", "phd", "none", 4
    ],
    [
    "Which language is used to create fb?", "python", "french", "java", "phd", "none", 4
    ],
    [
    "Which language is used to create fb?", "python", "french", "java", "phd", "none", 4
    ],
    [
    "Which language is used to create fb?", "python", "french", "java", "phd", "none", 4
    ],
    [
    "Which language is used to create fb?", "python", "french", "java", "phd", "none", 4
    ],
    [
    "Which language is used to create fb?", "python", "french", "java", "phd", "none", 4
    ],
    [
    "Which language is used to create fb?", "python", "french", "java", "phd", "none", 4
    ],
    [
    "Which language is used to create fb?", "python", "french", "java", "phd", "none", 4
    ],
    [
    "Which language is used to create fb?", "python", "french", "java", "phd", "none", 4
    ],
    [
    "Which language is used to create fb?", "python", "french", "java", "phd", "none", 4
    ],
    [
    "Which language is used to create fb?", "python", "french", "java", "phd", "none", 4
    ],
    [
    "Which language is used to create fb?", "python", "french", "java", "phd", "none", 4
    ],
]    

levels = [1000, 2000, 3000, 5000, 10000, 20000, 40000, 80000, 160000, 320000]
money = 0
for i in range(0, len(questions)):

    question = questions[i]
    print(f"\n\nQuestion for Rs. {levels[i]}")
    print(f"a. {question[1]}               b. {question[2]} ")
    print(f"c. {question[3]}               d. {question[4]} ")
    reply = int(input("Enter your anser (1-4) or 0 to quit" ))
    if (reply == 0):
        money = levels[i-1]
        break

    if(reply == question[-1]):
        print(f"Correct anser, you have won Rs. {levels[i]}")
        if(1 == 4):
            money = 10000
    elif (i == 9):
        money = 320000    
    elif (i == 14):
        money = 10000000    
    else:
        print("Wrong anser!!")
        break

print(f"Your take home money is {money}")    