t =(10, 20, 30, 20, "Hello")
print(t[0])
print("Index of 20:",t.index(20))
print("Count of 20:",t.count(20))

l =list(t)
l.append(100)
t =tuple(l)
print("Updated tuple:", t)