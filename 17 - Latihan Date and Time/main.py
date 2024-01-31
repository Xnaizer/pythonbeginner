# Date and time latihan

import datetime as dt
# https://docs-python-org.translate.goog/3/library/?_x_tr_sl=en&_x_tr_tl=id&_x_tr_hl=id&_x_tr_pto=tc
# kita dapat mengimport atau memasukkan variable tertentu dari library python
# salah satu nya datetime, lalu datetime di persingkat menjadi dt
#datetime as dt

hari_ini = dt.date.today()
print(hari_ini)
print(f"Hari ini adalah hari = {hari_ini:%a}")

#tahun, bulan, tanggal
tanggal = dt.date(2004,7,27)
print(tanggal)
print(f"27 juli 2004 adalah hari = {tanggal:%a}")

print("Silahkan masukkan tanggal, bulan, dan tahun lahir anda\n")
tanggal = int(input("tanggal \t:"))
bulan = int(input("bulan \t\t:"))
tahun = int(input("tahun \t\t:"))

tanggal_lahir = dt.date(tahun,bulan,tanggal)
print(f"tanggal lahir anda adalah {tanggal_lahir}")
print(f"Anda lahir di hari {tanggal_lahir:%A}")
#%a utk hari disingkatkan mon thu wed
# %A untuk hari full Monday Thuesday
umur = hari_ini - tanggal_lahir
print(f"umur anda adalah1 : {umur}")
umur_tahun1 = umur / 365
print(f"umur anda adalah2 : {umur_tahun1}")
umur_tahun2 = umur // 365
print(f"umur anda adalah3 : {umur_tahun2}")
umur_tahun3 = umur.days // 365
print(f"umur anda adalah4 : {umur_tahun3}")
umur_tahun4 = umur.days // 365
print(f"umur anda adalah5 : {umur_tahun4} tahun ")
umur_bulan_sisa = (umur.days % 365 ) // 30
print(f"bulan = {umur_bulan_sisa} bulan")
umur_bulan_sisa1 = ((umur.days % 365) % 30) 
print(f"hari = {umur_bulan_sisa1}")
print(f" Umur anda sekarang {umur_tahun4} tahun, {umur_bulan_sisa} Bulan, {umur_bulan_sisa1} hari.")