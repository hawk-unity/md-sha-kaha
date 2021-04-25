import hashlib
print("""  
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
+            git hub : https://github.com/ka4ir -> MD5          +
+                                                               +
+         git hub : https://github.com/hawk-unity? -> SHA512    +
+                                                               +
+                      1 - SHA512 CRYPT                         + 
+                                                               +
+                      2  - MD5 CRYPT                           +                 
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

""")
seçim = input("Seçim yapınız: ")
if seçim == "1":
    m=hashlib.sha512()
    sha512 = input("STRİNG : ")
    m.update(sha512.encode('utf-8'))
    print(m.hexdigest())
elif seçim == "2":
        sifreleyici = hashlib.md5()
        metin = input("lütfen Hashlenecek metini giriniz: ")
        sifreleyici.update(metin.encode("utf-8"))
        hash = sifreleyici.hexdigest()
        print("Çıktı>>> %s" % hash)
     
