# fungsi ini mengambil code dri file eksternal

#1.  untuk menyambung program eksternal
import program_print
import program_ucup

#2. import dengan data
import variabel
#data ada di namespace file variabel
print(variabel.data)
print(variabel.data1)

# import dengan fungsi
import matematika
hasil = matematika.tambah(4,5)
print(hasil)