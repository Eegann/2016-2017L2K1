# *-- coding: utf-8 --*

#
#
# *=*=* # ********************************************************************** # 
# *=*=* #                                                                        # 
# *=*=* #  Id:  readVideo.py 6022 11-03-2017                                     #
# *=*=* #                                                                        #
# *=*=* #  Name:     readVideo.py                                                #
# *=*=* #  Project:  L2K1                                                        #
# *=*=* #  Author:   Created by <Benjamin Cohen> on 11/03/2017.                  #
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
# <===> Inspired by url : http://stackoverflow.com/questions/32342935/using-opencv-with-tkinter <===>
#
#





#
#  Importation de l'ensemble des modules et fonctions nécessaires.
#

import tkinter as tk
import cv2
import PIL.Image
import PIL.ImageTk
from tkinter import *
import random


def readVideo(root, patch_video): # La fonction prend en paramètre la fenêtre ainsi que le chemin du fichier vidéo.
    
    
    cap = cv2.VideoCapture(patch_video)  

    def show_frame(): # Fonction de lecture des frames de la vidéo.

        _, frame = cap.read()
        frame = cv2.flip(frame, 1)
        cv2image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGBA)
        img = PIL.Image.fromarray(cv2image)
        imgtk = PIL.ImageTk.PhotoImage(image=img)
        lmain.imgtk = imgtk
        lmain.configure(image=imgtk)
        lmain.after(80, show_frame) # Permet l'accélération de la vidéo en sélectionnant le nombre de frames.




    # Définition des zones d'affichage

    canvas = Canvas(root, width=1000, height=1000, bg='white') 
    canvas.pack(expand=YES, fill=BOTH)

    lmain = Label(root, fg='white', bg='black')
    lmain.place(relx=.1, rely=.1)

    canvas.create_window(365, 361, window=lmain)


    show_frame()
   



if __name__ == "__main__":


    root = tk.Toplevel()
    readVideo(root, 'pupil.mp4') # Appel de la fonction readVideo().

    root.mainloop()