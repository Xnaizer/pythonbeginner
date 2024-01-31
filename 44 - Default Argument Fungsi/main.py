
# Default Argument

# def fungsi(argument):
# def fungsi(argument = nilai defaultnya ):

def say_hello(nama):
    print(f"Halloww {nama}")
    
say_hello("ucup")
#say_hello() akan eror karna tidak ada argumen

def say_hello(nama = "Gantengg"):
    print(f"Halloww {nama}")

say_hello()

def sapa_dia(nama, pesan = "Apa kabss bangg??"):
    #fungsi dengan 1 input biasa dan satu default argument
    print(f"haii {nama},{pesan}")
    

def htg_pangkat(angka,pangkat):
    hasil = angka**pangkat
    return hasil

print(htg_pangkat(2,5))

hasil = htg_pangkat(pangkat = 5, angka = 2)
print(hasil) # ini biasanya dipakai ketika memiliki argument yang banyak
# maka kita dapat memanggil argumen didalam dan lgsg memberi valuenya
# jika salah satu argument dipanggil lalu setelah , tidak ada pendeklarasian argument
# maka (angka = 1,3) akan eror'

# contoh 4

def fungsi(input1 = 1,input2 = 2):
    hasil = input1 + input2
    return hasil

print(fungsi())
print(fungsi(input1=10))

