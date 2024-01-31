'''write eksternal data'''

# 1. mode write, dia akan membuat file baru jika tak ada, dan akan menimpa isinya
with open("data_1.txt",'w',encoding="utf-8") as file:
    file.write("ucup surucup")

with open("data_1.txt",'w',encoding="utf-8") as file:
    file.write("overwrite")

# cara nambahin? pake append 

with open("data_2.txt",'w',encoding="utf-8") as file: #'w' itu adalah write
    file.write("xnaizer\n") # jika w diganti ke a maka file yang lama hanya akan ditambah dibawahnya jdi tidak akan overwrite

with open("data_2.txt",'a',encoding="utf-8") as file: # 'a' itu adalah append
    file.write("overwrite")

# mode r+
with open("data_3.txt",'w',encoding="utf-8") as file:
    file.write("data ke 3\n")

with open("data_3.txt",'r+',encoding="utf-8") as file: # 'a' itu adalah append:
    # data = file.read() klo ada ini "data ke 3 akan masuk ke file txt"
    file.write("baris 1 \n")
    file.write("baris 2 \n")
    file.write("baris 3 \n")


with open("data_3.txt",'r+',encoding="utf-8") as file: # 'a' itu adalah append:
    data = file.read()
    print(data)


with open("data_3.txt",'r+',encoding="utf-8") as file:
     # 'a' itu adalah append:
    file.write("otong \n")
    # fungsi dari R+ adalah menimpa baris yang ada sesuai dengan panjang data

