from tkinter import *
import cv2
import numpy as np
from tkinter import font

choix=IntVar

def fonctionVoirVideo(cheminVideo=NONE, cheminCsv=NONE, var_langue=NONE):
    pullData = open(cheminCsv,"r").read()  # on met le chemin du fichier (chaque repertoire du chemin sont séparé par // ou \)

    dataList = pullData.split('\n')  # chaque ligne est separée par un retour chariot ('\n')
    '''listedesD = []             #liste des debut de frame
    listedesF = []             #liste des fin de frame
    listedesX = []             #liste des x
    listedesY = []             #liste des y'''
    gaze = []  # on crée une liste vide
    del dataList[0]  # on supprime la premiere qui contient les info contenu dans chaque colonne
    for eachLine in dataList:  # on selectionne chaque ligne
        if len(eachLine) > 1:
            _, _, _, d, f, x, y, _, _, _ = eachLine.split(
                ',')  # on affecte pour chaque variable les valeurs qui nous interrese
            '''listedesD.append(float(d))    #on ajoute la valeur de d à listedesD
            listedesF.append(int(f))    #on ajoute la valeur f à listedesF
            listedesX.append(float(x))    #on ajoute la valeur x à listedesX
            listedesY.append(float(y))    #on ajoute la valeur y à listedesY'''
            x = float(x) * 1280  # on traduit les coordonées normal en coordonnées "pixel"
            y = ((float(y) * 720) - 720) * -1  # on traduit les coordonées normal en coordonnées "pixel"
            gaze.append([int(d), int(f), int(x), int(y)])  # on rempli la liste avec les valeurs que l'on a besoin


    cap = cv2.VideoCapture(cheminVideo)  # lien de la video
    tmp = [int(cap.get(cv2.CAP_PROP_FRAME_COUNT))]  # nombre de frame dans la video
    ##tmp = [5640]
    tmp.append(tmp[0] // 30)  # on a le nombre de seconde total (minute+seconde) de la video
    tmp.append(tmp[1] // 60)  # on a le nombre de minute de la video
    tmp.append(tmp[1] % 60)  # on a le nombre de seconde de la video
    print(tmp)
    '''
    def convertir(tmp): #convertit une durée en nombre de frame
        tmp[1]= tmp[2]*60+tmp[3]#nombre de seconde total
        tmp[0]=sec*30#notre video est à 30 fps(il y a 30 image/sec) donc on
    #multiplit par 30 pour avoir le nombre d'image(de frame) total
    '''


    def visualiser(de, fi):
        cap.set(cv2.CAP_PROP_POS_FRAMES, de[0])  # on indique à quel frame de la video on doit se placer
        cap.set(cv2.CAP_PROP_FPS, 33)  # valeur fps
        while cap.isOpened():
            ret, frame = cap.read()  # on prend une capture d'image et on la place dans frame
            copie = frame.copy()  # no fait une copie de la frame
            '''if cap.get(cv2.CAP_PROP_POS_FRAMES) == t[0]:
                 frame = cv2.circle(frame, (t[1], t[2]), 20, (0, 0, 90),-1)'''
            tb = np.zeros((720, 1280, 3), dtype=frame.dtype)  # on fait un tableau de 0, qui représentera une imagge noir

            for yi in range(len(gaze)):
                # print("ycycjcjhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhh")
                '''if (gaze[yi][1]>int(cap.get(cv2.CAP_PROP_POS_FRAMES))):  #on sort de la boucle si
                    break'''
                # if ((gaze[yi][0]<cap.get(cv2.CAP_PROP_POS_FRAMES)) and (gaze[yi][1]>cap.get(cv2.CAP_PROP_POS_FRAMES))):
                if cap.get(cv2.CAP_PROP_POS_FRAMES) in range(gaze[yi][0], gaze[yi][
                    1]):  # si la frame actuel se trouve entre la frame de debut et la frame de fin d'un gaze ploot

                    """copie = cv2.circle(frame, (gaze[yi][2], gaze[yi][3]), int((gaze[yi][1]-cap.get(cv2.CAP_PROP_POS_FRAMES))*2), (0, 0, 90),-1)   #on place un cercle dont le rayon diminue"""

                    copie = cv2.circle(frame, (gaze[yi][2], gaze[yi][3]),10, (0, 0, 90), int(((cap.get(cv2.CAP_PROP_POS_FRAMES))-(gaze[yi][0]+1))))

                    """copie = cv2.circle(frame, (gaze[yi][2], gaze[yi][3]),10, (0, 0, 90), int(((cap.get(cv2.CAP_PROP_POS_FRAMES))-(gaze[yi][0]+1)))*4)

                    copie = cv2.circle(frame, (gaze[yi][2], gaze[yi][3]),10, (0, 0, 90), int(((gaze[yi][1]+1)-(cap.get(cv2.CAP_PROP_POS_FRAMES))))*2)



                    frames = cv2.circle(copie, (gaze[yi][2], gaze[yi][3]), 20, (255, 255, 255),-1)
                    cv2.addWeighted(frames,0,frame,0.3,0,copie)

                    frame = cv2.circle(frame, (1280, 720), 20, (0, 0, 90),-1)

                    #frames =   cv2.circle(copie, (gaze[yi][2], gaze[yi][3]), int((gaze[yi][1]-cap.get(cv2.CAP_PROP_POS_FRAMES))*2), (0, 0, 90),-1)

                    cv2.addWeighted(frames,((gaze[yi][1]-int(cap.get(cv2.CAP_PROP_POS_FRAMES)))/(gaze[yi][1]-gaze[yi][0])),frame,1-((gaze[yi][1]-int(cap.get(cv2.CAP_PROP_POS_FRAMES)))/(gaze[yi][1]-gaze[yi][0])),0,copie)

                    copie = cv2.circle(frame, (gaze[yi][2], gaze[yi][3]),20, (0, 0, 90), int(((cap.get(cv2.CAP_PROP_POS_FRAMES))-(gaze[yi][0]+1)))) #on place un cercle vide


                    lb=np.zeros((720,1280,3),dtype=frame.dtype)   #tunnel lumineux
                    lb = cv2.circle(lb, (gaze[yi][2], gaze[yi][3]),60, (30, 30, 30), -1)
                    frames=cv2.add(lb,frame)
                    cv2.addWeighted(frames,0.8,frame,0,0,copie)

                    ########tb=np.zeros((720,1280,3),dtype=frame.dtype)
                    lb=np.zeros((720,1280,3),dtype=frame.dtype)  #heatmap
                    cv2.circle(lb, (gaze[yi][2], gaze[yi][3]),60, (30, 30, 30), -1)
                    tb=cv2.add(tb,lb)
                    frames=cv2.applyColorMap(tb,cv2.COLORMAP_HSV)

                    cv2.addWeighted(frames,0.2,frame,0.8,0,copie)

                    copie = cv2.line(frame, (gaze[yi][2]-5, gaze[yi][3]), (gaze[yi][2]+5, gaze[yi][3]), (0, 0, 90), int((gaze[yi][1]-cap.get(cv2.CAP_PROP_POS_FRAMES))*2))
                    copie = cv2.line(frame, (gaze[yi][2], gaze[yi][3]-5), (gaze[yi][2], gaze[yi][3]+5), (0, 0, 90), int((gaze[yi][1]-cap.get(cv2.CAP_PROP_POS_FRAMES))*2))

                    copie = cv2.line(frame, (gaze[yi][2]-5, gaze[yi][3]), (gaze[yi][2]+5, gaze[yi][3]), (0, 0, 90), int((gaze[yi][1]-cap.get(cv2.CAP_PROP_POS_FRAMES))/3))
                    copie = cv2.line(frame, (gaze[yi][2], gaze[yi][3]-5), (gaze[yi][2], gaze[yi][3]+5), (0, 0, 90), int((gaze[yi][1]-cap.get(cv2.CAP_PROP_POS_FRAMES))/3))

                    copie = cv2.line(frame, (gaze[yi][2]-int((gaze[yi][1]-cap.get(cv2.CAP_PROP_POS_FRAMES))), gaze[yi][3]), (gaze[yi][2]+int((gaze[yi][1]-cap.get(cv2.CAP_PROP_POS_FRAMES))), gaze[yi][3]), (0, 0, 90), 5)
                    copie = cv2.line(frame, (gaze[yi][2], gaze[yi][3]-int((gaze[yi][1]-cap.get(cv2.CAP_PROP_POS_FRAMES)))), (gaze[yi][2], gaze[yi][3]+int((gaze[yi][1]-cap.get(cv2.CAP_PROP_POS_FRAMES)))), (0, 0, 90), 5)

                    copie = cv2.line(frame, (gaze[yi][2]-int((gaze[yi][1]-cap.get(cv2.CAP_PROP_POS_FRAMES))), gaze[yi][3]), (gaze[yi][2]+int((gaze[yi][1]-cap.get(cv2.CAP_PROP_POS_FRAMES))), gaze[yi][3]), (0, 0, 90),  int((gaze[yi][1]-cap.get(cv2.CAP_PROP_POS_FRAMES))/3))
                    copie = cv2.line(frame, (gaze[yi][2], gaze[yi][3]-int((gaze[yi][1]-cap.get(cv2.CAP_PROP_POS_FRAMES)))), (gaze[yi][2], gaze[yi][3]+int((gaze[yi][1]-cap.get(cv2.CAP_PROP_POS_FRAMES)))), (0, 0, 90),  int((gaze[yi][1]-cap.get(cv2.CAP_PROP_POS_FRAMES))/3))"""

            if cap.get(cv2.CAP_PROP_POS_FRAMES) >= fi[0] or cv2.waitKey(1) & 0xFF == ord('q'):
                break
            cv2.imshow("mywindow", copie)

            k = cv2.waitKey(20) & 0xff
            r = cv2.CAP_PROP_FPS
            print(r)
            print(cap.get(cv2.CAP_PROP_POS_FRAMES))
            print(cap.get(cv2.CAP_PROP_FPS))
            print(cv2.CAP_PROP_POS_FRAMES)
            if k == 27 or cv2.waitKey(1) & 0xFF == ord('q'):
                break

                    ##frames = cv2.circle(copie, (gaze[yi][2], gaze[yi][3]), 20, (255, 255, 255),-1)
                    # cv2.addWeighted(frames,0,frame,0.3,0,copie)

            frame = cv2.circle(frame, (1280, 720), 20, (0, 0, 90), -1)

            if cap.get(cv2.CAP_PROP_POS_FRAMES) >= fi[0]:
                break
            cv2.imshow("mywindow", copie)

            k = cv2.waitKey(20) & 0xff
            r = cv2.CAP_PROP_FPS
            print(r)
            print(cap.get(cv2.CAP_PROP_POS_FRAMES))
            print(cap.get(cv2.CAP_PROP_FPS))
            print(cv2.CAP_PROP_POS_FRAMES)
            if k == 27:
                break


    def obtenir():  # fonction obtenir

        # message.config(text = "M = " + str(minuted.get())) #élaboration d'un message contenant la valeur pointer par le curseur au moment où l'on a cliqué
        a = minuted.get()  # affectation de la valeur pointer par le curseur au moment où l'on a cliqué à la variable a
        # message.config(text = "M = " + str(seconded.get())) #élaboration d'un message contenant la valeur pointer par le curseur au moment où l'on a cliqué
        b = seconded.get()  # affectation de la valeur pointer par le curseur au moment où l'on a cliqué à la variable a
        de = [(int(a) * 60 + int(b)) * 30]
        de.append(int(a) * 60 + int(b))
        de.append(int(a))
        de.append(int(b))
        print((int(a) * 60 + int(b)) * 30)
        print(de)

        # message.config(text = "M = " + str(minutef.get())) #élaboration d'un message contenant la valeur pointer par le curseur au moment où l'on a cliqué
        c = minutef.get()  # affectation de la valeur pointer par le curseur au moment où l'on a cliqué à la variable a
        # message.config(text = "M = " + str(secondef.get())) #élaboration d'un message contenant la valeur pointer par le curseur au moment où l'on a cliqué
        d = secondef.get()  # affectation de la valeur pointer par le curseur au moment où l'on a cliqué à la variable a
        fi = [(int(c) * 60 + int(d)) * 30]
        fi.append(int(c) * 60 + int(d))
        fi.append(int(c))
        fi.append(int(d))
        print((int(c) * 60 + int(d)) * 30)
        print(fi)
        if var_langue=="francais":
            if (tmp[1] < de[1]):
                message8.config(
                    text="Impossible de debuter la video après " + str(tmp[2]) + " minutes et " + str(tmp[3]) + " secondes !!!",
                    fg="red")
            if (tmp[1] < fi[1]):
                message9.config(
                    text="Impossible de terminer la video après " + str(tmp[2]) + " minutes et " + str(tmp[3]) + " secondes !!!",
                    fg="red")
            if (fi[1] < de[1]):
                message.config(text="Impossible de debuter la video après la fin de la video.", fg="red")
            if ((tmp[1] >= fi[1]) & (fi[1] > de[1]) & (tmp[1] >= fi[1])):
                visualiser(de, fi)
        else:
            if (tmp[1] < de[1]):
                message8.config(
                    text="Impossible to start the video after " + str(tmp[2]) + " minutes and " + str(tmp[3]) + " seconds !!!",
                    fg="red")
            if (tmp[1] < fi[1]):
                message9.config(
                    text="Impossible to end the video after " + str(tmp[2]) + " minutes and " + str(tmp[3]) + " seconds !!!",
                    fg="red")
            if (fi[1] < de[1]):
                message.config(text="Impossible to start the video after it's end.", fg="red")
            if ((tmp[1] >= fi[1]) & (fi[1] > de[1]) & (tmp[1] >= fi[1])):
                visualiser(de, fi)


    fenetre = Tk()  # création d'une fenêtre
    fenetre.geometry("300x350")  # on donne les dimensions de cette fenêtre
    message1 = Label(fenetre, text="La video dure " + str(tmp[2]) + " minutes et " + str(tmp[3]) + " secondes",
                     font='times 12 bold underline')
    message1.pack()  # affichage du message

    minuted = IntVar()
    seconded = IntVar()
    message2 = Label(fenetre, text="Début de la video :")
    message2.pack(anchor=N)  # affichage du message
    message4 = Label(fenetre, text="minutes ", fg="blue")
    message4.pack()  # on affiche ce bouton
    minuted = Spinbox(fenetre, from_=0, to=tmp[2], textvariable=minuted)  # creation des bouton plus et moins
    minuted.pack(anchor=E)  # affichage de ces bouton
    message5 = Label(fenetre, text="secondes ", fg="blue")
    message5.pack()  # affichage du message
    seconded = Spinbox(fenetre, from_=0, to=tmp[3], textvariable=seconded)  # creation des bouton plus et moins
    seconded.pack(anchor=E)  # affichage de ces bouton
    message8 = Label(fenetre)
    message8.pack()

    minutef = IntVar()
    secondef = IntVar()
    minutef.set(tmp[2])
    secondef.set(tmp[3])
    message3 = Label(fenetre, text="Fin de la video :")
    message3.pack(anchor=N)  # affichage du message
    message6 = Label(fenetre, text="minutes ", fg="blue")
    message6.pack()  # affichage du message
    minutef = Spinbox(fenetre, from_=0, to=tmp[2], textvariable=minutef)  # creation des bouton plus et moins
    minutef.pack(anchor=E)  # affichage de ces bouton
    message7 = Label(fenetre, text="secondes ", fg="blue")
    message7.pack()  # affichage du message
    secondef = Spinbox(fenetre, from_=0, to=tmp[3], textvariable=secondef)  # creation des bouton plus et moins
    secondef.pack(anchor=E)  # affichage de ces bouton
    message9 = Label(fenetre)
    message9.pack()

    message10 = Label(fenetre, text="Maintenir Q pour stopper la vidéo.")
    message10.pack()

    bouton = Button(fenetre, text="Confirmer", command=obtenir)  # création du bouton valider qui apelle la foction obtenir
    bouton.place(relx="0.5", rely="0.92", anchor=S)  # affichage de ce bouton
    message = Label(fenetre)
    message.pack()
    if var_langue=="anglais":
        message1["text"]="The video lasts " + str(tmp[2]) + " minutes and " + str(tmp[3]) + " seconds"
        message2["text"]="Beginning of the video :"
        message5["text"]="seconds"
        message3["text"]="End of the video :"
        message7["text"]="seconds"
        message10["text"]="Press Q to stop the video."

    fenetre.mainloop()

