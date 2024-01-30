import tkinter as tk
from PIL import ImageTk, Image
import maladieRespiratoire as rules
from experta import Fact
import tkinter.font as tkFont

# Rechercher dans les règles, quelle recommandation a été redirigée
def detectDisease():
    expertSystem = rules.maladieRespiratoire()
    expertSystem.reset()
    expertSystem.declare(Fact(TouxPersistante=str(TouxPersistante.get())))
    expertSystem.declare(Fact(Essoufflement=str(Essoufflement.get())))
    expertSystem.declare(Fact(DouleurThoracique=str(DouleurThoracique.get())))
    expertSystem.declare(Fact(SifflementsRespiratoires=str(SifflementsRespiratoires.get())))
    expertSystem.declare(Fact(FatigueExcessive=str(FatigueExcessive.get())))
    expertSystem.declare(Fact(Fievre=str(Fievre.get())))
    expertSystem.declare(Fact(RonflementFort=str(RonflementFort.get())))
    expertSystem.declare(Fact(ChangementsVoix=str(ChangementsVoix.get())))
    expertSystem.declare(Fact(CongestionNasale=str(CongestionNasale.get())))
    expertSystem.declare(Fact(CrachatsAnormaux=str(CrachatsAnormaux.get())))
    expertSystem.declare(Fact(DouleursArticulaires=str(DouleursArticulaires.get())))
    expertSystem.declare(Fact(Frissons=str(Frissons.get())))
    expertSystem.declare(Fact(MauxDeGorge=str(MauxDeGorge.get())))
    expertSystem.declare(Fact(MauxDeTete=str(MauxDeTete.get())))
    expertSystem.declare(Fact(Eternuements=str(Eternuements.get())))
    expertSystem.declare(Fact(PerteOdorat=str(PerteOdorat.get())))
    expertSystem.declare(Fact(PerteDuGout=str(PerteDuGout.get())))
    expertSystem.declare(Fact(PertePoids=str(PertePoids.get())))
    expertSystem.declare(Fact(Pâleur=str(Pâleur.get())))
    expertSystem.declare(Fact(Vertiges=str(Vertiges.get())))
    expertSystem.run()

    return expertSystem.maladies, expertSystem.description, expertSystem.traitement, expertSystem.photo


def openNewWindow():
    newWindow = tk.Toplevel()
    newWindow.title("Maladie Respiratoire")

    # définition de la géométrie du niveau supérieur
    newWindow.geometry("900x700")

    # widget Étiquette à afficher au niveau supérieur
    tk.Label(newWindow, text="Maladie Respiratoire").pack()

    name, description, traitement, photo = detectDisease()

    if name == description == traitement == photo == '':
        name = 'Malheureusement, nous n''avons pas pu identifier votre maladie respiratoire.'
        photo = r'C:\Users\Ghofrane\PycharmProjects\IA Project\photo\no.jpg'

    img = ImageTk.PhotoImage(Image.open(photo).resize((600, 300)))

    canvas = tk.Canvas(newWindow, width=900, height=700)
    canvas.pack()
    canvas.create_image(canvas.winfo_reqwidth() / 2, canvas.winfo_reqheight() / 4.5, anchor=tk.CENTER, image=img)
    canvas.img = img

    # nom maladies
    tk.Label(newWindow, text=str(name), font=("Helvetica", 16), fg="green").place(relx=0.5,
                                              rely=0.5,
                                              anchor='center')

    # description
    tk.Label(newWindow, text=str(description), font=("Helvetica", 14), fg="blue").place(relx=0.5,
                                                     rely=0.6,

                                                     anchor='center')

    # Ajouter un espace entre la description et le traitement
    tk.Label(newWindow, text="", font=("Helvetica", 12)).place(relx=0.5,
                                                               rely=0.7,
                                                               anchor='center')
    # traitement
    tk.Label(newWindow, text=str(traitement), font=("Helvetica", 12), wraplength=500).place(relx=0.5,
                                                     rely=0.7,
                                                     anchor='center')


background = "#eafffa"
source = tk.Tk()
source.title("Maladies Respiratoires")
source.config(bg=background)
source.resizable(True, True)

