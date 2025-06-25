pupils = int(input("How many pupils are in the class? "))
pizza = 8
total_pizzas = round(pupils/pizza) + 1
pizza_cost = 12
total_cost = total_pizzas * pizza_cost
print("The total cost is £",total_cost," and the total number of pizzas are", total_pizzas)