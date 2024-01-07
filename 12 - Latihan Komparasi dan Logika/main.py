#latihan logika dan komperasi
#membuat gabungan area rentang dari angka

#+++++3------10++++++

inputUser = float(input("masukkan angka yang bernilai \nkurang dari 3 \natau \nlebih besar dari 10\n: "))

#\n menampilkan dalam shell 
#\t spasi dalam argument

#+++++3--------
#Memeriksa angka kurang dari 3 
isKurangDari = ( inputUser < 3)
print("kurang dari 3 = " ,isKurangDari)

#-------10++++
#Memeriksa angka lebih dari 10
isLebihDari = ( inputUser > 10 )
print("Lebih dari 10 = ", isLebihDari)

isCorrect = isKurangDari or isLebihDari
print("angka yang anda masukkan : ", isCorrect)

print("\n",10*"-","\n")
print("============irisan==========")

inputUser = float(input("masukkan angka yang bernilai \nkurang dari 3 \ndan \nlebih besar dari 10\n: "))
#bagaimana jika  -------3++++++10-----

#-------3+++++
#Memeriksa angka kurang dari 3 
isLebihDari = ( inputUser > 3)
print("besar dari 3 = " ,isLebihDari)

#++++++10----
#Memeriksa angka lebih dari 10
isKurangDari = ( inputUser < 10 )
print("kurang dari 10 = ", isKurangDari)

isCorrect = isKurangDari and isLebihDari
print("angka yang anda masukkan : ", isCorrect)


print("\n",20*"Latihan","\n")










