abc = ("a", "b", "c", "d", "e")
print("len:", len(abc))

for c in abc:
    print(abc)

i = 0
while i < len(abc):
    print(abc[i])
    i += 1

i = len(abc) - 1
while i >= 0:
    print(abc[i])
    i -= 1

