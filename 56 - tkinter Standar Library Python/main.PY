# GUI = Graphical User Interface

import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo

window = tk.Tk()
window.configure(bg="white")
window.geometry("300x200")
window.resizable(False,False)
window.title("Program Python Awal")

# frame input
input_frame = ttk.Frame(window)
# membutuhkan penempatan Grid, Pack, Place
input_frame.pack(padx=10,pady=10,fill="x",expand=True)

# komponen - komponen
# 1. Label nama komponen
namadepan = ttk.Label(input_frame,text="Masukkan Nama Depan Anda :")
namadepan.pack(padx=10,fill="x",expand=True)

# 2. entry nama depan
NAMA_DEPAN = tk.StringVar()
namadepan1 = ttk.Entry(input_frame,textvariable=NAMA_DEPAN)
namadepan1.pack(padx=10,pady=5,fill="x",expand=True)

# 3. Label nama komponen
namabelakang = ttk.Label(input_frame,text="Masukkan Nama Belakang Anda :")
namabelakang.pack(padx=10,fill="x",expand=True)

# 4. entry nama belakang
NAMA_BELAKANG = tk.StringVar()
namabelakang1 = ttk.Entry(input_frame,textvariable=NAMA_BELAKANG)
namabelakang1.pack(padx=10,pady=5,fill="x",expand=True)

# 5. Tombol
def tombol_klik():
    pesan1 = " "
    pesan2 = " "

    if NAMA_DEPAN.get() == "Risna":
        pesan1 = " Kesayangan Bangettt "
    
    elif NAMA_BELAKANG.get == "Dwi Indriani":
        pesan2 = "Sehat sehat terus yaak "

    else :
        "Haloo Selamat Datang!"
    
    showinfo(title="Welcoming Card",message=f"{pesan1}{pesan2}")


enter_button = ttk.Button(input_frame,text="Run Program!",command=tombol_klik)
enter_button.pack(fill='x',expand=True,padx=10,pady=10)


window.mainloop()