# variables de choix pour les champs sélectionnés
TouxPersistante = tk.IntVar()
Essoufflement = tk.IntVar()
DouleurThoracique = tk.IntVar()
SifflementsRespiratoires = tk.IntVar()
FatigueExcessive = tk.IntVar()
Fievre = tk.IntVar()
RonflementFort = tk.IntVar()
ChangementsVoix = tk.IntVar()
CongestionNasale = tk.IntVar()
CrachatsAnormaux = tk.IntVar()
DouleursArticulaires = tk.IntVar()
Frissons = tk.IntVar()
MauxDeGorge = tk.IntVar()
MauxDeTete = tk.IntVar()
Eternuements = tk.IntVar()
PerteOdorat = tk.IntVar()
PerteDuGout = tk.IntVar()
PertePoids = tk.IntVar()
Pâleur = tk.IntVar()
Vertiges = tk.IntVar()


# interface du programme
fontStyle = tkFont.Font(family="Helvetica", size=18, weight="bold")
l1 = tk.Label(source, text="Bienvenue dans le système expert ", width=40,
              fg='#008080', bg=background, font=fontStyle)
l1.grid(row=0, column=1, pady=0, padx=3)

l1 = tk.Label(source, text="  Pour diagnostiquer les maladies respiratoires", width=40,
              fg='#008080', bg=background, font=fontStyle)
l1.grid(row=1, column=1, pady=0, padx=3)

fontTipo = tkFont.Font(family="Helvetica", size=12)
tk.Label(source, text="Vérifiez les options", width=30, fg='#cd2731',
         bg=background, font=fontTipo).grid(row=3, column=1, pady=0)


#Partie1

# q1 Toux Persistante
tk.Label(source, text="Avez-vous eu une toux persistante qui dure depuis une période prolongée ? ",
         width=45, bg=background, font=fontTipo, wraplength=400).grid(row=2, column=0)

c1 = tk.Checkbutton(source, text="No", variable=TouxPersistante, onvalue=0, bg=background)
c1.grid(row=3, column=0)

c2 = tk.Checkbutton(source, text="Oui", variable=TouxPersistante,
                    onvalue=1,
                    bg=background)
c2.grid(row=4, column=0)

# q2 Essoufflement
tk.Label(source, text="Éprouvez-vous des difficultés à respirer ou un essoufflement inhabituel ? ",
         width=40, bg=background, font=fontTipo, wraplength=400).grid(row=5, column=0)

c3 = tk.Checkbutton(source, text="Non", variable=Essoufflement,
                    onvalue=0,
                    bg=background)
c3.grid(row=6, column=0)

c4 = tk.Checkbutton(source, text="Oui", variable=Essoufflement,
                    onvalue=1,
                    bg=background)
c4.grid(row=7, column=0)

# q3 Douleur Thoracique
tk.Label(source, text="Ressentez-vous une douleur ou une gêne au niveau de la poitrine ? ",
         width=40, bg=background, font=fontTipo, wraplength=400).grid(row=8, column=0)

c5 = tk.Checkbutton(source, text="Non", variable=DouleurThoracique,
                    onvalue=0, bg=background)
c5.grid(row=9, column=0)

c6 = tk.Checkbutton(source, text="Oui", variable=DouleurThoracique,
                    onvalue=1, bg=background)
c6.grid(row=10, column=0)

# q4 Sifflements Respiratoires
tk.Label(source, text="Entendez-vous des sifflements ou des sibilances pendant la respiration ? ",
         width=50, bg=background, font=fontTipo, wraplength=400).grid(row=11, column=0)

c7 = tk.Checkbutton(source, text="Non", variable=SifflementsRespiratoires,
                    onvalue=0,
                    bg=background)
c7.grid(row=12, column=0)

c8 = tk.Checkbutton(source, text="Oui", variable=SifflementsRespiratoires,
                    onvalue=1,
                    bg=background)
c8.grid(row=13, column=0)

# q5 Fatigue Excessive
tk.Label(source, text="Éprouvez-vous une fatigue excessive ou une sensation de manque d'énergie ? ",
         width=50, bg=background, font=fontTipo, wraplength=400).grid(row=14, column=0)

c9 = tk.Checkbutton(source, text="Non", variable=FatigueExcessive,
                    onvalue=0,
                    bg=background)
