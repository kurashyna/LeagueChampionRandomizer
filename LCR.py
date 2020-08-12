from tkinter import *
from tkinter.messagebox import *
import random
champions = ["Aatrox","Ahri","Akali","Alistar","Amumu","Anivia","Annie","Aphelios","Ashe","Aurelion Sol","Azir","Bard","Blitzcrank"
,"Brand","Braum","Caitlyn","Camille","Cassiopea","Cho'Gath","Corki","Darius","Diana","Dr.Mundo","Draven","Ekko","Elise","Evelynn"
,"Ezreal", "Fiddlesticks","Fiora","Fizz","Galio","Gankplank","Garen","Gnar","Gragas","Graves","Hecarim","Heimerdinger","Illaoi",
"Irelia","Ivern","Janna","Jarvan IV","Jax","Jayce","Jhin","Jinx","Kai'sa","Kalista","Karma","Karthus","Kassadin","Katarina","Kayle"
,"Kayn","Kennen","Kha'Zix","Kindred","Kled","Kog'Maw","LeBlanc","Lee Sin","Leona","Lillia","Lissandra","Lucian","Lulu","Lux",
"Malphite","Malzahar","Maokai","Master Yi","Miss Fortune","Mordekaiser","Morgana","Nami","Nasus","Nautilus","Neeko","Nidalee",
"Nocturne","Nunu & Willump","Olaf","Orianna","Ornn","Pantheon","Poppy","Pyke","Qiyana","Quinn","Rakan","Rammus","Rek'Sai",
"Renekton","Rengar","Riven","Rumble","Ryze","Sejuani","Senna","Sett","Shaco","Shen","Shyvana","Singed","Sion","Sivir","Skarner",
"Sona","Soraka","Swain","Sylas","Syndra","Tahm Kench","Taliyah","Talon","Taric","Teemo","Thresh","Tristana","Trundle","Tryndamere"
,"Twisted Fate","Twitch","Udyr","Urgot","Varus","Vayne","Veigar","Vel'Koz","Vi","Viktor","Vladimir","Volibear","Warwick","Wukong",
"Xayah","Xerath","Xin Zhao","Yasuo","Yone","Yorick","Yuumi","Zac","Zed","Ziggs","Zilean","Zoe","Zyra"]

def solo():
    i = random.randint(0,149)
    champion = champions[i]
    soloTexte = "Le Champion choisi est : " + champion
    showinfo("LCR : Solo", soloTexte)

def multi():
    multiWindow = Toplevel(mainWindow)
    multiWindow.title("LCR: Mode Multijoueurs")
    n = 1
    pickedNombers = []
    for y in range(JoueursScale.get()):
        i = random.randint(0,149)
        while i in pickedNombers:
            i = random.randint(0,149)
        pickedNombers.append(i)
        champion = champions[i]
        titleText = "Champions choisis aléatoirement pour les " + str(JoueursScale.get()) + " joueurs"
        Texte = "Joueur " + str(n) + " doit jouer : " + champion
        Label(multiWindow, text=titleText, font=("Times", "15")).grid(row=0, column=0, padx=20, pady=15)
        Label(multiWindow, text=Texte, font=("Arial", "11")).grid(row=n+1, column=0, padx=20, pady=2)
        n = n+1
    multiWindow.resizable(False,False)
    Button(multiWindow, text="Quitter", font=("Times","12"), command=lambda: multiWindow.destroy(), width=30).grid(row=n+2, column=0, pady=10)

def askChamp():
    askWindow = Toplevel(mainWindow)
    askWindow.title("LCR : Aléatoire avec champions donnés")
    Label(askWindow, text="Nom du joueur: ", font=("Times", "12")).grid(row=1, column=0)
    Label(askWindow, text="Pick du joueur: ", font=("Times", "12")).grid(row=1, column=1)
    Label(askWindow, text="Aléatoire avec champions donnés", font=("Times", "18")).grid(row=0, column=0, columnspan=2)
    Pseudos = []
    Picks = []
    for y in range(JoueursScale.get()):    
        Pseudos.append(Entry(askWindow, font=("Arial", "13"), width=20))
        Picks.append(Entry(askWindow, font=("Arial", "13"), width=25))
        Pseudos[y].grid(row=y+2, column=0)
        Picks[y].grid(row=y+2, column=1)
        def go():
            ListePicks = []
            PickNumber = []
            for i in range(JoueursScale.get()):
                y = random.randint(0, JoueursScale.get()-1)
                while y in PickNumber:
                    y = random.randint(0, JoueursScale.get()-1)
                PickNumber.append(y)
                ListePicks.append(Picks[y].get())
                
            for i in range(JoueursScale.get()):
                Picks[i].delete(0,100)
                Picks[i].insert(0, ListePicks[i])
            ButtonValider.config(text="Mélanger à nouveau")

    ButtonValider = Button(askWindow, text="Mélanger", font=("Times", "11"), command=go, width=25)
    ButtonValider.grid(row=JoueursScale.get()+3, pady="10", column=1)
    Button(askWindow, text="Quitter", command=lambda: askWindow.destroy(),font=("Times", "11"), width=20 ).grid(row=JoueursScale.get()+3, column=0, pady="10")
    askWindow.resizable(False, False)

mainWindow = Tk()
mainWindow.title("League Champion Randomizer")
Label(mainWindow, text="League Champion Randomizer", font=("Times","18")).grid(row=0, column=0, columnspan=3)
Label(mainWindow, text="Version 1.1.1 | Jusqu'à Yone", font=("Times","10")).grid(row=1, column=0, columnspan=3)

NbrJoueurs = IntVar
JoueursScale = Scale(mainWindow, variable=NbrJoueurs, orient='horizontal', from_=1, to=10, resolution=1, tickinterval=9, label="Nombre de joueurs", length=200, font=("Arial", "11"))
JoueursScale.grid(row=2, column=0, columnspan=3)
Button(mainWindow, text="Mode Solo", command=solo, font=("Times", "12")).grid(row=3, column=0, pady=10, padx=10, sticky="n")
Button(mainWindow, text="Mode Multijoueurs", command=multi, font=("Times", "12")).grid(row=3, column=1, pady=10, sticky="n")
Button(mainWindow, text="Aléatoire avec champions donnés", font=("Times", "12"), command=askChamp).grid(row=3, column=2, pady=10, padx=10, sticky="n")
mainWindow.resizable(False,False)
mainWindow.mainloop()