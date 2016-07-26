from tkinter import *

pencere = Tk() #pencere değişkenine Tk() ile bir pencere oluşturmasını söylüyoruz.
pencere.title("Örnek 1 | Afmha") #Pencere başlığı
pencere.wm_iconbitmap("gray75") #Pencere ikonu
pencere.minsize(200, 200) #Pencere boyutu en az 200px, 200px boyutlarında olabilir.
pencere.maxsize(1000, 700) #Pencere boyutu en fazla 1000px, 700px boyutlarında olabilir.
pencere.geometry("500x500+0+0") #Pencere boyutunu 500px, 500px olarak ayarla ve 0, 0 kordinatlarından başlat.
pencere.state("normal") #Pencere drumu "normal"

karsilama_mesaji = Label(text="Merhabalar, hoşgeldiniz.", fg="green")
karsilama_mesaji.pack()

pencere.update() #Pencere durumunu güncelliyoruz.

mainloop()
