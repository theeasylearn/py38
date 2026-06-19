#create dictionary 
book = {'name':'Learning Python','price':1000,'author':'Ankit Patel','weight':250.55}

print(book)

#add new key value pair
book['publication'] = 'the easylearn'
book['country'] = 'india'

print(book)
#update key value pair
book['publication'] = 'T.E.L'

print("after updation",book)

#delete key value pair 

del book['publication']
print('after deletion ',book)





