lagu = []

def tambah_lagu(judul, penyanyi):
    lagu.append(f" Judul: {judul} penyanyi: {penyanyi}")
    print("Lagu berhasil ditambahkan")

def tampilkan_lagu():
    if not lagu:
        print("Belum ada koleksi lagu")
    else:
        for i, l in enumerate(lagu, start=1):
            print(f"{i}. {l['lagu']} - {l['penyanyi']}")

def hapus_lagu():
    for i in range(len(lagu)):
        lagu[i]["judul"]

def cari_lagu(keyword):
    hasil = list(filter(lambda x: keyword.lower() in x['penyanyi'].lower(), lagu))
    return hasil

def main()