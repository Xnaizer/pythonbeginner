# operator dalam bentuk methods

# merubah case dari string

# merubah semua ke upper case

salam = " bro! "
print("normal = " + salam )
salam = salam.upper()

# merubah ke lower case
alay = " aKu KecE AbieeeZzZzZZZZz"
print("normal = " + alay )
alay = alay.lower()
print("lower = " + alay) 

# pengecekan dengan isX method

# contoh untuk pengecekan lower case 
salam1 = "sist"
salam2 = "\\22\\22\\"
apakah_lower = salam1.islower() #hasilnya akan bolean
print(salam1 + " is lower = " + str(apakah_lower))
apakah_upper = salam1.isupper() #hasilnya akan bolean
print(salam1 + " is upper = " + str(apakah_upper))

# isalpha() -> untuk mengecek semuanya huruf
apakah_isalpha = salam1.isalpha()
print(salam1 + " isalpha / huruf semua = " + str(apakah_isalpha))

# isalnum -> huruf dan angka
apakah_num = salam2.isalnum() # jika ada salah satu huruf dan angka maka akan true
print(salam2 + " isnum / huruf dan angka  = " + str(apakah_num))


# isdecimal -> angka saja
apakah_decimal = salam2.isdecimal()
print(salam2 + " isdecimal / angka saja=  " + str(apakah_decimal))


# isspace -> spasi, tab, newline \n
apakah_isspace = salam2.isspace()
print(salam2 + " isspace / ada spasi, tab, \\n = " + str(apakah_isspace))


# istitle -> semua kata dimulai dengan huruf besar jikalau salah satu kecil maka false
apakah_title = salam1.istitle()
print(salam1 + " istitle / huruf besar diawal = " + str(apakah_title))

## ngecek komponen startswith () endswith() 
cek_start = "Sangjangnim Babi".startswith("Sangjangnim")
print("start = " + str(cek_start))
# apakah awalan kata adalah sangjanim ? True

cek_end = "Sangjangnim Babi".endswith("Bab") # ini perkata bukan pehuruf
print("start = " + str(cek_end))

## penggabungan komponen join() split ()
pisah = ['aku','sayang','kamu']
gabung = ','.join(pisah)
print(gabung)

gabungan = ' '.join(pisah)
print(gabungan)
gabungan = ' ehek '.join(pisah)
print(gabungan)

gabungan1 = "akuehmsayangehmkamu"
print(gabungan1.split('ehm'))

# alokasi karakter rjust(), ljust() center()

kanan = "kanan".rjust(10)
print("'"+kanan+"'")

kiri = "kiri".ljust(10)
print("'"+kiri+"'")

tengah = "tengah".center(10,"x") # jadi space yg kosong akan diisi dengan x karna perintah 
print("'"+tengah+"'")

# kebalikanya -> strip()

tengah = "tengah".strip("x") # menghilangkan tanda x dengan command x

print("'"+tengah+"'")