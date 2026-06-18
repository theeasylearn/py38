#create a list ([] = brackets) 
fruits = ['banana','apple','mango','pineapple','graps','Cherry']
print(fruits)

#display banana 
print(fruits[0])
#display 2nd item 
print(fruits[1])
#display 4th  item 
print(fruits[3])
#display 1st 3 items 
print(fruits[0:3])
#display last 2 items
print(fruits[3:])

#change apple with coconut 
fruits[1] = 'Coconut'
print(fruits)

#delete item 1st item 
del fruits[0]
print("after deletion fruits has ",fruits)

#insert new item at end 
fruits.append('blueberry')
#insert new item at begining 
fruits.insert(0,'kiwi')
print("after insertion fruits has ",fruits)

box = [True,False,100,3.14,'Car']
print(box)

#join (concatenate lists)
new_list = fruits + box 
print(new_list)

#delete whole list 
del new_list 

#print list 3 times
print(fruits * 3)

