# Make an empty list to store the pets in.
pets = []

# Make individual pets, and store each one in the list.
pet = {
    'animal type': 'persian cat',
    'name': 'malus',
    'owner': 'john',
    'weight': 7,
    'eats': 'fish',
}
pets.append(pet)

pet = {
    'animal type': 'macaw parrot',
    'name': 'coco',
    'owner': 'jimin',
    'weight': 2,
    'eats': 'seeds',
}
pets.append(pet)

pet = {
    'animal type': 'german shepherd',
    'name': 'rocky',
    'owner': 'jack',
    'weight': 40,
    'eats': 'meat',
}
pets.append(pet)

# Display information about each pet.
for pet in pets:
    print("\nHere's what I know about " + pet['name'].title() + ":")
    for key, value in pet.items():
        print("\t" + key + ": " + str(value))
