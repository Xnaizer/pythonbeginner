# looping dari list

# for loop
print("For Loops")
angkas = [4,2,3,1,6,5]

for i in angkas:
    print(f"angka = {i} ")

peserta = ["ucup","dika","kira"]

print(" "*20)

for i in peserta:
    print(f"angka = {i} ")

print(" "*20)
# for loop dan range
print("For loop dan range")
    
angkas = [1,2,6,4,2,6,2,9]

panjang = len (angkas)

for i in range(panjang):
    print(f"angkas = {angkas[i]} ")


print(" "*20)
# while
print("While Loops")
    
angkas = [1,2,6,4,2,6,2,9]

panjang = len (angkas)    

i = 0

while i < panjang:
    print(f"angkas = {angkas[i]} ")
    i += 1

print(" "*20)

#list comprehension
print("list comprehension")
data = ["ucup",1,2,3,"otong"]

[print(f"data = {i}") for i in data] #singkat bat

angkas = [1,2,6,4,2,6,2,9]
angkass = [i**2 for i in angkas]
print (angkass)

print(" "*20)
# enumerate
print("enumerate")
data_list = ["ucup",1,2,3,"otong"]

for index, data in enumerate(data_list):
    print(f"index = {index}, data = {data}")