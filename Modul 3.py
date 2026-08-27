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

def main()
