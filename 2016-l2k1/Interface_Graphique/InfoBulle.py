# *-- coding: utf-8 --*

#
#
# *=*=* # ********************************************************************** # 
# *=*=* #                                                                        # 
# *=*=* #  Id:  InfoBulle.py 8242 18-02-2017                                     #
# *=*=* #                                                                        #
# *=*=* #  Name:     InfoBulle.h                                                 #
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
# <===> Functions from url : https://www.developpez.net <===>
#
#


import tkinter as tk

#
#  Définition de la classe info bulle
#

class infoBulle(tk.Toplevel):


    #
    #  Définition du style ainsi que des différentes actions déclenchant les infos bulles.
    #

    def __init__(self, parent=None, texte='', temps=1000):
        tk.Toplevel.__init__(self, parent, bd=1, bg='black')
        self.tps = temps
        self.parent = parent
        self.withdraw()
        self.overrideredirect(1)
        self.transient()
        l = tk.Label(self, text=texte, bg="antiquewhite", justify='left')
        l.update_idletasks()
        l.pack()
        l.update_idletasks()
        self.tipwidth = l.winfo_width()
        self.tipheight = l.winfo_height()
        self.parent.bind('<Enter>', self.delai)
        self.parent.bind('<Button-1>', self.efface)
        self.parent.bind('<Leave>', self.efface)


    def delai(self, event):
        self.action = self.parent.after(self.tps, self.affiche)


    #
    #  Définition de l'affichage des infos bulles en fonction de la position.
    #

    def affiche(self):
        self.update_idletasks()
        posX = self.parent.winfo_rootx() + self.parent.winfo_width()
        posY = self.parent.winfo_rooty() + self.parent.winfo_height()
        if posX + self.tipwidth > self.winfo_screenwidth():
            posX = posX - self.winfo_width() - self.tipwidth
        if posY + self.tipheight > self.winfo_screenheight():
            posY = posY - self.winfo_height() - self.tipheight
        # ~ print posX,print posY
        self.geometry('+%d+%d' % (posX, posY))
        self.deiconify()
        self.wm_attributes('-topmost', 1)


    #
    #  Suppression des infos bulles.
    #

    def efface(self, event):
        self.withdraw()
        self.parent.after_cancel(self.action)
