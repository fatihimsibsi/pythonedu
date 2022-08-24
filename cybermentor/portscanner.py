#!/bin/python3

# öncelikle yapmak istediğimiz şey terminale  python3 portscanner.py <ip> ip adresi girdiğimizde çalışacak bir portscanner.py 

import sys
import socket
from datetime import datetime 

# ilk olarak hedefi tanımlamalıyız burada 
if len(sys.argv) == 2 : #sys.argv burada argüman demektir argüman0 portscanner.py argüman1 <ip> dir yanı burada. argümanlarda ekskiklik varmı diye kontrol ediyoruz. yani python3 argv[0] argv[1]  olarak toplamda 2 tane argüman varmı diye bakıyoruz.
	target = socket.gethostbyname(sys.argv[1]) # targeti 2. argümanımız olan ip adresini alık yerleştiriyoruz. # hostname i ipv4 e çeviriyoruz yani hostumuz yapıyoruz.
	
else:   # eksik argümanımız var ise argüman eksikliğini belirtiyoruz.
	print("eksik argüman girildi") 
	print(" örnek : python3 portscanner.py ipadress")
	
# banner hazırlıyoruz (şablon)
print("-" * 50)
print(f" {target} için portlar taranıyor ......")
print(f" tarama başlangıç saati : {str(datetime.now())}")
print("-" * 50)

