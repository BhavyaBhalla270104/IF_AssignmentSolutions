unit = int(input("Enter the number of units purchased: "))
cost = unit*100
if(cost>1000):
    cost = 0.85*cost
else:
    cost = unit*100    
print("You will have to pay",cost,"for the items you have purchased")    