# Width and multiline 

# Data

data_nama = "Ucup Surucup"
data_umur = 17
data_tinggi = 173.04
data_nomor_sepatu = 44

# String
data_string = f"nama = {data_nama}, umur = {data_umur}, tinggi = {data_tinggi}, sepatu = {data_nomor_sepatu}"
print(5*"="+"Data String"+5*"=")
print(data_string)

# String Multiline ( dengan menggunakan enter, newline, \n )
data_string = f"nama = {data_nama},\numur = {data_umur},\ntinggi = {data_tinggi},\nsepatu = {data_nomor_sepatu}"
print("\n"+5*"="+"Data String"+5*"=")
print(data_string)

# string multiline ( kutip triplets )
data_string = f"""
nama = {data_nama} , tinggi = {data_tinggi}
umur = {data_umur}
tinggi = {data_tinggi}
sepatu = {data_nomor_sepatu}
"""
print("\n"+5*"="+"Data String"+5*"=")
print(data_string)

# mengatur lebar
data_nama = "Ucup"
data_string = f"""
nama   = {data_nama} 
umur   = {data_umur:>5} #setelah sama dengan huruf bergeser 5 langkah
tinggi = {data_tinggi}
sepatu = {data_nomor_sepatu}
"""

# rata kanan
data_string = f"""
nama   = {data_nama:>5} 
umur   = {data_umur:>5} 
tinggi = {data_tinggi:>5}
sepatu = {data_nomor_sepatu:>5}
"""
print("\n"+5*"="+"Data String"+5*"=")
print(data_string)