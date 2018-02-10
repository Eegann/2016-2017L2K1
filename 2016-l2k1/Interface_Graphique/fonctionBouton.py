from tkinter import *
from tkinter import font
from tkinter import filedialog
from fonctionSup import *
import pickle

FichierCoda=""
FichierEye=""
FichierVideo=""

# On définit les 3 pages correspondant aux 3 boutons "Codamotion", "New" et "Eye-tracking".
# Les codes sont similaires et ont la même utilité dans les 3 fonctions suivantes.

def goNew():

    global FichierCoda
    global FichierEye
    global FichierVideo


    # Saisie de la langue actuelle.
    with open('Ressources/data/langue','rb') as langue:
        langue_depickler=pickle.Unpickler(langue)
        var_langue=langue_depickler.load()

    # Création de la fenetre
    fenetreNew=Toplevel()
    fenetreNew.geometry("600x500")
    fenetreNew.config(bg="#DCDCDC")
    fenetreNew.minsize(width=600, height=500)


    if var_langue=="francais":
        fenetreNew.title("Nouveau")
    else:
        fenetreNew.title("New")
    fenetreNew.grab_set()
    centrefenetre(fenetreNew)

    police_titre = font.Font(fenetreNew, size=18, weight='bold', family='Helvectica')  # Définition de la police d'affichage du titre.
    police_texte = font.Font(fenetreNew, size=12, family='Helvectica')  # Définition de la police affichage du texte.

    labelTitreNew = Label(fenetreNew, text="Choisissez les fichiers", fg="#FFFFFF", bg="#FF3D03", font=police_titre)
    labelTitreNew.place(relx=.50, rely=0, anchor="n", height="60", width="800")

    # Création des labels demandant les fichiers.
    labelCoda = Label(fenetreNew, text="Fichier Codamotion :", bg="#DCDCDC", font=police_texte)
    labelCoda.place(relx=.35, rely=.20, anchor="center", height="30", width="150")

    labelEye = Label(fenetreNew, text="Fichier Eye-tracking :", bg="#DCDCDC", font=police_texte)
    labelEye.place(relx=.35, rely=.45, anchor="center", height="30", width="150")

    labelVideo = Label(fenetreNew, text="Fichier vidéo :", bg="#DCDCDC", font=police_texte)
    labelVideo.place(relx=.35, rely=.70, anchor="center", height="30", width="150")

    # Création des boutons pour chercher les fichiers
    boutonCoda=Button(fenetreNew, text="Browse...", command=lambda :fichierCoda(labelNomCoda2), font=police_texte)
    boutonCoda.place(relx=.65, rely=.20, anchor="center", height="30", width="100")
    boutonCoda.config(highlightbackground="#DCDCDC")

    boutonEye=Button(fenetreNew, text="Browse...", command=lambda :fichierEye(labelNomEye2), font=police_texte)
    boutonEye.place(relx=.65, rely=.45, anchor="center", height="30", width="100")
    boutonEye.config(highlightbackground="#DCDCDC")

    boutonVideo=Button(fenetreNew, text="Browse...", command=lambda :fichierVideo(labelNomVideo2), font=police_texte)
    boutonVideo.place(relx=.65, rely=.70, anchor="center", height="30", width="100")
    boutonVideo.config(highlightbackground="#DCDCDC")

    # Création des emplacements ou seront mis les emplacement des fichiers.
    labelNomCoda1 = Label(fenetreNew, text="Chemin d'accès :", bg="#DCDCDC", font=police_texte)
    labelNomCoda1.place(relx=.15, rely=.30, anchor="center")

    labelNomCoda2 = Text(fenetreNew, wrap=NONE)
    labelNomCoda2.place(relx=.60, rely=.30, anchor="center", height="30", width="400")

    labelNomEye1 = Label(fenetreNew, text="Chemin d'accès :", bg="#DCDCDC", font=police_texte)
    labelNomEye1.place(relx=.15, rely=.55, anchor="center")

    labelNomEye2 = Text(fenetreNew, wrap=NONE)
    labelNomEye2.place(relx=.60, rely=.55, anchor="center", height="30", width="400")

    labelNomVideo1 = Label(fenetreNew, text="Chemin d'accès :", bg="#DCDCDC", font=police_texte)
    labelNomVideo1.place(relx=.15, rely=.80, anchor="center")

    labelNomVideo2 = Text(fenetreNew, wrap=NONE)
    labelNomVideo2.place(relx=.60, rely=.80, anchor="center", height="30", width="400")

    # Bouton permettant de lancer le traitement des données. En cours de réalisation.
    boutonValiderEye=Button(fenetreNew, text="Confirmer", font=police_texte, command=lambda : fonctionIntermediaireNew(FichierEye,FichierCoda,FichierVideo,var_langue,fenetreNew))
    boutonValiderEye.place(relx=.80, rely=.95, anchor="center", height="30", width="100")
    boutonValiderEye.config(highlightbackground="#DCDCDC")


    # Traduction des labels et des boutons
    if var_langue=="anglais":
        labelCoda["text"]="Codamotion file :"
        labelEye["text"]="Eye-tracking file :"
        labelVideo["text"]="Video file :"
        labelNomCoda1["text"]="File path :\n"
        labelNomEye1["text"]="File path :\n"
        labelNomVideo1["text"]="File path :\n"
        labelTitreNew["text"] = "Select files"
        boutonValiderEye["text"] ="Confirm"



