data0 = [1,2]
data1 = [3,4]

datalist = [1,2,3,4]

print(f"list biasa {datalist}")

list2d = [data0,data1]
print(f"list 2d {list2d}")
list2d = [data0,data1,datalist,4,5,7]
print(f"list 2d campuran {list2d}")

# contoh pengunaan

peserta0 = ["abah",25,"Laki-laki"]
peserta1 = ["risna",21,"perempuan"]
peserta2 = ["arya",21,"laki laki"]

list_peserta = [peserta0,peserta1,peserta2]
print(f"peserta = {list_peserta}")

for i in list_peserta:
    print(" "*20) # jikalau gamau pake ini bisa \n di akhiran
    print(f"nama\t : {i[0]}")
    print(f"umur\t : {i[1]}")
    print(f"gender\t : {i[2]} ") # \n disini\

# dengan reference
    
list_copy = list_peserta.copy()
print(f"peserta = {list_copy}")
peserta0[0] = "micheal"
print(f"peserta = {list_copy}")     # ini sudah berubah menjadi micheal
print(f"peserta = {list_peserta}")  # tapi kenapa ini juga ikut berubah?
# penjelasan di next folder


