# Break digunakan untuk menyelesaikan suatu kasus
# break digunakan ketika suatu nilai yang dicari sudah didapatkan 
# maka bisa di end saja kasusnya

angka = 0

while angka < 5:
    angka += 1
    print(f"angka skrg = {angka}")

    if angka == 3:
        print("nice!")
        break # jika udah sampe looping ke 3 maka akan selesai

    print("wassup!")

print("cukup finish!")