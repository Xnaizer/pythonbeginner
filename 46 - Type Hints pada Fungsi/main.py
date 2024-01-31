''' Type Hints untuk fungsi'''

# bentuk standar fungsi yang udah kita pelajari

# # studi kasus
# def fungsi(parameter):
#     hasil = parameter**2
#     print(hasil)

# fungsi(1)
# fungsi("ucup")
# fungsi(True)

# parameter disini akan menerima semua type data
# oleh karena itu jikalau ini dari fungsi ada lah sistem operasi aritmatika
# maka kejadian akan eror

# type hints

def sepuluh_pangkat(argument:int) -> int: # ini untuk mengetahui jikalau retunrnnya interger
    output = 10**argument
    return output

hasil = sepuluh_pangkat(2)
print(hasil)

def display(argument:str):
    print(argument)

display("ucup")

import os

# hasil = os.system("cls") #hilangin isi ini untuk melihat output
# print(hasil)