nilai_siswa =[85,90,78,92,88]

jumlah_nilai = sum(nilai_siswa)
jumlah_siswa = len(nilai_siswa)
rata_rata = sum(nilai_siswa) / len(nilai_siswa)
print("rata-rata nilai ujian matematika adalah = ", rata_rata)

stock_barang = [
    ["TV", 15],
    ["Laptop", 7],
    ["Kulkas", 10],
    ["Microwave", 5]
]

for barang in stock_barang:
    print(f"stock {barang[0]}: {barang[1]} unit" )