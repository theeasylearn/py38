fruits = {'banana','mango','pineapple','orange','mango'}
print(fruits)

fruits.add('kiwi')
fruits.add('graps')

print(fruits)

#remove value 
fruits.remove('kiwi')

print(fruits)

fruits2 = [
    "Mango",
    "Apple",
    "Banana",
    "Orange",
    "Grapes",
    "Pineapple",
    "Banana",
    "Watermelon",
    "Apple",
    "Papaya"
]

#remove duplicate items from list 

newset = set(fruits2) #convert list into set and also remove all duplicate items
print(newset)

a = {1,2,3,4,5}
b = {4,5,6,7,8}

#union 
union = a.union(b) 
intersection = a.intersection(b)

print("union ",union)
print("intersection ",intersection)

difference = a.difference(b)
print('difference ',difference)