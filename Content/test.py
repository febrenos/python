from re import A


w = open("test.txt", "w")
w.write("hello")
w.close()

m = [["a","b","c","d","e"]
    ,["f","g","h","i","j"]
    ,["k","l","m","n","o"]
    ,["p","q","r","s","t"]
    ,["u","v","w","x","y"]]

# a
# fb
# kgc
# plhd
# uqmie
# vrnj
# wso
# xt
# y

print(m[0][0])

print(f"{m[1][0]} {m[0][1]}")
print(f"{m[2][0]} {m[1][1]} {m[0][2]}")
print(f"{m[3][0]} {m[2][1]} {m[1][2]} {m[0][3]}")
print(f"{m[4][0]} {m[3][1]} {m[2][2]} {m[1][3]} {m[0][4]}")
print(f"{m[4][1]} {m[3][2]} {m[2][3]} {m[1][4]}")
print(f"{m[4][2]} {m[3][3]} {m[2][4]}")
print(f"{m[4][3]} {m[3][4]}")