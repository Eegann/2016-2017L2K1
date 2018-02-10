# *-- coding: utf-8 --*

#
#
# *=*=* # ********************************************************************** # 
# *=*=* #                                                                        # 
# *=*=* #  Id:  main.py 8022 18-02-2017                                          #
# *=*=* #                                                                        #
# *=*=* #  Name:     main.py                                                     #
# *=*=* #  Project:  L2K1                                                        #
# *=*=* #  Author:   Created by <Benjamin Cohen> on 18/02/2017.                  #
# *=*=* #                                                                        #
# *=*=* # ********************************************************************** #
#
#
# *=*=* Copyright © 2017 Benjamin Cohen. All rights reserved.
#
# *=*=* Lesser General Public License (LGPL 3.0).
# *=*=* See COPYING and COPYING.LESSER for license details.
#
#
# <===> Functions by Benjamin Cohen <===>
#
#



#
#  Importation de l'ensemble des modules et fonctions nécessaires à la fenêtre principale.
#


import sys
from fonctionSup import *
import os
import fonctionLangue
from menuBarre import *
from InfoBulle import *
from fonctionBouton import *
from BDD import * # Importation des fonctions nécessaires à la base de données.


if sys.version_info < (3, 0):
    # Python 2
    import Tkinter as tk
    from Tkinter import *
    from Tkinter import font
else:
    # Python 3
    import tkinter as tk
    from tkinter import *
    from tkinter import font


	
#
#  Définition de la fenêtre principale.
#

fenetre = tk.Tk()
fenetre.title("L2K1")
fenetre.geometry("1000x600")
fenetre.config(bg="#CECECE")
fenetre.minsize(width=1000, height=600)

centrefenetre(fenetre) # Fonction permettant le centrage de la fenêtre par rapport à l'écran de l'utilisateur.


# Définition des styles de police de la fenêtre principale
policeTitre = font.Font(fenetre, size=32, weight='bold', family='Myriad')
policeSousTitre= font.Font(fenetre, size=20, weight='bold', family='Myriad')
police1 = font.Font(fenetre, size=16, weight='bold', family='Courier')
police2 = font.Font(fenetre, size=13, weight='bold', family='Courier')
police3 = font.Font(fenetre, size=9, weight='bold', family='Helvectica')

#
#  Vérification de la première utilisation du logiciel avec le fichier pre.txt
#

if(not(os.path.isfile('Ressources/data/pre'))):

    # Si le fichier pre.txt n'existe pas, alors celui-ci est créé dans le répertoire data.

    with open('Ressources/data/pre', 'wb') as pre:
        pre_pickler = pickle.Pickler(pre)
        pre_pickler.dump(0)

    #
    #  Définition et création de la fenêtre de première utilisation
    #


    def afficheInfo():

        
        top = tk.Toplevel()
        top.grab_set()
        top.focus()

        global var_langue

        police_top = font.Font(top, size=15, weight='bold', family='Courier') # Définition du style de police de la fenêtre de première utilisation.

        top.overrideredirect(1)
        top.geometry("400x355")
        top.config(bg="#C8F2FA")

        centrefenetre(top)
        champ_label = tk.Label(top, text="Merci d'utiliser notre logiciel\nL2K1 basé sur <Python> soumis à\nla licence LGPL3.\n\n\n\nVous pouvez nous soutenir en\nfaisant un don.", bg="#C8F2FA", font=police_top)
        champ_label.pack()
        champ_label.place(relx=.50, rely=.47, anchor="center")
        if var_langue=="anglais":
            champ_label["text"] = "Thank you for using our software\nL2K1 based on <Python> subject to\nthe LGPL3 license.\n\n\n\nYou can support us\nby doing a donation"

        btn = tk.Button(top, text="   OK    ", command=lambda: top.destroy())
        btn.place(relx=0.78, rely=0.84, anchor="center")
        btn.config(highlightbackground="#C8F2FA")
        top.wm_attributes('-alpha', 0.98)


    afficheInfo()



goCheckBdd() # Fonction de vérification du choix de l'utilisateur concernant le relevé de données statistiques.



#
#  Chargement des images boutons de la fenêtre principale.
#

imEye = tk.PhotoImage(file="Ressources/image/bouton/eye.gif")
imCodamotion = tk.PhotoImage(file="Ressources/image/bouton/codamotion.gif")
imDon = tk.PhotoImage(file="Ressources/image/bouton/don.gif")
imNew = tk.PhotoImage(file="Ressources/image/bouton/new.gif")
imHelp = tk.PhotoImage(file="Ressources/image/bouton/help.gif")
imLanceur = tk.PhotoImage(file="Ressources/image/bouton/lanceur.gif")

