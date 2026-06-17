#accept input from user using python 
name = input("What is your name?")
print("welcome mr ",name)

#input function always return string
num1 = input("Enter 1st number")
num2 = input("Enter 2nd number")

#if we directly perform addition on string, python do concatenation instead of addition
#to solve this problem, we have to convert string into integer or float
num1 = int(num1)
num2 = float(num2)

#process 
addition = num1 + num2 
print("addition =",addition)