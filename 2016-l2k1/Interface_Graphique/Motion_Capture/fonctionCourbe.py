import matplotlib
matplotlib.use("TkAgg")

from tkinter import font
from tkinter.filedialog import *
from tkinter import *
from matplotlib import *
import tkinter as Tk

from Motion_Capture.MARCHERTRAIT import *
from Motion_Capture.dernier1 import *

import matplotlib.animation as animation
import numpy as np

import scipy.io as spio
import matplotlib.pyplot as plt

from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg

def fonctionCourbe(chemin, var_langue):

    #Définition de la fenêtre contenant les résultats.
    fenetreResultat=Toplevel()
    fenetreResultat.geometry("1350x700")
    fenetreResultat.config(bg="#CECECE")
    fenetreResultat.maxsize(width=1350, height=700)

    policeTitre = font.Font(fenetreResultat, size=20, weight='bold', family='Helvectica')  # Définition de la police d'affichage du titre.
    policetxt = font.Font(fenetreResultat, size=12, family='Helvectica')  # Définition de la police affichage du texte.

    labelCourbes = Label(fenetreResultat, text="Page de résultat", bg="#FF3D03", fg="#FFFFFF", font=policeTitre)
    labelCourbes.place(relx=0.5, rely=0, anchor="n", width="1500", height="70")

    matfile = (chemin) #Chargement du fichier codamotion
    matdata = spio.loadmat(matfile,squeeze_me=True)
    print (matdata.keys())

    o=matdata['Analog']['Analog21'].item()['value']  #Création d'un tableau avec les valeurs de Analog21
    print (o)
    t=o.tolist() #Création d'une liste équivalente au tableau de Analog21


    u=matdata['Analog']['Analog22'].item()['value'] #Création d'un tableau avec les valeurs de Analog22
    print (u)
    s=u.tolist() #Création d'une liste équivalente au tableau de Analog22

    r=matdata['Analog']['Analog23'].item()['value'] #Création d'un tableau avec les valeurs de Analog23
    v=r.tolist() #Création d'une liste équivalente au tableau de Analog23


    a=matdata['Analog']['Analog24'].item()['value'] #Création d'un tableau avec les valeurs de Analog24
    print (a)
    g=a.tolist() #Création d'une liste équivalente au tableau de Analog24

    ####Fonction de lissage
    def lissage(Ly, p):
        '''Fonction qui débruite une courbe par une moyenne glissante
        sur 2P+1 points'''
        Lxout = []
        Lyout = []
        for i in range(p, len(Ly) - p):
            Lxout.append(i)
        for i in range(p, len(Ly) - p):
            val = 0
            for k in range(2 * p):
                val += Ly[i - p + k]
            Lyout.append(val / 2 / p)

        return Lxout, Lyout

    x, y = lissage(t,2) #Lisser Analog21
    dr, gc = lissage(s,2) #Lisser Analog22
    ht, bs = lissage(v,2) #Lisser Analog23
    no, su = lissage(g,2) #Lisser Analog24

    if var_langue == "francais":
        CO = "Courbe originale"
        CL = "Courbe lissée"
        tem = "Temps (x10ms)"
        her = "Hertz (Hz)"
    else:
        CO = "Original curve"
        CL = "Smoothed curve"
        tem = "Time (x10ms)"
        her = "Hertz (Hz)"

    #Code de la ligne 79 à 99 basé sur:
    #http://stackoverflow.com/questions/12124350/how-to-update-the-contents-of-a-figurecanvastkagg
    #https://pythonprogramming.net/how-to-embed-matplotlib-graph-tkinter-gui/

    #Création de la figure
    fig = plt.figure()
    plt.rcParams.update({'font.size': 7})
    #Création des deux courbes
    ax1 = fig.add_subplot(211)
    ax1.plot(t)
    ax1.set_title(CO)
    ax2 = fig.add_subplot(212)
    ax2.plot(t)
    ax2.plot(x,y)
    ax2.set_title(CL)
    #Ajout des nom des axes
    ax2.set_xlabel(tem)
    ax2.set_ylabel(her)
    ax1.set_ylabel(her)
    #Création de canvas contenant la figure
    canvas = FigureCanvasTkAgg(fig, fenetreResultat)
    canvas.show()
    canvas.get_tk_widget().place(relx=0.30, rely=0.53, anchor="center", height=500, width=800)
    canvas.get_tk_widget().config(relief="raised", bd=2)
    #Création de la barre avec les boutons permettant de zoomer, enregistrer, se déplacer etc etc
    toolbar = NavigationToolbar2TkAgg(canvas, fenetreResultat)
    toolbar.update()


    #Bouton permettant de lancer la fonction qui affiche toutes les courbes sur une seule page.
    boutonCourbes=Button(fenetreResultat, text="Voir toutes les courbes", font=policetxt, command=lambda : goCourbes(t,s,v,g,x,y,dr,gc,ht,bs,no,su, var_langue))
    boutonCourbes.place(relx=0.30, rely=0.94, anchor="s")
    boutonCourbes.config(highlightbackground="#CECECE")





    #Fonction permettant de mettre a jour de contenu du canvas en fonction du choix de l'utilisateur.


    #Boutons permettant de choisir quel courbes mettre dans le canvas.
    boutonC1=Button(fenetreResultat, text="Tibia droit", bg="#9F9F9F", font=policetxt, command=lambda:changerCourbes(canvas, ax1, ax2, t, x, y, boutonC1, boutonC2, boutonC3, boutonC4, CL, CO, tem, her))
    boutonC1.place(relx=0.10, rely=0.14, anchor="center", height=30, width=120)
    boutonC1.config(highlightbackground="#CECECE")


    boutonC2 = Button(fenetreResultat, text="Tibia gauche", bg="#F0F0ED", font=policetxt, command=lambda:changerCourbes(canvas, ax1, ax2, s, dr, gc, boutonC2, boutonC1, boutonC3, boutonC4, CL, CO, tem, her))
    boutonC2.place(relx=0.233, rely=0.14, anchor="center", height=30, width=120)
    boutonC2.config(highlightbackground="#CECECE")

    boutonC3 = Button(fenetreResultat, text="Soléaire droit", bg="#F0F0ED", font=policetxt, command=lambda:changerCourbes(canvas, ax1, ax2, v, ht, bs, boutonC3, boutonC2, boutonC1, boutonC4, CL, CO, tem, her))
    boutonC3.place(relx=0.366, rely=0.14, anchor="center", height=30, width=120)
    boutonC3.config(highlightbackground="#CECECE")

    boutonC4 = Button(fenetreResultat, text="Soléaire gauche", bg="#F0F0ED", font=policetxt, command=lambda:changerCourbes(canvas, ax1, ax2, g, no, su, boutonC4, boutonC2, boutonC3, boutonC1, CL, CO, tem, her))
    boutonC4.place(relx=0.50, rely=0.14, anchor="center", height=30, width=120)
    boutonC4.config(highlightbackground="#CECECE")

    if var_langue=="anglais":
        boutonCourbes["text"]="See all curves"
        boutonC1["text"]="Right tibia"
        boutonC2["text"]="Left tibia"
        boutonC3["text"]="Right soleus"
        boutonC4["text"]="Left soleus"
        labelCourbes["text"]="Result page"


    #Définition de la fonction permettant de sélectionner les options de la représentation 3D
    def intermediaire3D():
        root = Tk()
        root.config(bg="#DCDCDC")
        if var_langue=="francais":
            root.title("Options 3D")
        else:
            root.title("3D options")
        root.geometry("350x800")
        root.resizable(width=False, height=False)  # Redimensionnement de la fenêtre immobilisée.

        police_options3D = font.Font(root, size=12, weight='bold', family='Helvectica') # Mise en place du style police.

        label1=Label(root, text="Sélection les numéros de boutons à afficher :", font=police_options3D)
        label1.config(bg="#DCDCDC")
        label1.pack()

        f3 = Frame(root)
        s3 = Scrollbar(f3)
        l3 = Listbox(f3, selectmode=MULTIPLE, exportselection=0, bg='#F9F9F8', font=police_options3D)  # EXTENDED
        f5 = Frame(root)
        l5 = Listbox(f5, selectmode=MULTIPLE, exportselection=0, bg='#F9F9F8', font=police_options3D)  # EXTENDED
        if var_langue=="francais":
            l3.insert(0, 'Déselectionner')
        else:
            l3.insert(0, 'Deselect')
        l3.itemconfig(0, bg='#ff6666')

        if var_langue=="francais":
            for i in range(1, 40): l3.insert(i, 'Marqueur ' + str(i))
        else:
            for i in range(1, 40): l3.insert(i, 'Marker ' + str(i))
        s3.config(command=l3.yview)
        l3.config(yscrollcommand=s3.set)
        l3.pack(side=LEFT, fill=Y)
        s3.pack(side=RIGHT, fill=Y)
        f3.pack()

        def clic3(evt):
            items = l3.curselection()
            if 0 in items:
                l3.selection_clear(0, 40)
            global leger
            leger.extend(l3.curselection())
            return print(items)  # On retourne l'élément (un string) sélectionné

        def clicd3(evt):
            print(evt.y)  # recupere la coordonée selon y
            print(l3.nearest(evt.y))  # reecupere le bouton le plus proche
            print(evt)
            fr = l3.nearest(evt.y)
            # vou[fr][i][0]
            # s1 = [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

            s2 = []
            s1 = []
            t = []
            fig = plt.figure()
            ax1 = fig.add_subplot(211)
            ax2 = fig.add_subplot(212, sharex=ax1)
            for i in range(len(vou[fr]) - 11550):
                s1.append(vou[fr][i][0])
                s2.append((vou[fr][i + 1][0] - vou[fr][i][0]) / 15)
                t.append(i)
                print('att')
                ax1.plot(t, s1)
                # ax2.plot(t, s2)
            del s1[i]
            ax2.plot(t, s2)
            # t=np.arange(59)

            multi = MultiCursor(fig.canvas, (ax1, ax2), color='r', lw=1)
            pts = ginput(2)
            print(pts)
            x = math.floor(pts[0][0])
            x1 = math.floor(pts[1][0])
            y = str(s1[x])
            v = str(s2[x])
            y1 = str(s1[x1])
            v1 = str(s2[x1])
            ax1.text(0, 50, r'y(t)=' + y, fontsize=15, bbox={'facecolor': 'blue', 'alpha': 0.5, 'pad': 10})
            ax2.text(0, 13, r'v(y)=' + v, fontsize=15)
            ax1.annotate('y(t)=' + y, xy=(x, s1[x]), xytext=(x + 1, s1[x] + 5),
                        arrowprops=dict(facecolor='black', shrink=0.05))
            ax2.annotate('v(y)=' + v, xy=(x, s2[x]), xytext=(x + 1, s2[x] + 5),
                        arrowprops=dict(facecolor='black', shrink=0.05))
            ax1.text(0, 50, r'y(t)=' + y1, fontsize=15, bbox={'facecolor': 'blue', 'alpha': 0.5, 'pad': 10})
            ax2.text(0, 13, r'v(y)=' + v1, fontsize=15)
            ax1.annotate('y(t)=' + y1, xy=(x1, s1[x1]), xytext=(x1 + 1, s1[x1] + 5),
                        arrowprops=dict(facecolor='black', shrink=0.05))
            ax2.annotate('v(y)=' + v1, xy=(x1, s2[x1]), xytext=(x1 + 1, s2[x1] + 5),
                        arrowprops=dict(facecolor='black', shrink=0.05))
            plt.show()

        l3.bind('<ButtonRelease-1>', clic3)  ## on associe l'évènement "relachement du bouton gauche la souris" à la listbox
        l3.bind('<Double-Button-1>', clicd3)
        label2=Label(root, text="Sélection du style :", font=police_options3D)
        label2.config(bg="#DCDCDC")
        label2.pack()
        f4 = Frame(root)
        s4 = Scrollbar(f4)
        l4 = Listbox(f4, selectmode=MULTIPLE, exportselection=0, bg='#F9F9F8', font=police_options3D)  # EXTENDED
        if var_langue=="francais":
            l4.insert(0, 'Déselectionner')
            l4.itemconfig(0, bg='#ff6666')
            l4.insert(1, 'Traits')
            l4.insert(2, 'Points')
            l4.insert(3, 'Relier')
            l4.insert(4, 'Effacer')
            l4.insert(5, 'Historique')
        else:
            l4.insert(0, 'Deselect')
            l4.itemconfig(0, bg='#ff6666')
            l4.insert(1, 'Lines')
            l4.insert(2, 'Dots')
            l4.insert(3, 'Link')
            l4.insert(4, 'Erase')
            l4.insert(5, 'History')
        s4.config(command=l3.yview)
        l4.config(yscrollcommand=s4.set)
        l4.pack(side=LEFT, fill=Y)
        s4.pack(side=RIGHT, fill=Y)
        f4.pack()

        def clic4(evt):
            items = l4.curselection()
            if 0 in items:
                l4.selection_clear(0, 4)
            if 1 in items:
                l4.selection_clear(3)
            if 3 in items:
                l4.selection_clear(1)
                '''#animate(i)'''

            fonction3D(fenetreResultat, chemin, l4.curselection(), [], [])
            if (3 in items) == False:
                l4.selection_clear(4)
            if 4 in items:
                global lourd
                lourd = []
            return print(items)  ## On retourne l'élément (un string) sélectionné

            fonction3D(fenetreResultat, chemin, l4.curselection(), [], [])

        l4.bind('<ButtonRelease-1>', clic4)  ## on associe l'évènement "relachement du bouton gauche la souris" à la listbox

        label3=Label(root, text="Points à afficher (tous par défaut):", font=police_options3D)
        label3.config(bg="#DCDCDC")
        label3.pack()
        s5 = Scrollbar(f5)

        if var_langue=="francais":
            l5.insert(0, 'Déselectionner')
        else:
            l5.insert(0, "Deselect")
        l5.itemconfig(0, bg='#ff6666')
        if var_langue=="francais":
            for i in range(1, 40): l5.insert(i, 'Marqueur ' + str(i))
        else:
            for i in range(1, 40): l5.insert(i, 'Marker ' + str(i))
        s5.config(command=l5.yview)
        l5.config(yscrollcommand=s5.set)
        l5.pack(side=LEFT, fill=Y)
        s5.pack(side=RIGHT, fill=Y)
        f5.pack()

        def clic5(evt):
            itemos = l5.curselection()
            if len(itemos) > 2:
                l5.selection_clear(itemos[0])
                print(len(itemos))
            if len(itemos) == 2:
                global lourd
                lourd.append(l5.curselection())
            if 0 in itemos:
                l5.selection_clear(0, 40)
            return print(itemos)  ## On retourne l'élément (un string) sélectionné

        l5.bind('<ButtonRelease-1>', clic5)  ## on associe l'évènement "relachement du bouton gauche la souris" à la listbox

        if var_langue=="anglais":
            label1["text"]="Select the number of buttons to display :"
            label2["text"]="Select the style :"
            label3["text"]="Dots to display (all by default) :"

        root.mainloop()
    ####################################################################################################






    boutonOption3D=Button(fenetreResultat, text="Options 3D", bg="#F0F0ED", font=policetxt, command=lambda:intermediaire3D())
    boutonOption3D.place(relx=0.84, rely=0.94, anchor="s")
    boutonOption3D.config(highlightbackground="#CECECE")
    if var_langue=="anglais":
        boutonOption3D["text"]="3D options"



