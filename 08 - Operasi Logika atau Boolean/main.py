# operasi logika atau boolean

# not , or, and, xor ( operator)


#not
print("===not===")
a = False  # jikau a = False maka not a adalah true begitu sebaliknya, karena Not adalah antonym dari nilai. True lawannya false.
c = not a
print("data a =", a)
print("-------NOT")
print ("data c =", c)


#or # jika salah satu true maka hasil true
print("===or===")
a = False
b = False
c = a or b
print(a,"OR",b,"=", c)
a = False
b = True
c = a or b
print(a," OR",b," =", c)
a = True
b = False
c = a or b
print(a,"  OR",b,"  =", c)
a = True
b = True
c = a or b
print(a,"   OR",b,"   =", c)

#and # jika salah satu false maka hasilnya false
print("===and===")
a = False
b = False
c = a and b
print(a,"and",b,"=", c)
a = False
b = True
c = a and b
print(a," and",b," =", c)
a = True
b = False
c = a and b
print(a,"  and",b,"  =", c)
a = True
b = True
c = a and b
print(a,"   and",b,"   =", c)

#xor # jika salah satu True maka True, klo sama keduanya maka False
print("===xor===")
a = False
b = False
c = a ^ b
print(a,"XOR",b,"=", c)
a = False
b = True
c = a ^ b
print(a," XOR",b," =", c)
a = True
b = False
c = a ^ b
print(a,"  XOR",b,"  =", c)
a = True
b = True
c = a ^ b
print(a,"   XOR",b,"   =", c)





