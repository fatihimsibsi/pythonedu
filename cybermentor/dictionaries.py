#!/bin/python3

#key/value pairs - anahtar değer çiftleri  {}
# [] list-   () tuples -  {} dictonaries 
icecekler = {"su" : 3 , "kutu kola" : 10 , "kutu gazoz" : 9 }
print(icecekler)

calisanlar = {"acemi" : ["hakkı" , "abbas"] , "deneyimli" : ["cafer" , "cemşit"] , "usta" : ["raşit" , "şerafettin"]}
print(calisanlar)

#ekleme 

calisanlar["patron"] = ["hurşit"]  # burada ekliyeceklerimizi  dictonary[key] = [value] şeklinde kullandık. key:value
print(calisanlar)

calisanlar.update({"çaycı" : ["rüstem" , "feridun"]}) #burada ise ekliyeceklermizi dictonary.update({key:value}) şeklinde ekledik.
print(calisanlar)

#bir keyin değerini güncellemk ister isek ; 

icecekler["su"] = 4
print(icecekler) 
