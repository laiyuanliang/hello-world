#year = int(input("year:"))

time = input("Please input a date like '2017-08-15':")
year = int(time.split('-')[0])
month = int(time.split('-')[1])
day = int(time.split('-')[2])

MList = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
M = {1:31, 2:29, 3:31, 4:30, 5:31, 6:30, 7:31, 8:31, 9:30, 10:31, 11:30, 12:31}
m= {1:31, 2:28, 3:31, 4:30, 5:31, 6:30, 7:31, 8:31, 9:30, 10:31, 11:30, 12:31}

if year % 400 == 0:
    if month in range(1,13) and day in range(1, M[month]+1): 
        print(f"leap year, valid date")
    else:
        print(f"leap year, invalid date")

elif year % 100 != 0 and year % 4 == 0:
    if month in range(1,13) and day in range(1, M[month]+1): 
        print(f"leap year, valid date")
    else:
        print(f"leap year, invalid date")

else:
    if month in range(1,13) and day in range(1, M[month]+1): 
        print(f"normal year, valid date")
    else:
        print(f"normal year, invalid date")
