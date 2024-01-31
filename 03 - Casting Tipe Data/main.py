#Casting itu apa ? 
#merubah dari satu tipe ke tipe yang lain

print("================int=====================")
data_int = 1;
print("data = ", data_int, "type data = ", type(data_int))

data_flt = float(data_int)
data_str = str(data_int)
data_bool = bool(data_int) # akan false ketika angka 0
print("data = ", data_flt, "type data = ", type(data_flt))
print("data = ", data_str, "type data = ", type(data_str))
print("data = ", data_bool, "type data = ", type(data_bool))

#data float
print("================float=====================")
data_float = 9.9 ;
print("data = ", data_float, "type data = ", type(data_float))

data_flt = int(data_float) #angka akan dibulatkan kebawah 9.6 9.9 akan menjadi 9
#dan false jika int 0
data_str = str(data_float)
data_bool = bool(data_float) # akan false ketika angka 0
print("data = ", data_flt, "type data = ", type(data_flt))
print("data = ", data_str, "type data = ", type(data_str))
print("data = ", data_bool, "type data = ", type(data_bool))


#data boolean
print("================bool=====================")
data_bool = False ;
print("data = ", data_bool, "type data = ", type(data_bool))

data_flt = int(data_bool) #angka akan dibulatkan kebawah 9.6 9.9 akan menjadi 9
#dan false jika int 0
data_str = str(data_bool)
data_float = float(data_bool) # akan false ketika angka 0
print("data = ", data_flt, "type data = ", type(data_flt))
print("data = ", data_str, "type data = ", type(data_str))
print("data = ", data_float, "type data = ", type(data_float))


#data 

print("================string=====================")
data_str = "2" ; # jikalau disini " " maka string ke boolean nya akan false, tpi jika ada variabel stringnya maka akan true
print("data = ", data_str, "type data = ", type(data_str))

data_int = int(data_str) 
data_bool = bool(data_str)
data_float = float(data_str) # akan false ketika angka 0
print("data = ", data_int, "type data = ", type(data_int))
print("data = ", data_bool, "type data = ", type(data_bool)) # khusus ini 
print("data = ", data_float, "type data = ", type(data_float))


