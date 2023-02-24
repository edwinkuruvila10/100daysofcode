#union nd update
s1 = {1, 2, 3, 4 ,5, 6}
s2 = {3, 6, 7}
print(s1.union(s2))
s1.update(s2)
print(s1, s2)

#intersection
city = {"tokiyo", "spain", "delhi", "od"}
city1 = {"tokiyo", "odaynchal", "xsd", "od"}
city2 = city.intersection(city1)
print(city2)
#update of intersection
city = {"tokiyo", "spain", "delhi", "od"}
city1 = {"tokiyo", "odaynchal", "xsd", "od"}
city.intersection_update(city1)
print(city)
#symmetric differnce
city = {"tokiyo", "spain", "delhi", "od"}
city1 = {"tokiyo", "odaynchal", "xsd", "od"}
city = city.symmetric_difference(city1)
print(city)
#differnce 
city = {"tokiyo", "spain", "delhi", "od"}
city1 = {"tokiyo", "odaynchal", "xsd", "od"}
city = city.difference(city1)
print(city)

#sets methods
city = {"tokiyo1", "spain", "delhi", "od1"}
city1 = {"tokiyo", "odaynchal", "xsd", "od"}
print(city.isdisjoint(city1))

#Add method
citys = {"tokiyo", "spain", "delhi", "od"}
citys.add("germany")
print(citys)

#remove methods
citys = {"tokiyo", "spain", "delhi", "od"}
citys.remove("od")
print(citys)

#pop methods
citys = {"tokiyo", "spain", "delhi", "od"}
item = citys.pop()
print(citys)
print(item)

#check if item exits
info = {"carlo", 19, False, 5.9}
if "carlo" in info:
    print("carlo is present.")
else:
    print("carlo is not present.")

#Clear methods 
citys = {"tokiyo", "spain", "delhi", "od"}
citys.clear()
print(citys)