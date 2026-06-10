numbers = [10, 20, 30, 40, 20, 10, 50]
print("Original:",numbers)
numbers.append(60)
numbers.remove(20)
numbers[0] = 100
print("Ascending:", sorted(numbers))
print("Descending:", sorted(numbers,reverse=True))
print("Max:",max(numbers))
print("Min:",min(numbers))
print("Sum:",sum(numbers))

unique = list(set(numbers))
print(unique)
print(numbers[1:4])
