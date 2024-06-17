import random

def take_shower():
    return "Showering"

def eat_breakfast():
    meal=cook_food()
    return f"Eating {meal}"

def cook_food():
    items=["Oatmeal","Eggs","Protein Shake"]
    return items[random.randrange(0,len(items)-1)]

def wakeUp():
    take_shower()
    eat_breakfast()
    cook_food()

wakeUp()