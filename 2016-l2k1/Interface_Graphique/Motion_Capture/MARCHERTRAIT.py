import numpy as np
import scipy.io as spio
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.animation as animation
import time
import math
import matplotlib
from pylab import plot, ginput, show, axis
from mpl_toolkits.mplot3d import Axes3D
from tkinter import *
import numpy as np
import scipy.io as spio
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
matplotlib.use("TkAgg")
from matplotlib.figure import Figure
from matplotlib.widgets import MultiCursor

def fonction3D(fenetreResultat,chemin,selection,lourd,leger):
    vou = []
    matfile = chemin
    matdata = spio.loadmat(matfile, squeeze_me=True)
    for i in range(1, len(matdata['Marker'].item()) + 1):
        i = str(i)
        if (len(i) == 1):
            i = '0' + i
        o = matdata['Marker']['Marker' + i].item()['value'].tolist()  # 21A24
        vou.append(o)
    print(matdata.keys())

    import tkinter as Tk
    # fig = Figure()
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    ax.set_xlabel('X Label')
    ax.set_ylabel('Y Label')
    ax.set_zlabel('Z Label')
    canvas = FigureCanvasTkAgg(fig, fenetreResultat)
    # canvas.show()

    canvas.get_tk_widget().place(relx=.80, rely=.53, anchor="center", height=500, width=600)
    canvas.get_tk_widget().config(relief="raised", bd=2)

    def numeros ():
        if len(leger)>0:
            for tu in leger:
                ax.text(vou[tu][i][0], vou[tu][i][1], vou[tu][i][2], '%s' % (str(tu)), size=20, zorder=1, color='k')
    if 1 in selection:
        def trace2(i):
            if not ( 1 in selection):
                ani.stop()
            if not (4 in selection):
                ax.cla()
            if i < 11610:
                xList = []
                yList = []
                zList = []
                # for qe in range (0,37) :##in (matdata['Marker'].item()):
                #   xList.append(v[qe][abo][0])
                #  yList.append(v[qe][abo][1])
                #  zList.append(v[qe][abo][2])
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
                    ax.plot_wireframe([vou[18][i][0], vou[19][i][0], vou[20][i][0], vou[21][i][0], vou[18][i][0]],
                                      [vou[18][i][1], vou[19][i][1], vou[20][i][1], vou[21][i][1], vou[18][i][1]],
                                      [vou[18][i][2], vou[19][i][2], vou[20][i][2], vou[21][i][2], vou[18][i][2]])
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
                                      [vou[21][i][1], (vou[26][i][1] + vou[28][i][1]) / 2, vou[19][i][1]],
                                      [vou[21][i][2], (vou[26][i][2] + vou[28][i][2]) / 2, vou[19][i][2]])
                if not (vou[34][i][0] == 0 or vou[35][i][0] == 0 or vou[36][i][0] == 0):
                    ax.plot_wireframe([vou[34][i][0], vou[35][i][0], vou[36][i][0], vou[34][i][0]],
                                      [vou[34][i][1], vou[35][i][1], vou[36][i][1], vou[34][i][1]],
                                      [vou[34][i][2], vou[35][i][2], vou[36][i][2], vou[34][i][2]])
                if not (vou[26][i][0] == 0 or vou[28][i][0] == 0 or vou[34][i][0] == 0 or vou[35][i][0] == 0 or vou[36][i][
                    0] == 0):
                    ax.plot_wireframe(
                        [(vou[26][i][0] + vou[28][i][0]) / 2, (vou[34][i][0] + vou[35][i][0] + vou[36][i][0]) / 3],
                        [(vou[26][i][1] + vou[28][i][1]) / 2, (vou[34][i][1] + vou[35][i][1] + vou[36][i][1]) / 3],
                        [(vou[26][i][2] + vou[28][i][2]) / 2, (vou[34][i][2] + vou[35][i][2] + vou[36][i][2]) / 3])

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
                    ax.plot_wireframe([vou[16][i][0], (vou[16][i][0] + vou[37][i][0] + vou[21][i][0]) / 3, vou[21][i][0]],
                                      [vou[16][i][1], (vou[16][i][1] + vou[37][i][1] + vou[21][i][1]) / 3, vou[21][i][1]],
                                      [vou[16][i][2], (vou[16][i][2] + vou[37][i][2] + vou[21][i][2]) / 3, vou[21][i][2]])
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
                    ax.plot_wireframe([vou[14][i][0], (vou[22][i][0] + vou[24][i][0]) / 2, vou[16][i][0]],
                                      [vou[14][i][1], (vou[22][i][1] + vou[24][i][1]) / 2, vou[16][i][1]],
                                      [vou[14][i][2], (vou[22][i][2] + vou[24][i][2]) / 2, vou[16][i][2]])
                if not (vou[30][i][0] == 0 or vou[31][i][0] == 0 or vou[32][i][0] == 0):
                    ax.plot_wireframe([vou[30][i][0], vou[31][i][0], vou[32][i][0], vou[30][i][0]],
                                      [vou[30][i][1], vou[31][i][1], vou[32][i][1], vou[30][i][1]],
                                      [vou[30][i][2], vou[31][i][2], vou[32][i][2], vou[30][i][2]])
                if not (vou[31][i][0] == 0 or vou[30][i][0] == 0 or vou[32][i][0] == 0 or vou[22][i][0] == 0 or vou[24][i][
                    0] == 0):
                    ax.plot_wireframe(
                        [(vou[31][i][0] + vou[30][i][0] + vou[32][i][0]) / 3, (vou[22][i][0] + vou[24][i][0]) / 2],
                        [(vou[31][i][1] + vou[30][i][1] + vou[32][i][1]) / 3, (vou[22][i][1] + vou[24][i][1]) / 2],
                        [(vou[31][i][2] + vou[30][i][2] + vou[32][i][2]) / 3, (vou[22][i][2] + vou[24][i][2]) / 2])
                    print("rio")
                print (i)
                numeros()

        def ho2():
            global ani
            ani = animation.FuncAnimation(fig, trace2, np.arange(1, 11610), interval=19, blit=False)
        ho2()
    if 2 in selection:

        def trace1(i):
            if not (2 in selection):
                ani.stop()
            if not(4 in selection):
                ax.cla()

            if (i < 11610):
                xList = []
                yList = []
                zList = []
                ax.cla()
                for qe in range(0, len(matdata['Marker'].item())):
                    xList.append(vou[qe][i][0])
                    yList.append(vou[qe][i][1])
                    zList.append(vou[qe][i][2])
                    # ax.text(v[qe][abo][0],v[qe][abo][1],v[qe][abo][2],'%s' % (str(qe)), size=20,zorder=1,color='k')

                ax.scatter(xList, yList, zList, c='b', marker='o', depthshade=True, picker=True)
                numeros()


        def ho1():
            global ani
            ani = animation.FuncAnimation(fig, trace1, np.arange(1, 11610), interval=19, blit=False)
        ho1()
    if 3 in selection :

        def trace(i):
            if not (3 in selection):
                ani.stop()
            if not (4 in selection):
                ax.cla()
            for lyi in range(0, len(lourd)):
                # items = l5.curselection()
                fr = lourd[lyi][0]
                en = lourd[lyi][1]
                # trait,=ax.plot([vou[fr][i][0],vou[en][i][0]],[vou[fr][i][1],vou[en][i][1]], [vou[fr][i][2],vou[en][i][2]])
                trait = ax.plot_wireframe([vou[fr][i][0], vou[en][i][0]], [vou[fr][i][1], vou[en][i][1]],
                                [vou[fr][i][2], vou[en][i][2]])
            # actualise(trait,i,fr,en,vou)

            print(i)
            numeros()

        def ho():
            global ani
            ani = animation.FuncAnimation(fig, trace, np.arange(1, 11610), interval=19, blit=False)
        ho()
        def trace3(i):
            if (not (1 in selection)) and (not(2 in selection)) and (not(3 in selection)):
                ani.stop()
            if not(4 in selection):
                ax.cla()
            if (i < 11610):
                numeros()
        def ho3():
            global ani
            ani = animation.FuncAnimation(fig, trace3, np.arange(1, 11610), interval=19, blit=False)
        ho3()


    '''canvas = FigureCanvasTkAgg(fig, fenetreResultat)
    # canvas.show()

    canvas.get_tk_widget().place(relx=.80, rely=.53, anchor="center", height=500, width=600)
    canvas.get_tk_widget().config(relief="raised", bd=2)'''

    # fig = plt.figure()
    # ani = animation.FuncAnimation(fig, animate, interval=1)
    print('rouli')
    # animate(i)
    # plt.show()
