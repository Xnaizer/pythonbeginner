''' **kwargs'''

def fungsi1(nama,tinggi,berat):
    '''fungsi biasa'''
    print(f"{nama} punya tinggi {tinggi} dan berat {berat}")

fungsi1("ucup",170,70)


def fungsi2(**kwargs):
    print(kwargs)
    print(kwargs["nama"])
    print(kwargs["tinggi"])
    print(kwargs["berat"])

fungsi2(nama = "ucup",tinggi = 150,berat = 60)

# studi kasus

def math(*args,**kwargs):
    hasil = 0
    if kwargs["option"] == "tambah": 
        for i in args:
            hasil += i

    elif kwargs["option"] == "kali":
        hasil = 1
        for i in args:
            hasil *= i
    
    else:
        print("tak ada operasi")

    return hasil



hasil = math(1,2,3,4,5,6,option="tambah") 
print(f"hasil jumlah adalah {hasil}")   
hasil = math(1,2,3,4,5,6,option="kali")   
print(f"hasil perkalian adalah {hasil}")   


# **kwargs akan mengambil setiap argument yang menggunakan pendeklarasian variable
# contoh : def func(nama = "ayam")

# *args akan mengambil semua argumen yang tidak menggunanakan pendeklarasian variabel
# contoh : def func(1,2,4,5,6,7,7,3,2)