def goCoda():

    global FichierCoda

    with open('Ressources/data/langue','rb') as langue:
        langue_depickler=pickle.Unpickler(langue)
        var_langue=langue_depickler.load()

    fenetreCoda = Toplevel()
    fenetreCoda.geometry("600x220")
    fenetreCoda.config(bg="#DCDCDC")
    fenetreCoda.minsize(width=600, height=220)
    fenetreCoda.title("Nouveau Codamotion")
    fenetreCoda.grab_set()

    centrefenetre(fenetreCoda)

    police_titre = font.Font(fenetreCoda, size=18, weight='bold', family='Helvectica')  # Définition de la police d'affichage du titre.
    police_texte = font.Font(fenetreCoda, size=12, family='Helvectica')  # Définition de la police affichage du texte.

    labelTitreCoda = Label(fenetreCoda, text="Choisissez les fichiers", fg="#FFFFFF", bg="#FF3D03", font=police_titre)
    labelTitreCoda.place(relx=.50, rely=0, anchor="n", height="60", width="800")

    labelCoda = Label(fenetreCoda, text="Fichier Codamotion :", bg="#DCDCDC", font=police_texte)
    labelCoda.place(relx=.35, rely=.40, anchor="center", height="30", width="150")

    boutonCoda = Button(fenetreCoda, text="Browse...", command=lambda: fichierCoda(labelNomCoda2), font=police_texte)
    boutonCoda.place(relx=.65, rely=.40, anchor="center", height="30", width="100")
    boutonCoda.config(highlightbackground="#DCDCDC")

    labelNomCoda1 = Label(fenetreCoda, text="Chemin d'accès :", bg="#DCDCDC", font=police_texte)
    labelNomCoda1.place(relx=.15, rely=.65, anchor="center")

    labelNomCoda2 = Text(fenetreCoda, wrap=NONE)
    labelNomCoda2.place(relx=.60, rely=.65, anchor="center", height="30", width="400")

    boutonValider = Button(fenetreCoda, text="Valider", font=police_texte, command=lambda: fonctionIntermediaireCoda(FichierCoda, var_langue, fenetreCoda))
    boutonValider.place(relx=.80, rely=.90, anchor="center", height="30", width="100")
    boutonValider.config(highlightbackground="#DCDCDC")

    if var_langue=="anglais":
        labelCoda["text"]="Codamotion file :"
        labelNomCoda1["text"] = "File path :\n"
        labelTitreCoda["text"]="Select files"
        boutonValider["text"] = "Validate"

