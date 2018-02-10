import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.animation as animation
import time
import math
import matplotlib
from pylab import plot, ginput, show, axis
from tkinter import *
import numpy as np
import scipy.io as spio
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
matplotlib.use("TkAgg")
from matplotlib.figure import Figure
from matplotlib.widgets import MultiCursor

def fonctionOption3D(chemin):
    global oui
    oui = []
    global bok
    bok=55

    lourd=[]
    leger=[]

    matfile = chemin
    matdata = spio.loadmat(matfile, squeeze_me=True)
    vou = []
    for i in range(1, len(matdata['Marker'].item()) + 1):
        i = str(i)
        if (len(i) == 1):
            i = '0' + i
        o = matdata['Marker']['Marker' + i].item()['value'].tolist()  # 21A24
        vou.append(o)
    print(matdata.keys())


    import tkinter as Tk
    #fig = Figure()
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    ax.set_xlabel('X Label')
    ax.set_ylabel('Y Label')
    ax.set_zlabel('Z Label')


    root = Tk.Tk()
    '''def animate(i):
        #matplotlib.pyplot.ion()
        print('hello')
        global bok
        bok += 100
        fr = l5.curselection()[0]
        en = l5.curselection()[1]


        #plt._auto_draw_if_interactive(fig,ax)
        #plt.draw()


        #ani = animation.FuncAnimation(fig, animate, interval=1)'''
    """f1 = Tk.Frame(root)
    s1 = Tk.Scrollbar(f1)
    l1 = Tk.Listbox(f1)
    for i in range(40): l1.insert(i,'Marqueur '+str(i))
    s1.config(command = l1.yview)
    l1.config(yscrollcommand = s1.set)
    l1.pack(side = Tk.LEFT, fill = Tk.Y)
    s1.pack(side = Tk.RIGHT, fill = Tk.Y)
    f1.pack()
    f2 = Tk.Frame(root)
    s2 = Tk.Scrollbar(f2)
    l2 = Tk.Listbox(f2)
    def clic(evt):
        i=l1.curselection()## Récupération de l'index de l'élément sélectionné
        print(i)
        return print(l1.get(i))  ## On retourne l'élément (un string) sélectionné
    l1.bind('<ButtonRelease-1>',clic)  ## on associe l'évènement "relachement du bouton gauche la souris" à la listbox
    f2 = Tk.Frame(root)
    s2 = Tk.Scrollbar(f2)
    l2 = Tk.Listbox(f2)
    for i in range(40): l2.insert(i,'Marqueur '+str(i))
    s2.config(command = l2.yview)
    l2.config(yscrollcommand = s2.set)
    l2.pack(side = Tk.LEFT, fill = Tk.Y)
    s2.pack(side = Tk.RIGHT, fill = Tk.Y)
    f2.pack()
    def clic2(evt):
        i=l2.curselection()## Récupération de l'index de l'élément sélectionné
        print(i)
        return print(l2.get(i))  ## On retourne l'élément (un string) sélectionné
    l2.bind('<ButtonRelease-1>',clic2)"""  ## on associe l'évènement "relachement du bouton gauche la souris" à la listbox
    f3 = Tk.Frame(root)
    s3 = Tk.Scrollbar(f3)
    l3 = Tk.Listbox(f3,selectmode = Tk.MULTIPLE, exportselection=0) #EXTENDED
    f5 = Tk.Frame(root)
    l5 = Tk.Listbox(f5,selectmode = Tk.MULTIPLE, exportselection=0) #EXTENDED
    l3.insert(0,'DESELECTIONNER')

    def actualise(trait,i,fr,en,vou):
        trait.set_xdata([vou[fr][i][0],vou[en][i][0]])
        trait.set_ydata([vou[fr][i][1],vou[en][i][1]])
        trait.set_zdata([vou[fr][bok+i][2],vou[en][bok+i][2]])
        print('salut')
        return trait,
    def trace(i):
        if not (5 in l4.curselection()):
            ax.cla()
        print('comment')
        global lourd
        print(lourd)
        print('oui  oui    oui')
        print(len(lourd))
        for lyi in range (0,len(lourd)):
            print('hvdejhbcjjehvcjzhrbvjhrbvjzebcbjverbcjerbvjhebvzr')
            #items = l5.curselection()
            fr=lourd[lyi][0]
            en=lourd[lyi][1]
            #trait,=ax.plot([vou[fr][i][0],vou[en][i][0]],[vou[fr][i][1],vou[en][i][1]], [vou[fr][i][2],vou[en][i][2]])
            trait=ax.plot([vou[fr][i][0],vou[en][i][0]],[vou[fr][i][1],vou[en][i][1]], [vou[fr][i][2],vou[en][i][2]])
        #actualise(trait,i,fr,en,vou)
        if len(l3.curselection()) > 0:
            for tu in l3.curselection():
                ax.text(vou[tu][i][0], vou[tu][i][1], vou[tu][i][2], '%s' % (str(tu)), size=20, zorder=1, color='k')
        print(i)
    def ho():
        global ani
        ani = animation.FuncAnimation(fig, trace, np.arange(1, 200), interval=19, blit=False)
    def trace1(i):
        if not (5 in l4.curselection()):
            ax.cla()

        print('comment')
        global lourd
        print(lourd)
        print('oui  oui    oui')
        print(len(lourd))
        if (i < 11610) and 2 in l4.curselection():
            xList = []
            yList = []
            zList = []
            ax.cla()
            for qe in range(0, len(matdata['Marker'].item())):
                xList.append(vou[qe][i][0])
                yList.append(vou[qe][i][1])
                zList.append(vou[qe][i][2])
                # ax.text(v[qe][abo][0],v[qe][abo][1],v[qe][abo][2],'%s' % (str(qe)), size=20,zorder=1,color='k')
            if len(l3.curselection())>0:
                for tu in l3.curselection():
                    ax.text(vou[tu][i][0], vou[tu][i][1], vou[tu][i][2], '%s' % (str(tu)), size=20, zorder=1, color='k')

            ax.scatter(xList, yList, zList, c='b', marker='o', depthshade=True, picker=True)
        #actualise(trait,i,fr,en,vou)
        print(i)
    def ho1():
        global bni
        bni = animation.FuncAnimation(fig, trace1, np.arange(1, 200), interval=19, blit=False)
    def trace2(i):
        ax.cla()
        print('comment')
        global lourd
        print(lourd)
        print('oui  oui    oui')
        print(len(lourd))
        if i < 11610 and 1 in l4.curselection() :
            xList = []
            yList = []
            zList = []
            # for qe in range (0,37) :##in (matdata['Marker'].item()):
            #   xList.append(v[qe][abo][0])
            #  yList.append(v[qe][abo][1])
            #  zList.append(v[qe][abo][2])
            if not(5 in l4.curselection()):
                ax.cla()
            if len(l3.curselection())>0:
                for tu in l3.curselection():
                    ax.text(vou[tu][i][0], vou[tu][i][1], vou[tu][i][2], '%s' % (str(tu)), size=20, zorder=1, color='k')
            if not (vou[0][i][0] == 0 or vou[3][i][0] == 0 or vou[1][i][0] == 0 or vou[2][i][0] == 0):
                ax.plot_wireframe([vou[0][i][0], vou[1][i][0], vou[3][i][0], vou[2][i][0], vou[0][i][0]],
                              [vou[0][i][1], vou[1][i][1], vou[3][i][1], vou[2][i][1], vou[0][i][1]],
                              [vou[0][i][2], vou[1][i][2], vou[3][i][2], vou[2][i][2], vou[0][i][2]])
            if not (vou[0][i][0] == 0 or vou[3][i][0] == 0):
                ax.plot_wireframe([vou[0][i][0], vou[3][i][0]],
                              [vou[0][i][1], vou[3][i][1]],
                              [vou[0][i][2], vou[3][i][2]])
            if not (vou[1][i][0] == 0 or vou[2][i][0] == 0):
                ax.plot_wireframe([vou[1][i][0], vou[2][i][0]],
                              [vou[1][i][1], vou[2][i][1]],
                              [vou[1][i][2], vou[2][i][2]])

            if not (vou[3][i][0] == 0 or vou[37][i][0] == 0 or vou[4][i][0] == 0 or vou[5][i][0] == 0):
                ax.plot_wireframe([vou[3][i][0], vou[4][i][0], vou[37][i][0], vou[5][i][0], vou[3][i][0]],
                              [vou[3][i][1], vou[4][i][1], vou[37][i][1], vou[5][i][1], vou[3][i][1]],
                              [vou[3][i][2], vou[4][i][2], vou[37][i][2], vou[5][i][2], vou[3][i][2]])
            if not (vou[3][i][0] == 0 or vou[37][i][0] == 0):
                ax.plot_wireframe([vou[3][i][0], vou[37][i][0]],
                              [vou[3][i][1], vou[37][i][1]],
                              [vou[3][i][2], vou[37][i][2]])
            if not (vou[4][i][0] == 0 or vou[3][i][0] == 0 or vou[37][i][0] == 0 or vou[5][i][0] == 0):
                ax.plot_wireframe([vou[4][i][0], (vou[3][i][0] + vou[37][i][0]) / 2, vou[5][i][0]],
                              [vou[4][i][1], (vou[3][i][1] + vou[37][i][1]) / 2, vou[5][i][1]],
                              [vou[4][i][2], (vou[3][i][2] + vou[37][i][2]) / 2, vou[5][i][2]])
            if not (vou[6][i][0] == 0 or vou[8][i][0] == 0 or vou[4][i][0] == 0):
                ax.plot_wireframe([vou[4][i][0], (vou[6][i][0] + vou[8][i][0]) / 2],
                              [vou[4][i][1], (vou[6][i][1] + vou[8][i][1]) / 2],
                              [vou[4][i][2], (vou[6][i][2] + vou[8][i][2]) / 2])

            if not (vou[6][i][0] == 0 or vou[8][i][0] == 0 or vou[7][i][0] == 0 or vou[9][i][0] == 0):
                ax.plot_wireframe([vou[6][i][0], vou[7][i][0], vou[8][i][0], vou[9][i][0], vou[6][i][0]],
                              [vou[6][i][1], vou[7][i][1], vou[8][i][1], vou[9][i][1], vou[6][i][1]],
                              [vou[6][i][2], vou[7][i][2], vou[8][i][2], vou[9][i][2], vou[6][i][2]])
            if not (vou[6][i][0] == 0 or vou[8][i][0] == 0):
                ax.plot_wireframe([vou[6][i][0], vou[8][i][0]],
                              [vou[6][i][1], vou[8][i][1]],
                              [vou[6][i][2], vou[8][i][2]])
            if not (vou[7][i][0] == 0 or vou[9][i][0] == 0):
                ax.plot_wireframe([vou[7][i][0], vou[9][i][0]],
                              [vou[7][i][1], vou[9][i][1]],
                              [vou[7][i][2], vou[9][i][2]])
            if not (vou[5][i][0] == 0 or vou[10][i][0] == 0 or vou[12][i][0] == 0):
                ax.plot_wireframe([vou[5][i][0], (vou[10][i][0] + vou[12][i][0]) / 2],
                              [vou[5][i][1], (vou[10][i][1] + vou[12][i][1]) / 2],
                              [vou[5][i][2], (vou[10][i][2] + vou[12][i][2]) / 2])
            if not (vou[10][i][0] == 0 or vou[11][i][0] == 0 or vou[12][i][0] == 0 or vou[13][i][0] == 0):
                ax.plot_wireframe([vou[10][i][0], vou[11][i][0], vou[12][i][0], vou[13][i][0], vou[10][i][0]],
                              [vou[10][i][1], vou[11][i][1], vou[12][i][1], vou[13][i][1], vou[10][i][1]],
                              [vou[10][i][2], vou[11][i][2], vou[12][i][2], vou[13][i][2], vou[10][i][2]])
            if not (vou[10][i][0] == 0 or vou[12][i][0] == 0):
                ax.plot_wireframe([vou[10][i][0], vou[12][i][0]],
                              [vou[10][i][1], vou[12][i][1]],
                              [vou[10][i][2], vou[12][i][2]])
            if not (vou[11][i][0] == 0 or vou[13][i][0] == 0):
                ax.plot_wireframe([vou[11][i][0], vou[13][i][0]],
                              [vou[11][i][1], vou[13][i][1]],
                              [vou[11][i][2], vou[13][i][2]])

            if not (vou[18][i][0] == 0 or vou[20][i][0] == 0 or vou[21][i][0] == 0):
                ax.plot_wireframe([vou[18][i][0], vou[19][i][0], vou[20][i][0], vou[21][i][0],vou[18][i][0]],
                              [vou[18][i][1], vou[19][i][1], vou[20][i][1], vou[21][i][1],vou[18][i][1]],
                              [vou[18][i][2], vou[19][i][2], vou[20][i][2], vou[21][i][2],vou[18][i][2]])
            if not (vou[18][i][0] == 0 or vou[20][i][0] == 0):
                ax.plot_wireframe([vou[18][i][0], vou[20][i][0]],
                              [vou[18][i][1], vou[20][i][1]],
                              [vou[18][i][2], vou[20][i][2]])
            if not (vou[19][i][0] == 0 or vou[21][i][0] == 0):
                ax.plot_wireframe([vou[19][i][0], vou[21][i][0]],
                              [vou[19][i][1], vou[21][i][1]],
                              [vou[19][i][2], vou[21][i][2]])

            if not (vou[26][i][0] == 0 or vou[27][i][0] == 0 or vou[28][i][0] == 0 or vou[29][i][0] == 0):
                ax.plot_wireframe([vou[26][i][0], vou[27][i][0], vou[28][i][0], vou[29][i][0], vou[26][i][0]],
                              [vou[26][i][1], vou[27][i][1], vou[28][i][1], vou[29][i][1], vou[26][i][1]],
                              [vou[26][i][2], vou[27][i][2], vou[28][i][2], vou[29][i][2], vou[26][i][2]])
            if not (vou[26][i][0] == 0 or vou[28][i][0] == 0):
                ax.plot_wireframe([vou[26][i][0], vou[28][i][0]],
                              [vou[26][i][1], vou[28][i][1]],
                              [vou[26][i][2], vou[28][i][2]])
            if not (vou[27][i][0] == 0 or vou[29][i][0] == 0):
                ax.plot_wireframe([vou[27][i][0], vou[29][i][0]],
                              [vou[27][i][1], vou[29][i][1]],
                              [vou[27][i][2], vou[29][i][2]])
            if not (vou[21][i][0] == 0 or vou[26][i][0] == 0 or vou[28][i][0] == 0 or vou[19][i][0] == 0):
                ax.plot_wireframe([vou[21][i][0], (vou[26][i][0] + vou[28][i][0]) / 2, vou[19][i][0]],
                              [vou[21][i][1],(vou[26][i][1] + vou[28][i][1]) / 2, vou[19][i][1]],
                              [vou[21][i][2],(vou[26][i][2] + vou[28][i][2]) / 2, vou[19][i][2]])
            if not (vou[34][i][0] == 0 or vou[35][i][0] == 0 or vou[36][i][0] == 0):
                ax.plot_wireframe([vou[34][i][0], vou[35][i][0], vou[36][i][0], vou[34][i][0]],
                              [vou[34][i][1], vou[35][i][1], vou[36][i][1], vou[34][i][1]],
                              [vou[34][i][2], vou[35][i][2], vou[36][i][2], vou[34][i][2]])
            if not (vou[26][i][0] == 0 or vou[28][i][0] == 0 or vou[34][i][0] == 0 or vou[35][i][0] == 0 or vou[36][i][0] == 0):
                ax.plot_wireframe([(vou[26][i][0] + vou[28][i][0]) / 2, (vou[34][i][0]+ vou[35][i][0]+ vou[36][i][0])/3],
                              [(vou[26][i][1] + vou[28][i][1]) / 2, (vou[34][i][1]+ vou[35][i][1]+ vou[36][i][1])/3],
                              [(vou[26][i][2] + vou[28][i][2]) / 2, (vou[34][i][2]+ vou[35][i][2]+ vou[36][i][2])/3])

            if not (vou[14][i][0] == 0 or vou[15][i][0] == 0 or vou[16][i][0] == 0 or vou[17][i][0] == 0):
                ax.plot_wireframe([vou[14][i][0], vou[15][i][0], vou[16][i][0], vou[17][i][0], vou[14][i][0]],
                              [vou[14][i][1], vou[15][i][1], vou[16][i][1], vou[17][i][1], vou[14][i][1]],
                              [vou[14][i][2], vou[15][i][2], vou[16][i][2], vou[17][i][2], vou[14][i][2]])
            if not (vou[14][i][0] == 0 or vou[16][i][0] == 0):
                ax.plot_wireframe([vou[14][i][0], vou[16][i][0]],
                              [vou[14][i][1], vou[16][i][1]],
                              [vou[14][i][2], vou[16][i][2]])
            if not (vou[15][i][0] == 0 or vou[17][i][0] == 0):
                ax.plot_wireframe([vou[15][i][0], vou[17][i][0]],
                              [vou[15][i][1], vou[17][i][1]],
                              [vou[15][i][2], vou[17][i][2]])
            if not (vou[14][i][0] == 0 or vou[37][i][0] == 0 or vou[19][i][0] == 0):
                ax.plot_wireframe([vou[14][i][0], vou[37][i][0], vou[19][i][0]],
                              [vou[14][i][1], vou[37][i][1], vou[19][i][1]],
                              [vou[14][i][2], vou[37][i][2], vou[19][i][2]])
            if not (vou[16][i][0] == 0 or vou[37][i][0] == 0 or vou[21][i][0] == 0):
                ax.plot_wireframe([vou[16][i][0],(vou[16][i][0] + vou[37][i][0] + vou[21][i][0])/3, vou[21][i][0]],
                              [vou[16][i][1],(vou[16][i][1] + vou[37][i][1] + vou[21][i][1])/3, vou[21][i][1]],
                              [vou[16][i][2],(vou[16][i][2] + vou[37][i][2] + vou[21][i][2])/3, vou[21][i][2]])
            if not (vou[22][i][0] == 0 or vou[23][i][0] == 0 or vou[24][i][0] == 0 or vou[25][i][0] == 0):
                ax.plot_wireframe([vou[22][i][0], vou[23][i][0], vou[24][i][0], vou[25][i][0], vou[22][i][0]],
                              [vou[22][i][1], vou[23][i][1], vou[24][i][1], vou[25][i][1], vou[22][i][1]],
                              [vou[22][i][2], vou[23][i][2], vou[24][i][2], vou[25][i][2], vou[22][i][2]])
            if not (vou[22][i][0] == 0 or vou[24][i][0] == 0):
                ax.plot_wireframe([vou[22][i][0], vou[24][i][0]],
                              [vou[22][i][1], vou[24][i][1]],
                              [vou[22][i][2], vou[24][i][2]])
            if not (vou[23][i][0] == 0 or vou[25][i][0] == 0):
                ax.plot_wireframe([vou[23][i][0], vou[25][i][0]],
                              [vou[23][i][1], vou[25][i][1]],
                              [vou[23][i][2], vou[25][i][2]])
            if not (vou[14][i][0] == 0 or vou[22][i][0] == 0 or vou[24][i][0] == 0 or vou[16][i][0] == 0):
                ax.plot_wireframe([vou[14][i][0], (vou[22][i][0] + vou[24][i][0]) / 2,vou[16][i][0]],
                              [vou[14][i][1], (vou[22][i][1] + vou[24][i][1]) / 2,vou[16][i][1]],
                              [vou[14][i][2], (vou[22][i][2] + vou[24][i][2]) / 2,vou[16][i][2]])
            if not (vou[30][i][0] == 0 or vou[31][i][0] == 0 or vou[32][i][0] == 0 ):
                ax.plot_wireframe([vou[30][i][0], vou[31][i][0], vou[32][i][0],  vou[30][i][0]],
                              [vou[30][i][1], vou[31][i][1], vou[32][i][1],  vou[30][i][1]],
                              [vou[30][i][2], vou[31][i][2], vou[32][i][2],  vou[30][i][2]])
            if not (vou[31][i][0]==0 or vou[30][i][0]==0 or vou[32][i][0]==0 or vou[22][i][0]==0 or vou[24][i][0]==0):

                ax.plot_wireframe([(vou[31][i][0]+vou[30][i][0]+ vou[32][i][0])/3, (vou[22][i][0] + vou[24][i][0]) / 2],
                                [(vou[31][i][1]+vou[30][i][1]+ vou[32][i][1])/3, (vou[22][i][1] + vou[24][i][1]) / 2],
                                [(vou[31][i][2]+vou[30][i][2]+ vou[32][i][2])/3, (vou[22][i][2] + vou[24][i][2]) / 2])
    def ho2():
        global ani
        ani = animation.FuncAnimation(fig, trace2, np.arange(1, 200), interval=19, blit=False)
    for i in range(1,40): l3.insert(i,'Marqueur '+str(i))
    s3.config(command = l3.yview)
    l3.config(yscrollcommand = s3.set)
    l3.pack(side = Tk.LEFT, fill = Tk.Y)
    s3.pack(side = Tk.RIGHT, fill = Tk.Y)
    f3.pack()
    def clic3(evt):
        items = l3.curselection()
        if 0 in items :
            l3.selection_clear(0, 40)
        global leger
        print (leger)
        leger=l3.curselection()
        return print(items)  ## On retourne l'élément (un string) sélectionné
    def clicd3(evt):
        print(evt.y)#recupere la coordonée selon y
        print(l3.nearest(evt.y))#reecupere le bouton le plus proche
        print(evt)
        fr=l3.nearest(evt.y)
        #vou[fr][i][0]
        #s1 = [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

        s2 = []
        s1 = []
        t=[]
        fig = plt.figure()
        ax1 = fig.add_subplot(211)
        ax2 = fig.add_subplot(212, sharex=ax1)
        for i in range(len(vou[fr]) - 11550):
            s1.append(vou[fr][i][0])
            s2.append((vou[fr][i+1][0] -vou[fr][i][0] )/15)
            t.append(i)
            print('att')
            ax1.plot(t, s1)
            #ax2.plot(t, s2)
            if i==11550:
                del s1[i]
        ax2.plot(t, s2)
        #t=np.arange(59)
        print (t)
        print (s1)
        #t = range(i+1)
        print('bientot')



        #ax2 = fig.add_subplot(212, sharex=ax1)
        #ax2.plot(t, s2)

        multi = MultiCursor(fig.canvas, (ax1, ax2), color='r', lw=1)
        plt.show()
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


    l3.bind('<ButtonRelease-1>',clic3)  ## on associe l'évènement "relachement du bouton gauche la souris" à la listbox
    l3.bind('<Double-Button-1>',clicd3)
    f4 = Tk.Frame(root)
    s4 = Tk.Scrollbar(f4)
    l4 = Tk.Listbox(f4,selectmode = Tk.MULTIPLE, exportselection=0)#EXTENDED
    l4.insert(0,'DESELECTIONNER')
    l4.insert(1,'TRAITS')
    l4.insert(2,'POINTS')
    l4.insert(3,'RELIER')
    l4.insert(4,'   effacer tout les traits relier')
    l4.insert(5,'HISTORIQUE')
    s4.config(command = l3.yview)
    l4.config(yscrollcommand = s4.set)
    l4.pack(side = Tk.LEFT, fill = Tk.Y)
    s4.pack(side = Tk.RIGHT, fill = Tk.Y)
    f4.pack()
    def clic4(evt):
        items = l4.curselection()
        if 0 in items :
            l4.selection_clear(0, 4)
        if 1 in items :
            l4.selection_clear(3)
            # animate(i)

            # fig = plt.figure()
            # fig.tight_layout()
            canvas = FigureCanvasTkAgg(fig, master=root)
            # canvas.show()

            canvas.get_tk_widget().pack(side=Tk.TOP, fill=Tk.BOTH, expand=1)
            # canvas.get_tk_widget().grid(column=0, row=1)
            print('okokok')
            # fig.canvas.draw()
            # canvas.after(50, animate(fig,i))
            # canvas.show()
            # ax.mouse_init()
            # ani=animation.FuncAnimation(fig, trace, np.arange(1, 200), interval=25, blit=False)
            # plt.show()

            ho2()
        if 2 in items :
            # animate(i)

            # fig = plt.figure()
            # fig.tight_layout()
            canvas = FigureCanvasTkAgg(fig, master=root)
            # canvas.show()

            canvas.get_tk_widget().pack(side=Tk.TOP, fill=Tk.BOTH, expand=1)
            # canvas.get_tk_widget().grid(column=0, row=1)
            print('okokok')
            # fig.canvas.draw()
            # canvas.after(50, animate(fig,i))
            # canvas.show()
            # ax.mouse_init()
            # ani=animation.FuncAnimation(fig, trace, np.arange(1, 200), interval=25, blit=False)
            # plt.show()

            ho1()
        if 3 in items :
            l4.selection_clear(1)
            #animate(i)

            #fig = plt.figure()
            #fig.tight_layout()
            canvas = FigureCanvasTkAgg(fig, master=root)
            #canvas.show()

            canvas.get_tk_widget().pack(side=Tk.TOP, fill=Tk.BOTH, expand=1)
            #canvas.get_tk_widget().grid(column=0, row=1)
            print('okokok')
            #fig.canvas.draw()
            #canvas.after(50, animate(fig,i))
            #canvas.show()
            #ax.mouse_init()
            #ani=animation.FuncAnimation(fig, trace, np.arange(1, 200), interval=25, blit=False)
            #plt.show()


            ho()
        if (3 in items)==False :
            l4.selection_clear(4)
        if 4 in items:
            global lourd
            lourd=[]
        return print(items)  ## On retourne l'élément (un string) sélectionné
    l4.bind('<ButtonRelease-1>',clic4)  ## on associe l'évènement "relachement du bouton gauche la souris" à la listbox

    s5 = Tk.Scrollbar(f5)

    l5.insert(0,'DESELECTIONNER')
    for i in range(1,40): l5.insert(i,'Marqueur '+str(i))
    s5.config(command = l5.yview)
    l5.config(yscrollcommand = s5.set)
    l5.pack(side = Tk.LEFT, fill = Tk.Y)
    s5.pack(side = Tk.RIGHT, fill = Tk.Y)
    f5.pack()
    def clic5(evt):
        itemos = l5.curselection()
        if len(itemos)>2:
            l5.selection_clear(itemos[0])
            print(len(itemos))
        if len(itemos)== 2:
            global lourd
            lourd.append(l5.curselection())
        if 0 in itemos :
            l5.selection_clear(0, 40)
        return print(itemos)  ## On retourne l'élément (un string) sélectionné
    l5.bind('<ButtonRelease-1>',clic5)  ## on associe l'évènement "relachement du bouton gauche la souris" à la listbox


    root.mainloop()
    #fig = plt.figure()
    #ani = animation.FuncAnimation(fig, animate, interval=1)
    print('rouli')
    #animate(i)
    #plt.show()

