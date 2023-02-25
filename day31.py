#update
ep1 ={122: 45, 123: 55, 124: 88}
ep2 ={321: 66, 331: 77}
ep1.update(ep2)
print(ep1)
#clear
ep1 ={122: 45, 123: 55, 124: 88}
ep2 ={321: 66, 331: 77}
ep1.clear()
print(ep1)
#empty
ep1 ={122: 45, 123: 55, 124: 88}
ep2 ={321: 66, 331: 77}
ep1.clear()
print(ep1)
empt = {}
print(empt)
#pop
ep1 ={122: 45, 123: 55, 124: 88}
ep2 ={321: 66, 331: 77}
ep1.pop(122)
print(ep1)
#del
ep1 ={122: 45, 123: 55, 124: 88}
ep2 ={321: 66, 331: 77}
del ep1["122"]
print(ep1)