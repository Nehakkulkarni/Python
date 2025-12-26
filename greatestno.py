#Write a program to find the greatest of three numbers.

num1=int(input("num1: "))
num2=int(input("num2: "))
num3=int(input("num3: "))

if( (num1>num2) and (num1>num3)):
    print("Number",num1," is greatest number.")
elif(num2>num1 and num2>num3):
    print("Number ",num2," is the greatest number.")
else:
    print("Number", num3, "is the greatest number.")