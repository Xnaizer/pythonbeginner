# __main__ adalah untuk top level code enviroment


# print(__name__) == "__main__ "
## __name__ pada file program utama

print(f"nilai __name__ pada main.py = '{__name__}'")
## __name__ pada program eksternal adalah
import fungsi #name akan berubah menjadi nama file ketika dipanggil ke dalam file yang berbeda
# atau berada pada program file utama

## contoh penggunaan __main__

# deklarasi
def fungsi_tambah(a:int,b:int)->int:
    angka1 = 5
    angka2 = 10
    hasil = fungsi_tambah(angka1,angka2)
    print(f"hasil tambah = {hasil}")

## import package
# import package # tidak akan bisa karena tak berguna 
    
    # maka akan berguna jika digunakan di terminal
    # python package 
    # akan menampilkan isi __main__.p pada folder package
    # karna akan mengeksekusi file utama ketika di panggil foldernya
    #   python -m package akan menampilakan semua isi file main
    # python -m venv melihat command yang bisa digunakan