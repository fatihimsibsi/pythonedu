#!/bin/python3

Liste = [ " bir " , "iki" , 3 , "dört" , "5" ]
print(Liste[1]) #ikinci elemanı yazdıracaktır
print(Liste[0]) # birinci elamanı yazdıracaktır
print(Liste[2]) # üçüncü elemanı yazdıracaktır.
print(Liste[4])
#tip bakımı : 
print(type(Liste[2]))
print(type(Liste[0]))
print(type(Liste[4]))

## aralık belirtme 

print(Liste[2:5]) # ilk index nolu elamanı ve ikinci index nosuna kadar yazdırır. index 2 dahil index 2 den idex 5 e  kadar ayzdıracaktır.


print(Liste[2:]) # index nolu elamanı ve ondan sonra gelen bütün elamanları yazdırır.

print(Liste[:4]) # index nolu elamana kadar index 0 dan başlayarak yazdırır.

#tersten işlemler.

print(Liste[-1]) # tersten işlem yaparken index 0 geçersizdir terten ilk eleman index -1 dir. 
print(Liste[-3 : -1])# tersten bakıldığında index -1 den (ilk elamdan) index -3 e kadar olan elamanları yazdırır
print(Liste[-1:]) # tersten bakıldığında index -1 den düz olan son elemana kadar yazdırır. ( budurumda sadece kendini yazdırır) 
print(Liste[:-3]) # tersten bakıldığında ilk elamandan index -3 e kadar olan elamnları yazdırır.

print(len(Liste)) # listenin içindeki elaman saysını gösterir.
Liste.append("altı") #listeye eleman ekler 
Liste.insert(2 , "üç" ) # listenin istenilen indexine elaman ekler 
print(Liste)

Liste.pop() #içine yazlan indexteki öğeyi siler içinde birşey yok ise son elamanı siler 

print(Liste)

Liste.pop(2)

print(Liste)

Liste2 = ["çakı" , "çakmak" , "donlastiği"]

Liste3 = Liste + Liste2 #iki listeyi ekliyerek yeni bir liste elde ettik

print(Liste3)

Liste4 = Liste3 + [" bir " , "lira" ] # bir listeye yeni elamanlar ekliyerek yeni bir liste oluşturduk.
print(Liste4) 

## iki boyutlu listeler 2d list

yaslar = [["fati" , 21] , ["hakkı" , 31] , ["corç emmi" , 48]] 
print(yaslar)
fati_yas = yaslar[0][1] # fati isimli kiçi ilk olarak index 0 da yer almaktadır. fathin yası ise içierideki listenin index 1 de 
fati_isim = yaslar[0][0] # fati dış listenin index 0 dır. fatinin ismi ise iç listede index 0 dadır.
hakki_yas = yaslar[1][1] # hakkı dış listede index 1 de yar alamaktadır hakkının yaşı ise iç listede index 1 de yer almaktadır.
print(fati_yas)
print(fati_isim)
print(hakki_yas)

yaslar[2][1] = 44 ## der isek 2d listede belirtilen indexdexe ekleme yada düzeltme yapabiliriz.
print(yaslar)

