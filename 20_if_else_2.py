# write a program to display how many days given month has 
# input : 1 output : this month has 31 days 
# input : 4 output : this month has 30 days 
# input : 2 output : this month has 28/29 days 
# 1,3,5,7,8,10,12 month has 31 days
# 4,6,9,11 month has 30 days and 2 month has 28/29 days

month = int(input("Enter month (between 1 to 12)"))

if month == 2:
    print("this month has 28/29 days")
    exit(1)  # stop program 

if month == 1 or month==3 or month==5 or month==7 or month==8 or month==10 or month==12:
    print("this month has 31 days")
else:
    print("this month has 30 days")


