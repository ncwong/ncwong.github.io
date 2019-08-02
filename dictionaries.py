hairColors = ["Brown", "Blue", "Red", "Blonde", "Black", "Purple"]

print(hairColors[2])

people = ["Bob Ross", "Kendra", "Liv", "Taylor Swift", "Lil Nas X", "Kat"]

print(people[1] + " has: " + hairColors[1] + " hair. ")

peopleAndColors = {"Bob Ross": "Brown", "Kendra": "Blue", "Liv": "Red", "Taylor Swift": "Blonde", "Lil Nas X": "Black", "Kat": ["Purple", "Blue"]}

print(peopleAndColors["Kat"][1])

print(list(peopleAndColors.keys())[3])

print("Bob Ross has: " + peopleAndColors["Bob Ross"] + " hair.")

name = "Lil Nas X"

print(name + " has: " + peopleAndColors[name] + " hair.")
