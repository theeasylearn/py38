# write a program to convert user given 24 hours format time into 12 hours format time 
# input : 21 output : 9 PM
# input : 13 output : 1 PM
# input : 11 output : 11 AM

hours = int(input("Enter hours")) # 15
if hours>12:
    hours = hours - 12
    print(f"{hours} PM")
else:
    print(f"{hours} AM")
print("Good bye")

