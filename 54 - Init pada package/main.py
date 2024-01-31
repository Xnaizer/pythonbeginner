import sains.matematika.basic # seharusnya ini tidak akan berjalan programnyaa karena matematikanya tidak di deklerasikan
#tetapi karna di forlder sains __init__ sudah dideklarasikan, maka matetika tidak perlu di deklerasikan kembali
# tapi untuk fisika tidak dapat berjalan karena blum dideklerasikan di init

hasil_tambah = sains.matematika.basic.tambah(1,2,3,4,5,6)
print(f"hasil tambah = {hasil_tambah}")

hasil_kali = sains.matematika.basic.kali(1,2,3,4,5,6)
print(f"hasil kali = {hasil_kali}")