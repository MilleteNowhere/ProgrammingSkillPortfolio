#Creates 2 dictionarys for Days in month and Months in year.

MonthsInYear = {
    '1': 'January',
    '2': 'February',
    '3': 'March',
    '4': 'April',
    '5': 'May', 
    '6': 'June',
    '7': 'July',
    '8': 'August',
    '9': 'September',
    '10': 'October',
    '11': 'November',
    '12': 'December'
}

DaysInMonth = {
    'January': 31,
    'February': 28,
    'March': 31,
    'April': 30,
    'May': 31,
    'June': 30,
    'July': 31,
    'August': 31,
    'September': 30,
    'October': 31,
    'November': 30,
    'December': 31
}

#Checks for userinputs
Input = input("Input Month Number [1-12]: ")
month = MonthsInYear.get(Input)

#Checks if answer is inside the Dictionary
if month:
    days = DaysInMonth.get(month)
    print(f"{month} has {days} days.")
else:
    print("Invalid Input.")




