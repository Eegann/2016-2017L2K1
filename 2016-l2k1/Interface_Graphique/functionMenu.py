# *-- coding: utf-8 --*

#
#
# *=*=* # ********************************************************************** # 
# *=*=* #                                                                        # 
# *=*=* #  Id:  fonctionMenu.py 8104 05-03-2017                                  #
# *=*=* #                                                                        #
# *=*=* #  Name:     fonctionMenu.py                                             #
# *=*=* #  Project:  L2K1                                                        #
# *=*=* #  Author:   Created by <Benjamin Cohen> on 05/03/2017.                  #
# *=*=* #                                                                        #
# *=*=* # ********************************************************************** #
#
#
# *=* Copyright © 2017 Benjamin Cohen. All rights reserved.
#
# *=* Lesser General Public License (LGPL 3.0).
# *=* See COPYING and COPYING.LESSER for license details.
#
# <===> Functions by Benjamin Cohen <===>
#
#



#
# Importation de l'ensemble des modules et fonctions nécessaires.
#

import os
import sys
import pickle
from lanceur import *
import subprocess
from fonctionSup import *
import tkFontChooser
import webbrowser
from time import sleep

if sys.version_info < (3, 0):
    # Python 2
    import Tkinter as tk
    from Tkinter import messagebox
    from Tkinter import font
else:
    # Python 3
    import tkinter as tk
    from tkinter import messagebox
    from tkinter import font
    from tkinter import *




#
# Définition de la fonction de confirmation de fermeture de fenêtre.
#

def fermer(root):

    with open('Ressources/data/langue', 'rb') as langue:
        langue_depickler = pickle.Unpickler(langue)
        var_langue = langue_depickler.load()

    if var_langue=="francais":

        if messagebox.askokcancel("Quitter", "Voulez-vous vraiment quitter ?"):
           root.destroy()
           exit()  
    else:
        if messagebox.askokcancel("Exit", "Do you really want to exit ?"):
           root.destroy()
           exit()  

    



#
# Définition des fonctions d'ouverture du client mail en fonction des développeurs du projet.
#


def goMailDev1(event=None): # Correspond au développeur N°1 \\DEV1 => Alexandre Heintzmann


    if (os.sys.platform == 'win32'):
        os.system("start mailto:alexandre.heintzmann@etu.parisdescartes.fr")
    if (os.sys.platform == 'darwin'):
        os.system("open mailto:alexandre.heintzmann@etu.parisdescartes.fr")


def goMailDev2(event=None): # Correspond au développeur N°2 \\DEV2 => Benjamin Cohen


    if (os.sys.platform == 'win32'):
        os.system("start mailto:benjamin.cohen4@etu.parisdescartes.fr")
    if (os.sys.platform == 'darwin'):
        os.system("open mailto:benjamin.cohen4@etu.parisdescartes.fr")


def goMailDev3(event=None): # Correspond au développeur N°3 //DEV3 => Helmy El Rais


    if (os.sys.platform == 'win32'):
        os.system("start mailto:helmy.el-rais@etu.parisdescartes.fr")
    if (os.sys.platform == 'darwin'):
        os.system("open mailto:helmy.el-rais@etu.parisdescartes.fr")


def goMailDev4(event=None): # Correspond au développeur N°4 //DEV4 => Raphael Depain


    if (os.sys.platform == 'win32'):
        os.system("start mailto:raphael.depain@etu.parisdescartes.fr")
    if (os.sys.platform == 'darwin'):
        os.system("open mailto:raphael.depain@etu.parisdescartes.fr")


def goMailDev5(event=None): # Correspond au développeur N°5 //DEV5 => Thomas Zhou


    if (os.sys.platform == 'win32'):
        os.system("start mailto:thomas.zhou@etu.parisdescartes.fr")
    if (os.sys.platform == 'darwin'):
        os.system("open mailto:thomas.zhou@etu.parisdescartes.fr")




