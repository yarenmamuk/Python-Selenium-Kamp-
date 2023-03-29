# for
# i=0 i<10 

for i in range(10):
    print(i)

print("***************")

for i in range(5,10):
    print(i)

print("***************")

for i in range(0,51,10): # 0 dan 51e kadar 10ar arttır
    print(i)

#print("***************")
# for i in range(0.1,0.5):
#   print(i)

krediler = ["İhtiyaç Kredisi", "Taşıt Kredisi", "Konut Kredisi"]
for kredi in krediler:
    print(kredi)

print("***************")

for i in range(len(krediler)):
    print(krediler[i])

print("***************")

#sonsuz döngü
i=0
while i < 10:
    print("x")
    i += 1
print("y")

print("***************")

krediler = ["İhtiyaç Kredisi", "Taşıt Kredisi", "Konut Kredisi"]
i = 0
while i < len(krediler): 
    print(krediler[i])
    i+=1
    if krediler[i] == "Konut Kredisi":
        break

print("**********************")

i=0
while i < len(krediler): 
    i+=1 # 0 başladı ama 1 ekledi yani 1. indeksi yazdı
    print(krediler[i])
    if krediler[i] == "Konut Kredisi":
        break

# fonksiyonlar
print("FONKSİYONLAR")

fiyat = 100
indirim = 20

#definition define

def calculate():
    print(100-20)

def calculateWithParams(fiyat,indirim):
    print(fiyat-indirim)

def sayHello(name):
    print(f"Merhaba {name}")

calculate()
calculateWithParams(50, 10)
calculateWithParams(100, 30)
sayHello("Halit")
sayHello("Yaren")

def calculateAndReturn(price, discount):
    return price-discount

yeniFiyat=calculateAndReturn(200, 50)
print(yeniFiyat)

#void
def calculatePrice(price, discount): #return yok çıktı none
    print(price-discount)
    
def calculatePriceAndReturn(price, discount):
    return price-discount

print("******************************")
fonk1 = calculatePrice(100, 50)
fonk2 = calculatePriceAndReturn(300, 100)
print(f"87. satır: {fonk1}")
print(f"90. satır: {fonk2}")




   