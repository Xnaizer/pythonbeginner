sisi = int(input("Masukkan panjang sisi (bilangan ganjil): "))
count = 1
spasi = sisi // 2

# Top part of the diamond
while count <= sisi:
    if count % 2:
        print(" " * spasi, "*" * count)
        count += 2
        spasi -= 1
    else:
        count += 1
        continue

# Bottom part of the diamond
count = sisi - 2
spasi = 1
while count >= 1:
    if count % 2:
        print(" " * spasi, "*" * count)
        count -= 2
        spasi += 1
    else:
        spasi += 1
        continue