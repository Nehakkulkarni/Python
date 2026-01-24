Eng = float(input("Enter English marks: "))
Maths = float(input("Enter Math marks: "))
Phy = float(input("Enter Physics marks: "))
Chem = float(input("Enter Chemistry marks: "))
Comp = float(input("Enter Computer marks: "))

total = Eng+Maths+Phy+Chem+Comp
percentage = total/500*100
print("Percentage =",percentage)

""" Enter English marks: 80
Enter Math marks: 87
Enter Physics marks: 90
Enter Chemistry marks: 78
Enter Computer marks: 95 
86.0  """