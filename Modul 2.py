class Dosen:
    def __init__(self, nama, nidn, mata_kuliah):
        self.nama = nama
        self.nidn = nidn
        self.mata_kuliah = mata_kuliah

    def info(self):
        print(f"Nama Dosen              : {self.nama}")
        print(f"Nomor nidn Dosen        : {self.nidn}")
        print(f"Mata Kuliah yang diajar : {self.mata_kuliah}")
        print("=======================================")

    def update_mata_kuliah(self, mk_baru):
        self.mata_kuliah = mk_baru


dosen1 = Dosen("Sugiono", "12345", "Pemrograman Dasar")
dosen2 = Dosen("Sukimin", "5555", "Praktikum 1")
dosen3 = Dosen("Siti", "09876", "bahasa indonesia")

dosen1.info()
dosen2.info()
dosen3.info()

print("\n========Update Mata Kuliah==========")
dosen1.update_mata_kuliah("Pemrograman web")
dosen1.info()