#
# Définition des fonctions d'ouverture des sites Web correspondant aux développeurs du projet.
#


def goSiteDev1(): # Correspond au développeur N°1 \\DEV1 => Alexandre Heintzmann

    webbrowser.open_new("http://www.ens.math-info.univ-paris5.fr/~ih00038")


def goSiteDev2(): # Correspond au développeur N°2 \\DEV2 => Benjamin Cohen

    webbrowser.open_new("http://www.ens.math-info.univ-paris5.fr/~ih07415/OS.html")


def goSiteDev3(): # Correspond au développeur N°3 //DEV3 => Helmy El Rais

    webbrowser.open_new("http://www.ens.math-info.univ-paris5.fr/~if04688")


def goSiteDev4(): # Correspond au développeur N°4 //DEV4 => Raphael Depain

    webbrowser.open_new("http://www.ens.math-info.univ-paris5.fr/~ii06422")

def goSiteDev5(): # Correspond au développeur N°5 //DEV5 => Thomas Zhou

    webbrowser.open_new("http://www.ens.math-info.univ-paris5.fr/~ig03148")





#
# Définition de la fonction de redirection vers la page Web de soutien du projet.
#

def goDon():

    webbrowser.open_new("https://www.paypal.com/cgi-bin/webscr?cmd=_s-xclick&hosted_button_id=FB5JNATH5NM6Y")





#
# Définition de la fonction de redirection web vers la licence LGPL de distribution du logiciel.
#

def goLicenceWeb(event=None):

    with open('Ressources/data/langue', 'rb') as langue:
        langue_depickler = pickle.Unpickler(langue)
        var_langue = langue_depickler.load()

    if var_langue=="francais":
        webbrowser.open_new("http://dachary.org/loic/gpl-french.pdf")

    else:
        webbrowser.open_new("http://dachary.org/loic/gpl-english.pdf")





#
# Définition de la fonction d'ouverture de la licence LGPL de distribution du logiciel.
#

def goLicencePdf(event=None):

    with open('Ressources/data/langue', 'rb') as langue:
        langue_depickler = pickle.Unpickler(langue)
        var_langue = langue_depickler.load()

    if (os.sys.platform == 'win32'):

        if var_langue=="francais":
            os.system("start Ressources/documentation/gpl-french.pdf")

        else:
            os.system("start Ressources/documentation/gpl-english.pdf")

    if (os.sys.platform == 'darwin'):

        if var_langue=="francais":
            os.system("open Ressources/documentation/gpl-french.pdf")
        else:
            os.system("start Ressources/documentation/gpl-english.pdf")





#
# Définition de la fonction de style des liens dynamiques.
#


def lien_text(lab, event=None):
    url = tkFontChooser.Font(lab, lab.cget("font"))
    url.configure(underline=True)
    lab.configure(font=url)
    lab.config(fg="blue")





#
# Définition de la fonction d'ouverture du manuel d'aide du logiciel L2K1.
#

def goHelp(): # En cours : +ADD.

    with open('Ressources/data/langue', 'rb') as langue:
        langue_depickler = pickle.Unpickler(langue)
        var_langue = langue_depickler.load()

    if (os.sys.platform == 'win32'):

        if (var_langue=="francais"):
            os.system("start Ressources/documentation/L2K1_Help_FR.pdf")
        else:
            os.system("start Ressources/documentation/L2K1_Help_FR.pdf")

    if (os.sys.platform == 'darwin'):

        if (var_langue=="francais"):
            os.system("open Ressources/documentation/L2K1_Help_FR.pdf")
        else:
            os.system("open Ressources/documentation/L2K1_Help_FR.pdf")




#
# Définition de la fonction permettant d'obtenir une vue globale des informations concernant le logiciel.
#


