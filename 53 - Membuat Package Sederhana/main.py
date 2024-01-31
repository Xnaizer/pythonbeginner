import time
from sains import fisika
from sains.fisika import gaya as gy

t_start = time.time()
import sains.matematika

#nama var = package.module.definisi/fungsi
hasil_tambah = sains.matematika.tambah(1,2,3,4,5)
print(f"hasil tambah dari package adalah {hasil_tambah}")
t_end = time.time()

print(f"waktu eksekusi adalah = {t_end - t_start}")

gaya = fisika.gaya(90,10)
print(f"hasil dari package fisika adalah {hasil_tambah}")

gaya = gy(90,10)
print(f"hasil dari package fisika adalah {hasil_tambah}")