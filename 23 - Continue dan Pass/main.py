# continue , pass , break
# pass berfungsi sebagai dummy yang tak akan dieksekusi
angka = 0
while angka <5:
    angka += 1
    if angka == 3:
        print("wadhap")
        print(angka)

angka = 0
while angka < 5:
    angka += 1
    if angka == 3:
        pass

    print(angka)

# Continue

angka = 0
print(f"angka skrg = {angka}")

while angka < 5:
    angka += 1
    print(f"angka skrg = {angka}")

    if angka == 3:
        print("niceessssss loop")
        continue # akan membuat loop  balik ke while angka <5

    print("wahhassp")

print("nice !!")