#Enables the While loop for any code that falls under the loop
while True:
    ATMPT = 5
    FailedATMPT = (ATMPT - 1)
    CorrectPass = input ("Please input Passcode here: ")
    
    if CorrectPass == "12345":
        print ("Password Correct, Welcome Back")
        break
    else:
        print (f"Incorrect passsword you have..{FailedATMPT} Tries left. Please try again.")
        FailedATMPT -- 1
        if FailedATMPT < 0:
            print ("All attempts failed. Local authororities contacted. Have a great day.")
            break
        continue
