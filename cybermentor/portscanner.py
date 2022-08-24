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

try :
	for port in range(50,85):
		s = socket.socket(socket.AF_INET , socket.SOCK_STREAM) # diyerek  bir s tanımlıyruz. burada AF_INET  ipv4 tür . SOCK_STREAM ise port
		#s tanımımızı kullancak olur isek şunu yapmalıyız host , port çünkü tanımızda host = ipv4    port = sockstreamdır.
		socket.setdefaulttimeout(1) # 1 sn bekledikten sonra time out vermesini söylüyor
		result = s.connect_ex((target,port)) #burada connect i değil connect_ex i kullanıyoruz bunun nedeni ise connect eğerki bağlantı yapılmadıysa bunun nedeni belirten farklı farklı çıktılar verir fakat connect_ex bağlantı yapılmadığında nedenini değil sadece 0 sonucunu verir# burada forun içinde dönen port numrasını yeni bir port olarak açmaya çalışıyoruz eğerki o portu açamaz isek bu o portun kullanıldığı anlamına gelmektedir.
		if result == 0:  ##açılmyan portu alması grektiğini söylüyoruz.
			print(f"{port} portu kullanımdadır.") # açılmayan port kullanımda olduğu için burada yazdırıyoruz.
		s.close() # bir sonraki döngüde karışıklık çıkarmaması için s i kapatarak sıfırlıyoruz.

except socket.error: #socket error verir ise yanıtsız kalmamk için programı kapatıyoruz.
		print("hata")
		sys.exit()
