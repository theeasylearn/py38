#read only list(tuple)

gods = ('Bramha','Vishnu','Shiv')
print(gods)
#print 1st god
print(gods[0])
#print 2nd god
print(gods[1])
#print 1st two god
print(gods[:2])

# del gods[0]
# gods[0] = 'brahmji

print("Count of Vishnu ",gods.count('Vishnu'))
print("index of shiv ",gods.count('Shiv'))

print(gods * 2)
devtas = ('Surdev','Shandev','Chandradev','Kuber','Indra')
print(gods,devtas)
print(gods+devtas)