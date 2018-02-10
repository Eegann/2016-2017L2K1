# *-- coding: utf-8 --*

#
#
# *=*=* # ********************************************************************** # 
# *=*=* #                                                                        # 
# *=*=* #  Id:  fonctionSup.py 8204 18-02-2017                                   #
# *=*=* #                                                                        #
# *=*=* #  Name:     fonctionSup.py                                              #
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
# <===> Functions from url: http://python.jpvweb.com/mesrecettespython/doku.php?id=geometrie_fenetre <===>
#
#
 

from tkinter import filedialog
from Motion_Capture.fonctionCourbe import *
from Eye_Tracking.voirVideo import *
import threading 

#
# Fonctions permettant le centrage de la fenêtre.
#

x = 0

def geoliste(geo):
    r = [i for i in range(0, len(geo)) if not geo[i].isdigit()]
    return [int(geo[0:r[0]]), int(geo[r[0] + 1:r[1]]), int(geo[r[1] + 1:r[2]]), int(geo[r[2] + 1:])]


def centrefenetre(fen):
    fen.update_idletasks()
    l, h, x, y = geoliste(fen.geometry())
    fen.geometry("%dx%d%+d%+d" % (l, h, (fen.winfo_screenwidth() - l) // 2, (fen.winfo_screenheight() - h) // 2))

#
# Fonction permettant de demander un fichier.
#

def demandeFichier():
    nomfichier=filedialog.askopenfilename()
    return nomfichier

#
# Fonction permettant la mise à jour des courbes.
#

def fonctionIntermediaireCoda(FC,VL,fen):
    fonctionCourbe(FC, VL)
    fen.destroy()


def fonctionIntermediaireEye(FE,FV, VL, fen):
    fen.destroy()
    t=threading.Thread(target=fonctionVoirVideo, kwargs={'cheminVideo':FV, 'cheminCsv':FE, 'var_langue':VL})
    t.start()



def fonctionIntermediaireNew(FE,FC,FV,VL,fenetreNew):
    fenetreNew.destroy()
    t=threading.Thread(target=fonctionVoirVideo, kwargs={'cheminVideo':FV, 'cheminCsv':FE, 'var_langue':VL})
    t.start()
    fonctionCourbe(FC,VL)
