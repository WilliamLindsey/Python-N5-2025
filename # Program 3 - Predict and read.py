# Program 2 - Predict and read
cost = float(input("Enter cost of the item in £ and p: "))
noPounds = round(cost)+1
print("You will need £"+str(noPounds))
print("And you will get "+str(noPounds-cost)+"p change")
