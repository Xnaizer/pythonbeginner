'''Tutorial membaca file eksternal'''

print(3*"=", "Membaca File Txt " , 3*"=")
file = open("data.txt",mode="r")

print(f"status read : {file.readable()}")
print(f"status write : {file.writable()}")
# print(file.read()) #baca seluruh file

# print(file.readline()) # membaca baris pertama
# print(file.readline()) # membaca baris kedua dan ketika ada command ini lagi dibawah akan membaca yang ke tiga dan seterusnya
print(file.readline(),end="") #untuk tidak ada enter diakhir

print(file.readlines()) # semua baris menjadi list

#disini harus close juga
print(f"apakah file sudah di close? {file.closed}")
#cara close 
file.close()
print(f"apakah file sudah di close? {file.closed}")

# salah satu teknik membuka file di python

print("\n",3*"=", " Membaca file txt dengan write ",3*"=")
with open("data.txt",mode="r") as file:
    content = file.readline()
    print(content,end="")
    print(f"apakah file sudah di close? : {file.closed}")

print(f"apakah file sudah di close? : {file.closed}")







