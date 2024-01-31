# Fungsi dengan return value
# y = x + 1 ata y = f(x) ini fungsi, x input, maka y adalah outputnya

# def func(input ):
#   hasil = input**2
#   return hasil
# atau sama aja
# y = func(4)
# y = 16
# input -> fungsi -> output

# template fungsi return
# def nama_fungsi(argument):
#       badan fungsi
#       retunr output

# fungsi kuadrat

y = 3**2
print(y)
print("atauuuuuuu")

def kuadrat(angka):
    output_kuadrat = angka**2
    return output_kuadrat

y = kuadrat(5)
print(y)
print(kuadrat(6))

z = 10 + kuadrat(7)
print(z)

# fungsi return multi input

def tambah(ang1,ang2):
    return ang1 + ang2

a = tambah(1,2)

def kuadrat1(ang1):
    return ang1**2

a = kuadrat1(2)
print(a)

def operasi_matematika(ang1,ang2):
    tambah = ang1 + ang2
    kurang = ang1 - ang2

    return tambah,kurang

tambah1,kurang1 = operasi_matematika(3,2)
print(f"Hasil tambah : {tambah1}")
print(f"Hasil kurang : {kurang1}")
