import tkinter as tk

class oyuncu(tk.Label):
    def __init__(self, master):
        super().__init__(master = master, background = "white")
        self.eklemeSayisi = 3
        self.ulkeler = []
        self.renk = ""
        self.sira = 0

        """if self.ulkeSayisi / 3 < 3:
            self.eklemeSayisi = 3
        else:
            self.eklemeSayisi = self.ulkeSayisi / 3"""

    ulkeSayisi = 0
    kartlar = []
    kitalar = []
    def ekranaEkle(self):
        self["text"] = self.renk
        self["foreground"] = self.renk
    def ulkeSecildi(event):
        pass

    def saldiri(self):
        pass

    def kartKullan(self):
        pass

    def askerTasima(self, nereden, nereye):
        pass

    def bonusHesapla(self, index, ulke, gezilenler):
        aynirenkler = 0
        gezilenler.append(ulke._name)
        for komsu in ulke.komsular:
            if komsu.arkaPlan == ulke.arkaPlan and not komsu.bonusHesaplandimi:
                aynirenkler += 1;
                if(aynirenkler + index >= 5):
                    self.eklemeSayisi += 3
                    ulke.isaretle()
                else:
                    try:
                        gezilenler.index(komsu._name)
                    except:
                        self.bonusHesapla( index + 1,komsu,gezilenler)

