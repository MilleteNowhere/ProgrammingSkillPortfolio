# This calls our a Dictionary and creates the keys needed

My_Info = {'name': 'Andrew', 'age': '17', 'Hometown': 'Metro Manila'} 

#This is supposed to print all the data by grabbing the info using the keys and inputting
#Them into a single, multi-lined print call

print(f"My Name is: {My_Info.get('name')}\n"
      f"My Age is: {My_Info.get('age')}\n"
      f"My Hometown is: {My_Info.get('Hometown')}")

