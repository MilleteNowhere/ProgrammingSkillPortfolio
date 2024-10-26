def evenorodd(num): #This Function checks if the USer Input is odd or even.
    if num % 2 == 0:
        print(f"Your input {num} is an even number")
    else:
        print(f"Your input {num} is an odd number")
        
def main():
    while True:
        try:
            UserInput = int(input("Enter a number: ")) # Takes user input
            break
        except:
            print ("User input is Text. Please input a new variable.") # Prints this if user input is a String
            
    UserResult = evenorodd(UserInput)
    print(UserResult)
        
if __name__ == "__main__":
        main()
