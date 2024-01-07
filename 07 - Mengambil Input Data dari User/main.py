#episode input user
#data yang dimasukkan pasti string
data = input ("masukkan data : ")

print("data = ", data, "type = ", type(data))

#jika data yang dimasukkan int
data_int = int(input("masukkan angka : "))
print("data = ", data_int, "type = ", type(data_int))

#bagaima dengan boolean
data_bool = bool(input("masukkan nilai boolean : "))
print("data = ", data_bool, "type = ", type(data_bool)) # ini akan menghasilkan true walau diisi angka 1 atau 0
# biar sesuai dengan angka 1 adalah true dan 0 adalah false maka tambahkan int

#bagaima dengan boolean
data_bool = bool(int(input("masukkan nilai boolean : ")))
print("data = ", data_bool, "type = ", type(data_bool)) # ini akan menghasilkan true walau diisi angka 1 atau 0
# biar sesuai dengan angka 1 adalah true dan 0 adalah false maka tambahkan int