#Fonction permettant d'afficher toutes les courbes sur une seule page.
def goCourbes(t,s,v,g,x,y,dr,gc,ht,bs,no,su, var_langue):

    #Création de la figure Courbes
    fig = plt.figure(num="Courbes", figsize=(12,6))
    plt.subplots_adjust(hspace = 0.5)
    if var_langue=="francais":
        fig.canvas.set_window_title('Courbes musculaires')
    else:
        fig.canvas.set_window_title('Muscular curves')
    plt.rcParams.update({'font.size': 8})

    #On définit toutes les courbes nécessaires.

    #Définition de la 1ère courbe.
    plt.subplot(241)
    if var_langue=="francais":
        plt.title("Muscle du tibia droit\n(original)")
        plt.xlabel('Temps (x10ms)')
    else:
        plt.title("Muscle of the right tibia\n(original)")
        plt.xlabel('Time (x10ms)')
    plt.plot(t)

    plt.ylabel('Hertz (Hz)')

    # Définition de la 2nd courbe.
    plt.subplot(242)
    if var_langue=="francais":
        plt.title("Muscle du tibia gauche\n(original)")
        plt.xlabel('Temps (x10ms)')
    else:
        plt.title("Muscle of the left tibia\n(original)")
        plt.xlabel('Time (x10ms)')
    plt.plot(s)

    # Définition de la 3ème courbe.
    plt.subplot(243)
    plt.plot(v)
    if var_langue=="francais":
        plt.title("Muscle du soléaire droit\n(original)")
        plt.xlabel('Temps (x10ms)')
    else:
        plt.title("Muscle of the right soleus\n(original)")
        plt.xlabel('Time (x10ms)')


    # Définition de la 4ème courbe.
    plt.subplot(244)
    if var_langue=="francais":
        plt.title("Muscle du soléaire gauche\n(original)")
        plt.xlabel('Temps (x10ms)')
    else:
        plt.title("Muscle of the left soleus\n(original)")
        plt.xlabel('Time (x10ms)')
    plt.plot(g)

    # Définition de la 5ème courbe.
    plt.subplot(245)
    if var_langue=="francais":
        plt.title("(lissée)")
        plt.xlabel('Temps (x10ms)')
    else:
        plt.title("(smoothed)")
        plt.xlabel('Time (x10ms)')
    plt.plot(t)
    plt.plot(x, y)
    plt.ylabel('Hertz (Hz)')

    # Définition de la 6ème courbe.
    plt.subplot(246)
    if var_langue=="francais":
        plt.title("(lissée)")
        plt.xlabel('Temps (x10ms)')
    else:
        plt.title("(smoothed)")
        plt.xlabel('Time (x10ms)')
    plt.plot(s)
    plt.plot(dr, gc)

    # Définition de la 7ème courbe.
    plt.subplot(247)
    if var_langue=="francais":
        plt.title("(lissée)")
        plt.xlabel('Temps (x10ms)')
    else:
        plt.title("(smoothed)")
        plt.xlabel('Time (x10ms)')
    plt.plot(v)
    plt.plot(ht, bs)

    # Définition de la 8ème courbe.
    plt.subplot(248)
    if var_langue=="francais":
        plt.title("(lissée)")
        plt.xlabel('Temps (x10ms)')
    else:
        plt.title("(smoothed)")
        plt.xlabel('Time (x10ms)')
    plt.plot(g)
    plt.plot(no, su)

    #Fonction permettant d'afficher les figures (Le canvas uniquement, pas intégré dans une fenetre tkinter!)
    try:
        fig.show()
    except AttributeError:
        print(" ")




def changerCourbes(canvas, ax1, ax2, t, x, y, b1, b2, b3, b4, CL, CO, tem, her):

    ax1.cla()
    ax2.cla()
    ax1.set_title(CO)
    ax1.set_ylim(min(t), max(t))
    ax1.plot(t)
    ax2.set_ylim(min(t), max(t))
    ax2.plot(t)
    ax2.plot(x,y)
    ax2.set_title(CL)
    ax2.set_xlabel(tem)
    ax2.set_ylabel(her)
    ax1.set_ylabel(her)
    canvas.draw()

    b1["bg"] = "#9F9F9F"
    b2["bg"] = "#F0F0ED"
    b3["bg"] = "#F0F0ED"
    b4["bg"] = "#F0F0ED"


    