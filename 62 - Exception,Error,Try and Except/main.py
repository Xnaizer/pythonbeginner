# data_input = int(input("Masukkan angka : "))

# hasil = 10/data_input
# print(hasil)
# aplikasi kan eror akan ketika kta memasukkan nilai yang 0 / run time error
# syntaks error karena syntaks ada yang tidak lengkap persyaratannya

#exception akan terjadi saat program
# mengalami eror saat runtime

#contoh sederhana untuk menangkap exceptipon
from math import nan

## contoh sederhana
# input_user = int(input("Masukkan nilai angka : "))
# hasil = nan

# try:
#     hasil = 10/input_user

# except:
#     print("input tidak boleh 0")

# print(f"hasil = {hasil}")

##contoh di aplikasi

while(True):
    angka = int(input("Masukkan angka pembagi : "))
    try:
        hasil = 10/angka
        print(f"hasil = {hasil}")
        is_done = input("lanjutkan (y/n) ? ")
        if is_done == "n":
            break

    except:
        print("pembagi nol, silahkan masukkan input lagi")

print("akhir dari program 1")

# dengan cara begini program kita akan terus berlanjut sampai inputnya bener
# try and except atau try and catch

while(True):
    try:
        with open("data.txt",'r') as file:
            print(file.read())
        break

    except:
        print("file data.txt tidak ditemukan, membuat file baru")
        with open("data.txt",'w',encoding='utf-8') as file:
            file.write("file baru2")
        break

print("akhir dari program 2")



