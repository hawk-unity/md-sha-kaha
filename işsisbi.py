import hashlib as hasher
import hashlib 
import passlib 
from passlib.hash import mssql2005 as m25
from passlib.hash import mssql2000 as m20

while True : 
    print("""
        ----------------------------------------------------
         git hub : https://github.com/ka4ir    
        ----------------------------------------------------                                                 
         git hub : https://github.com/hawk-unity                                                         
        ----------------------------------------------------
            1 - SHA512 CRYPT     |                     
            2 - MD5 CRYPT        |  
            3 - SHA 256 CRYPT    |
            4 - SHA 224 CRYPT    |
            5 - SHA 384 CRYPT    |
            6 - MD 4 CRYPT       |
			7 - MSSQL 2005 HASH  |
				""")
    seçim = input("Seçim yapınız: ")
    if seçim == "1":
        m=hashlib.sha512()
        sha512 = input("STRİNG :")
        m.update(sha512.encode('utf-8'))
        print(m.hexdigest())
    elif seçim == "2":
        sifreleyici = hashlib.md5()
        metin = input("lütfen Hashlenecek metini giriniz:")
        sifreleyici.update(metin.encode("utf-8"))
        hash = sifreleyici.hexdigest()
        print("Çıktı>>> %s" % hash)
    elif seçim =="3":
        me=hashlib.sha256()
        sha256 = input("STRİNG :")
        me.update(sha256.encode('utf-8'))
        print(me.hexdigest())
    elif seçim =="4":
        me=hashlib.sha224()
        sha224 = input("STRİNG :")
        me.update(sha224.encode('utf-8'))
        print(me.hexdigest())
    elif seçim == "5":
        me=hashlib.sha384()
        sha384 = input("STRİNG :")
        me.update(sha384.encode('utf-8'))
        print(me.hexdigest())
    elif seçim == "6":
         text = input("STRİNG : ")
         hashObject = hashlib.new('md4', text.encode('utf-8'))
         digest = hashObject.hexdigest()
         print(digest)
    elif seçim == "7":
		   x = input("STRİNG :")
		   x2 = m25.hash(x)
		   print("hash: "+ x2)
