a="harry !!!!!!!!!! harry"
print(len(a))
print(a)
print(a.upper()) 
print(a.lower()) 
print(a.rstrip("!"))
print(a.replace("harry", "john"))
#split
print(a.split(" "))
#capitalize
blogHeading="introduction to js"
print(blogHeading.capitalize())
#center
str1="Welcome to console!!!"
print(len(str1))
print(len(str1.center(50)))
#count
print(a.count("harry"))
#endswith
str1="Welcome to console"
print(str1.endswith("!!!"))
 
str1="Welcome to console !!!"
print(str1.endswith("to", 4, 10))
#find()
str1="He's name is edwin. he is an smart boy."
print(str1.find("is"))
#isalnum
str1="Welcome to console"
print(str1.isalnum())
str1="hello world"
print(str1.islower())

str1="we wish you a merry christmas"
print(str1.isprintable())
str1 = "      "
print(str1.isspace())
str2 = "                "
print(str2.isspace())
#swapecase
str1="Python is a interpreted language"
print(str1.swapcase())
#title
str1="his name is edwin. edwin is a smart guy."
print(str1.title())