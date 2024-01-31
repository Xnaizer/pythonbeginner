import datetime

mahasiswa1 = {
    "nama":"Xnaizer",
    "npm":"270479134",
    "sks_lulus":112,
    "beasiswa":False,
    "lahir":datetime.datetime(2000,1,1),
}
mahasiswa2 = {

    "nama":"Chocachips",
    "npm":"25047473",
    "sks_lulus":130,
    "beasiswa":True,
    "lahir":datetime.datetime(2000,2,29),
}

mahasiswa3 = {

    "nama":"Stevenoer",
    "npm":"270479695",
    "sks_lulus":128,
    "beasiswa":False,
    "lahir":datetime.datetime(2000,7,5),
}

data_mahasiswa = {
    'LUVOUH01':mahasiswa1,
    'LUVOUH02':mahasiswa2,
    'LUVOUH03':mahasiswa3,
}

print(f"{'Key':<10} {'Nama':<13} {'Sks':<5} {'Beasiswa':<10} {'Lahir':<15}")
print("-"*50)

for i in data_mahasiswa:
    KEY = i
    NAMA = data_mahasiswa[KEY] ['nama']
    NIM  = data_mahasiswa[KEY] ['npm']
    SKS  = data_mahasiswa[KEY] ['sks_lulus']
    BEASISWA = data_mahasiswa[KEY] ['beasiswa']
    LAHIR = data_mahasiswa[KEY]['lahir'].strftime("%x")
    
    print(f"{KEY:<10} {NAMA:<13} {SKS:^5} {BEASISWA:<10} {LAHIR:<15}")

