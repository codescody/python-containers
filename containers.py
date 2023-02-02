# 1.

students_names = ["Matt", "Cody", "Ji", "Colin"]

print(students_names[0])
print(students_names[1])

# 2.

foods = ("Steak", "Ahi Tuna", "Chicken", "Burger")
for food in foods:
    print(food, "is a good food")

# 3.

for food in range(-2, 0):
    print(foods[food])

# 4.

home_town = {"city":"Saint Petersburg", "state":"Florida", "population":258512}
print(f"I was born in {home_town['city']}, {home_town['state']} - Population of {home_town['population']}")

# 5.

for key, val in home_town.items():
	print( f"{key} = {val}" )



