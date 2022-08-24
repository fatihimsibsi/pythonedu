#!/bin/python3

# soketler bağlantı kurmak için kullanılır. örnk : portlar(bağlantınoktaları) ve ip adresler arasında 

import socket 
HOST = "127.0.0.1" #BİZE AİT HOST ip adresi 
PORT = 7777 #BAĞLANMAK İSTEDİĞİMİZ PORT 

s = socket.socket(socket.AF_INET , socket.SOCK_STREAM) # diyerek  bir s tanımlıyruz. burada AF_INET  ipv4 tür . SOCK_STREAM ise port 
#s tanımımızı kullancak olur isek şunu yapmalıyız host , port çünkü tanımızda host = ipv4    port = sockstreamdır. 

s.connect((HOST , PORT)) # der isek söyledğimiz ip adresi üzerinden söylediğimiz porta giriş yapacak portla iletişime geçecektir. 
