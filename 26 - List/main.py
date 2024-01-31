## ---- List -----

#kumpulan data numbers
data_angka = [1,2,3,4,5]
print(data_angka)
data_angka = [4,3,6,1,7]
print(data_angka)

#kumpulan data string
data_string = ["abang","mau","ayam"]
print(data_string)

#kumpulan data boolean
data_boolean = [True,False,False,True]
print(data_boolean)

#data campuran
data_campuran = [1,"apasi",2,"gajelas",3,"gatau"]
print(data_campuran)

## cara alternatif membuat list
data_range = range(0,10,2) # range(start,stop,step)
data_list = list(data_range)
print(data_list)

## membuat list dengan loop, list comprehension
list_pake_for = [i for i in range(0,10)]
print(list_pake_for)
list_pake_for = [i**2 for i in range(0,10)]
print(list_pake_for)

## membuat list pake for pake if
list_pake_for_if=[i for i in range(0,10) if i != 5]
print(list_pake_for_if)
list_pake_for_if=[i for i in range(0,10) if i%2 == 0]
print(list_pake_for_if)

list_pake_for_if=[i for i in range(0,10) if i%2 != 0]
print(list_pake_for_if)


