
a = 10 
b = 10
c = 20
d = 30

result = a == b and c < d
print(f"{result} = {a} == {b} and {c} < {d}")

result = a < c and c > d
print(f"{result} = {a} < {c} and {c} > {d}")

result = a > c and c > d
print(f"{result} = {a} > {c} and {c} < {d}")

result = a < c or c > d
print(f"{result} = {a} < {c} or {c} > {d}")

result = a > c or c < d
print(f"{result} = {a} > {c} or {c} < {d}")

result = a > c or c > d
print(f"{result} = {a} > {c} or {c} > {d}")

result =not ( a == b and c < d)
print(f"not {result} = {a} == {b} and {c} < {d}")

