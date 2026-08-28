lagu = []

def tambah_lagu(judul, penyanyi):
    lagu.append({"judul": judul, "penyanyi": penyanyi})
    print("Lagu berhasil ditambahkan")

def tampilkan_lagu():
    if not lagu:
        print("Belum ada koleksi lagu")
    else:
        for i, l in enumerate(lagu, start=1):
            print(f"{i}. {l['judul']} - {l['penyanyi']}")

def hapus_lagu(judul):
    for i in range(len(lagu)):
        if lagu[i]["judul"] == judul:
            lagu.pop(i)
            print("Lagu berhasil dihapus")
            return

    print("Judul tidak dapat ditemukan")


def cari_lagu(keyword):
    hasil = list(filter(lambda x: keyword.lower() in x['penyanyi'].lower(), lagu))
    return hasil


def main():
    while True:
        print("\n  ===Kumpulan Koleksi Lagu===")
        print("1. Tambah Lagu")
        print("2. Tampilkan Semua Lagu")
        print("3. Hapus Lagu")
        print("4. Cari Lagu")
        print("5. Keluar")\

        pilihan = input("Silahkan Pilih Menu (1-5): ")

        if pilihan == "1":
            judul = input("Masukkan judul lagu: ")
            penyanyi = input("Masukkan nama penyanyi: ")
            tambah_lagu(judul, penyanyi)

        elif pilihan == "2":
            tampilkan_lagu()

        elif pilihan == "3":
            judul = input("Masukkan judul yang ingin dihapus: ")
            hapus_lagu(judul)

        elif pilihan == "4":
            keyword = input("Masukkan nama penyanyi yang ingin dicari: ")
            hasil = cari_lagu(keyword)
            if hasil:
                print(f"Lagu dari penysnyi {keyword}: ")
                for pilih in hasil:
                    print(f"=> {pilih['judul']}")
            else:
                print(f"Penyanyi {keyword} tidak ditemukan")


        elif pilihan == "5":
            print("Terima kasih, sampai jumpa lagi")
            break

        else:
            print("Pilihan tidak valid, silahkan pilih lagi!!")

if __name__ == "__main__":
    main()