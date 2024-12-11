import tkinter as tk

def tambah_Kelas():
    tambah_Kelas = entri_tambah.get()
    daftar_kelas.insert(tk.END, tambah_Kelas)
    entri_tambah.delete(0, tk.END)

def hapus_Kelas():
    index = daftar_kelas.curselection()
    if index:
        daftar_kelas.delete(index)

# Membuat jendela utama
jendela = tk.Tk()
jendela.title("Form Kelas")
jendela.geometry("500x500")


label_judul = tk.Label(jendela, text="Daftar Kelas")
label_judul.pack()


daftar_kelas = tk.Listbox(jendela)
daftar_kelas.insert(tk.END, "X", "XI", "XII")
daftar_kelas.pack()

# Membuat label dan tombol untuk menghapus jurusan
label_hapus = tk.Label(jendela, text="Kelas yang ingin dihapus:")
label_hapus.pack()
tombol_hapus = tk.Button(jendela, text="Hapus", command=hapus_Kelas)
tombol_hapus.pack()




# Membuat label dan entry untuk menambahkan jurusan
label_tambah = tk.Label(jendela, text="Kelas yang ingin ditambahkan:")
label_tambah.pack()
entri_tambah = tk.Entry(jendela)
entri_tambah.pack()
tombol_tambah = tk.Button(jendela, text="Tambahkan", command=tambah_Kelas)
tombol_tambah.pack()

# Menjalankan jendela
jendela.mainloop()