def goApropos():


    fenApropos = tk.Toplevel()
    fenApropos.geometry("380x500")
    fenApropos.config(bg="#ECECEC")


    with open('Ressources/data/langue', 'rb') as langue:
        langue_depickler = pickle.Unpickler(langue)
        var_langue = langue_depickler.load()


    if var_langue=="francais":
        fenApropos.title("A propos de L2K1")
    else:
        fenApropos.title("About L2K1")



    fenApropos.resizable(width=False, height=False)  # Redimensionnement de la fenêtre immobilisée.

    imlogo = tk.PhotoImage(file="Ressources/image/logo/logo.gif")
    labLo = tk.Label(fenApropos, image=imlogo, bg="#ececec")  # Mise en place du label pour le logo du logiciel.

    f1 = tk.Frame(fenApropos, width=800, height=50)  # Définition de l'espace d'affichage N°1.
    f1.config(bg="#ececec")


    t1 = tk.Text(f1, wrap=tk.NONE)  # Définition du texte d'affichage lié à la barre de défilement vertical.
    t1.config(width=40, height=9)
    t1.focus_force()

    #
    # Insertion du texte d'information N°1.
    #

    if var_langue=="francais":
        t1.insert('1.0', "\nLe logiciel L2K1 ne communique aucune\ninformation de son environnement\nou de l'utilisation faite par\nl’utilisateur sans son consentement.\n\nSelon la licence LGPL3, le code source\nde l’application n'est pas publié.\n\nL2K1 ne modifie aucune des bibliothèques\n« Framework » fournies.\n\nEn utilisant notre logiciel\nvous acceptez par la présente de\ndédouaner de toutes responsabilités\nle(s) développeur(s) du logiciel.\n\nAucune information personnelle,\nconnexion Internet n'est nécessaire\npour utiliser le logiciel, néanmoins\ncertaines fonctionnalités peuvent\nnécessiter une connexion Internet\npour fonctionner. \n\t\t\t     <L2K1>\n")
    else:
        t1.insert('1.0',"\nThe L2K1 software does not provide any\ninformation about the environment or\nabout the utilization made by the user\nwithout his agreement.\n\nAccording to the LGPL3 license, the\nsoftware's source code won't be\npublished.\n\nL2K1 does not alter any of the provided\n« Framework » libraries.\n\nBy using our software, you accept to\nclear the software developer(s) from\nany responsabilities.\n\nNo personal information, or Internet\nconnection is required to use our\nsoftware, still some functions may need\nan Internet connection to work. \n\t\t\t        <L2K1>\n")


    t1.config(highlightbackground="#ececec", state='disabled')


    f2 = tk.Frame(fenApropos, width=800, height=50)  # Définition de l'espace d'affichage N°2.
    f2.config(bg="#ececec")

    t2 = tk.Text(f2, wrap=tk.NONE)  # Définition du texte d'affichage lié à la barre de défilement vertical.
    t2.config(width=40, height=9)


    #
    # Insertion du texte d'information N°2.
    #

    if var_langue=="francais":
        t2.insert('1.0', "\n\t\t<Auteurs>\n\n\tAlexandre Heintzmann\n\tBenjamin Cohen\n\tHelmy El Rais\n\tRaphael Depain\n\tThomas Zhou\n\n\n    Merci d'utiliser notre logiciel\n    L2K1 basé sur <Python> soumis à\n    la licence LGPL3.\n\n    Nous tenons à remercier Madame\n    Danping Wang en qualité\n    d'encadrante pour son implication\n    dans le projet L2K1.\n\n    Vous pouvez nous soutenir en\n    faisant un don.\n\n    Traduit par Alexandre Heintzmann.\n\n")
    else:
        t2.insert('1.0', "\n\t\t<Authors>\n\n\tAlexandre Heintzmann\n\tBenjamin Cohen\n\tHelmy El Rais\n\tRaphael Depain\n\tThomas Zhou\n\n    Thank you for using our software\n    L2K1 based on <Python> subject\n    to the LGPL3 license.\n\n    We would like to thank miss\n    Danping Wang as supervisor, for\n    her involvment in the L2K1\n    project.\n\n    You can support us by giving a\n    donation.\n\n    Translated by Alexandre Heintzmann.\n\n")

    t2.config(highlightbackground="#ececec", state='disabled')




    def AMTextAuteur(event=None, nsa=[True]):  # Fonction permettant d'afficher et de masquer la zone de texte d'information N°1.

        #
        # Vérification et actions en fonction de l'état de la variable nsa[0]
        #

        if nsa[0]:

            labLo.place_forget()  # Masquer le logo
            f1.pack_forget()  # Affichage de la zone d'information N°1.

            t2.grid(column=0, row=0, padx=0, pady=232)
            t2.focus_set()

            f2.pack()
            nsa[0] = False

        else:
            f2.pack_forget()  # Masquer la zone d'information N°2.
            f1.pack_forget()  # Masquer la zone d'information N°1.
            labLo.place(relx=.5, rely=.61, anchor="center")  # Affichage de la zone d'information.
            nsa[0] = True

    def AMTextInformation(event=None, nsa=[True]):  # Fonction permettant d'afficher et de masquer la zone du texte d'information N°2.

        #
        # Vérification et actions en fonction de l'état de la variable nsa[0]
        #

        if nsa[0]:

            labLo.place_forget()  # Masquer le logo.
            f2.pack_forget()  # Affichage de la zone d'information N°2.

            t1.grid(column=0, row=0, padx=0, pady=232)
            t1.focus_set()

            f1.pack()
            nsa[0] = False

        else:
            f1.pack_forget()  # Masquer la zone d'information N°1.
            f2.pack_forget()  # Masquer la zone d'information N°2.
            labLo.place(relx=.5, rely=.61, anchor="center")
            nsa[0] = True

    police_apropos_titre = font.Font(fenApropos, size=18, weight='bold', family='Helvectica')  # Définition de la police d'affichage du titre.
    police_apropos_txt = font.Font(fenApropos, size=12, family='Helvectica')  # Définition de la police affichage du texte.

    #
    # Définition de différentes zones (Label) de texte d'affichage.
    #

    champ_label_titre = tk.Label(fenApropos, text="L2K1", bg="#ECECEC", font=police_apropos_titre)
    champ_label_titre.place(relx=.5, rely=.1, anchor="center")

    champ_label_version = tk.Label(fenApropos, text="Version 0.96", bg="#ECECEC", font=police_apropos_txt)
    champ_label_version.place(relx=.5, rely=.20, anchor="center")

    champ_label_langue = tk.Label(fenApropos, text="Langues disponibles : Français (FR) - Anglais (EN)", bg="#ECECEC", font=police_apropos_txt)
    champ_label_langue.place(relx=.5, rely=.25, anchor="center")

    champ_label_icon = tk.Label(fenApropos, text="Icon : (Licence) Gratuit pour un usage commercial.", bg="#ECECEC", font=police_apropos_txt)
    champ_label_icon.place(relx=.5, rely=.30, anchor="center")

    champ_label_base1 = tk.Label(fenApropos, text="Basé sur <Python>\n ", bg="#ECECEC", font=police_apropos_txt)
    champ_label_base1.place(relx=.5, rely=.40, anchor="center")

    champ_label_base2 = tk.Label(fenApropos, text="L2K1 © 2016-2017 Tous droits reservés.", bg="#ECECEC", font=police_apropos_txt)
    champ_label_base2.place(relx=.5, rely=.93, anchor="center")

    champ_label_licence1 = tk.Label(fenApropos, text="Soumis à une licence LGPL3", bg="#ECECEC", font=police_apropos_txt)
    champ_label_licence1.place(relx=.5, rely=.42, anchor="center")
    champ_label_licence1.bind("<Enter>", lien_text(champ_label_licence1, event=None))
    champ_label_licence1.bind("<Button-1>", goLicenceWeb)  # Déclenchement de la fonction goLicenceWeb lors du clic de l'utilisateur.

    champ_label_Auteur = tk.Label(fenApropos, text="Infos", bg="#ECECEC", font=police_apropos_txt)
    champ_label_Auteur.place(relx=.2, rely=.81, anchor="center")
    champ_label_Auteur.bind("<Enter>", lien_text(champ_label_Auteur, event=None))
    champ_label_Auteur.bind("<Button-1>", AMTextInformation)  # Déclenchement de la fonction AMTextInformation lors du clic de l'utilisateur.

    champ_label_licence2 = tk.Label(fenApropos, text="Licence", bg="#ECECEC", font=police_apropos_txt)
    champ_label_licence2.place(relx=.5, rely=.81, anchor="center")
    champ_label_licence2.bind("<Enter>", lien_text(champ_label_licence2, event=None))
    champ_label_licence2.bind("<Button-1>",goLicencePdf)  # Déclenchement de la fonction goLicencePdf lors du clic de l'utilisateur.

    champ_label_credit = tk.Label(fenApropos, text="Crédit", bg="#ECECEC", font=police_apropos_txt)
    champ_label_credit.place(relx=.8, rely=.81, anchor="center")
    champ_label_credit.bind("<Enter>", lien_text(champ_label_credit, event=None))
    champ_label_credit.bind("<Button-1>", AMTextAuteur)  # Déclenchement de la fonction AMTextAuteur lors du clic de l'utilisateur.


    if var_langue == "anglais":

        champ_label_langue["text"] = "Available languages : French (FR) - English (EN)"
        champ_label_icon["text"] = "Icon : (License) Free for any commercial use."
        champ_label_base1["text"] = "Based on <Python>\n "
        champ_label_base2["text"] = "L2K1 © 2016-2017 All rights reserved."
        champ_label_licence1["text"] = "Subject to the LGP3 license."
        champ_label_Auteur["text"] = "Information"
        champ_label_licence2["text"] = "License"
        champ_label_credit["text"] = "Credits"
    #
    # Création de l'animation de la barre de progression
    #

    pb = tk.ttk.Progressbar(fenApropos, orient="horizontal", length=100, mode='determinate')
    pb.place(relx=0.5, rely=0.61, anchor="center")
    pb["value"] = 0
    pb["maximum"] = 100

    for i in range(100):  # Boucle de progression de la barre de chargement.
        pb["value"] += 1
        pb.update()
        sleep(0.01)
    pb.destroy()  # Destruction de la barre de chargement.

    labLo.place(relx=.5, rely=.61, anchor="center")
    fenApropos.wm_attributes('-alpha', 0.96)  # Définition du style de transparence de la fenêtre.

    fenApropos.mainloop()



