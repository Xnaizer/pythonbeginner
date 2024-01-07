#operasi aritmatika
'''
pioritas
1. ()
2. eksponen **
3. perkalian, pembagian, mod, floor dll
4. penjumlahan dan pengurangan

'''
a = 10
b = 3

#operasi tambah
hasil = a + b
print(a, "+", b ,"=", hasil)


#operasi kurang
hasil = a - b
print(a, "-", b ,"=", hasil)


#operasi perkalian
hasil = a * b
print(a, "*", b ,"=", hasil)


#operasi pembagian
hasil = a / b
print(a, "/", b ,"=", hasil)

#operasi eksponen / berpangkat
hasil = a ** b
print(a, "**", b ,"=", hasil)

#operasi modulus / sisa angka dari operasi hitungan
hasil = a % b
print(a, "%", b ,"=", hasil)

#operasi floor division ( pembulatan koma)
hasil = a // b
print(a, "//", b ,"=", hasil)

#pioritas operasi, operational precedence

x = 3
y = 2
z = 4

hasil = x ** y * z + x / y - y % z // x
print(x,'**',y,"*",z,"+",x,"/",y,"-",y,"%",z,"//",x,"=", hasil)
#proses perhitungannya mengikuti aturan kabataku
#dan jika dikurungkan , maka yang didalam kurung adalah pioritas utama

p = 3
q = 2
r = 4

hasil1 = (((p ** q) * r) + (p / q)) - ((q % r) // p)
print(p,'**',q,"*",r,"+",p,"/",q,"-",q,"%",r,"//",p,"=", hasil1)
#ini adalah pembuktian bahwa perhitungan matematika sudah menggunakana kabataku
#dalam pemrosesan.
