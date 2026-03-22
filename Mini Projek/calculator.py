def tambah(a, b):
    return a + b

def kurang(a, b):
    return a - b

def kali(a, b):
    return a * b

def bagi(a, b):
    if b == 0:
        print("Tidak bisa membagi dengan angka 0")
    return a / b

def pangkat(a, b):
    return a ** b

while True:
    print("\n==== Mini Calculator ====")
    print("1. Pertambahan: ")
    print("2. Pengurangan: ")
    print("3. Perkalian: ")
    print("4. Pembagian:")
    print("5. Perkalian: ")
    print("6. Keluar Program")

    pilihan = int(input("Masukkan pilihan kamu : "))

    if pilihan == 6:
        print("Program selesai")
        break

    if pilihan not in [1, 2, 3, 4, 5, 6]:
        print("Pilihan tidak valid")
        continue

    try:
        angka1 = float(input("Masukkan angka pertama: "))
        angka2 = float(input("Masukkan angka kedua: "))
    except:
        print("input harus angka")
        continue

    if pilihan == 1:
        hasil = tambah(angka1, angka2)

    elif pilihan == 2:
        hasil = kurang(angka1, angka2)

    elif pilihan == 3:
        hasil = kali(angka1, angka2)
    
    elif pilihan == 4:
        hasil = bagi(angka1, angka2)

    elif pilihan == 5:
        hasil = pangkat(angka1, angka2)

    print("Hasil, ", hasil)
