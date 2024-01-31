'''Fungsi dengan argument (input)'''

#def nama_fungsi1(): #didalam ()argument,parameter,input yang akan masuk ke badan fungsi
    #badan fungsi

def func1(nama):
    # fungsi diatas akan menerima input dengan variabel nama
    print(f"Selamat datang di dunia wahai {nama}")

func1("arya")

def tambah(ang1,ang2):
    #fungsi tambah
    hasil = ang1 + ang2
    print(f"{ang1} + {ang2} = {hasil}")

tambah(20,1)


def say_hi(boyband):
    data = boyband.copy()
    for i in boyband:
        print(f"yang terhormat {i}")

anggota = ["ucup","otong","bambang"]

say_hi(anggota)