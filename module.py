from functools import reduce

numbers =[10, 20, 30, 40]
result = reduce(lambda x,y:x + y,numbers)
print("Sum of elements:",result)