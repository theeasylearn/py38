#create a list ([] = brackets) 
fruits = ['banana','apple','mango','pineapple','graps','Cherry','banana','banana']
vegetables = ['tomato', 'potato', 'onion', 'carrot', 'broccoli', 'spinach', 'cucumber', 'capsicum', 'cauliflower', 'cabbage']
print(fruits,vegetables) #i can display multiple list in one print 

print("_" * 100)
#merge fruits into vegetables
vegetables.extend(fruits)
print(vegetables)

#clear list (remove all item but not list)
vegetables.clear() 
print(vegetables)

#remove mango
fruits.remove('mango')

#remove 2nd item
fruits.pop(1)
print("after deletion fruits has ",fruits)

#count no of banana 
print("Count of banana ",fruits.count('banana'))
print("Position of graps ",fruits.index("graps"))
# print("Position of watermelon ",fruits.index("watermelon"))
fruits.sort()
print("sorted fruits ",fruits)
fruits.reverse()
print("reversely sorted fruits ",fruits)
print("good bye")

# fruits2 = fruits wrong way of coping list 
fruits2 = fruits.copy() #right way 
fruits2.clear()
print(fruits2,fruits)