# Operasi Komparasi
# Operasi untuk membandingkan nilai
# hasilnya selalu boolean T/F

#operatornya > , < , >= , <= , == , != , is , is not

a = 4
b = 2

# lebih besar dari >
print("========== lebih besar dari ( > )========")
hasil = a > 3
print (a,">",3,"=", hasil)

hasil = b > 3
print (b,">",3,"=", hasil)

hasil = b > 2
print (b,">",2,"=", hasil)

# kurang dari <
print("========== kurang dari ( < )========")
hasil = a < 3
print (a,"<",3,"=", hasil)

hasil = b < 3
print (b,"<",3,"=", hasil)

hasil = b < 2
print (b,"<",2,"=", hasil)

# lebih dari sama dengan
print("========== lebih dari sama dengan ( >= )========")
hasil = a >= 3
print (a,">=",3,"=", hasil)

hasil = b >= 3
print (b,">=",3,"=", hasil)

hasil = b >= 2
print (b,">=",2,"=", hasil)

# kurang dari sama dengan
print("========== lebih dari sama dengan ( <= )========")
hasil = a <= 3
print (a,"<=",3,"=", hasil)

hasil = b <= 3
print (b,"<=",3,"=", hasil)

hasil = b <= 2
print (b,"<=",2,"=", hasil)

#  sama dengan
print("========== lebih dari sama dengan ( == )========")
hasil = a == 4
print (a,"==",4,"=", hasil)

hasil = b == 3
print (b,"==",3,"=", hasil)

hasil = b == 2
print (b,"==",2,"=", hasil)

#  tidak sama dengan
print("========== tak sama dengan ( != )========")
hasil = a != 4
print (a,"!=",4,"=", hasil)

hasil = b != 3
print (b,"!=",3,"=", hasil)

hasil = b != 2
print (b,"!=",2,"=", hasil)

#"is" sebagai komparasi objek identity
print("========== a ============")
x = 5 #ini adalah assigment membuat object
y = 5
print("nilai x = ,", x, ",id = ", hex(id(x)))
print("nilai y = ,", y, ",id = ", hex(id(y)))
#id akan sama ketika assigmentnya sama ( 5 )
# hex(id(x)) digunakan untuk mengonversi id tersebut menjadi format heksadesimal.

hasil = x is y
print("x is y = ", hasil)

print("=========== b ===========")

x = 5 #ini adalah assigment membuat object
y = 7
print("nilai x = ,", x, ",id = ", hex(id(x)))
print("nilai y = ,", y, ",id = ", hex(id(y)))
#id akan sama ketika assigmentnya sama ( 5 )
# hex(id(x)) digunakan untuk mengonversi id tersebut menjadi format heksadesimal.

hasil = x is y
print("x is y = ", hasil)

# is not 

print("===========is not ===========")
x = 5 #ini adalah assigment membuat object
y = 5
print("nilai x = ,", x, ",id = ", hex(id(x)))
print("nilai y = ,", y, ",id = ", hex(id(y)))
#id akan sama ketika assigmentnya sama ( 5 )
# hex(id(x)) digunakan untuk mengonversi id tersebut menjadi format heksadesimal.

hasil = x is not y
print("x is y = ", hasil)

print("======================")

x = 5 #ini adalah assigment membuat object
y = 6
print("nilai x = ,", x, ",id = ", hex(id(x)))
print("nilai y = ,", y, ",id = ", hex(id(y)))
#id akan sama ketika assigmentnya sama ( 5 )
# hex(id(x)) digunakan untuk mengonversi id tersebut menjadi format heksadesimal.

hasil = x is not y
print("x is y = ", hasil)




