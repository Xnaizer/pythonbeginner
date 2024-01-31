print("\n",15*"==Latihan==","\n")

#Soal Latihan Logika dan Komperasi
#1. --- 1 +++ 5 --- 10 +++ 15 ---
#2. +++ 1 --- 5 +++ 10 --- 15 +++

print ( "Nomor 1 = " )

#--- 1
angka1 = float(input('masukkan angka \nlebih besar dari 1 \nkurang dari 5 \nbesar dari 10 \nkurang dari 15 :  '))

isBesarSatu = ( angka1 > 1 )
print ( "angka besar dari 1 : ", isBesarSatu)

#++++5---
isKurangLima = ( angka1 < 5 )
print ( "angka kurang dari 5 : ", isKurangLima)

#---10
isBesarSepuluh = ( angka1 > 10 )
print ( "angka besar dari 10 : ", isBesarSepuluh)

#+++++15
isKurangLimaBelas = ( angka1 < 15 )
print ( "angka kurang dari 15 : ", isKurangLimaBelas)

isCorrect1 = isBesarSatu and isKurangLima or isBesarSepuluh and isKurangLimaBelas
print("angka yang anda masukkan : ", isCorrect1 )

print("\n",25*"=","\n")
print("1Nomor 2 : ")
#2. +++ 1 --- 5 +++ 10 --- 15 +++

angka2 = float(input("Masukkan angka \nkurang dari satu \nbesar dari 5 \nkecil dari 10 \nbesar dari 15 : "))

#++++1

isKurangSatu = ( angka2 < 1)
print("angka kurang dari 1 : ", isKurangSatu)

#----5++
isBesarLima = ( angka2 > 5)
print("angka besar dari 5 : ", isBesarLima)

#++++10
isKurangSepuluh = ( angka2 < 10 )
print("angka kurang dari 10 : ", isKurangSepuluh)

#--15++++
isBesarLimaBelas = ( angka2 > 15 )
print("angka besar dari 15 : ", isBesarLimaBelas)

isCorrect2 = isKurangSatu or isBesarLima and isKurangSepuluh or isBesarLimaBelas
print( "angka yang anda masukkan : ", isCorrect2 )



