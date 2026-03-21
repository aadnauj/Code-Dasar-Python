expenses = []

def tambah_pengeluaran():
    nama = input("Masukkan nama pengeluaran: ")
    harga = int(input("Masukkan total harga: "))

    data = {
        "nama" : nama,
        "harga" : harga,
    }

    expenses.append(data)

    print("Pengeluaran berhasil ditambakan \n")


def lihat_pengeluaran():
    if len(expenses) == 0:
        print("Belum ada pengeluaran")
        return

    print("Daftar Pengeluaran \n")
    for i, item in enumerate(expenses, start=1):
        print(f"{i}, {item["nama"]} - Rp.{item["harga"]}")
    
    print()

def total_pengeluaran():
    total = 0

    for item in expenses:
        total += item["harga"]

    print(f"Total pengeluaran anda : {total}\n")


while True:
    print("==== EXPENSE TRANCKER ====")
    print("1. Masukkan pengeluaran")
    print("2. Lihat Pengeluaran")
    print("3. Total Pengeluaran")
    print("4. Keluar")

    pilihan = input("Pilih yang kamu mau: ")

    if pilihan == "1":
        tambah_pengeluaran()
    
    elif pilihan == "2":
        lihat_pengeluaran()

    elif pilihan == "3":
        total_pengeluaran()

    elif pilihan == "4":
        print("Program telah selesai")
        break

    else:
        print("Pilihan tidak valid")
        break



        
