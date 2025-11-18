#The list of names
names = ["Jake", "Zac", "Ian", "Ron", "Sam", "Dave"]

#Asks the user for a name
search_name = str(input("Search name: "))
search_name = search_name.capitalize()

#Checks if the name exists in the list
if search_name in names:
    print(f"{search_name} was found in the list.")
else:
    print(f"{search_name} was not found in the list.")
