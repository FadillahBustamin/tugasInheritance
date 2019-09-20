class Ibu(object):
    def __init__(self, nama, tinggi, berat):
        self.nama = nama
        self.tinggi = tinggi
        self.berat = berat

    def sifat(self):
        print("baik hati dan rajin menabung")

    def kebiasaan(self):
        print("nyanyi di kamar mandi")
# class Anak turunan dari class Ibu
class Anak(Ibu):
    pass

i = Ibu("Darnisa", 155, 55)
print()
print("Nama:", i.nama)
print("Tinggi:", i.tinggi, "cm")
print("Berat:", i.berat, "kg")
i.sifat()
i.kebiasaan()

# objek dari class Anak memiliki seluruh yang dimiliki class Ibu
a = Anak("Dillah", 157, 42)
print()
print("Nama:", a.nama)
print("Tinggi:", a.tinggi, "cm")
print("Berat:", a.berat, "kg")
a.sifat()
a.kebiasaan()
