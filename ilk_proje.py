import sys
guvenli_liste = ["Umut" , "İlker" , "Deniz" , "Mehtap"]
isim = input("Lütfen isim giriniz: ")
if isim in guvenli_liste:
    print("Hoş Geldin")
else:
    print("İzniniz yok.Program sonlandırılıyor")
    sys.exit()