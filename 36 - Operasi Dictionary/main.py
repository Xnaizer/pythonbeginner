# operator dictionary

data_dict = {
    "cup":"ucup surucup",
    "tong":"otong surotong",
    "dung":"dudung surudung",
}

# panjang directory
inilendict = len(data_dict)
print(f"panjang directory : {inilendict}")

# mengecek key exist atau tudak
inikey = "cup"
inicheckkey = inikey in data_dict
print(f"apakah {inikey} ada di data_dict : {inicheckkey}")

# mengakses value (read) dengan get
print(data_dict["cup"])
print(data_dict.get("cup"))
print(data_dict.get("kiss","key yang diketikkan tidak ada"))

# mengupdate data
data_dict["cup"] = "ucup sis ganteng" # mengupdate data
print(data_dict)
data_dict["sep"] = "asep si kastep" # menanmbahkan data
print(data_dict)

data_dict.update({"cup":"ucup serucup lagi"})
print(data_dict)

data_dict.update({"faqih":"faqihza si mang eak"})
print(data_dict)


