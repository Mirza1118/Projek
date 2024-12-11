import tkinter as tk
from tkinter import ttk
# Membuat jendela utama
window = tk.Tk()
window.geometry("500x500")
window.title("Form Siswa")

# Label dan entry untuk nama
label_nama = tk.Label(window, text="Nama:")
label_nama.pack()
entry_nama = tk.Entry(window)
entry_nama.pack() 


# Label dan combobox untuk kelas
label_kelas = tk.Label(window, text="Kelas:")
label_kelas.pack()
var_kelas = tk.StringVar(window)
combobox_kelas = ttk.Combobox(window, textvariable=var_kelas)
combobox_kelas['values'] = ('X', 'XI', 'XII')
combobox_kelas.pack()

# Label dan combobox untuk jurusan
label_jurusan = tk.Label(window, text="Jurusan:")
label_jurusan.pack()
var_jurusan = tk.StringVar(window)
combobox_jurusan = ttk.Combobox(window, textvariable=var_jurusan)
combobox_jurusan['values'] = ('RPL', 'DKV', 'Akuntansi','MPK','FKK','LPB','ULW','BD')
combobox_jurusan.pack()

# Label dan radio button untuk jenis kelamin
label_jenis_kelamin = tk.Label(window, text="Jenis Kelamin:")
label_jenis_kelamin.pack()
var_jenis_kelamin = tk.StringVar()
radio_laki = tk.Radiobutton(window, text="Laki-laki", variable=var_jenis_kelamin, value="Laki-laki")
radio_laki.pack()
radio_perempuan = tk.Radiobutton(window, text="Perempuan", variable=var_jenis_kelamin, value="Perempuan")
radio_perempuan.pack()

# Label dan entry untuk alamat, NISN, dan no HP
label_alamat = tk.Label(window, text="Alamat:")
label_alamat.pack()
entry_alamat = tk.Text(window, height=3, width=30)
entry_alamat.pack()

label_nisn = tk.Label(window, text="NISN:")
label_nisn.pack()
entry_nisn = tk.Entry(window)
entry_nisn.pack()

label_no_hp = tk.Label(window, text="No HP:")
label_no_hp.pack()
entry_no_hp = tk.Entry(window)
entry_no_hp.pack()

# Tombol submit
button_submit = tk.Button(window, text="Submit Data")
button_submit.pack()

# Fungsi untuk menampilkan data yang diinputkan (bisa dikembangkan)
def submit_data():
    nama = entry_nama.get()
    kelas = var_kelas.get()
    jurusan = var_jurusan.get()
    jenis_kelamin = var_jenis_kelamin.get()
    alamat = entry_alamat.get("1.0", tk.END)
    nisn = entry_nisn.get()
    no_hp = entry_no_hp.get()
    
    
    print("Nama:", nama)
    print("Kelas:", kelas)
    print("Jurusan:", jurusan)
    print("Jenis Kelamin:",jenis_kelamin )
    print("Alamat:", alamat)
    print("NISN", nisn)
    print("No.HP:", no_hp)
   

button_submit.config(command=submit_data)

window.mainloop()
