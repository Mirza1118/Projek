import tkinter as tk

def tambah_jurusan():
    jurusan_baru = entri_tambah.get()
    daftar_jurusan.insert(tk.END, jurusan_baru)
    entri_tambah.delete(0, tk.END)

def hapus_jurusan():
    index = daftar_jurusan.curselection()
    if index:
        daftar_jurusan.delete(index)

# Membuat jendela utama
jendela = tk.Tk()
jendela.title("Form Jurusan")
jendela.geometry("500x500")

# Membuat label
label_judul = tk.Label(jendela, text="Daftar Jurusan")
label_judul.pack()

# Membuat listbox untuk menampilkan daftar jurusan
daftar_jurusan = tk.Listbox(jendela)
daftar_jurusan.insert(tk.END, "RPL", "DKV", "AK", "LPK3", "MP", "ULW", "BD", "LPB")
daftar_jurusan.pack()

# Membuat label dan tombol untuk menghapus jurusan
label_hapus = tk.Label(jendela, text="Jurusan yang ingin dihapus:")
label_hapus.pack()
tombol_hapus = tk.Button(jendela, text="Hapus", command=hapus_jurusan)
tombol_hapus.pack()




# Membuat label dan entry untuk menambahkan jurusan
label_tambah = tk.Label(jendela, text="Jurusan yang ingin ditambahkan:")
label_tambah.pack()
entri_tambah = tk.Entry(jendela)
entri_tambah.pack()
tombol_tambah = tk.Button(jendela, text="Tambahkan", command=tambah_jurusan)
tombol_tambah.pack()

# Menjalankan jendela
jendela.mainloop()