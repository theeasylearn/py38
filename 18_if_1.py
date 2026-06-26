# write a program to calculate profit or loss amount from user given purchase and sales price. 

purchase_price = int(input("Enter purchase price ")) #125
sales_price = int(input("Enter sales price")) #100

difference = sales_price - purchase_price

if difference>0: # < <= >= == !=
    print("you have earned profit of ",difference)

if difference<0:
    print("you have made loss of ",difference)

print("Good bye")


