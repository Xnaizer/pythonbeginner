import datetime

data_waktu = datetime.datetime.now()
print(f" datetime now : {data_waktu}")
print(f" year now : {data_waktu.year}")
print(f" day now : {data_waktu.strftime('%A')}")

from collections import Counter

data = ["a","b","c","d","a","b","c","f"]
data_hitung = Counter(data)
print(f"data count = {data_hitung}")
print(f"data count a = {data_hitung['a']}")
print(f"data count f = {data_hitung['f']}")

import io

# file = io.open("file_text.text","r")
file = io.open("test.txt","r")
print(f"ini isi file {file.read()}")