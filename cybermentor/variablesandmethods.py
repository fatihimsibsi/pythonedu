#!/bin/python3

degisken1 = " çakı çakmak don lastiği 1 TL efenim" 
print(degisken1)

print(degisken1.upper()) # uppercase 
print(degisken1.lower()) # lowercase
print(degisken1.title()) # titlecase
print(len(degisken1)) #


isim = "Fati"
yas = 21 #int
kilo = 83.5 #float vürgüllüdür
print(isim) 
print(yas)
print(kilo)

print(" benim adım " + isim + " ben " + str(yas) + " yaşındayım ve " + str(kilo) + " kiloyum" )


toplam = 30  #toplama bir değer verdik 

print(toplam)

toplam += 1  # toplama ekleyip eşitlemesini söyledik

print(toplam)

toplanacak = 2  # toplanacak atadık 

toplam += toplanacak  #toplama toplanacak eklenip eşitleneceğini söyledik 
print(toplam)

toplanacak += 15 # toplanacak a 15 ekleyip eşitledik 
print("toplancak : " + str(toplanacak))
toplam += toplanacak # toplama toplanacağı ekleyip eşitledik .
print(toplam) # sonuç olarak 30 a 1 ekledik ardından topnacağı ekleyererek 33 oldu ardından ise toplacağa 15 eklediğimiz için toplanacak 17 ye eişt oldu. toplam ı toplanacakla toplayıp eşitleyince ise sonucumuz 33+ 17 den 50 olmuş oldu.
