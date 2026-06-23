# write a program to display 2 digit amount into words 
#  input : 19 output one nine 
#  input : 65 output six five 
#  input : 75 output seven five 

amount = input("enter amount")
amount = int(amount)
last = amount % 10 # 9
first = amount // 10 #1
list = ['zero','one','two','three','four','five','six','seven','eight','nine']
print(list[first],list[last])


