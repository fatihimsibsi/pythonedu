#!/bin/python3

bool1 = True 
bool2 = 3*3 == 9
bool3 = False 
bool4 = 3*3 != 9 

print(bool1,bool2,bool3,bool4)

print(type(bool1))
bool5= "True" # yanlış kullanımdır bu şekilde string olarak atanmıştır. doğru yada yanlışlığı değil sadece bir dizeyi belirtir.
print(type(bool5))


## boolean ilişkileri ve operatörleri 

buyuktur = 7 > 5 
kucuktur = 5 < 7 
buyuk_yada_esittir = 7 >= 7 
kucuk_yada_esittir = 7 <= 7 

ve_test = (7 > 5 )  and (5 < 7 ) #true
ve_test2 = (7 > 5 ) and  (5 > 7) #false
yada_test = (7 > 5 )  and (5 < 7 ) #true
yada_test2 = (7 > 5 ) and  (5 > 7) #true 

not_test = not True #False 
