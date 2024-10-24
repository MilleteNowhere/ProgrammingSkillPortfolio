#Enables While Loop.
while True:
    Name = ["Jake", "Zac", "Ian", "Ron", "Sam", "Dave"] #Creates a list of names
    Input = input("Search for Name?: ") #Grabs user input

    if Input in Name: #Checks if Name input is in list.
        print(f"Name found: {Input}")
        break #Breaks loop if name is found
    else:
        print(f"'{Input}' This name is not in the List.")
