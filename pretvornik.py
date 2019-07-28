
import tkinter as tk
class Pretvornik:
    def __init__(self, valuta):

        self.valuta = valuta
        valuta.title("Pretvornik valut")
        self.valute = ['--', 'Evro', 'Ameriški dolar', 'Japonski jen', 'Bolgarski lev', 'Češka krona', 'Britanski funt',
                      'Madžarski forint', 'Švicarski frank', 'Ruski rubelj', 'Indonezijska rupija',
                      'Južnokorejski won', 'Mehiški peso', 'Tajski baht', 'Filipinski peso', 'Malezijski ringgit']
        self.menjalnitecaj = {'Evro':1.0,
                             'Ameriški dolar': 1.1215,
                             'Japonski jen': 121.03,
                             'Bolgarski lev': 1.9558,
                             'Češka krona': 25.534,
                             'Britanski funt': 0.89968,
                             'Madžarski forint': 324.95,
                             'Švicarski frank': 1.1007,
                             'Ruski rubelj': 70.6525,
                             'Indonezijska rupija': 15639.32,
                             'Južnokorejski won': 1320.34,
                             'Mehiški peso': 21.3416,
                             'Tajski baht': 34.593,
                             'Filipinski peso': 57.321,
                             'Malezijski ringgit': 4.612}

        #input
        self.tekst1 = tk.Label(root, text="Preračunaj iz")
        self.tekst1.place(x=20, y=10) 

        self.napis1 = tk.StringVar(root)
        self.napis1.set('Evro')

        self.gumb1 = tk.OptionMenu(root, self.napis1, *self.valute) 
        self.gumb1.place(x=20, y=30)

        self.okno1 = tk.Entry(root, bd=1, width=10)
        self.okno1.place(x=30, y=70) 
        self.okno1.insert(0, "0,00") 
       

        #output
        self.tekst2 = tk.Label(root, text="Preračunaj v")
        self.tekst2.place(x=170, y=10)

        self.napis2 = tk.StringVar(root)
        self.napis2.set('Ameriški dolar')

        self.gumb2 = tk.OptionMenu(root, self.napis2, *self.valute)
        self.gumb2.place(x=170, y=30)

        #gumbi
        self.pretvori = tk.Button(root, text="Zamenjaj", command=self.Zamenjaj)
        self.pretvori.place(x=120, y=110)
        
        self.ponastavi = tk.Button(root, text="Ponastavi", command=self.Reset)
        self.ponastavi.place(x=115, y=140)
        
        

    def Convert(self):            
        if (self.napis1.get() != '--' and self.napis2.get() != '--'):
            self.vrednost = float(self.okno1.get().replace(',', '.') if self.okno1.get() else 0) * self.menjalnitecaj.get(self.napis2.get()) / self.menjalnitecaj.get(self.napis1.get())
            self.okno2 = tk.Label(root, text='                                                                      ')
            self.okno2.place(x=150, y=70) 
            self.okno2 = tk.Label(root, text=str(self.vrednost), bg="pink")
            self.okno2.place(x=180, y=70) 
            
        else:
            self.okno2 = tk.Label(root, text='Prosim izberite valuto.       ', bg="red")
            self.okno2.place(x=170, y=70)

        self.valuta.after(100, self.Convert)

    def Zamenjaj(self):
        x1 = self.napis1.get()
        x2 = self.napis2.get()
        self.napis1.set(x2)
        self.napis2.set(x1)
        
    def Reset(self):
        self.okno2 = tk.Label(root, text = "                                                                             ")
        self.okno2.place(x=100, y=70)
        self.napis1.set('--')
        self.napis2.set('--')
         

root = tk.Tk()
my_gui = Pretvornik(root)
root.geometry("330x250+10+10")
root.after(100, my_gui.Convert)
root.mainloop()