#
# Définition de la fonction permettant d'ëtre redirigé vers le mail du support.
#

def goSupport():

    #
    # Chargement des images d'animation.
    #

    image_cof1 = tk.PhotoImage(file='Ressources/image/animation/cof1.gif')
    image_cof2 = tk.PhotoImage(file='Ressources/image/animation/cof2.gif')
    image_cof3 = tk.PhotoImage(file='Ressources/image/animation/cof3.gif')
    image_cof4 = tk.PhotoImage(file='Ressources/image/animation/cof4.gif')

    fenSupport = tk.Toplevel()  # Définition des paramètres de base de la fenêtre.
    fenSupport.geometry("780x130")
    fenSupport.config(bg="#C0C0C0")
    fenSupport.title("Support")
    centrefenetre(fenSupport)
    fenSupport.resizable(width=False, height=False)  # Redimensionnement de la fenêtre immobilisée.
    fenSupport.overrideredirect(1)

    tmp_image_cofX = image_cof1.subsample(2, 2)  # redimensionnement de l'image d'animation.
    label2 = tk.Label(fenSupport, image=tmp_image_cofX, bg="#C0C0C0")  # Définition du label d'animation.
    label2.place(relx=.11, rely=.45, anchor="center")

    with open('Ressources/data/langue', 'rb') as langue:
        langue_depickler = pickle.Unpickler(langue)
        var_langue = langue_depickler.load()


    global aff
    aff = StringVar()
    secTmp = 0
    secs = 0

    def suppDo(secs):

        def labelDec():

            global secTmp, aff
            secTmp -= 1

            if var_langue=="francais":

                aff.set("Bonjour, vous allez être redirigé vers le mail du support dans : " + str(secTmp) + " sec(s)")  # Mise à jour de l'affichage textuel en fonction du temps restant.

            else:
                aff.set("You will be redirected to the support's mail in : " + str(secTmp) + " sec(s)")  # Mise à jour de l'affichage textuel en fonction du temps restant.

            #
            # Mise à jour de l'affichage d'animation en fonction du temps restant.
            #


            if secTmp == 4:
                sleep(1)
                tmp_image_cofX = image_cof1.subsample(2, 2)
                label2.config(image=tmp_image_cofX)

            elif secTmp == 3:
                sleep(1)
                tmp_image_cofX = image_cof2.subsample(2, 2)
                label2.config(image=tmp_image_cofX)

            elif secTmp == 2:
                sleep(1)
                tmp_image_cofX = image_cof3.subsample(2, 2)
                label2.config(image=tmp_image_cofX)

            elif (secTmp == 1 or secTmp == 0):
                sleep(1)
                tmp_image_cofX = image_cof4.subsample(2, 2)
                label2.config(image=tmp_image_cofX)


            label1.update_idletasks()  # Actualisation du label.

            if not secTmp:  # Déclenchement de l'action une fois le temps écoulé.

                if (os.sys.platform == 'win32'):
                    os.system("start mailto:osadn0@gmail.com")
                if (os.sys.platform == 'darwin'):
                    os.system("open mailto:osadn0@gmail.com")
                fenSupport.destroy()

        global secTmp

        # Définition et affichage du label.

        police_Support = font.Font(fenSupport, size=14, weight='bold')

        if var_langue=="francais":

            aff.set("Bonjour, vous allez être redirigé vers le mail du support dans : 5 sec(s)")
        else:

            aff.set("You will be redirected to the support's mail in : 5 sec(s)")

        label1 = tk.Label(fenSupport, textvariable=aff, bg="#C0C0C0", font=police_Support)
        label1.place(relx=.57, rely=.47, anchor="center")

        secTmp = secs
        for i in range(1, secs + 1):
            fenSupport.after(i * 1000, labelDec)  # rappel de la fonction labelDec.

    suppDo(5)

    fenSupport.mainloop()


