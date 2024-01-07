# operasi yang dapat dilakukan dengan penyingkatan
# operasi ditambah dengan assigment

a = 5 # adalah assigment
print("nilai a = ""hasilnya" , a)
# nilai a disini adalah 5

a = a + 1 #atau dapat dipersingkat dengan a += 1
print("nilai a = ""hasilnya" , a)
# sementara nilai a disini adalah 6 karena udah nambah 1

a += 1 # artinya sama aja dengan a + 1
print("nilai a += 1 ""hasilnya" , a)
# oleh karena itu nilai a disini adalah 7 karena berlanjut nilainya

a -= 2 # artinya ini dikurang 2, maka hasilnya akan 5
print("nilai a -= 2 ""hasilnya" , a)

a *= 3 # artinya ini akan dikalikan dengan 3
print("nilai a *= 3 ""hasilnya" , a)

a /= 5 # artinya ini akan dibagi 5
print("nilai a /= 5 ""hasilnya" , a)


b = 10
print("nilai b = 10" )

b %= 4 # artinya ini akan dibagi habis oleh 4 dan menampilkan sisa pembagi/ Modular
print("nilai b %= 5 ""hasilnya" , b)

b = 10
b //= 4 # artinya ini akan dibagi habis oleh 4 ( menampilkan brp banyak yang bisa di bagi oleh angka 4/angka lainnya)
print("nilai b //= 4 "  "hasilnya", b)

a = 5
print("nilai a = 5" )
a**= 3 # ini berarti a akan dipangkatkan dengan 3 
print("nilai a **= 4 "  "hasilnya", a)

# operasi bitwise
print("===================bitwise==")
c = True
print(" nilai c = ", c)
# Bitwise Or ( | )
c |= False
print("nilai C |= False akan menjadi ", c )


c = False
print(" nilai c = ", c)
c |= False
print("nilai C &= False akan menjadi ", c )

# Bitwise AND ( & )
c = True
print(" nilai c = ", c)
c &= False
print("nilai C &= False akan menjadi ", c )

c = False
print(" nilai c = ", c)
c &= False
print("nilai C &= False akan menjadi ", c )

c = True
print(" nilai c = ", c)
c &= True
print("nilai C &= True akan menjadi ", c )

# Bitwise  XOR 
c = True
print(" nilai c = ", c)
c ^= False
print("nilai C ^= False akan menjadi ", c )

c = False
print(" nilai c = ", c)
c ^= False
print("nilai C ^= False akan menjadi ", c )

c = True
print(" nilai c = ", c)
c ^= True
print("nilai C ^= True akan menjadi ", c )

# geser geser
d = 0b0100
print("nilai d =", format(d,'04b'))
d >>= 2
print("nilai d >>= 2, nilai d menjadi ",format(d,'04b') )

d <<= 1
print("nilai d <<= 1, nilai d menjadi ", format(d,'04b'))