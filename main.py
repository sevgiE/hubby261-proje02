import tkinter as tk
from tkinter import *
import time
from dataURL import DataURL
from getURL import GetURL

pencere = tk.Tk()
pencere.title("Ana Pencere")
pencere.geometry("200x100")

baslik = Label(pencere, text="MiniÖrümcek")
etiket1 = Label(pencere, text="[Mini örümceğe hoşgeldiniz!! ]")
etiket2 = Label(pencere, text="[Lütfen bir sayı tuşlayınız. ]")
etiket3 = Label(pencere, text="[Menüye yönlendiriliyorsunuz... ]")
buton1 = Button(pencere, text="<<< Buton >>>", fg="red",bg="green")
buton2 = Button(pencere, text="<<< Buton >>>", fg="black". bg="red", command=pencere


etiket.pack()
etiket2.pack()
etiket3.pack()
              
                
buton1 = Button(pencere, text= "0) Çıkış ", command=pencere1)
buton1.pack()

buton2 = Button(pencere, text= "1) URL Lİstele", command=pencere2)
buton2.pack()

buton3 = Button(pencere, text= "2) URL Ekle", command=pencere3)
buton3.pack()

buton4 = Button(pencere, text= "3) Örümcek Gönder", command=pencere4)
buton4.pack()

buton5 = Button(pencere, text= "4) Sonuçları Listele", command=pencere5)
buton5.pack()
                
useDataURL = DataURL()
useGetURL = GetURL()

#print("-: Mini Örümceğe hoş geldiniz! :-")
#print("|------------------------------|")
#print("")
#time.sleep(2)

while True:
    print("Menü: 0)Çıkış 1)URL Listele 2)URL Ekle 3)Örümcek Gönder 4)Sonuçları Listele")
    menuSecim = (input("Tercihiniz: "))
    if menuSecim.isdigit():
        menuSecim = int(menuSecim)
        if menuSecim == 0:
            print("Mini Örümcek kapatılıyor...")
            time.sleep(1)
            break
        elif menuSecim == 1:
            useDataURL.dataRead()
        elif menuSecim == 2:
            useDataURL.dataWrite()
        elif menuSecim == 3:
            useGetURL.getWeb()
        elif menuSecim == 4:
            useGetURL.getList()
        elif menuSecim>=4:
            print("0 ile 4 arasında bir seçim yapınız.")
    else:
        print("Lütfen geçerli bir menü numarası giriniz.")
         
          
                
