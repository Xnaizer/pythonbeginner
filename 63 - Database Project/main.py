import os
import CRUD as CRUD

if __name__ == "__main__":
    sistem_operasi = os.name

    match sistem_operasi: # match adalah opsi lain seperti if untuk mencocokkan kejadian variable
        case "posix" : os.system("clear")
        case "nt" : os.system("cls")

    print("===========================")
    print(" SELAMAT DATANG DI PROGRAM ")
    print("   DATABASE PERPUSTAKAAN   ")
    print("===========================")

    # check ada basenya ada atau tidak
    CRUD.init_console()

while(True):
    match sistem_operasi: # match adalah opsi lain seperti if untuk mencocokkan kejadian variable
        case "posix" : os.system("clear")
        case "nt" : os.system("cls")

    print("===========================")
    print(" SELAMAT DATANG DI PROGRAM ")
    print("   DATABASE PERPUSTAKAAN   ")
    print("===========================")

    print(f"1. Read Data")
    print(f"2. Create Data")
    print(f"3. Update Data")
    print(f"4. Delete Data")

    user_option = input("Masukkan Opsi : ")

    
    try:
        match user_option:
            case "1": CRUD.read_console()
            case "2": CRUD.create_console()
            case "3": CRUD.update_console()
            case "4": CRUD.delete_console()                                     
            case _ if int(user_option) > 4: print("Pilihan tidak tersedia, Harap Pilih lagi: ")
    except ValueError:
        print("Input harus berupa angka. ")
    except:
        print(" ")
   
    is_done = input("Apakah Selesai (y/n)? ")
    if is_done == "y" or is_done == "Y" :
        break
    

print(" Program Berakhir, Terima Kasih! ")