temperature = []
loop = 7
for i in range(loop):
    temperature=input("Enter temperature in Celsius: ")
    while temperature < -20 or temperature > 50:
        if temperature < -20:
            print("Must be higher than -20 degrees.")
        elif temperature > 50:
            print("Must be lower than 50 degrees.")
        temperature=input("Enter temperature in Celsius: ")
print('Average temperature is: ', sum(temperature)/loop)