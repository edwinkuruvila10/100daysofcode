#Single value 
info = {"name":"edwin", "age":21, "eligible":True}
print(info)
print(info["name"])
print(info.get("name"))

#multiple values
info = {"name":"edwin", "age":21, "eligible":True}
print(info)
print(info["name"])
print(info.keys())

for key in info.keys():
    print(info[key])

#key value pairs
print(info.items())
for key, value in info. items():
    print(f"The value corresponding to the key {key} is {value}")