#!/bin/python3

# gelişmiş dizeler 

adim = "fatih"
print(adim[0]) # bu stringin dizenin ilk karakterini verecektir.
print(adim[-1]) # bu dizenin son karakterini verecektir. 

cümle = "bu bir cümledir"  #  eğerki ben bu cümlenin ilk kelimesini yazdırmak istersem 
print(cümle[:3]) # diyerek yazdırabilirim

# eğerki cümlenin ilk kelimseinin uzunluğunu bilmiyorsam ve index yoluyla çekimiyorsam şunu yapmalıyım 

print(cümle.split()) # bu fonksiyona delimeter denir yani sınırlayıcı eğerki içine birşey yazmaz isek default olarak boşluk karakterlerini sınırlıyacaktır. ve boşluklardan kesip bir liste aline getircektir


cümle_split = cümle.split() 
print(type(cümle_split))
# ilk kelimeyi almak ister isek 
print(cümle_split[0]) # kodunu kullanarak ilk kelimemizi yazdırmış oluruz.

# join ile birleştirmek 

cümle_join = " ".join(cümle_split) # burada listedeki her elemanın arasına boşluk koyarak onu bir stringe dönüştürdük.
print(type(cümle_join))
print(cümle_join)


# string in içinde çift tırnak kullanımı. 

#alinti1 = " ve şöyle dedi " sen çok kötü bir insansın"" # çift tırnakları karıştırdığı için yazım hatası verecektir. ilk çift tırnakta başlangıç 2. çif tınakta bitiş sayacaktır ve 3. 4. çif tırnakların ne  olduğunu anlıyamyacaktır. 

# print(alinti1)

# stringlerde kelmileri kullanmak için çift tırnak yada tek tırnak ile kullanabiliriz. 

alinti2 = " ve şöyle dedi ' sen çok kötü bir insansın ' "  # açılışımızı çift tırnak ile yaptığımız için tek tırnağı kullandığımız zaman karıştırmadı.
print(alinti2) 

alinti3 = ' ve şöyle dedi " sen çok kötü bir insansın" ' # stringi tek tırnak ile açtığımız için ve içerisinde çift tırnak kullandığımızdan  karıştırmadı .

print(alinti3)

# peki ya illaki ikiside çift tırnak içinde kuallanmak ister isek escape charcter yardımı ile yapabiliriz " \ " 

alinti4 = " ve şöyle dedi \" sen çok kötü bir insansın \" "  # burada \ kullanarak ounla birleşik olan karakterin kaçamak karakter olduğunu belirmiş olduk yani o karakter görmezden gelindi ve sadece yazım olarak algılanacak ve işleme sokulmayacaktır. böylelikle kullandığımız çift tırnağı bitim tırnağı olarak algılamıyacaktır. 
print(alinti4) 


bosluklu_metin = "                selam                   "  # eğerki biz bu metindeki sadece istediğimiz karakterleri yok etmek ister isek 
print(bosluklu_metin.strip()) # sprit bizim o stringdegi istedğimiz karakterleri yok edecektir. içi boş ise default olarak boşluğu koyacaktır. 

x_metin = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxselamm:)xxxxxxxxxxxxxxxxxxxx" 
print(x_metin.strip("x"))




print("F" in "Fati") #True  büyük küçük harflere duyarlıdır.
print("f" in "Fati") #False 

#büyük küçüke duyarlı olduğu için içerisindeki f i bulamadı 


harf = "F"
kelime = "Fati"

print(harf.lower() in kelime.lower()) #iki stringide bir değişkeni atatatak lowerını alıyoruz bu şekilde iki stringde küçük harflerle yazıldığı için sonucumuzda sapma yaşanmıyor



muzik = " Cahildim Dünyanın Rengine Gandım" 
print("Benim favori şarkım" + muzik + "dir ") #diyerek yazdıra biliriz fakat eğerki biz değişkenden sonra bir daha bir string girmek istersek tekrardan çift tırnak atmalı ve eklmeliyiz ve bu işlemimizi uzatır. bunun yerine 
print("Benim fovori şarkım {} dir".format(muzik)) #diyerek daha basit bir şekilde yapabiliriz.

# eğerki birden fazla değişken kullancak isek ; 

muzik2 = "Sen ayrı trende ben ayrı garda" 

print("Benim favori şarkılarım {} ve {} dir".format(muzik,muzik2)) # şeklinde kullanabiliriz ve formatın içine yazdığımız sırada değişkenleri atıyacaktır.

print("Benim favori şarkılarım {} ve {} dir".format(muzik2,muzik)) 

print("benim fovori şarkım %s dir" %muzik) 
muzik3 = "Cırtı cırtlak"
print(f"Benim favori şarkım {muzik} dir") 
print(f"benim favori şarkılarım {muzik} , {muzik2} ve {muzik3} dir") #en kullanışlı olan budur çünkü diğer metodlarda birden fazla değişken kullancağımız zaman sıralamasına dikkat ememiz greklidir fakat bunda değişkeni direk stringin içine yazdığımız için çok daha kullanışlıdır. 







