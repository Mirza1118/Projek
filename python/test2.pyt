array_kosong = []

array_angka = [1,2,3,4,5]
array_huruf = ['a','b','c','d']

print("menampilkan array angka")
print(array_angka)

print("merubah array angka elemen ke 2")
print(array_angka)
array_angka.append(200)
print(array_angka)

print("menambah elemen di akhir array")
array_angka.append(300)
print(array_angka)
print("menambah elemen di tengah array")
array_angka.insert(3,100)
print(array_angka)

print("menghapus elemen di akhir array")
array_angka.remove(5)
print(array_angka)