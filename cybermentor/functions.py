#!/bin/python3
# fonksiyonlar

def ben_kimim(): # paremetreleri olmadan bir fonskiyondur. paremetreteri eklmeek için alt satırda tab a basarak girilmelidir. Buna girinti denir.(indentation)
	isim = "fati" # girinti içine yazılmış bir değişken olduğu için lokal değişkendir bu tanım için geçerlidir. tekbaşına girinti dışında çalıştırılamaz.
	yas = 21 
	print("Benim adım " + isim + " yaşım ise " + str(yas) )
	
ben_kimim()


def yuz_ekle(num): # fonskiyonumuzu tanımlıyoruz ve parakntez içine yazılan şeyin num olduğunu belirtiyoruz.
	print( num + 100 ) # parantez içine yazılana 100 ekleyip yazdırıyoruz.
	
yuz_ekle(50) # parantez içine 50 yazdığımız için 50 ye 100 ekliyecektir.
 	



def toplama_islemi(x,y): # x ve y olarak iki adet değişkenimizin olduğunu ve bunları parantezin içinden gösterildiği şekilde verileeğini belirttik.
	print( x + y ) # fonsiyonun parantezi içinden aldığıız x ve y yi toplayarak yazdırdık.
	
toplama_islemi(50,63) # bilinmeyenleri parantez içinde verdik.
	


def carpma_islemi(x,y): # iki girdi alacağını söyeldik 
	return x*y  # x ve y bin çarpılıp geri döndrüleceğini yani değerin tutulacağını belirttirk.
	
print(carpma_islemi(7,7)) # fonskiyonun içinde print beelirtmediğimiz için print fonsiyonunun içinde oluşturmuş olduğumuz fonsiyonu ve değişkenleri girdik.  return burada carpma_islemi(x,y) = x*y görevini görmüş oldu 

def kare_kok(sayi): # sayımızı aldık 
 	print( int(sayi) ** .5 ) # .5 = 0.5 diyerek verilen sayının -(1/2) kuvvetiyle çarptık.
 	
kare_kok(16)
 
 
def yeni_satir():
	print("\n") # diyerek boş satırlar yazdırdık
	
yeni_satir() 


