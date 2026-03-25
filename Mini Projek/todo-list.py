todos = []

def tambah_tugas():
    tugas = input("Masukkan tugas kamu hari ini: ")

    data = {
        "tugas" : tugas,
        "status" : False
    }

    todos.append(data)

    print("Tugas berhasil ditambahkan \n")

def lihat_tugas():
    if len(todos) == 0:
        print("Tidak ada tugas")
        return
    
    print("Berikut daftar tugas")
    for i, item in enumerate(todos, start=1):
        statusTugas = "✓" if item["status"] else "✗"

        print(f"{i}. {item["tugas"]} [{statusTugas}]")


    print()

def tandai_selesai():
    lihat_tugas()

    if len(todos) == 0:
        return

    nomor = int(input("Masukkan nomor tugas yang sudah selesai: "))

    if nomor < 1 or nomor > len(todos):
        print("Tugas tidak valid")
        return
    
    todos[nomor -1]["status"] = True

    print("Tugas ditandai telah selesai")

def hapus_tugas():
    lihat_tugas()

    if len(todos) == 0:
        return
    
    nomor = int(input("Masukkan nomor tugas yang ingin dihapus: "))

    if nomor < 0 or nomor > len(todos):
        print("Nomor tidak valid")
        return

    todos.pop(nomor - 1)

    print("Tugas berhasil dihapus")

while True:

    print("---- Your To Do List")
    print("1. Tambah tugas ")
    print("2. Lihat tugas ")
    print("3. Tandai tugas ")
    print("4. Hapus tugas")
    print("5. Keluar dari program")

    pilihan = input("Pilih kebutuhanmu: ")
    if pilihan == "1":
        tambah_tugas()

    elif pilihan == "2":
        lihat_tugas()

    elif pilihan == "3":
        tandai_selesai()

    elif pilihan == "4":
        hapus_tugas()

    elif pilihan == "5":
        print("Program telah selesai")
        break

    else:
        print("pilihan tidak valid")
