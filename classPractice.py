class Banka:
    def krediBasvur(self):
        print("Kredi başvurusu yapıldı")
    
    def krediHesapla(self):
        print("Hesaplar yapıldı")

banka = Banka()
banka.krediBasvur()

# self
# self demek classın kendisi
class Matematik:
    def __init__(self,sayi1,sayi2): # constructor-yapıcı
        self.sayi1 = sayi1
        self.sayi2 = sayi2
        print("Matematik başladı (referansı oluştu)")

    def topla(self):
        return self.sayi1 + self.sayi2
    def cikar(self):
        return self.sayi1 - self.sayi2
    def bol(self):
        return self.sayi1 / self.sayi2
    def ccarp(self):
        return self.sayi1 * self.sayi2


matematik = Matematik(6,7)
sonuc = matematik.bol()
print("Sonuç: " + str(sonuc))

class Person:
    def __init__(self,name,lastName):
        self.name = name
        self.lastName = lastName


musteri1 = Person("Ahmet", "Demiroğ")
musteri2 = Person("Kerem", "Varış")
musteri3 = Person("Yaren", "Mamuk")

print(musteri1.name)
