dizi = ["İhtiyaç Kredisi", 10, 5.2, True]
print(dizi)

krediler = ["İhtiyaç Kredisi", "Taşıt Kredisi", "Konut Kredisi"]
print(type(krediler))

print(krediler[0])

# print(krediler[5]) >>> out of range hatası 
print(len(krediler)) #lenght

krediler.append("Özel Kredi") # değer ekleme
print(krediler)

krediler.append("X kredisi")
print(krediler)

krediler.pop() # default olursa son yazılanı siler pop içine sayı yazılırsa onu siler.
print(krediler)

krediler.pop(0) # 0. indextekini siler
print(krediler)

krediler.remove("Taşıt Kredisi") #index sırasına göre bulduğu ilk değeri siler başka varsa o kalır.
print(krediler)

krediler.extend(["Y Kredisi", "Z Kredisi"]) # birden fazla ekleme yapmak için kullanılır.
print(krediler)