# Création des labels de titre.

labelTitre = Label(fenetre, text="Projet L2K1", fg="#FFFFFF", bg="#FF8103", font=policeTitre)
labelTitre.place(relx=.20, rely=0, anchor="n", height="85", width="800")

labelSousTitre = Label(fenetre, text="Bienvenue sur le projet L2K1", fg="#FFFFFF", bg="#FF8103", font=policeSousTitre)
labelSousTitre.place(relx=.75, rely=0, anchor="n", height="85", width="800")

labelFeetPage = Label(fenetre,relief="ridge", borderwidth=1, fg="#FFFFFF", bg="#a7a7a7", font=policeSousTitre)
labelFeetPage.place(relx=.5, rely=0.92, anchor="center",  height="120", width="2000")
labelFeetPage.config(highlightbackground="black")

champ_label_txt_feet = tk.Label(fenetre, text="L2K1 © 2016-2017 Tous droits reservés.",  fg="#CECECE", bg="#a7a7a7", font=police3)
champ_label_txt_feet.place(relx=.5, rely=.98, anchor="center")

#
#  Création des boutons de la fenêtre principale.
#

# Bouton nouveau permettant la sélection et le traitement des données obtenues. //  non achevées

boutonNew = tk.Button(fenetre, text="Synchronisation", bg="#ECECEC", font=police1, command= lambda:goNew())

if (os.sys.platform == 'win32'):
    boutonNew.place(relx=0.83, rely=0.40, anchor="center")
    tmi1 = imNew.subsample(1, 1)
    boutonNew.config(image=tmi1, compound="right", highlightbackground="#51585e")
else :
    boutonNew.place(relx=0.83, rely=0.48, anchor="center")
    tmi1 = imNew.subsample(2, 2)
    boutonNew.config(image=tmi1, compound="right", height="105", width="230", highlightbackground="#51585e")



# Bouton Eye permettant la séléction et le traitement des données sur les yeux uniquement. //  non achevées

boutonEye = tk.Button(fenetre, text=" Eye-tracking ", bg="#ECECEC", font=police1, command= lambda:goEye())

if (os.sys.platform == 'win32'):
    boutonEye.place(relx=0.17, rely=0.40, anchor="center")
    tmi2 = imEye.subsample(8, 8)
    boutonEye.config(image=tmi2, compound="right", highlightbackground="#51585e")
else :
    boutonEye.place(relx=0.17, rely=0.48, anchor="center")
    tmi2 = imEye.subsample(10, 10)
    boutonEye.config(image=tmi2, height="105", width="230", compound="right", highlightbackground="#51585e")


# Bouton Codamotion permettant la séléction et le traitement des données sur la marche uniquement. //  non achevées

boutonCodamotion = tk.Button(fenetre, text="  Codamotion  ", bg="#ECECEC", font=police1, command= lambda:goCoda())

if (os.sys.platform == 'win32'):
    boutonCodamotion.place(relx=0.50, rely=0.40, anchor="center")
    tmi3 = imCodamotion.subsample(8, 8)
    boutonCodamotion.config(image=tmi3, compound="right", highlightbackground="#51585e")
else :
    boutonCodamotion.place(relx=0.50, rely=0.48, anchor="center")
    tmi3 = imCodamotion.subsample(9, 9)
    boutonCodamotion.config(image=tmi3, compound="right", height="105", width="230", highlightbackground="#51585e")

# Bouton donation permettant à l'utilisateur d'effectuer un don.

boutonDon = tk.Button(fenetre, text=" Nous soutenir ", bg="#ECECEC", font=police2, command=lambda:goDon())

if (os.sys.platform == 'win32'):
    boutonDon.place(relx=.20, rely=.90, anchor="center")
    tmi4 = imDon.subsample(5, 5)
    boutonDon.config(image=tmi4, compound="right", highlightbackground="#51585e")
else :
    boutonDon.place(relx=.17, rely=.91, anchor="center")
    tmi4 = imDon.subsample(6, 6)
    boutonDon.config(image=tmi4, height="45", width="150", compound="right", highlightbackground="#51585e")


# Bouton Aide permettant d'obtenir un manuel d'aide détaillé du logiciel.

