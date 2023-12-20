import calendar

user_str = input("Enter a date:")
arr = user_str.split("/")
year = int(arr[2])
month = int(arr[1])
day = int(arr[0])
dayNum = calendar.weekday(year, month, day)
if dayNum == 0:
    print("Monday")
elif dayNum == 1:
    print("Tuesday")
elif dayNum == 2:
    print("Wednesday")
elif dayNum == 3:
    print("Thursday")
elif dayNum == 4:
    print("Friday")
elif dayNum == 5:
    print("Saturday")
elif dayNum == 6:
    print("Sunday")
