
#empty dictionary 
building = {}
print(building)

#NEW KEY VALUE PAIR
building['name'] = 'Eva surbhi'
building['pincode'] = 364001

#adding list into dictionary 
building['floor'] = [1,2,3,4,5]
#adding tuple into dictionary 
building['parking'] = ('A1','B2','C3')

print(building)

del building['floor'][0]
print(building) 
# del building['parking'][0]
# building['parking'][0] = 'E5'
print('GOOD BYE') 

