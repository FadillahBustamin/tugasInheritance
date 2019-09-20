class Ayah(object):
   def __init__(self, a):
      self.namaayah = a
   def cetakA(self):
      print("Nama Ayah : ", self.namaayah)

class Ibu(object):
   def __init__(self, b):
      self.namaibu = b
   def cetakB(self):
      print("Nama Ibu : ", self.namaibu)

class Anak(Ayah, Ibu):
   def __init__(self, a, b, c):
      Ayah.__init__(self, a)
      Ibu.__init__(self, b)
      self.namaanak = c
   def cetakC(self):
      print("Nama Anak : ", self.namaanak)

def main():
   obj = Anak("Bustamin", "Darnisa", "Dillah")

   obj.cetakA()
   obj.cetakB()
   obj.cetakC()

if __name__ == "__main__":
   main()
