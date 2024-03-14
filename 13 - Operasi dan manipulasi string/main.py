# operasi dan manipulasi string

# 1. menyambungkan string ( concatenate )
nama_pertama = "ucup"
nama_tengah = "D"
nama_akhir = "flame"

nama_lengkap = nama_pertama + " " + nama_tengah + "'" + nama_akhir
print(nama_lengkap)


nama_pertama = nama_pertama + " " + nama_tengah + "'" + nama_akhir
print(nama_pertama) # nama_pertama di line 12 akan di print karna ketimpa

# 2. menghitung panjang dari string dengan operator length

panjang = len(nama_lengkap)
print("panjang dari " + nama_lengkap + "=" + str(panjang))

# 3. operator untuk string

# mengecek apakah ada komponen char atau string di string

d = "d"
status = d in nama_lengkap 
print("string " + d + " ada di " + nama_lengkap + "=" + str(status))

D1 = "D"
status1 = D1 in nama_lengkap 
print("string " + D1 + " ada di " + nama_lengkap + "=" + str(status1))

D2 = "D'fe" # jikalau satu huruf berbeda maka semuanya salah, karna perintah D2 khusus kata D'Fe 
# sementara D'fe dalam nama lengkap tidak ada, oleh karena itu dia menjadi false
status2 = D2 in nama_lengkap 
print("string " + D2 + " ada di " + nama_lengkap + "=" + str(status2))

D1 = "d"
status1 = D1 not in nama_lengkap 
print("string " + D1 + " ada di " + nama_lengkap + "=" + str(status1))

# mengulang string

print("wk"*10)
print(15*"wk")


#indexing
#mengambil data dari string

print ("index ke-0 : " + nama_lengkap[0])
# u c u p   D ' F l a m e = total ada 12 text ( termasuk spasi)
# 0 1 2 3 4 5 6 7 8 9 10 11 = indeks
print ("index ke-1 : " + nama_lengkap[1])
print ("index ke-2 : " + nama_lengkap[2])
print ("index ke-3 : " + nama_lengkap[3])
print ("index ke-4 : " + nama_lengkap[4])
print ("index ke-5 : " + nama_lengkap[5])
print ("index ke-6 : " + nama_lengkap[6])
print ("index ke-7 : " + nama_lengkap[7])
print ("index ke-8 : " + nama_lengkap[8])
print ("index ke-9 : " + nama_lengkap[9])


print ("index ke- -1 : " + nama_lengkap[-1]) #dimulai penghitungan dari paling terakhir kata 
print ("index ke- -2 : " + nama_lengkap[-2])
print ("index ke- -3 : " + nama_lengkap[-3])
print ("index ke- -4 : " + nama_lengkap[-4])
print ("index ke- -5 : " + nama_lengkap[-5])

# klo ambil indeks x sampai x gimana bwang ?
print ("indeks ke 0-3 : " + nama_lengkap[0:3])
# loh kok jadi ucu bang ? bukannya ke 3 itu p harusnya ucup dong
# nah itu klo di python angka terakhir adalah batas, dan batas itu ga diambil teksnya
# makanya klo mau ambil suatu teks string harus lebihin 1 

print ("indeks ke 0-4 ucup +1 ya karena ketentuan python : " + nama_lengkap[0:4])
print ("indeks ke 3-8 : " + nama_lengkap[3:9])
print ("indeks ke [0,2,4,6,8,10] :" + nama_lengkap[0:11:2])
# ucup D'flame
# uu 'lm mengambil huruf pembagian 2
# [0:11:2] 0 adalah indeks awal yang diinginkan, 11 adalah indeks batas akhir, 2 adalah kelipatan huruf yang diinginkan
print("mengambil index -1,-5 : " + nama_lengkap[-5:-1]) # tak dapat mengambil huruf e karena ketentuan 

# item paling kecil
print("paling kecil : " + min(nama_lengkap)) #btw ini jawabannya spasi asci code 32
print("paling besar : " + max(nama_lengkap)) # ini u karena asci codenya 117

ascii_code = ord(" ")
print(" ascii_code untuk spasi adalah " + str(ascii_code))

data = 117
print("ascii code 117 adalah : " + chr(data))

# 4. operator dalam bentuk method

data = "otong surotong pararotong"
jumlah = data.count("o")
print("jumlah data o pada " + data + " = " + str(jumlah))