'''* args '''

# memasukkan data/argument

def fungsi2(nama,tinggi,berat):
    print(f"{nama} punya tingggi {tinggi} dan berat {berat}")

fungsi2("ucup",170,40)

def fungsi(data_list):
    data = data_list.copy()
    nama = data[0]
    tinggi = data[1]
    berat = data[2]
    print(f"{nama} punya tinggi {tinggi} dan berat {berat}")

fungsi(["otong",130,70])

#kenalan dengan args

def fungsi1(*args): 
    nama = args[0]
    tinggi = args[1]
    berat = args[2]
    print(f"{nama} punya tingggi {tinggi} dan berat {berat}")

fungsi1("ucup",150,70)

# studi kasus 
def tambah(*data):
    output = 0
    for i in data:
        output += i
    
    return output

hasil = tambah(1,2,3,4,5,6,7,8,9)
print(f"hasil = {hasil}")

hasil = tambah(10,5,12)
print(f"hasil = {hasil}")