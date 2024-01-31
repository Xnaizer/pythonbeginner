import datetime
import os 

mahasiswa_template = {
    'nama':'nama',
    'npm':'00000000',
    'sks_lulus':0,
    'lahir':datetime.datetime(1111,1,11)
}



os.system("cls") # klo ios os.system("clear")
data_mahasiswa = {}

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

print(database)

















