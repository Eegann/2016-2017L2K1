# *-- coding: utf-8 --*

#
#
# *=*=* # ********************************************************************** #
# *=*=* #                                                                        #
# *=*=* #  Id:  lanceur.py 8442 18-02-2017                                       #
# *=*=* #                                                                        #
# *=*=* #  Name:     lanceur.py                                                  #
# *=*=* #  Project:  L2K1                                                        #
# *=*=* #  Author:   Created by <Benjamin Cohen> on 18/03/2017.                  #
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
# <===> Inspired by url : http://python.jpvweb.com/mesrecettespython/doku.php?id=compte_a_rebours <===>
#
#


#
#  Importation de l'ensemble des modules et fonctions nécessaires au lanceur.
#

import sys
import threading
import time
import os

import tkinter
from tkinter import font
from tkinter import filedialog

from InfoBulle import *
from fonctionLangue import *




######## VAR #######
T1 = 0
T2 = 0
T3 = 0
tmpAide = True
patch_file = " "
####################


#
# Définition de la fonction permettant de mettre à jour le temps restant.
#

def hms_check(sd): # La fonction hms_check() prend en paramètre le temps en seconde et retourne le temps en heures, minutes et secondes.

    h = 0
    m = 0
    s = sd
    if s >= 60:
        m = s // 60
        s -= m * 60
        if m >= 60:
            h = m // 60
            m -= h * 60

    if(s==0 and m==0 and h==0): # Vérification afin de déterminer si le temps entré par l'utilisateur est écoulé.

        # Exécution de l'action en fonction du système d'exploitation de l'utilisateur.

        if (os.sys.platform == 'win32'):
            os.system("start " + "\"\" " + patch_file)

        if (os.sys.platform == 'darwin'):
            os.system("open " + patch_file)

    return ("%02d:%02d:%02d" % (h, m, s))



#
# Définition de la class Comptearebours.
#

class Comptearebours(threading.Thread):

    def __init__(self, h, m, s): # Définition du constructeur de la class Comptearebours.
        threading.Thread.__init__(self)
        self.t = h * 3600 + m * 60 + s
        self.encore = True

    def run(self): # Fonction permettant la mise à jour.
        global app
        t1 = int(time.time()) # Utilisation du temps de l'ordinateur pour décrémenter le compteur.
        app.varsaisie.set(hms_check(self.t))
        while self.encore:
            t2 = int(time.time())
            if t2 > t1:
                self.t -= t2 - t1
                if self.t <= 0:
                    self.t = 0
                    self.encore = False
                app.varsaisie.set(hms_check(self.t))
                t1 = t2
            time.sleep(0.01)

    def stop(self): # Fonction permettant de stopper le chronomètre.
        self.encore = False



#
# Définition de la class Application.
#

