cost_price = float(input("Enter Cost Price: "))
selling_price = float(input("Enter Selling Price: "))

if (cost_price<selling_price):
    profit = selling_price - cost_price
    print("Profit is: ", profit)
elif (selling_price<cost_price):
    loss = cost_price - selling_price
    print("Loss is:", loss)
else:
    print("No profit, No loss")

"""  Enter Cost Price: 550
Enter Selling Price: 650
Profit is:  100.0 
Enter Cost Price: 200
Enter Selling Price: 170
Loss is: 30.0   """
