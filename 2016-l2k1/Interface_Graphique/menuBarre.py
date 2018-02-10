# *-- coding: utf-8 --*

#
#
# *=*=* # ********************************************************************** # 
# *=*=* #                                                                        # 
# *=*=* #  Id:  menuBarre.py 8086 01-03-2017                                     #
# *=*=* #                                                                        #
# *=*=* #  Name:     menuBarre.py                                                #
# *=*=* #  Project:  L2K1                                                        #
# *=*=* #  Author:   Created by <Benjamin Cohen> on 01/03/2017.                  #
# *=*=* #                                                                        #
# *=*=* # ********************************************************************** #
#
#
# *=*=* Lesser General Public License (LGPL 3.0).
# *=*=* See COPYING and COPYING.LESSER for license details.
#
# <===> Functions by Benjamin Cohen <===>
#
#



#
#  Importation de toutes les dépendances nécessaires à la barre de menu.
#


import tkinter as tk
import fonctionLangue
from functionMenu import *
from BDD import * # Importation des fonctions spécifiques à la base de données.



#
# Définition de la barre de menu qui prend en paramètre la fenêtre principale ainsi que son titre.
#


def menu_barre(root, title, labelTitre, labelSousTitre, champ_label_txt_feet, boutonHelp, boutonLanceur, boutonNew, boutonDon, boutonEye, boutonCodamotion, i1, i2, i3, i4, i5, i6):

    menubarre = tk.Menu(root)


    #
    # Création du premier volet de la barre de menu.
    #
    menu1 = tk.Menu(menubarre, tearoff=0)
    menu1.add_command(label="À propos", command = lambda: goApropos())
    menu1.add_command(label="Langue", command= lambda: goLangue(labelTitre, labelSousTitre, champ_label_txt_feet, boutonNew, boutonDon, boutonHelp, boutonLanceur, boutonEye, boutonCodamotion, i1, i2, i3, i4, i5, i6, menubarre, menu1, menu2, menu3))
    menu1.add_command(label="Lanceur", command = lambda: goLanceur())
    menu1.add_separator()
    menu1.add_command(label="Quitter", command=lambda: fermer(root))
    menubarre.add_cascade(label=title, menu=menu1)


    #
    # Création du second volet de la barre de menu.
    #

    menu2 = tk.Menu(menubarre, tearoff=0)
    menu2.add_command(label="Aide L2K1", command=lambda: goHelp())
    menu2.add_command(label="Licence GPL", command=lambda: goLicencePdf())
    menu2.add_separator()
    menu2.add_command(label="Licence GPL en ligne", command = lambda: goLicenceWeb())
    menu2.add_command(label="Contacter le support", command=lambda: goSupport())
    menubarre.add_cascade(label="Aide", menu=menu2)


    #
    #  Création du troisième volet de la barre de menu.
    #

    menu3 = tk.Menu(menubarre, tearoff=0)
    menu3.add_command(label="Auteur", command=lambda: goAuteur())
    menu3.add_command(label="Nous soutenir", command=lambda:goDon())
    menu3.add_command(label="Confidentialité", command=lambda: goConfidentialite())
    menubarre.add_cascade(label="...", menu=menu3)

    if var_langue=="anglais":
        menubarre.entryconfigure(2, label="Help")
        menu1.entryconfigure(0, label="About")
        menu1.entryconfigure(1, label="Language")
        menu1.entryconfigure(2, label="Launcher")
        menu1.entryconfigure(4, label="Quit")
        menu2.entryconfigure(0, label="Help L2K1")
        menu2.entryconfigure(1, label="GPL license")
        menu2.entryconfigure(3, label="Online GPL license")
        menu2.entryconfigure(4, label="Contact support")
        menu3.entryconfigure(0, label="Author")
        menu3.entryconfigure(1, label="Support us")
        menu3.entryconfigure(2, label="Privacy policy")

    root.config(menu=menubarre)