def goEye():

    global FichierEye
    global FichierVideo

    with open('Ressources/data/langue','rb') as langue:
        langue_depickler=pickle.Unpickler(langue)
        var_langue=langue_depickler.load()

    fenetreEye = Toplevel()
    fenetreEye.geometry("600x400")
    fenetreEye.minsize(width=600, height=400)
    fenetreEye.maxsize(width=600, height=400)
    fenetreEye.config(bg="#DCDCDC")
    fenetreEye.title("Nouveau")
    fenetreEye.grab_set()

    centrefenetre(fenetreEye)

    police_titre = font.Font(fenetreEye, size=18, weight='bold', family='Helvectica')  # Définition de la police d'affichage du titre.
    police_texte = font.Font(fenetreEye, size=12, family='Helvectica')  # Définition de la police affichage du texte.

    labelTitreEye = Label(fenetreEye, text="Choisissez les fichiers", fg="#FFFFFF", bg="#FF3D03", font=police_titre)
    labelTitreEye.place(relx=.50, rely=0, anchor="n", height="60", width="800")

    labelEye = Label(fenetreEye, text="Fichier Eye-tracking :", bg="#DCDCDC", font=police_texte)
    labelEye.place(relx=.35, rely=.25, anchor="center", height="30", width="150")

    labelVideo = Label(fenetreEye, text="Fichier vidéo :", bg="#DCDCDC", font=police_texte)
    labelVideo.place(relx=.35, rely=.60, anchor="center", height="30", width="150")

    boutonEye = Button(fenetreEye, text="Browse...", command=lambda: fichierEye(labelNomEye2), font=police_texte)
    boutonEye.place(relx=.65, rely=.25, anchor="center", height="30", width="100")
    boutonEye.config(highlightbackground="#DCDCDC")

    boutonVideo = Button(fenetreEye, text="Browse...", command=lambda: fichierVideo(labelNomVideo2), font=police_texte)
    boutonVideo.place(relx=.65, rely=.60, anchor="center", height="30", width="100")
    boutonVideo.config(highlightbackground="#DCDCDC")

    labelNomEye1 = Label(fenetreEye, text="Chemin d'accès :", bg="#DCDCDC", font=police_texte)
    labelNomEye1.place(relx=.15, rely=.40, anchor="center")

    labelNomEye2 = Text(fenetreEye, wrap=NONE)
    labelNomEye2.place(relx=.60, rely=.40, anchor="center", height="30", width="400")

    labelNomVideo1 = Label(fenetreEye, text="Chemin d'accès :", bg="#DCDCDC", font=police_texte)
    labelNomVideo1.place(relx=.15, rely=.80, anchor="center")

    labelNomVideo2 = Text(fenetreEye, wrap=NONE)
    labelNomVideo2.place(relx=.60, rely=.80, anchor="center", height="30", width="400")

    boutonValider = Button(fenetreEye, text="Valider", font=police_texte, command=lambda:fonctionIntermediaireEye(FichierEye,FichierVideo,var_langue,fenetreEye))
    boutonValider.place(relx=.80, rely=.90, anchor="center", height="30", width="100")
    boutonValider.config(highlightbackground="#DCDCDC")


    if var_langue == "anglais":
        
        labelEye["text"] = "Eye-tracking file :"
        labelVideo["text"] = "Video file :"
        labelNomEye1["text"] = "File path :\n"
        labelNomVideo1["text"] = "File path :\n"
        labelTitreEye["text"] = "Select files"
        boutonValider["text"] = "Validate"



def fichierCoda(labelNomCoda1):
    global FichierCoda
    FichierCoda=demandeFichier()
    labelNomCoda1.config(state='normal')
    labelNomCoda1.insert('1.0', FichierCoda)
    labelNomCoda1.config(state='disabled')
    if FichierCoda.endswith("mat"):
        labelNomCoda1["background"] = "#A3FEA3"
    else:
        labelNomCoda1["background"] = "#FE6969"

def fichierEye(labelNomEye1):
    global FichierEye
    FichierEye = demandeFichier()
    labelNomEye1.config(state='normal')
    labelNomEye1.insert('1.0', FichierEye)
    labelNomEye1.config(state='disabled')
    if FichierEye.endswith("csv"):
        labelNomEye1["background"] = "#A3FEA3"
    else:
        labelNomEye1["background"] = "#FE6969"

def fichierVideo(labelNomVideo1):
    global FichierVideo
    FichierVideo = demandeFichier()
    labelNomVideo1.config(state='normal')
    labelNomVideo1.insert('1.0', FichierVideo)
    labelNomVideo1.config(state='disabled')
    if FichierVideo.endswith("mp4"):
        labelNomVideo1["background"] = "#A3FEA3"
    else:
        labelNomVideo1["background"] = "#FE6969"

