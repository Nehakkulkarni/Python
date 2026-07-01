file = open("example.txt","w")
file.write("Python is an simple to use programming language.\n")
file.write("It is used for websites.\n")
file.close()

file = open("example.txt","r")
print(file.read())
file.close()

file = open("example.txt","a")
file.write("It also has many useful libraries.\n")
file.close()

file = open("example.txt","r")
print(file.read())
file.close()