class Application(tkinter.Frame):   #


    def __init__(self, master=None): # Définition du constructeur de la class Comptearebours.
        global var_langue
        tkinter.Frame.__init__(self, master)
        master.geometry("660x300")
        master.config(bg="#CECECE")

        #
        # Définition des styles et police de la class Application.
        #

        police_saisie = font.Font(master, size=24, weight='bold', family='Courier')
        police_scanf_time = font.Font(master, size=16, weight='bold', family='Courier')

        if (os.sys.platform == 'darwin'):
            police_bu = font.Font(master, size=14, weight='bold', family='Courier')

        else :
            police_bu = font.Font(master, size=10, weight='bold', family='Courier')



        #
        # Création de la zone d'affichage du compte à rebours.
        #

        self.varsaisie = tkinter.StringVar()
        self.varsaisie.set("00:00:00")
        self.saisie = tkinter.Entry(master, width=8, textvariable=self.varsaisie,  bg ='bisque', fg='#ED1F1F', font=police_saisie)
        self.saisie.place(relx=.35, rely=.20, anchor="center")
        self.saisie.config(state='readonly')


        #
        # Création de la zone de saisie par l'utilisateur.
        #

        self.grid()
        self.time = tkinter.StringVar()
        self.scanf_Time = tkinter.Entry(master, background="white",  width=13, textvariable=self.time, font=police_scanf_time)
        self.scanf_Time.focus_set()
        self.scanf_Time.place(relx=.65, rely=.20, anchor="center")

        self.labelNomFichier = tkinter.Text(master, wrap=tk.NONE)
        self.labelNomFichier.place(relx=.60, rely=.50, anchor="center", height="25", width="400")
        self.labelNomFichier.config(highlightbackground="#a7a7a7", state='disabled')

        #
        # Création du bouton de validation.
        #

        self.depart = tkinter.Button(master, text=" OK   ", command=lambda: self.go(self), font=police_bu)
        self.depart.place(relx=.48, rely=.85, anchor="center")
        self.depart.config(highlightbackground="#CECECE")
        self.depart.config(state='disabled')

        #
        # Création du bouton permettant d'annuler ou de recommencer la saisie du temps.
        #

        self.stop = tkinter.Button(master, text=" Annuler / Recommencer  ", command=lambda: self.end(self), font=police_bu)
        self.stop.place(relx=.80, rely=.85, anchor="center")
        self.stop.config(highlightbackground="#CECECE")
        self.stop.config(state='disabled')

        #
        # Création du bouton permettant à l'utilisateur de sélectionner le fichier à exécuter.
        #

        self.browse = tkinter.Button(master, text="Browse...", command=lambda: self.browse_file(self), font=police_bu)
        self.browse.place(relx=.20, rely=.5, anchor="center")
        self.browse.config(highlightbackground="#CECECE")

        #
        # Création du bouton permettant à l'utilisateur d'obtenir l'affichage des infos bulles afin d'aider celui-ci lors de l'utilisation du lanceur.
        #

        self.aide = tkinter.Button(master, text="Aide", command=lambda: self.infoAide(self), font=police_bu)
        self.aide.config()
        self.aide.place(relx=.08, rely=.85, anchor="center")
        self.aide.config(highlightbackground="#CECECE")
        infoB0_aide = infoBulle(parent=self.aide, texte="Ce bouton vous permet d'obtenir l'affichage\ndes différentes infos bulles d'aide semblable\nà celle-ci afin de vous guider lors de l'utilisation du lanceur.")

        if var_langue=="anglais":
            self.stop["text"]=" Cancel / Restart  "
            self.browse["text"]="Browse..."
            self.aide["text"]="Help"


    #
    # Fonction permettant l'envoie des données de temps saisies par l'utilisateur.
    #

    def go(self, event):

        #
        # Permet la découpe des données et leurs répartitions dans trois variables (T1, T2, T3) en fonction des heures, minutes et secondes.
        #
        try:
            T1 = int(self.time.get().split(':')[0])
            T2 = int(self.time.get().split(':')[1])
            T3 = int(self.time.get().split(':')[2])   
        except ValueError:
            T1 = 0
            T2 = 0
            T3 = 0
        self.scanf_Time.config(state='readonly') # Empêche la saisie de données supplémentaires par l'utilisateur.
        self.depart.config(state='disabled') # Empêche la validation de données supplémentaires par l'utilisateur.

        self.compt = Comptearebours(T1, T2, T3) # Appel de la class Comptearebours avec les données fournies par l'utilisateur.
        self.compt.setDaemon(True)
        self.compt.start()

    #
    # Fonction permettant d'arrêter le compte à rebours.
    #

    def end(self, event):

        self.compt.stop()

        self.scanf_Time.config(state='normal') # Permet à nouveau la saisie de données supplémentaires par l'utilisateur.
        self.depart.config(state='normal') # Permet à nouveau la validation de données supplémentaires par l'utilisateur.

    #
    # Fonction permettant la sélection du fichier à exécuter par l'utilisateur.
    #

    def browse_file(self, event):

        global patch_file
        patch_file = tkinter.filedialog.askopenfilename() # Récupération du chemin d'accès au fichier.
        patch_file =  " \"" + patch_file + "\""

        #
        # Vérification de la validité du fichier sélectionné et application de paramètres en conséquent.
        #

        if patch_file == ' ""': # Vérifie si aucun fichier n'est sélectionné.

            self.labelNomFichier.config(state='normal')
            self.labelNomFichier.delete("1.0", END)
            self.labelNomFichier.config(state='disabled')
            self.labelNomFichier.config(background="#FE6969")
            self.depart.config(state='disabled')
            self.stop.config(state='disabled')

        else : # Vérifie que le fichier est bien sélectionné et affiche le chemin de celui-ci.

            self.labelNomFichier.config(state='normal')
            self.labelNomFichier.delete("1.0", END)
            self.labelNomFichier.insert('1.0',  patch_file)
            self.labelNomFichier.config(background="#A3FEA3", state='disabled')
            self.depart.config(state='normal')
            self.stop.config(state='normal')



    #
    # Fonction permettant la définition et l'affichage des différentes infos bulles.
    #

    def infoAide(self, event):

        global tmpAide
        if tmpAide:

            tmpAide = False

            if var_langue == "francais":

                infoB1_saisie = infoBulle(parent=self.saisie, texte="Cet affichage correspond au temps du compte à rebours\nvous permettant de connaître\nle temps restant avant l'exécution du fichier.")
                infoB2_scanf_Time = infoBulle(parent=self.scanf_Time, texte="Cette zone vous permet de saisir\nle temps souhaité avant l'exécution du fichier.\nVeuillez veiller a bien indiqué le temps\nen respectant le format suivant : XX:XX:XX")
                infoB3_depart = infoBulle(parent=self.depart, texte="Ce bouton vous permet de confirmer\nle temps saisie afin de démarrer\nle compte à rebours.")
                infoB4_stop = infoBulle(parent=self.stop, texte="Ce bouton vous permet soit d'annuler\nun compte à rebours déjà effectif\nou de recommencer la saisie du temps souhaité\navant l'exécution du fichier.")
                infoB5_browse = infoBulle(parent=self.browse, texte="Ce bouton vous permet\nde sélectionner le fichier à exécuter.")
                infoB6_browse_file = infoBulle(parent=self.labelNomFichier, texte="Cet affichage correspond\nau chemin d'accès du fichier sélectionné.\nLa couleur de l'affichage peut varier,\nrouge si aucun fichier n'est sélectionné,\nvert dans le cas contraire.")

            elif var_langue == "anglais":

                infoB1_saisie = infoBulle(parent=self.saisie, texte="This display shows the time left before .")
                infoB2_scanf_Time = infoBulle(parent=self.scanf_Time, texte="This zone allows you to select\nthe time before executing the file.\nPlease make sur that the indicated time is writen\nas the format : XX:XX:XX")
                infoB3_depart = infoBulle(parent=self.depart, texte="This button allows you to confirm\nthe selected time in order to\nbegin the countdown.")
                infoB4_stop = infoBulle(parent=self.stop, texte="This button allows you to stop the running countdown.")
                infoB5_browse = infoBulle(parent=self.browse, texte="This button allows you to select\nthe file that will be executed.")
                infoB6_browse_file = infoBulle(parent=self.labelNomFichier, texte="This display shows the selected file's\n acces path.\nThe color can change,\nred means that no file is selected,\notherwise it will  be green.")


#
# Définition du main.
#

if __name__ == "__main__":


    from fonctionSup import *  # importation des fonctions permettant le centrage de la fenêtre.

    #
    # Définition de la fenêtre d'affichage du lanceur.
    #

    fenGoTime = tkinter.Tk()
    fenGoTime.title("GoTime")
    fenGoTime.resizable(width=False, height=False)

    centrefenetre(fenGoTime)
    app = Application(fenGoTime)
    app.config(bg="#CECECE")

    fenGoTime.wm_attributes('-alpha', 0.98, '-topmost', 1)


    fenGoTime.mainloop()
