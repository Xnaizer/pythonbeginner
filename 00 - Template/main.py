import time
start_time = time.time()

print("hello world")
print("oiii")

print("ogheyy")
# ini file yaa jgn di exe

#compile ke bycode / exe
#python -m py_compile ( nama file )
#masuk ke direktor compilenya lalu run dgn python ( nama compilenya )
#gunakan TAB untuk mempercepat atau mengseleksi isi yang berhubungan
for a in range (1,10000000):
    a = 10
print(time.time() - start_time, "detik")
#source code -> interpreter -> Terminal
#interpreter adalah bahasa pemograman
#terminal adalah tempat eksekusi code
#source akan di eksekusi berdasarkan urutan
#source code bisa diubah menjadi bycode (proses compile)
#dengan mengetikan " python -m py_compile ( nama_file )"
#lalu file baru main.cpython-3 akan terbuat
#kesimpulannya file yang sudah di compile akan lebih cepat ketimbang file biasa, karna ekseskusi sudah tidak 1 per 1.
