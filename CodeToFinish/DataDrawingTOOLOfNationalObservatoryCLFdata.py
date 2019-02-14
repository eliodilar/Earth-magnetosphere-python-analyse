# -*- coding: utf-8 -*-

#-------Lib_declaration--------
import os 
from tkinter import * 
from tkinter.filedialog import *
import csv
import matplotlib.pyplot as plt
import numpy as np
#------------End_LIB------------


#-------------------------Class_declaration--------------------------------
class DrawingXYZ:

    def __init__(self):
        self.Value=""
        self.X= []
        self.Y= []
        self.Z= []
        self.T= []
        self.NbX=0
        self.NbY=0
        self.NbZ=0
        self.NbF=0

    def WatchRowDatCSV(self):
        _Cpt = 0
    
        #ouverture de l'explorateur windows
        filepath = askopenfilename(title="Ouvrir une image",filetypes=[('all files','.*')])
        _chemin=filepath
    
        #stockage et traitement des données csv
        _Data_Row_Csv = csv.reader(open(_chemin, newline=''), delimiter=' ', quotechar='|')
        
        for row in _Data_Row_Csv:
            _Cpt+=1
            if _Cpt == 28:
                self.Value=row

                label = Label(FrameColonne, text="Formatage par colonne du fichier CSV")
                label.pack()
                    
                #affichage du formatage du fichier CSV
                FormatBox = StringVar()
                FormatBoxLabel = Label(FrameColonne, textvariable=FormatBox, bg="white", relief='sunken')
                FormatBox.set(str(self.Value))
                FormatBoxLabel.pack()
              
                break
        

    def CSVLoader(self):

        _Cpt = 0

        print("Openning CSV File.")
    
        #ouverture de l'explorateur windows
        filepath = askopenfilename(title="Ouvrir une image",filetypes=[('all files','.*')])
        _chemin=filepath
    
        #stockage et traitement des données csv
        _Data_Row_Csv = csv.reader(open(_chemin, newline=''), delimiter=' ', quotechar='|')

        
        #dremplissage du buffer de X
        for row in _Data_Row_Csv:
            _Cpt+=1
            if _Cpt > 27:
                self.X.append(float(row[3]))

        _Cpt = 0
        
        #decoupage horraire celon la taille des données ( sur 24 h a modifier avecmin, sec, tkinter)
        for row in self.X:
            _Cpt+=1
            self.T.append(_Cpt*(24.0/len(self.X)))
        

    def DrawPlotXT(self):

        fig, ax = plt.subplots()
        ax.plot(self.T, self.X, color="green", linewidth=0.7, linestyle="-", label="CLFX")
        plt.legend(loc='upper left')
        plt.show()


    def GetFormatCSV(self):
        return self.Value

    def SetIdColX(self, X):
        self.NbX=X


    def SetIdCol(self, X, Y, Z, F):
        self.NbX=X
        self.NbY=Y
        self.NbZ=Z
        self.NbF=F
        
#----------------------------End_Class_declaration-----------------------------


#---------------------------------MAIN LOOP------------------------------------
fenetre = Tk()

Classe_Drawing = DrawingXYZ()

# frame fenetre
FrameFenetre = Frame(fenetre, borderwidth=4, relief=GROOVE)
FrameFenetre.pack(side=LEFT, padx=30, pady=30)

# frame Traitement
FrameTraitement = Frame(FrameFenetre, borderwidth=4, relief=GROOVE)
FrameTraitement.pack(side=LEFT, padx=30, pady=30)

# frame Colonne
FrameColonne = Frame(FrameFenetre, borderwidth=4, relief=GROOVE)
FrameColonne.pack(side=LEFT, padx=10, pady=10)

#Titre
label = Label(FrameFenetre, text="Générateur de courbe ")
label.pack()


# bouton de sortie
bouton=Button(FrameTraitement, text="Quitter", command=fenetre.quit)
bouton.pack()

# bouton Data CSV watcher
boutonCSVWatch=Button(FrameTraitement, text="Watch CSV Data Formating", command=Classe_Drawing.WatchRowDatCSV)
boutonCSVWatch.pack()

# bouton d'ouverture csv
boutonCSV=Button(FrameTraitement, text="OpenCSVFile", command=Classe_Drawing.CSVLoader)
boutonCSV.pack()

# bouton d'ouverture csv
boutonDraw=Button(FrameTraitement, text="Traçer la courbe de X / T", command=Classe_Drawing.DrawPlotXT)
boutonDraw.pack()

# Input X col selection number
entree = Entry(FrameColonne, width=30)
entree.pack()

# bouton de validation selection colonne
bouton=Button(FrameColonne, text="Col validation selector", command=Classe_Drawing.SetIdColX(entree.get()))
bouton.pack()


fenetre.mainloop()
#-------------------------------END_MAIN_LOOP-----------------------------------------------------

fenetre.destroy()