#
# Définition de la fonction de présentation des auteurs.
#

def goAuteur():

    with open('Ressources/data/langue', 'rb') as langue:
        langue_depickler = pickle.Unpickler(langue)
        var_langue = langue_depickler.load()

    fenAuteur = tk.Toplevel()
    fenAuteur.geometry("560x760")
    fenAuteur.config(bg="#CECECE")
    fenAuteur.title("Auteur")
    centrefenetre(fenAuteur)

    fenAuteur.resizable(width=False, height=False) #  Redimensionnement de la fenêtre immobilisée.

    police_auteur = font.Font(fenAuteur, size=12, weight='bold', family='Helvectica') # Mise en place du style police correspondant aux auteurs.
    police_url = font.Font(fenAuteur, size=11, weight='bold', family='Helvectica') # Mise en place du style police correspondant auxs mail des auteurs.


    #
    # Affichage correspondant à l'auteur <Alexandre Heintzmann>.
    #

    champ_label_auteur1 = tk.Label(fenAuteur, text="<Alexandre Heintzmann>\n\n Etudiant à l'université Paris Descartes\n UFR : Mathématiques - Informatique\n", bg="#CECECE", font=police_auteur)
    champ_label_auteur1.place(relx=0.5, rely=0.10, anchor="center")

    champ_label_mail_auteur1 = tk.Label(fenAuteur, text="Mail de contact : alexandre.heintzmann@etu.parisdescartes.fr", bg="#CECECE", font=police_url)
    champ_label_mail_auteur1.place(relx=0.5, rely=0.16, anchor="center")

    champ_label_mail_auteur1.bind("<Enter>", lien_text(champ_label_mail_auteur1, event=None)) # Définition d'action d'ouverture en fonction de l'utilisateur.
    champ_label_mail_auteur1.bind("<Button-1>", goMailDev1)

    bouton_auteur1 = tk.Button(fenAuteur, text="Visitez le site Web", bg="#ECECEC",command=lambda: goSiteDev1())
    bouton_auteur1.place(relx=.7, rely=.20, anchor="center")
    bouton_auteur1.config(highlightbackground="#CECECE")


    #
    # Affichage correspondant à l'auteur <Benjamin Cohen>.
    #

    champ_label_auteur2 = tk.Label(fenAuteur, text="<Benjamin Cohen>\n\n Etudiant à l'université Paris Descartes\n UFR : Mathématiques - Informatique\n", bg="#CECECE", font=police_auteur)
    champ_label_auteur2.place(relx=0.5, rely=0.29, anchor="center")

    champ_label_mail_auteur2 = tk.Label(fenAuteur, text="Mail de contact : benjamin.cohen4@etu.parisdescartes.fr", bg="#CECECE", font=police_url)
    champ_label_mail_auteur2.place(relx=0.5, rely=0.34, anchor="center")

    champ_label_mail_auteur2.bind("<Enter>", lien_text(champ_label_mail_auteur2, event=None)) # Définition d'action d'ouverture en fonction de l'utilisateur.
    champ_label_mail_auteur2.bind("<Button-1>", goMailDev2)

    bouton_auteur2 = tk.Button(fenAuteur, text="Visitez le site Web", bg="#ECECEC", command=lambda: goSiteDev2())
    bouton_auteur2.place(relx=.7, rely=.38, anchor="center")
    bouton_auteur2.config(highlightbackground="#CECECE")

    #
    # Affichage correspondant à l'auteur <Helmy El Rais>.
    #

    champ_label_auteur3 = tk.Label(fenAuteur, text="<Helmy El Rais>\n\n Etudiant à l'université Paris Descartes\n UFR : Mathématiques - Informatique\n", bg="#CECECE", font=police_auteur)
    champ_label_auteur3.place(relx=0.5, rely=0.47, anchor="center")

    champ_label_mail_auteur3 = tk.Label(fenAuteur, text="Mail de contact : helmy.el-rais@etu.parisdescartes.fr", bg="#CECECE", font=police_url)
    champ_label_mail_auteur3.place(relx=0.5, rely=0.52, anchor="center")

    champ_label_mail_auteur3.bind("<Enter>", lien_text(champ_label_mail_auteur3, event=None)) # Définition d'action d'ouverture en fonction de l'utilisateur.
    champ_label_mail_auteur3.bind("<Button-1>", goMailDev3)

    bouton_auteur3 = tk.Button(fenAuteur, text="Visitez le site Web", bg="#ECECEC", command=lambda: goSiteDev3())
    bouton_auteur3.place(relx=.7, rely=.56, anchor="center")
    bouton_auteur3.config(highlightbackground="#CECECE")

    #
    # Affichage correspondant à l'auteur <Raphael Depain>.
    #

    champ_label_auteur4 = tk.Label(fenAuteur, text="<Raphael Depain>\n\n Etudiant à l'université Paris Descartes\n UFR : Mathématiques - Informatique\n", bg="#CECECE", font=police_auteur)
    champ_label_auteur4.place(relx=0.5, rely=0.65, anchor="center")

    champ_label_mail_auteur4 = tk.Label(fenAuteur, text="Mail de contact : raphael.depain@etu.parisdescartes.fr", bg="#CECECE", font=police_url)
    champ_label_mail_auteur4.place(relx=0.5, rely=0.72, anchor="center")

    champ_label_mail_auteur4.bind("<Enter>", lien_text(champ_label_mail_auteur4, event=None)) # Définition d'action d'ouverture en fonction de l'utilisateur.
    champ_label_mail_auteur4.bind("<Button-1>", goMailDev4)

    bouton_auteur4 = tk.Button(fenAuteur, text="Visitez le site Web", bg="#ECECEC", command=lambda: goSiteDev4())
    bouton_auteur4.place(relx=.7, rely=.76, anchor="center")
    bouton_auteur4.config(highlightbackground="#CECECE")

    #
    # Affichage correspondant à l'auteur <Thomas Zhou>.
    #

    champ_label_auteur5 = tk.Label(fenAuteur, text="<Thomas Zhou>\n\n Etudiant à l'université Paris Descartes\n UFR : Mathématiques - Informatique\n", bg="#CECECE",font=police_auteur)
    champ_label_auteur5.place(relx=0.5, rely=0.85, anchor="center")

    champ_label_mail_auteur5 = tk.Label(fenAuteur, text="Mail de contact : thomas.zhou@etu.parisdescartes.fr", bg="#CECECE", font=police_url)
    champ_label_mail_auteur5.place(relx=0.5, rely=0.92, anchor="center")

    champ_label_mail_auteur5.bind("<Enter>", lien_text(champ_label_mail_auteur5, event=None)) # Définition d'action d'ouverture en fonction de l'utilisateur.
    champ_label_mail_auteur5.bind("<Button-1>", goMailDev5)

    bouton_auteur5 = tk.Button(fenAuteur, text="Visitez le site Web", bg="#ECECEC", command=lambda: goSiteDev5())
    bouton_auteur5.place(relx=.7, rely=.96, anchor="center")
    bouton_auteur5.config(highlightbackground="#CECECE")


    if var_langue=="anglais":
        champ_label_auteur1["text"]="<Alexandre Heintzmann>\n\n Student at Paris Descartes University\n UFR : Mathematics - Computer Science\n"
        champ_label_mail_auteur1["text"]="Email : alexandre.heintzmann@etu.parisdescartes.fr"
        bouton_auteur1["text"]="Website"

        champ_label_auteur2["text"] = "<Benjamin Cohen>\n\n Student at Paris Descartes University\n UFR : Mathematics - Computer Science\n"
        champ_label_mail_auteur2["text"] = "Email : benjamin.cohen4@etu.parisdescartes.fr"
        bouton_auteur2["text"] = "Website"

        champ_label_auteur3["text"] = "<Helmy El Rais>\n\n Student at Paris Descartes University\n UFR : Mathematics - Computer Science\n"
        champ_label_mail_auteur3["text"] = "Email : helmy.el-rais@etu.parisdescartes.fr"
        bouton_auteur3["text"] = "Website"

        champ_label_auteur4["text"] = "<Raphael Depain>\n\n Student at Paris Descartes University\n UFR : Mathematics - Computer Science\n"
        champ_label_mail_auteur4["text"] = "Email : raphael.depain@etu.parisdescartes.fr"
        bouton_auteur4["text"] = "Website"

        champ_label_auteur5["text"] = "<Thomas Zhou>\n\n Student at Paris Descartes University\n UFR : Mathematics - Computer Science\n"
        champ_label_mail_auteur5["text"] = "Email : thomas.zhou@etu.parisdescartes.fr"
        bouton_auteur5["text"] = "Website"

    fenAuteur.wm_attributes('-alpha', 0.96) # Définition du style de transparence de la fenêtre.

    fenAuteur.mainloop()

#
# Définition de la fonction permettant l'ouverture du lanceur.
#

def goLanceur():


   if (os.sys.platform == 'win32'):
       subprocess.Popen("python lanceur.py", shell=True)
   if (os.sys.platform == 'darwin'):
       subprocess.Popen("python3 lanceur.py", shell=True)


