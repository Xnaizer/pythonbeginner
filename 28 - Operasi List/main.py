data_angka = [1,2,5,7,4,1,3,5,7,2,3,3.2,2,1,4,5,9,8,0]
print(f"data angka = \n {data_angka}")

#count data

dataj1 = data_angka.count(1)
dataj2 = data_angka.count(2)
dataj3 = data_angka.count(3)
dataj4 = data_angka.count(4)

print(f"jumlah angka 1 = {dataj1}")
print(f"jumlah angka 2 = {dataj2}")
print(f"jumlah angka 3 = {dataj3}")
print(f"jumlah angka 4 = {dataj4}")

# ambil posisi data
data = ["ucup","ujang","megi","dudung"]
print(f"data = {data}")

cari_index1 = data.index("dudung")
cari_index2 = data.index("ucup")
cari_index3 = data.index("megi")

print(f"index si dudung = {cari_index1}")
print(f"index si ucup = {cari_index2}")
print(f"index si megi = {cari_index3}")

# mengurutkan list
print(f"data angka sebelum di sorting {data_angka}")
data_angka.sort() # akan sesuai dengan 0 - 9
print(f"data angka setelah di sorting {data_angka}")

print(f"data string sebelum di sorting {data}")
data.sort() # akan sesuai abjad a - z
print(f"data string setelah di sorting {data}")

#balik listnya
data_angka.reverse()
data.reverse()
print(f"data di reverse = \n{data_angka} \n{data}")





