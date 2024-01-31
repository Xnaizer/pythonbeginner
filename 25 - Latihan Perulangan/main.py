# latihan perulangan segitiga siku siku

sisi = 10

# # menggunakan for
# count = 1 #ini adalah dummy
# for i in range(4):
#     print("*"*count)
#     count += 1


# # menggunakan while
# count = 1 
# while True:
#     print("*"*count)
#     count += 1

#     if count > sisi:
#         break

# # hanya ganjil saja
# count = 1
# for i in range(5):
#     if i%2 == 0:
#         print("ini genap : ",i)
#     else:
#         print("ini ganjil :",i)
# # klo segitiganya gimana 
        
# count = 1 
# while True:
#     print("*"*count)
#     count += 1 

#     if  count%2:
#         print("ganjil")

#     if count > sisi:
#         break


# print("+"*10)
# # situasi lain
# count = 1
# while True:
#     if (count%2):
#         print("*"*count)
#         count += 1

#     else:
#         count += 1
#         continue

#     if count > sisi:
#         break



# # bikin segitiga sama sisi
# count = 1
# spasi = int(sisi/2)

# while True:
#     if (count%2):
#         print(" "*spasi,"*"*count)
#         count += 1
#         spasi -= 1

#     else:
#         count += 1
#         continue

#     if count > sisi :
#         break

# bikin belah ketupat
sisi = 9
count = 1
spasi = sisi // 2

# Top part of the diamond
while count <= sisi:
    if count % 2:
        print(" " * spasi, "*" * count)
        count += 2
        spasi -= 1
    else:
        count += 1
        continue

# Bottom part of the diamond
count = sisi - 2
spasi = 1
while count >= 1:
    if count % 2:
        print(" " * spasi, "*" * count)
        count -= 2
        spasi += 1
    else:
        spasi += 1
        continue