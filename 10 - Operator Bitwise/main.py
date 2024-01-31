'''
# = operasi dengan masing masing bit
# Operator bitwise atau binary
Int X     --->     0 0 0 0 0 0 0 0
nilai    Indeks  = 7 6 5 4 3 2 1 0
contoh : 

Int 1 --> 0 0 0 0 0 0 0 1 terletak di indeks 0 maka :
                                         2**0 = 1

Int 2 --> 0 0 0 0 0 0 1 0 terletak di indeks 1 maka :
                                         2**1 = 2

0 0 0 0 0 1 0 1 brp int ?
2**0 + 2**3 = 1 + 8 = Int 9

jika 2 | 1 itu :
0 0 0 0 0 0 1 0
0 0 0 0 0 0 0 1
---------------- | ( bitwise)
0 0 0 0 0 0 1 1
maka : 2**1 + 2**0 = Int 3

Operator yang digunakan : or , and , xor , not
                          
    
'''

print("============ Bitwise ============")
a = 13
b = 27

# bitwise OR ( | )
c = a | b
print("\n===========OR============")
print ("nilai : ", a, " binary : ", format(a,"08b"))
print ("nilai : ", b, " binary : ", format(b,"08b"))
print("------------------------------------( | )")
print ("nilai : ", c, " binary : ", format(c,"08b"))

# bitwise AND ( & )

c = a & b
print("\n===========AND============")
print ("nilai : ", a, " binary : ", format(a,"08b"))
print ("nilai : ", b, " binary : ", format(b,"08b"))
print("------------------------------------( & )")
print ("nilai : ", c, " binary : ", format(c,"08b"))


# bitwise xor ( ^ )

c = a ^ b
print("\n===========xor============")
print ("nilai : ", a, " binary : ", format(a,"08b"))
print ("nilai : ", b, " binary : ", format(b,"08b"))
print("------------------------------------( ^ )")
print ("nilai : ", c, " binary :", format(c,"08b"))


# bitwise not ( ~ )

c = ~a 
print("\n===========not============")
print ("nilai : ", a, " binary : ", format(a,"08b"))
print ("nilai : ", b, " binary : ", format(b,"08b"))
print("------------------------------------( ~ )")
print ("nilai : ", c, " binary :", format(c,"08b"))

'''
untuk bitwise not itu agak berbeda karna hasilnya kebalikannya
klo positive berbalik menjadi negatif begitupun sebaliknya tapi

0   0  0  0  0  0  0 | 0  0  0  0  0  0  0  0 
-7 -6 -5 -4 -3 -2 -1 | 0 +1 +2 +3 +4 +5 +6 +7
jika -1 berbanding terbalik ke 0
-2 = +1
-3 = +2
dan seterusnya

dan bitwise not tidak bisa c = a ~ b
hanya bisa c = ~(variable)


'''
#membanding balikan 0 ke 1 dan 1 ke 0 menggunakan xor
# caranya : 
print("\n===========xor reverse============")
d = 0b00000101
e = 0b11111111
print ("nilai menjadi : ", e^d, "binary : ",  format( e^d ,"08b"))

#shifting

#shift right (>>)
c = a >> 1 
d = b >> 1 # geser ke kanan satu kali
print("\n===========shift right============")
print ("nilai : ", a, " binary : ", format(a,"08b"))
print ("nilai : ", b, " binary : ", format(b,"08b"))
print("------------------------------------( >> )")
print ("nilai a : ", c, " binary :", format(c,"08b"))
print ("nilai a : ", d, " binary :", format(d,"08b"))

#shift right (>>)
c = a << 1 
d = b << 1 # geser ke kanan satu kali
print("\n===========shift left============")
print ("nilai : ", a, " binary : ", format(a,"08b"))
print ("nilai : ", b, " binary : ", format(b,"08b"))
print("------------------------------------( << )")
print ("nilai a : ", c, " binary :", format(c,"08b"))
print ("nilai a : ", d, " binary :", format(d,"08b"))







