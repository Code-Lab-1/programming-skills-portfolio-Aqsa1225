rivers = {
    'nile': 'egypt',
    'amazon river': 'brazil',
    'river thames': 'london',
    'danube river': 'germany',
    'mekong river': 'thailand',
    }

for river, country in rivers.items():
    print("The " + river.title() + " flows through " + country.title() + ".")

print("\nThe following rivers are included in this data set:")
for river in rivers.keys():
    print("- " + river.title())

print("\nThe following countries are included in this data set:")
for country in rivers.values():
    print("- " + country.title())