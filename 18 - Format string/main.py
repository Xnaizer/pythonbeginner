# format string

# contoh generic
# string
nama = "marlene"
str = "hello1 " + nama

print(str)

format_str = f"hello2 {nama}"
print(format_str)

# angka # ini gabisa gatau nape

# angka = str(2005.5)
# format_str1 = "angka = " + angka
# print(format_str1)

angka2 = 2222.4
format_str2 = f"angka = {angka2}"
print(format_str2)

# boolean
boolean = True
format_srtbool = f"boolean = {boolean}"
print(format_srtbool)

# bilangan bulat
angka3 = 15
format_str3 = f"bilangan bulat = {angka3:d}"
print(format_str3)

# bilangan ribuan
angka4 = 2000
format_str4 = f"ribuan = {angka4:,}"
print(format_str4)

# bilangan desimal
angka5 = 2005.32134
format_str5 = f"desimal = {angka5:.2f}" #.2f itu adalah mengambil 2 angka dibelakang koma
print(format_str5)

# menampilkan leading zero
angka6 = 2005.1111
format_str6 = f"desimal = {angka6:8.2f}" #.2f itu adalah mengambil 2 angka dibelakang koma
print(format_str6) #8 itu adalah total ruangan yang diinginkan, pada terminal keliatan klo bergeser/ didepannya ada spasi pembatas.
# terus gimana klo mau space didepannya itu kea angka 0 ?

format_str6 = f"desimal = {angka6:010.2f}" # tambahin 0didepan x(spasi).2f
print(format_str6)


# menampilkan tanda plus / minus

angka_minus = -10
angka_plus = 10.1233
format_minus = f"minus = {angka_minus:+d}"
format_plus = f"plus = {angka_plus:+.2f}"

print(format_minus)
print(format_plus)


# memformat persen

persentase = 0.045
format_persen = f"persen = {persentase:%}"
print(format_persen)
format_persen = f"persen = {persentase:.2%}"
print(format_persen)

# melakukan operasi aritmatika di dalam placeholder

harga = 100000
jumlah = 5
format_oppp = f"harga total = Rp.{harga*jumlah:,} "
print(format_oppp)

# format angka lain( binary, octal, hexadecimal)

angka7 = 255
format_binary = f"bin = {bin(angka7)}"
format_octal = f"oct = {oct(angka7)}" 
format_hex =  f"hex = {hex(angka7)}"

print(format_binary)
print(format_octal)
print(format_hex)