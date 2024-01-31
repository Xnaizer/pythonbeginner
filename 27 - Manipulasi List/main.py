## Operasi data list

#indeks  0(-3), 1(-2), 2(-1)
data = ["arya","gilang","dudung"]
data0 = data[0]
data1 = data[1]
data2 = data[2]
print(f"data pertama (index 0) = {data0}")
print(f"data pertama (index 1) = {data1}")
print(f"data pertama (index 2) = {data2}")

datamin1 = data[-1]
print(f"data terakhir (index -1) = {datamin1}")

# mengambil info jumlah data dalam list
panjang_data = len(data)
print(f"panjang data = {panjang_data}")

#menambahkan item pada list sesuai posisi
print(f"data sebelum di tambah \n {data}")

data.insert(1,"Asep")
print(f"data sesudah di tambah \n {data}")

# menambah diakhir list menggunakan append
data.append("jarjit")
print(f"data sesudah di tambah lagi \n {data}")

#menggabungkan list dengan list
databaru = ["data1","data2","data3"]
data.extend(databaru)
print(f"data gabungan = \n {data}")

#merubah data
data[2]= "micheal"
print(f"data ubah = \n {data}")

#menghapus data
data.remove("dudung")
print(f"data ubah = \n {data}")

#menghapus data paling belakang
data.pop()
print(f"data ubah akhir = \n {data}")

