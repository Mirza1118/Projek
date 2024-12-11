import tkinter as tk

# Membuat jendela
window = tk.Tk()

# Daftar jurusan
jurusan = ["Teknik Informatika", "Sistem Informasi", "Ilmu Komputer", "Matematika"]

# Membuat listbox
listbox = tk.Listbox(window, width=30, height=5)
for jurusan in jurusan:
    listbox.insert(tk.END, jurusan)
listbox.pack()

# Fungsi untuk mendapatkan pilihan
def pilih_jurusan():
    pilihan = listbox.get(tk.ACTIVE)
    print("Jurusan yang dipilih:", pilihan)

# Tombol
button = tk.Button(window, text="Pilih", command=pilih_jurusan)
button.pack()

window.mainloop()