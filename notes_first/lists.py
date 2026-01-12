# VL 1st Types of Lists Notes

siblings = ["Alex", "Katie", "Andrew", "Tia", "Treyson", "Xavier", "Jake", "Katie"]

print(siblings[3])
siblings[-2] = "DOW"

print(siblings)


fruit = ("apple", "orange", "peach", "kiwi", "raspberry")
home = (0,0)
x,y = home

#fruit[3] = "pineapple"
print(x)

#set
colors = {"Orange", "Purple", "Green", "Blue", "Yellow", "Red", "Green"}
colors.add("Pink")
colors.remove("Purple")
for i in colors:
    if i == "Orange":
        i = "Burgendy"
    print(i)

print(colors)