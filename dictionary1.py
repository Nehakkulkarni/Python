student = {
    "name":"Riya",
    "roll_no":120,
    "marks":85
}

print("Original Dictionary:",student)
student["grade"] = "A"
print("After Adding:",student)

student["marks"]=90
print("After Updating Marks:",student)
del student["roll_no"]
print("After Deleting roll_no:",student)

print("Keys:")
for key in student.keys():
    print(key)
print("Values:")
for value in student.values():
    print(value)
print("Items:")
for key, value in student.items():
    print(key,":",value)
text = "python is easy python is powerful"
words = text.split()

frequency = {}
for word in words:
    frequency[word]=frequency.get(word, 0)+1
print("\nWord Frequency:")
for word,count in frequency.items():
    print(word,":",count)