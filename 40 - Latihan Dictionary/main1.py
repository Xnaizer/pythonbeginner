# ini versi yang bisa terus terusan ngeinput


import datetime
import os 
import string
import random

mahasiswa_template = {
    'nama':'nama',
    'npm':'00000000',
    'sks_lulus':0,
    'lahir':datetime.datetime(1111,1,11)
}



os.system("cls") # klo ios os.system("clear")
data_mahasiswa = {}


while True:

    print("-"*20)
    print(f"{'SELAMAT DATANG':^20} ")
    print(f"{'DATA MAHASISWA':^20} ")
    print("-"*20)

    # dikode ini kita menginginkan kalo kita membuat database
    # dimana kita ingin membuat database dengan keys yang sama seperti mahasiswa_template.
    # maka kita akan menggunakan dict dan fromkeys dan keys.

    database = dict.fromkeys(mahasiswa_template.keys())
    database['nama'] = input("Masukkan nama kamu : ")
    database['npm'] = input("Masukkan npm kamu : ")
    database['sks_lulus'] = input("Masukkan jumlah sks lulus kamu : ")
    TAHUN_KELAHIRAN = int(input("Masukkan Tahun Kelahiran kamu (YYYY) :"))
    BULAN_KELAHIRAN = int(input("Masukkan Bulan Kelahiran kamu (1-12):"))
    HARI_KELAHIRAN = int(input("Masukkan Hari Kelahiran kamu (1-31):"))
    database['lahir'] = datetime.datetime(TAHUN_KELAHIRAN,BULAN_KELAHIRAN,HARI_KELAHIRAN)

    KEY = ''.join(random.choice(string.ascii_uppercase) for i in range(6)) #DISINI PENTING karena mengupdate key secara random
    # kita ingin membuat key, secara random, dan memilih string asci uppercode untuk 6x
    data_mahasiswa.update({KEY:database}) # supaya data terus masuk ke database
    os.system("cls")
    print("="*39)
    print("="*15,"DATABASE","="*14)

    print("="*39)
    print(f"{'Key':<10} {'Nama':<25} {'Npm':<15} {'Sks':<5}  {'Lahir':<15}")
    for i in data_mahasiswa:
        KEY = i
        NAMA = data_mahasiswa[KEY] ['nama']
        NPM  = data_mahasiswa[KEY] ['npm']
        SKS  = data_mahasiswa[KEY] ['sks_lulus']
        LAHIR = data_mahasiswa[KEY]['lahir'].strftime("%x")
        print(f"{KEY:<10} {NAMA:<25} {NPM:<15} {SKS:^5} {LAHIR:<15}")
        
    

    isLanjut= input("\n\nApakah akan dilanjutkan ? (y/n)")

    if isLanjut == "n":
        break  

    os.system("cls")
print("Program Selesai")











