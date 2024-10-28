#Enables the While loop for any code that falls under the loop
while True:
    
    #Create a name dictionary with capability for userinput
    Name = ["Jake", "Zac", "Ian", "Ron", "Sam", "Dave"]
    Input = input("Search for Name?: ")

# checks if Userinput is within the dictionary and stops loop if true, but continues it if invalid
    if Input in Name:
        print(f"Name found: {Input}")
        break
    else:
        print(f"'{Input}' This name is not in the List.")
