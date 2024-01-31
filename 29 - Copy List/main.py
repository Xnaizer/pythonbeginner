## teknik menduplikat list

a = ["ucup","otong","dudung"]
print(f"a = {a}")

b = a # ini bukan cara untuk menduplikat list
print(f"b = {b}")

# kita akan merubah member dari a 

# ini akan merubah kedua list
a[1] = "micheal"
b.sort()
print(f"a = {a}")
print(f"b = {b}")

# address dari kedua list a dan b
print(f"address a = {hex(id(a))}")
print(f"address b = {hex(id(b))}")
# ini bukan cara menduplikat list karna address keduanya sama
# jikalau address keduanya sama maka tidak mungkin list a dan b akan berbeda

#menduplikat menggunakan copy

print("membuat list c dengan mengcopy ")
c = a.copy()
print(f"address a = {hex(id(a))}")
print(f"address b = {hex(id(b))}")
print(f"address c = {hex(id(c))}")

print(f"a = {a}")
print(f"b = {b}")
print(f"c = {c}")

print("ubah data c")
c[0]= "Dadang"


print(f"a = {a}")
print(f"b = {b}")
print(f"c = {c}")