c9.grid(row=15, column=0)

c10 = tk.Checkbutton(source, text="Oui", variable=FatigueExcessive,
                     onvalue=1,
                     bg=background)
c10.grid(row=16, column=0)

# q6 Fiévre
tk.Label(source, text="Avez-vous de la fièvre ou une température corporelle élevée ?",
         width=50, bg=background, font=fontTipo).grid(row=17, column=0)

c11 = tk.Checkbutton(source, text="Non", variable=Fievre,
                     onvalue=0,
                     bg=background)
c11.grid(row=18, column=0)

c12 = tk.Checkbutton(source, text="Oui", variable=Fievre,
                     onvalue=1,
                     bg=background)
c12.grid(row=19, column=0)

# q7 Ronflement Fort
tk.Label(source, text="Souffrez-vous de ronflements forts pendant le sommeil ?",
         width=50, bg=background, font=fontTipo).grid(row=20, column=0)

c13 = tk.Checkbutton(source, text="Non", variable=RonflementFort,
                     onvalue=0,
                     bg=background)
c13.grid(row=21, column=0)

c14 = tk.Checkbutton(source, text="Oui", variable=RonflementFort,
                     onvalue=1,
                     bg=background)
c14.grid(row=22, column=0)

# q8 Changements du voix
tk.Label(source, text="Notez-vous des changements dans votre voix, tels que enrouement ou rauque ?",
         width=40, bg=background, font=fontTipo, wraplength=400).grid(row=23, column=0)

c15 = tk.Checkbutton(source, text="Non", variable=ChangementsVoix,
                     onvalue=0,
                     bg=background)
c15.grid(row=24, column=0)

c16 = tk.Checkbutton(source, text="Oui", variable=ChangementsVoix,
                     onvalue=1,
                     bg=background)
c16.grid(row=25, column=0)

#Partie 2

# q9 Congestion Nasale
tk.Label(source, text="Éprouvez-vous une congestion nasale ou une obstruction nasale persistante ?",
         width=50, bg=background, font=fontTipo, wraplength=400).grid(row=9, column=1)

c17 = tk.Checkbutton(source, text="Non", variable=CongestionNasale,
                     onvalue=0, bg=background)
c17.grid(row=10, column=1)

c18 = tk.Checkbutton(source, text="Oui", variable=CongestionNasale,
                     onvalue=1, bg=background)
c18.grid(row=11, column=1)

# q10 Crachats Anormaux
tk.Label(source, text="Avez-vous remarqué des crachats anormaux ?",
         width=50, bg=background, font=fontTipo).grid(row=12, column=1)

c19 = tk.Checkbutton(source, text="Non", variable=CrachatsAnormaux,
                     onvalue=0, bg=background)
c19.grid(row=13, column=1)

c20 = tk.Checkbutton(source, text="Oui", variable=CrachatsAnormaux,
                     onvalue=1,
                     bg=background)
c20.grid(row=14, column=1)

# q11 Douleurs Articulaires
tk.Label(source, text="Ressentez-vous des douleurs musculaires ou articulaires ?",
         width=50, bg=background, font=fontTipo).grid(row=15, column=1)

c21 = tk.Checkbutton(source, text="Non", variable=DouleursArticulaires,
                     onvalue=0,
                     bg=background)
c21.grid(row=16, column=1)

c22 = tk.Checkbutton(source, text="Oui", variable=DouleursArticulaires,
                     onvalue=1,
                     bg=background)
c22.grid(row=17, column=1)

# q12 Frissons
tk.Label(source, text="Éprouvez-vous des frissons ?",
         width=50, bg=background, font=fontTipo).grid(row=18, column=1)

c23 = tk.Checkbutton(source, text="Non", variable=Frissons,
                     onvalue=0,
                     bg=background)
c23.grid(row=19, column=1)

c24 = tk.Checkbutton(source, text="Oui", variable=Frissons,
                     onvalue=1,
                     bg=background)
c24.grid(row=20, column=1)


#Partie 3

# q13 Maux De Gorge
tk.Label(source, text="Ressentez-vous des maux de gorge ?",
         width=50, bg=background, font=fontTipo, wraplength=400).grid(row=2, column=2)

