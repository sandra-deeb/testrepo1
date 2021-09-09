a = [("At", 85), ("Br", 35), ("Cl", 17), ("F", 9), ("I", 53)]

b = sorted(a, key=lambda e: e[1])
print(b)

c = sorted(a, reverse=True,  key=lambda e: e[1])
print(c)

d = sorted(a)
print(d)
