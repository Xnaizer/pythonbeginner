# lambda function

def kuadrat(angka):
    return angka**2

print(f"hasil fungsi kuadrat {kuadrat(3)}")

# dengan menggunakan lambda
kuadrat1 = lambda angka : angka**2
print(f"hasil fungsi lmda  kuadrat {kuadrat1(5)}")

pangkat = lambda num,pow : num**pow
print(f"hasil fungsi lmda  pangkat {pangkat(5,3)}")

## kegunaan ?

# sorting untuk list
data_list = ["otong","ucup","dudung"]
data_list.sort()
print(f"sorted list = {data_list}")

# klo pake func
def panjang_nama(nama):
    return len(nama)

data_list.sort(key=panjang_nama)
print(f"sorted list ke 2= {data_list}")

# klo pake lambda
data_list = ["otong","ucup","dudung"]
data_list.sort(key = lambda nama:len(nama))

# filter
data_angka = [1,2,3,4,5,6,7,8,9,10,11,12,13]

def kurdarlima(angka):
    return angka < 5

data_angka1 = list(filter(kurdarlima,data_angka))
data_angka2 = list(filter(lambda x:x<5,data_angka))
print("data filter angka kurang dari lima1 : ", data_angka1)
print("data filter angka kurang dari lima2 : ", data_angka2)

# kasus genap
data_angka3 = list(filter(lambda x:x%2 == 0,data_angka))
print("data filter untuk yang genap : ",data_angka3)

# kasus ganjil
data_angka4 = list(filter(lambda x:x%2 != 0,data_angka))
print("data filter untuk yang ganjil : ",data_angka4)

# anonymous function
# currying <-- haskell curry

def pangkat(angka,n):
    hasil = angka**n
    return hasil

data_hasil = pangkat(5,2)
print(f"fungsi diatas = {data_hasil}")

# klo dengan currying

def pangkat1(n):
    return lambda angka:angka**n

pangkat2 = pangkat1(2) # ini menentukan si n
print(f"hasil dari pangkat with currying : {pangkat2(5)}") # dan ini menentukan si angka
print(f"hasil dari pangkat bebas : {pangkat1(5)(4)}") # dan ini menentukan si n baru si angka
# berarti diatas itu 4^5