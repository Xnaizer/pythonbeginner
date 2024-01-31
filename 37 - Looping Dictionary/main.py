# looping dictionary

teman_teman = {
    "cup":"ucup serucup",
    "tong":"otong surotong",
    "dung":"dudung surudung",
    "sep":"asep si kasyep",
    "cuy":"ucuy surucuy",
}
print(" "*20)

# looping first try (yang keluar adalah keynya)

for i in teman_teman:
    print(i)

# operator untuk mengambil item / iterables
keys = teman_teman.keys()
print(keys) # akan ngeprint key atau id pada list
print(" "*20)
for i in teman_teman.keys():
    print(teman_teman.get(i))

print(" "*20)

values = teman_teman.values()
print(values) # akan ngeprint data yang ada

print(" "*20)
for i in teman_teman.values():
    print(i)

print(" "*20)
itemss = teman_teman.items()
print(itemss)

print(" "*20)
for key,i in teman_teman.items():
    print(f"key = {key}, value = {i}")








