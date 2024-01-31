# program list buku

list_buku = []
while True:
    print("Masukkan Data Buku")
    judul = input(" Masukkan judul buku\t: ")
    penulis = input("Masukkan nama penulis\t: ")



    buku_baru = [judul,penulis]
    list_buku.append(buku_baru)
    print(buku_baru)    

    print("\n\n","="*10,"Data Buku","="*10)
    print("No. | Judul\t\t | Penulis")
    for index, i in enumerate(list_buku):
        print(f"{index}. |{i[0]} | {i[1]}")

    print("\n\n","="*20)
    isLanjut= input("Apakah akan dilanjutkan ? (y/n)")

    if isLanjut == "n":
        break

print("Program Selesai")