boutonHelp = tk.Button(fenetre, text="     Aide     ", bg="#ECECEC", font=police2, command=lambda:goHelp())

if (os.sys.platform == 'win32'):
    boutonHelp.place(relx=.80, rely=.90, anchor="center")
    tmi5 = imHelp.subsample(2, 2)
    boutonHelp.config(image=tmi5, compound="right", highlightbackground="#51585e")
else :
    boutonHelp.place(relx=.84, rely=.91, anchor="center")
    tmi5 = imHelp.subsample(2, 2)
    boutonHelp.config(image=tmi5, height="45", width="150", compound="right", highlightbackground="#51585e")


# Bouton Lanceur permettant d'obtenir indépendamment du logiciel une fenêtre lanceur afin d'effectuer certaines tâches en différé.

boutonLanceur = tk.Button(fenetre, text="    Lanceur   ", bg="#ECECEC", font=police2, command=lambda:goLanceur())

if (os.sys.platform == 'win32'):
    boutonLanceur.place(relx=.50, rely=.90, anchor="center")
    tmi6 = imLanceur.subsample(4, 4)
    boutonLanceur.config(image=tmi6, compound="right", highlightbackground="#51585e")
else :
    boutonLanceur.place(relx=.50, rely=.91, anchor="center")
    tmi6 = imLanceur.subsample(6, 6)
    boutonLanceur.config(image=tmi6, height="45", width="150", compound="right", highlightbackground="#51585e")
   


# Traduit les textes si la langue enregistrée est anglais ou si la langue du système n'est pas français.

if var_langue == "anglais":
    labelTitre["text"] = "Project L2K1"
    labelSousTitre["text"] = "Welcome to the L2K1 project"
    boutonNew["text"] = "      New     "
    boutonDon["text"] = "   Support us  "
    boutonHelp["text"] = "     Help     "
    boutonLanceur["text"] = "   Launcher   "
    champ_label_txt_feet["text"] = "L2K1 © 2016-2017 All rights reserved."


#
# Définition des infos bulles correspondant aux boutons et permettant lors de leurs survols d'obtenir des informations sur leurs actions.
#

if var_langue == "francais":
    i1 = infoBulle(parent=boutonNew,        texte="Ce bouton vous permet d'initier la phase de traitement des données.")
    i2 = infoBulle(parent=boutonEye,        texte="Ce bouton vous permet d'initier la phase de traitement des données\nconcernant Eye-tracking uniquement.")
    i3 = infoBulle(parent=boutonCodamotion, texte="Ce bouton vous permet d'initier la phase de traitement des données\nconcernant Codamotion uniquement.")
    i4 = infoBulle(parent=boutonHelp,       texte="Ce bouton vous permet d'otenir un manuel d'aide\ndétaillé sur le fonctionnement de ce logiciel.")
    i5 = infoBulle(parent=boutonLanceur,    texte="Le lanceur vous permet d'effectuer\ncertaines actions en les paramétrant au préalable\nafin de les déclencher à un moment précis.")
    i6 = infoBulle(parent=boutonDon,        texte="Vous serez redirigé vers un site de donation en cliquant sur ce bouton.")

elif var_langue == "anglais":
    i1 = infoBulle(parent=boutonNew,        texte="This button allows you to initiate the data processing phase.")
    i2 = infoBulle(parent=boutonEye,        texte="This button allows you to initiate the data processing phase which only concers Eye-tracking.")
    i3 = infoBulle(parent=boutonCodamotion, texte="This button allows you to initiate the data processing phase which only concers Codamotion.")
    i4 = infoBulle(parent=boutonHelp,       texte="This button allows you to have a detailed\nhelp manual on how this software works.")
    i5 = infoBulle(parent=boutonLanceur,    texte="The launcher allows you to perform\ncertain actions by setting them beforehand\nto trigger them at a specific time.")
    i6 = infoBulle(parent=boutonDon,        texte="You will be redirected to a page where you can make a donation by clicking on this button.")


menu_barre(fenetre, "L2K1", labelTitre, labelSousTitre, champ_label_txt_feet, boutonHelp, boutonLanceur, boutonNew, boutonDon, boutonEye, boutonCodamotion, i1, i2, i3, i4, i5, i6)

fenetre.protocol("WM_DELETE_WINDOW", lambda: fermer(fenetre)) # Capture de la fermeture de la fenêtre afin d'éditer une alerte spécifique pour confirmer la fermeture.
fenetre.mainloop()


