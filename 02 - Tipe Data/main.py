# tipe data apa saja di python?

#interger atau angka satuan
data_int = 1
print("data : ", data_int, "bertipe : ", type(data_int))

#float atau angka dengan koma
data_float = 1.5
print("data : ", data_float, "bertipe : ", type(data_float))

#string atau kumpulan karakter
data_string = "hewan"
print("data : ", data_string, "bertipe : ", type(data_string))

#boolean atau true/false
data_bool = True
print("data : ", data_bool, "bertipe : ", type(data_bool))
print("data : ", data_bool, "bertipe : ", type(data_bool))

#tipe data khusus

#bilangan kompleks
data_complex = complex(5,6)
print("data : ", data_complex, "bertipe : ", type(data_complex))

#tipe data dari bahasa C

from ctypes import c_double

data_c_double = c_double(10.5)
print("data : ", data_c_double, "bertipe : ", type(data_c_double))




 