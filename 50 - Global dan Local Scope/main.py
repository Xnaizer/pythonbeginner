## global dan local scope

nama = "otong" # variable global dan dapat diakses didalam function

# akses variabel global dalam fungsi
def fungsi():
    print(f"fungsi menapilkan {nama}")

fungsi()

# akses variabel global dalam loop
for i in range(0,5):
    print(f"loop {i} - {nama}")

# percabangan
    
if True:
    print(f"if menampilkan {nama}")

## variable local scope
    
def fungsi2():
    var_local = "ucup" # ini var lokal

fungsi2()
#print(var_local) # tidak akan bisa.

# contoh 1 penggunaan akses variable

def say_otong():
    print(f"hello {nama}")

nama = "otong"
say_otong()

# def say_otong():
#     print(f"hello {nama}")

# say_otong()
# nama = "otong" klo begini akan eror karena nama setelah pemanggilan func
## jadi nama kea engga kedetect didalam fungsi

## contoh 2 merubah variable global

angka = 0
nama = "ucup"

def ubahangka(nilaibaru):
    global angka #fungsi ini mendapat akses merubah angka
    angka=nilaibaru
    
def ubahnama(namabaru):
    global nama #fungsi ini mendapat akses merubah nama
    nama=namabaru

print(f"sebelum : {angka}")
ubahangka(10)
print(f"Sesudah : {angka}")

print(f"sebelum : {nama}")
ubahnama("otong")
print(f"Sesudah : {nama}")

# contoh 3 
angka = 0 

for i in range(0,5):
    angka += i
    angka_dummy = 0

print(angka)
print(angka_dummy)

if True:
    angka = 10
    angka_dummy = 3

print(angka)
print(angka_dummy)