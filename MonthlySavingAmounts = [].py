Month = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
total = 0
for index in range(0,12):
    message = "Enter the amount you want to save in " + Month[index] + ": "
    MonthlySavingAmount=float(input(message))
    total = total + MonthlySavingAmount
    
print("The total amount saved in a year is ", total )