n = int(input("Enter number of terms: "))
i = 0
a = 0
b = 1
while i < n:
    print(a, end=" ")
    temp = a + b
    a = b
    b = temp
    i += 1
print()




