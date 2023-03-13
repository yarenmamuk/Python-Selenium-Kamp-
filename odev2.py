"""Bir öğrenci kayıt sistemi yazdığımızı düşünelim. Sistemimizdeki öğrencileri bir listede sadece ad soyad olacak şekilde tutalım.

Bu öğrenci kayıt sistemine;

Aldığı isim soy isim ile listeye öğrenci ekleyen
Aldığı isim soy isim ile eşleşen değeri listeden kaldıran
Listeye birden fazla öğrenci eklemeyi mümkün kılan
Listedeki tüm öğrencileri tek tek ekrana yazdıran
Öğrencinin listedeki index numarası öğrenci numarası olarak kabul edildiğini düşünerek öğrencinin numarasını öğrenmeyi mümkün kılan
Listeden birden fazla öğrenci silmeyi mümkün kılan (döngü kullanınız)
fonksiyonları geliştiriniz ve her bir fonksiyonu en az bir kere çağırarak konsolda test ediniz. """


students = ["Yaren Mamuk", "Melis Uslu", "Kürşat Alperen", "Sezay Tütüncüler","Beste Tekçeli"]

stundentName = input("Öğrenci adı: ")
studentSurname = input("Öğrenci soyadı: ")
# print(stundentName + " " + studentSurname)

# Aldığı isim soy isim ile listeye öğrenci ekleyen
students.append(stundentName + " " + studentSurname)
print(students)

# Aldığı isim soy isim ile eşleşen değeri listeden kaldıran
removeStudent = input("Silmek istediğiniz öğrencinin adı-soyadı: ")
students.remove(removeStudent)
print(students)

# Listeye birden fazla öğrenci eklemeyi mümkün kılan
number = int(input("Eklemek istediğiniz öğrenci sayısını giriniz: "))
i = 0
while(i<number):
    newStudent = input("Öğrenci ad-soyad: ")
    i+=1
    students.extend([newStudent])   
    print(newStudent)
print(students)

# Listedeki tüm öğrencileri tek tek ekrana yazdıran
for student in students:
    print(student)

# Öğrencinin listedeki index numarası öğrenci numarası olarak kabul edildiğini düşünerek öğrencinin numarasını öğrenmeyi mümkün kılan
studentNumber = input("Numarasını öğrenmek istediğiniz öğrencinin adı-soyadı: ")
number = students.index(studentNumber)
print(studentNumber + " öğrenicinin numarası: " + str(number))


# Listeden birden fazla öğrenci silmeyi mümkün kılan (döngü kullanınız)
removeStudents = int(input("Silmek istediğiniz öğrenci sayısı: "))
i =0
while (i < removeStudents):
    removeStudent = input("Silmek istediğiniz öğrencinin adı-soyadı: ")
    students.remove(removeStudent)
    i +=1
    print(students)

    