c25 = tk.Checkbutton(source, text="Non", variable=MauxDeGorge,
                     onvalue=0,
                     bg=background)
c25.grid(row=3, column=2)

c26 = tk.Checkbutton(source, text="Oui", variable=MauxDeGorge,
                     onvalue=1,
                     bg=background)
c26.grid(row=4, column=2)

# q14  Maux De Tete
tk.Label(source, text="Éprouvez-vous des maux de tête ?",
         width=50, bg=background, font=fontTipo, wraplength=400).grid(row=5, column=2)

c27 = tk.Checkbutton(source, text="Non", variable=MauxDeTete,
                     onvalue=0,
                     bg=background)
c27.grid(row=6, column=2)

c28 = tk.Checkbutton(source, text="Oui", variable=MauxDeTete,
                     onvalue=1,
                     bg=background)
c28.grid(row=7, column=2)

# q15  Eternuements
tk.Label(source, text="Éternuez-vous fréquemment ?",
         width=50, bg=background, font=fontTipo, wraplength=400).grid(row=8, column=2)

c29 = tk.Checkbutton(source, text="Non", variable=Eternuements,
                     onvalue=0,
                     bg=background)
c29.grid(row=9, column=2)

c30 = tk.Checkbutton(source, text="Oui", variable=Eternuements,
                     onvalue=1,
                     bg=background)
c30.grid(row=10, column=2)

# q16   Perte d'odorat
tk.Label(source, text="Experienciez-vous une perte d'odorat ?",
         width=50, bg=background, font=fontTipo, wraplength=400).grid(row=11, column=2)

c31 = tk.Checkbutton(source, text="Non", variable=PerteOdorat,
                     onvalue=0,
                     bg=background)
c31.grid(row=12, column=2)

c32 = tk.Checkbutton(source, text="Oui", variable=PerteOdorat,
                     onvalue=1,
                     bg=background)
c32.grid(row=13, column=2)

# q17 Perte Du Gout
tk.Label(source, text="Experienciez-vous une perte du goût ?",
         width=50, bg=background, font=fontTipo, wraplength=400).grid(row=14, column=2)

c33 = tk.Checkbutton(source, text="Non", variable=PerteDuGout,
                     onvalue=0,
                     bg=background)
c33.grid(row=15, column=2)

c34 = tk.Checkbutton(source, text="Oui", variable=PerteDuGout,
                     onvalue=1,
                     bg=background)
c34.grid(row=16, column=2)

# q18 Perte du Poids
tk.Label(source, text="Observiez-vous une perte de poids involontaire ?",
         width=50, bg=background, font=fontTipo, wraplength=400).grid(row=17, column=2)

c35 = tk.Checkbutton(source, text="Non", variable=PertePoids,
                     onvalue=0,
                     bg=background)
c35.grid(row=18, column=2)

c36 = tk.Checkbutton(source, text="Oui", variable=PertePoids,
                     onvalue=1,
                     bg=background)
c36.grid(row=19, column=2)

# q19 Pâleur
tk.Label(source, text="Observez-vous une pâleur inhabituelle ?",
         width=50, bg=background, font=fontTipo, wraplength=400).grid(row=20, column=2)

c37 = tk.Checkbutton(source, text="Non", variable=Pâleur,
                     onvalue=0,
                     bg=background)
c37.grid(row=21, column=2)

c38 = tk.Checkbutton(source, text="Oui", variable=Pâleur,
                     onvalue=1,
                     bg=background)
c38.grid(row=22, column=2)

# q20 Vertiges
tk.Label(source, text="Éprouvez-vous une sensation de vertige liée à votre respiration ?",
         width=50, bg=background, font=fontTipo, wraplength=400).grid(row=23, column=2)

c39 = tk.Checkbutton(source, text="Non", variable=Vertiges,
                     onvalue=0,
                     bg=background)
c39.grid(row=24, column=2)

c40 = tk.Checkbutton(source, text="Oui", variable=Vertiges,
                     onvalue=1,
                     bg=background)
c40.grid(row=25, column=2)


b1 = tk.Button(source, text="        Confirmer        ", command=openNewWindow, bg='#008080')
b1.grid(row=23, column=1, padx=10, pady=(10, 25), sticky="N")


# boucle de main pour exécuter l'application
source.mainloop()