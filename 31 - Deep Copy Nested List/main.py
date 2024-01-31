data0 = [1,2]
data1 = [3,4]

data2d = [data0,data1]
data2d_copy = data2d.copy()
print(f"data = {data2d}")
print(f"data copy = {data2d_copy}")

# mengambil

data = data2d[0] # mengambil list pertama
print(f"data = {data}")

data = data2d[0][0] # mengambil list 1 dan mengambil data pertama pada list pertama
print(f"data = {data}")

# address semuanya ?

print(f"address data asli = {hex(id(data2d[0]))} ")
print(f"address data copy = {hex(id(data2d_copy[0]))} ")

print(f"address data asli = {hex(id(data2d))} ")
print(f"address data copy = {hex(id(data2d_copy))} ")

# maka karna tidak bisa dikarenakan address yang masih terkait karna sama
# kita akan gunakan deepcopy

from copy import deepcopy

data2d = [data0,data1]
data2d_deepcopy = deepcopy(data2d)

print(f"address data asli = {hex(id(data2d))} ")
print(f"address data deepcopy = {hex(id(data2d_deepcopy))} ")

print(f"address data asli = {hex(id(data2d[0]))} ")
print(f"address data copy = {hex(id(data2d_deepcopy[0]))} ")

data2d[1][0] = 30
print(f" data = {data2d}")
print(f" data copy = {data2d_copy}")
print(f" data deep = {data2d_deepcopy}")



