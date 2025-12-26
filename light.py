light = input("Enter traffic light color: ").lower()
#.lower() converts all letters in a string to lowercase.
if light == "green":
    print("Go")
elif light == "red":
    print("Stop")
elif light == "yellow":
    print("Wait")
else:
    print("Not valid colour")



