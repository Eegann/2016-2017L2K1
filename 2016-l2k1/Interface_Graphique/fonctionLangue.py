# On importe les package nécessaire au bon fonctionnement du programme

import os
import pickle
from tkinter import *
import locale
from InfoBulle import *
from tkinter import font

# On vérifie si le fichier "langue" exisite déjà
# On récupère sa valeur s'il existe
# Sinon, on récupère la langue de l'OS

var_langue = StringVar

if (not (os.path.isfile('Ressources/data/langue'))):
    var_langue, var_decodeur = locale.getdefaultlocale()

    if var_langue.startswith('fr'):
        var_langue = "francais"
    else:
        var_langue = "anglais"

    with open('Ressources/data/langue', 'wb') as langue:
        langue_pickler = pickle.Pickler(langue)
        langue_pickler.dump(var_langue)
else:
    with open('Ressources/data/langue', 'rb') as langue:
        langue_depickler = pickle.Unpickler(langue)
        var_langue = langue_depickler.load()

        if var_langue != "francais" and var_langue != "anglais":

            if var_langue.startswith('fr'):
                var_langue = "francais"
            else:
                var_langue = "anglais"


# Fonction permettant d'ouvrir l'onglet pour changer la langue

def goLangue(labelTitre, labelSousTitre, champ_label_txt_feet, boutonNew, boutonDon, boutonHelp, boutonLanceur, boutonEye, boutonCodamotion, i1, i2, i3, i4,
             i5, i6, menubarre, menu1, menu2, menu3):
    global var_langue

    choix_langue = StringVar()
    fenetreLangue = Toplevel()
    fenetreLangue.geometry("400x200")
    fenetreLangue.minsize(width=400, height=200)
    fenetreLangue.maxsize(width=400, height=200)
    fenetreLangue.config(bg="#DCDCDC")
    fenetreLangue.resizable(width=False, height=False)
    police_titre_langue = font.Font(fenetreLangue, size=18, weight="bold", family="Helvectica")
    police_langue = font.Font(fenetreLangue, size=12, family='Helvectica')

    if var_langue == "francais":
        fenetreLangue.title("Langue")
    else:
        fenetreLangue.title("Language")

    labelLangue = Label(fenetreLangue, text="Choisissez la langue", fg="#FFFFFF", bg="#FF3D03", font=police_titre_langue)
    labelLangue.place(relx=.5, rely=0.1, anchor="center", height="50", width="800")

    choix_francais = Radiobutton(fenetreLangue, text="Français", variable=choix_langue, value="francais", bg="#DCDCDC", font=police_langue)

    choix_francais.place(relx=.50, rely=.45, anchor="center")

    choix_anglais = Radiobutton(fenetreLangue, text="Anglais  ", variable=choix_langue, value="anglais", bg="#DCDCDC", font=police_langue)
    choix_anglais.place(relx=.50, rely=.59, anchor="center")

    # On appelle la fonction qui permet de changer la langue en cliquant sur le bouton "Appliquer".

    boutonValider = Button(fenetreLangue, text="Appliquer", font=police_langue, command=lambda: changeLangue(choix_langue, choix_francais, choix_anglais, labelTitre, labelSousTitre, champ_label_txt_feet, labelLangue, boutonNew, boutonDon, boutonValider, boutonQuitter, boutonHelp, boutonLanceur, boutonEye, boutonCodamotion, i1, i2, i3, i4, i5, i6, menubarre, menu1, menu2, menu3))
    boutonValider.place(relx=.67, rely=.85, anchor="center")
    boutonValider.config(highlightbackground="#DCDCDC")

    boutonQuitter = Button(fenetreLangue, text="Quitter", font=police_langue, command=fenetreLangue.destroy)
    boutonQuitter.place(relx=.87, rely=.85, anchor="center")
    boutonQuitter.config(highlightbackground="#DCDCDC")

    if var_langue == "francais":

        choix_francais.select()
        changeLangue(choix_langue, choix_francais, choix_anglais, labelTitre, labelSousTitre, champ_label_txt_feet, labelLangue, boutonNew, boutonDon, boutonValider, boutonQuitter, boutonHelp, boutonLanceur, boutonEye, boutonCodamotion, i1, i2, i3, i4, i5, i6, menubarre, menu1, menu2, menu3)
    else:

        choix_anglais.select()
        changeLangue(choix_langue, choix_francais, choix_anglais, labelTitre, labelSousTitre, champ_label_txt_feet, labelLangue, boutonNew, boutonDon, boutonValider, boutonQuitter, boutonHelp, boutonLanceur, boutonEye, boutonCodamotion, i1, i2, i3, i4, i5, i6, menubarre, menu1, menu2, menu3)


# Fonction qui permet de changer les labels, en fonction de la valeur de var_langue

