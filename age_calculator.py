from datetime import datetime


def check_birthdate(year,month,day):
    today = datetime(2020,1,26)
    birthdate = datetime(year, month, day)
    if today > birthdate:
        return True
    return False

def calculate_age(year,month,day):
    today = datetime(2020,1,26)
    birthdate = datetime(year,month,day)
    user_age = int((today-birthdate).days /365)
    print("You are %d years old" %(user_age))

year = int(input("Enter year of birth"))
month = int (input("Enter month of birth"))
day = int (input("Enter day of birth"))

if check_birthdate (int(year), int(month), int(day)) == True
    calculate_age(int(year,), int(month), int(day))

else
print("Input is invalid")









