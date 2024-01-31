# Membuat Kalkulator Sederhana

# Latihan
print(20*"=")
print(" Aplikasi Kalkulator Sederhana ")
print(20*"="+ "\n")
      
angka1 = float(input("Masukkan Angka Pertama = " ))
operator = input("Pilihan eksekusi angka(+,-,*,/) = ")
angka2 = float(input("Masukan angka kedua = "))

# percabangannya
if operator == "+":
    hasil = angka1 + angka2
    print(f"Hasilnya adalah  {hasil}")

elif operator == "-":
    hasil = angka1 - angka2
    print(f"Hasilnya adalah  {hasil}")

elif operator == "*" or operator == "x":
    hasil = angka1 * angka2
    print(f"Hasilnya adalah  {hasil}")

elif operator == "/":
    hasil = angka1 / angka2
    print(f"Hasilnya adalah  {hasil}")

else:
    print("masukkan yang bener donk! :<")

print("akhir dari program")
