a = 10
b = 3 
print(f" a = {a} b = {b}")
# a = a + b slow
a+=b # fast
print(f"after addition  a = {a} b = {b}")

a -=  b 
print(f"after subtraction  a = {a} b = {b}")

a *= b 
print(f"after multiplication  a = {a} b = {b}")

a /= b 
print(f"after division  a = {a} b = {b}")

a **= b 
print(f"after power  a = {a} b = {b}")

a //= b 
print(f"after floor division  a = {a} b = {b}")

a %= b 
print(f"after modules  a = {a} b = {b}")
