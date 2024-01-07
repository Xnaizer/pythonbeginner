
data = " ini adalah string"
print(data)
print(type(data))

# 1. cara membuat string
'''
1. dengan single quote ' texthere '
2. dengan double quote " text here "
'''

data1 = 'single quote'
data2 = " double string"

print (data1 + data2)

print ("'apa iyah bener itu '")
print ('"apasih masa"')
print('kamu cebelapa imut cih')
print(" aku suka kamu hehe :D ")

# membuat tanda ' menjadi string
print(' kamu terlalu indah ya\' :D ')
#menambahkan " \ " di kiri '

print(" kamu terlalu indah ya\" :D ")
print('g\'day, isn\'t it? ')

#backslash \ biar di print sebagai string
print("C:\\user\\mangeak") #\\ jadi 2 biar jadi string


#tab
print("ucup\t tolong jauhi \t aku")

#backspace
print("ucup tolong deketin     \b\b\b\b\baku")

#newline
print("ucup tolong kebawah ya \nambilin tas aku")
print("ini juga enter/ baris baru \rkebawah")

'''
\n itu adalah LF / Line Feed (unix,macos,linus)
\r itu Carriage Return (commodore, acorn, lisp)
\r\n itu line feed Carriage Return (windows)


'''

# String literal atau raw
#hati hati
print (' C:\new folder') # akan ditampilkan ew folder
#maka
print (' C:\\new folder') # akan ditampilkan ew folder
#atau menggunakan raw jika backslash digunakan dalam tempo yang banyak
print(r"C:\asda\cadada\nadasd\rasda\nad\\awdwa ")

#multiline literal string

print("""
Nama : Ucup
kelas: 2sd
""")

print(r"""
Nama : Ucup
kelas: 2sd
website : www.ucup.com\newnormal\gg\r
""")