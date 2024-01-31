import numpy as np

vectora = np.array([1,2,3,4])
lista = [1,2,3,4]
print(f"list a = {lista}")
# print(list**2) # ini akan eror

print(f"vector a = {vectora}")
print(vectora**2)
print(vectora*2)
print(vectora+2)

matriksb = np.array([(1,2),(3,4)])
print(f"matriks b = \n{matriksb}")
print(f"matriks b**2 = \n{matriksb**2}")

zerosc = np.zeros((2,2))
print(f"zerox c = \n{zerosc}")

onesc = np.ones((2,2))
print(f"zerox c = \n{onesc}")

jumlah = matriksb + matriksb**2 + onesc
print(jumlah)