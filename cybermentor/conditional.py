#!/bin/python3

def ortalama(x):
	if x >= 50:
		return " sınıftan geçtin"
	else:
		return " sınıftan kaldın" 
		
print(ortalama(52))
print(ortalama(31))



def ortalama2(x):
	if x >= 50 :
		print("geçtiniz")
	else:
		print("kaldınız")
		

ortalama2(52)
ortalama2(31)


def alkol(yas,para):
	if(yas >= 18) and (para >=30 ) :
		return "satın alabilirsin"
	elif (yas >= 18 ) and (para < 30 ):
		return "paranız yetmiyor"
	elif (yas < 18 )  and (para >= 30 ): 
		return "yaşınız alkol almaya yetmiyor"
		
	else: 
		return "yaşınız ve paranız yetmiyor"
		

print(alkol(22,50))
print(alkol(17,50))
print(alkol(15,20))
print(alkol(25,15))