def changeLangue(choix_langue, choix_francais, choix_anglais, labelTitre, labelSousTitre, champ_label_txt_feet, labelLangue, boutonNew, boutonDon, boutonValider, boutonQuitter, boutonHelp, boutonLanceur, boutonEye, boutonCodamotion, i1, i2, i3, i4,i5, i6, menubarre, menu1, menu2, menu3):
	global var_langue
	var_langue = choix_langue.get()

	if var_langue == "anglais":

		labelTitre["text"] = "Project L2K1"
		labelSousTitre["text"]="Welcome to the L2K1 project"
		boutonNew["text"] = "      New     "
		boutonDon["text"] = "   Support us  "
		boutonHelp["text"] = "     Help     "
		boutonLanceur["text"] = "   Launcher   "
		champ_label_txt_feet["text"]="L2K1 © 2016-2017 All rights reserved."

		i1 = infoBulle(parent=boutonNew, texte="This button allows you to initiate the data processing phase.")
		i2 = infoBulle(parent=boutonEye, texte="This button allows you to initiate the data processing phase concerning eyes only.")
		i3 = infoBulle(parent=boutonCodamotion, texte="This button allows you to initiate the data processing phase concerning the walk only.")
		i4 = infoBulle(parent=boutonHelp, texte="This button allows you to have a detailed\nhelp manual on how this software works.")
		i5 = infoBulle(parent=boutonLanceur, texte="The launcher allows you to perform\ncertain actions by setting them beforehand\nto trigger them at a specific time.")
		i6 = infoBulle(parent=boutonDon, texte="You will be redirected to a donation site by clicking this button.")

		menubarre.entryconfigure(2, label="Help")
		menu1.entryconfigure(0, label="About")
		menu1.entryconfigure(1, label="Language")
		menu1.entryconfigure(2, label="Launcher")
		menu1.entryconfigure(4, label="Quit")
		menu2.entryconfigure(0, label="Help L2K1")
		menu2.entryconfigure(1, label="license")
		menu2.entryconfigure(3, label="Online documentation")
		menu2.entryconfigure(4, label="Contact support")
		menu3.entryconfigure(0, label="Author")
		menu3.entryconfigure(1, label="Support us")
		menu3.entryconfigure(2, label="Privacy policy")

		labelLangue["text"] = "Choose the language"
		boutonValider["text"] = "Apply"
		boutonQuitter["text"] = "Close"
		choix_francais["text"] = "French "
		choix_anglais["text"] = "English"

	else:
		labelTitre["text"] = "Projet L2K1"
		labelSousTitre["text"] = "Bienvenu sur le projet L2K1"
		boutonNew["text"] = "    Nouveau   "
		boutonDon["text"] = " Nous soutenir "
		boutonHelp["text"] = "     Aide     "
		boutonLanceur["text"] = "    Lanceur   "
		champ_label_txt_feet["text"] = "L2K1 © 2016-2017 Tous droits reservés."
		
		i1 = infoBulle(parent=boutonNew, texte="Ce bouton vous permet d'initier la phase de traitement des données.")
		i2 = infoBulle(parent=boutonEye, texte="Ce bouton vous permet d'initier la phase de traitement des données\nconsernant les yeux uniquement.")
		i3 = infoBulle(parent=boutonCodamotion, texte="Ce bouton vous permet d'initier la phase de traitement des données\nconsernant la marche uniquement.")
		i4 = infoBulle(parent=boutonHelp, texte="Ce bouton vous permet d'otenir un manuel d'aide\ndétaillé sur le fonctionnement de ce logiciel.")
		i5 = infoBulle(parent=boutonLanceur, texte="Le lanceur vous permet d'effectuer\ncertaines actions en les paramétrant au préalable\nafin de les déclencher à un moment précis.")
		i6 = infoBulle(parent=boutonDon, texte="Vous serez redirigé vers un site de donation en cliquant sur ce bouton.")

		menubarre.entryconfigure(2, label="Aide")
		menu1.entryconfigure(0, label="À propos")
		menu1.entryconfigure(1, label="Langue")
		menu1.entryconfigure(2, label="Lanceur")
		menu1.entryconfigure(4, label="Quitter")
		menu2.entryconfigure(0, label="Aide L2K1")
		menu2.entryconfigure(1, label="licence")
		menu2.entryconfigure(3, label="Documentation en ligne")
		menu2.entryconfigure(4, label="Contacter le support")
		menu3.entryconfigure(0, label="Auteur")
		menu3.entryconfigure(1, label="Nous soutenir")
		menu3.entryconfigure(2, label="Confidentialité")

		labelLangue["text"] = "Choisissez la langue"
		boutonValider["text"] = "Appliquer"
		boutonQuitter["text"] = "Quitter"
		choix_francais["text"] = "Français"
		choix_anglais["text"] = "Anglais  "

# On enregistre la valeur de var_langue pour connaitre la langue des textes pour les prochaines utilisations.

	with open('Ressources/data/langue', 'wb') as langue:
		langue_pickler = pickle.Pickler(langue)
		langue_pickler.dump(var_langue)
