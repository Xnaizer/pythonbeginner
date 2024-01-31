# Latihan Perulangan Looping

#Segitiga siku siku
# *
# **
# ***
# ****
# *****
# ******

sisi = 4

# pakai for
count = 1 # dummy variable
for i in range(sisi):
    print("*"*count)
    count += 1
print("ini akhir nomor 1\n")
# pakai while

count = 1
while True:
    print("*"*count) # klo ini aja di run maka akan di print berulang terus menerus (tanpa count)
    count += 1
# karna disini posisinya bakalan True mulu, maka akan di eksekusi mulu codenya ampe dajjal dateng keanya masih jalan
# maka pake if pass
    if count == 7:
        break    #inijugabisa
    
    # if count > sisi:
    #     break

count = 1
while True:
    print("*"*count) # klo ini aja di run maka akan di print berulang terus menerus (tanpa count)
    count += 1
# karna disini posisinya bakalan True mulu, maka akan di eksekusi mulu codenya ampe dajjal dateng keanya masih jalan
# maka pake if pass
    if count == 7:
        break    #inijugabisa
    
    # if count > sisi:
    #     break



