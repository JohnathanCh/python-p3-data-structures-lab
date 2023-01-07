import pdb

spicy_foods = [
    {
        "name": "Green Curry",
        "cuisine": "Thai",
        "heat_level": 9,
    },
    {
        "name": "Buffalo Wings",
        "cuisine": "American",
        "heat_level": 3,
    },
    {
        "name": "Mapo Tofu",
        "cuisine": "Sichuan",
        "heat_level": 6,
    },
]

def get_names(spicy_foods):
    return [dict["name"] for dict in spicy_foods]

def get_spiciest_foods(spicy_foods):
    return [dict for dict in spicy_foods if dict["heat_level"] > 5]

def print_spicy_foods(spicy_foods):
    stuff = [f"{dict['name']} ({dict['cuisine']}) | Heat Level: {'🌶' * dict['heat_level']}" for dict in spicy_foods]
    
    for food in stuff:
        print(food)
        # print(f"{dict['name']} ({dict['cuisine']}) | Heat Level: {'🌶' * dict['heat_level']}")
    # pdb.set_trace()
    return stuff

def create_spicy_food(spicy_foods, spicy_food):
    spicy_foods.append(spicy_food)
    return spicy_foods

def get_spicy_food_by_cuisine(spicy_foods, cuisine):
    for food in spicy_foods:
       if food["cuisine"] == cuisine:
            return food 

def print_spiciest_foods(spicy_foods):
    new_foods = get_spiciest_foods(spicy_foods)
    print_spicy_foods(new_foods)
    

def get_average_heat_level(spicy_foods):
    nums = [food["heat_level"] for food in spicy_foods]
    return sum(nums)/len(nums)
