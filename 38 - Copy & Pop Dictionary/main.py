# Copy Dictionary

teman_teman = {
    "cup":"ucup serucup",
    "tong":"otong surotong",
    "dung":"dudung surudung",
    "sep":"asep si kasyep",
    "cuy":"ucuy surucuy",
}

friends = teman_teman
print(f"teman-teman : {teman_teman}\n")
print(f"friends : {teman_teman}\n")

teman_teman["cup"] = " ucup si kweren "
print(f"teman-teman : {teman_teman}\n")
print(f"friends : {friends}\n")

# ini yang terjadi adalah  var teman" dan friends 2 diatas menghasilkan output yang sama
# karena tidak meggunakan .copy

friends = teman_teman.copy()
print(f"teman-teman : {teman_teman}\n")
print(f"friends : {teman_teman}\n")

teman_teman["cup"] = " ucup si kweren "
print(f"teman-teman : {teman_teman}\n")
print(f"friends : {friends}\n")

# Pop Dictionary # diambil berdasarkan key

print("="*10,"Data Pop","="*10)
print(friends)
dataasep = friends.pop("sep")
print(f"data asep = {dataasep}\n")
print(f"friends = {friends}\n")

# popitem dictionary # diambil yang terakhir
dataasep = friends.popitem()
print(f"data asep = {dataasep}\n")
print(f"friends = {friends}\n")



