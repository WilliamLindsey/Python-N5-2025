DogFoodWeights = []
loop = 5
for index in range(loop):
    DogFoodWeights=int(input("Enter the weight of the dog food in grams: ") )
    while DogFoodWeights < 0 or DogFoodWeights > 300:
        if DogFoodWeights < 0:
            print("The weight of the dog food is too light.")
        elif DogFoodWeights > 300:
            print("The weight of the dog food is too heavy.")
        DogFoodWeights=int(input("Enter the weight of the dog food in grams: ")
print('The weight of the dog food is: ', sum(DogFoodWeights) 'grams.")