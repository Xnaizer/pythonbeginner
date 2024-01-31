# Latihan Fingsi 

import os 


# os.system("cls")

# print(f"{'PROGRAM MENGHITUNG LUAS':^40}")
# print(f"{'DAN KELILING PERSEGI PANJANG':^40}")
# print(f"{'-'*40:^40}")

# # mengambil input user
# LEBAR = int(input("Masukkan nilai lebar :  "))
# PANJANG = int(input("Masukkan nilai panjang : "))

# # program menghiting luas
# LUAS = PANJANG*LEBAR
# KELILING = 2*(PANJANG+LEBAR)

# print(f"hasil perhitungan luas = {LUAS}")
# print(f"hasil perhitungan keliling {KELILING} ")

def header():
    # ini fungsi header
    os.system("cls")

    print(f"{'PROGRAM MENGHITUNG LUAS':^40}")
    print(f"{'DAN KELILING PERSEGI PANJANG':^40}")
    print(f"{'-'*40:^40}")

def user_input():
    lebar = int(input("Masukkan nilai lebar :  "))
    panjang = int(input("Masukkan nilai panjang : "))

    return lebar,panjang

def luas(lebar,panjang):
    return (lebar*panjang)

def keliling(lebar,panjang):
    return 2*(lebar+panjang)

def display(message,value):
    print(f"hasil perhitungan {message} = {value}")


while True:
    header()
    pilihan = input("Pilih 1 untuk menghitung luas,\nPilih 2 untuk menghitung keliling\nPilihan anda :  ")
    if pilihan == "1":
        print(f"{' '*40:^40}")
        print(f"{'-'*40:^40}")
        print("Menghitung LUAS")
        print(f"{'-'*40:^40}")
        LEBAR,PANJANG = user_input()
        LUAS2 = luas(LEBAR,PANJANG)
        display(" luas = ",LUAS2)

    elif pilihan == "2":
        print(f"{' '*40:^40}")
        print(f"{'-'*40:^40}")
        print("Menghitung Keliling")
        print(f"{'-'*40:^40}")
        print("Menghitung Keliling")
        LEBAR,PANJANG = user_input()
        KELILING1 = keliling(LEBAR,PANJANG)
        display(" keliling = " ,KELILING1 )
    
    isContiniue = input ("\napakah lanjut (y/n): ")
    if isContiniue =="n":
        break

print("Program selesaii, Terimakasih")