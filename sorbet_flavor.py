"""
You're working for a restaurant and they're asking you to generate the sorbet menu.
Provide a script printing every possible sorbet duos from a given list of flavors.
Don't print recipes with twice the same flavor (no "Chocolate, Chocolate"), and don't
print twice the same recipe (if you print "Vanilla, Chocolate", don't print "Chocolate,
Vanilla", or vice-versa).
"""
FLAVORS = [
    "Banana",
    "Chocolate",
    "Lemon",
    "Pistachio",
    "Raspberry",
    "Strawberry",
    "Vanilla",
]
for i in range(len(FLAVORS)):
    for j in range(i+1,len(FLAVORS)):
        print(f"{FLAVORS[i]}, {FLAVORS[j]}")

