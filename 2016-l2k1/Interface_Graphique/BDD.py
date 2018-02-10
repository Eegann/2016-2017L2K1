# *-- coding: utf-8 --*

#
#
# *=*=* # ********************************************************************** #
# *=*=* #                                                                        #
# *=*=* #  Id:  BDD.py 8104 25-03-2017                                           #
# *=*=* #                                                                        #
# *=*=* #  Name:     BDD.py                                                      #
# *=*=* #  Project:  L2K1                                                        #
# *=*=* #  Author:   Created by <Benjamin Cohen> on 25/03/2017.                  #
# *=*=* #                                                                        #
# *=*=* # ********************************************************************** #
#
#
# *=*=* Copyright © 2017 Benjamin Cohen. All rights reserved.
#
# *=*=* Lesser General Public License (LGPL 3.0).
# *=*=* See COPYING and COPYING.LESSER for license details.
#
# <===> Functions by Benjamin Cohen <===>
#
#




#
# Importation de l'ensemble des modules et fonctions nécessaires à la fenêtre.
#

import sys
import pickle
import os
import subprocess

from tkinter import *
from tkinter import font
import tkinter as tk
from fonctionSup import *
from InfoBulle import *
from fonctionLangue import var_langue





def goConfidentialite():

    #
    # Définition de la fenêtre.
    #

    fenetreBdd = tk.Toplevel()
    fenetreBdd.geometry("575x350")
    fenetreBdd.title("Confidentialité")
    fenetreBdd.config(bg='#C0C0C0')

    centrefenetre(fenetreBdd) # Fonction permettant le centrage de la fenêtre par rapport à l'écran de l'utilisateur.


    #
    # Définition des images du bouton.
    #

    image_up = tk.PhotoImage(file='Ressources/image/check/up.gif')
    image_down = tk.PhotoImage(file='Ressources/image/check/down.gif')

    tmi_bdd0 = image_up.subsample(1, 1)
    tmi_bdd1 = image_down.subsample(1, 1)

    #
    # Définition des styles de police de la fenêtre.
    #

    police_SousTitre = font.Font(fenetreBdd, size=18, weight="bold", family="Helvectica")
    police_txt_feet = font.Font(fenetreBdd, size=16, weight='bold', family='Courier')

    #
    # Mise en place des différents labels d'affichage.
    #

    labelTitre = Label(fenetreBdd, fg="#FFFFFF", bg="#960018")
    labelTitre.place(relx=.20, rely=.05, anchor="center", height="55", width="800")

    labelSousTitre = Label(fenetreBdd, text="Diagnostic et usages", fg="#FFFFFF", bg="#960018", font=police_SousTitre)
    labelSousTitre.place(relx=.5, rely=0.06, anchor="center", height="55", width="800")

    labelFeet = Label(fenetreBdd,relief="ridge", borderwidth=1, fg="#FFFFFF", bg="#a7a7a7")
    labelFeet.place(relx=.5, rely=0.96, anchor="center",  height="30", width="2000")
    labelFeet.config(highlightbackground="black")

    champ_label_txt_feet = tk.Label(fenetreBdd, text="",  fg="#CECECE", bg="#a7a7a7", )
    champ_label_txt_feet.place(relx=.5, rely=.97, anchor="center")



    affichageF1 = tk.Frame(fenetreBdd, width=600, height=200) # Définition de l'espace d'affichage.
    affichageF1.place(relx=.5, rely=.44, anchor="center")
    affichageF1.config(bg="#C0C0C0")


    texteT1 = tk.Text(affichageF1 , wrap=tk.NONE)  # Définition du texte d'affichage.
    texteT1.config(width=65, height=7)

    if var_langue=="francais":
        texteT1.insert('1.0', "\n  Envoyer des données d'utilisation et de diagnostics anonymes \n\n\n Vous pouvez nous aider à améliorer L2K1 en envoyant\n des données statistiques d'utilisation.\n Cette rubrique permet d'activer ou de désactiver la collecte\n des données statistiques d'utilisation du logiciel.\n Cette option est désactivée par défaut.\n Vous pouvez à tout moment choisir de l'activer ou la désactiver.\n Si vous souhaitez activer cette option,des informations\n d'utilisation tel que le type du système d'exploitation, date\n etc nous seront transmises.\n\n Information : L'activation de cette option peut nécessiter\n le mot de passe utilisateur.\n\n")
        texteT1.config(highlightbackground="#C0C0C0", state='disabled')
    else:
        texteT1.insert('1.0', "\n  Send anonym using data and diagnostic data \n\n\n You can help us improve L2K1 by sending\n statistic using data.\n This window allows you to activate or not\n the gathering of using data of this software.\n This option is deactivated by default.\n You can chose at any moment to activate or not this option.\n If you want to activate this option, some informations on the\noperation système, the date etc will be transmitted to us.\n\n Information : The activation of this option may require\n your password.\n\n")


    texteT1.place(relx=.5, rely=.4, anchor="center")
    texteT1.focus_force()




    #
    # Définition de la fonction de modification du choix de l'utilisateur.
    #

    def sauvegarder(event):


        with open('Ressources/data/pre', 'rb') as pre: # Lecture des paramètres de l'utilisateur.
            pre_depickler = pickle.Unpickler(pre)
            toggle = pre_depickler.load()


        if (os.sys.platform == 'darwin'): # Vérification du système d'exploitation de l'utilisateur.

                if toggle == "0":

                    #
                    # Mise en place d'une exception système pour le client de base de données.
                    #

                    dossier = os.path.dirname(os.path.abspath(__file__))
                    spctl = subprocess.Popen('spctl --add --label "clientMacOS.out" ' + dossier + '/Client/Log/MacOS/clientMacOS.out', stdout=subprocess.PIPE,stderr=subprocess.PIPE, shell=True)
                    stdout, stderr = spctl.communicate()



                    if(str(stderr) == "b''"): # Vérification du retour de la commande système.

                        label_BDD.config(image=tmi_bdd0) # Modification de l'état du bouton.
                        toggle = "1"

                        with open('Ressources/data/pre', 'wb') as pre: # Enregistrement des paramètres de l'utilisateur.
                            pre_pickler = pickle.Pickler(pre)
                            pre_pickler.dump("1")



                else:

                    label_BDD.config(image=tmi_bdd1) # Modification de l'état du bouton.
                    toggle = "0"

                    with open('Ressources/data/pre', 'wb') as pre: # Enregistrement des paramètres de l'utilisateur.
                        pre_pickler = pickle.Pickler(pre)
                        pre_pickler.dump("0")




        if (os.sys.platform == 'win32'): # Vérification du système d'exploitation de l'utilisateur.


                if toggle == "0":

                        label_BDD.config(image=tmi_bdd0) # Modification de l'état du bouton.
                        toggle = "1"

                        with open('Ressources/data/pre', 'wb') as pre: # Enregistrement des paramètres de l'utilisateur.
                            pre_pickler = pickle.Pickler(pre)
                            pre_pickler.dump("1")



                else: #

                    label_BDD.config(image=tmi_bdd1) # Modification de l'état du bouton.
                    toggle = "0"

                    with open('Ressources/data/pre', 'wb') as pre: # Enregistrement des paramètres de l'utilisateur.
                        pre_pickler = pickle.Pickler(pre)
                        pre_pickler.dump("0")




    label_BDD = tk.Label(fenetreBdd) # Définition du bouton du client de la base de données.
    label_BDD.place(relx=.5, rely=.73, anchor="center")



    with open('Ressources/data/pre', 'rb') as pre: # Lecture des paramètres de l'utilisateur.
            pre_depickler = pickle.Unpickler(pre)
            toggle = pre_depickler.load()

    #
    # Définition de l'état du bouton du client de la base de données en fonction des paramètres initiaux de l'utilisateur.
    #

    if toggle == "1":
        label_BDD.config(image=tmi_bdd0, bg='#C0C0C0')
    else:
        label_BDD.config(image=tmi_bdd1, bg='#C0C0C0')


    label_BDD.bind('<Button-1>', sauvegarder) # Définition de l'action au clic du bouton.
    fenetreBdd.resizable(width=False, height=False)  # Redimensionnement de la fenêtre immobilisée.

    fenetreBdd.mainloop()





#
# Fonction permettant l'exécution du client de la base de données à chaque lancement du logiciel.
#

def goCheckBdd():


    with open('Ressources/data/pre', 'rb') as pre: # Lecture des paramètres de l'utilisateur.
        pre_depickler = pickle.Unpickler(pre)
        toggle = pre_depickler.load()


    if toggle == "1":

        #
        # Exécution du client en fonction du système d'exploitation
        #

        if (os.sys.platform == 'win32'):
            os.system("exec Client/Log/WinOS/clientWinOS.exe")

        if (os.sys.platform == 'darwin'):
            os.system("exec Client/Log/MacOS/clientMacOS.out")


