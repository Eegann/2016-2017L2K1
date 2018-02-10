# *-- coding: utf-8 --*

#
#
# *=*=* # ********************************************************************** #
# *=*=* #                                                                        #
# *=*=* #  Id:  pupilDataConversion.py 6442 11-03-2017                           #
# *=*=* #                                                                        #
# *=*=* #  Name:     pupilDataConversion.py                                      #
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
# <===> Inspired by url : https://github.com/pupil-labs/pupil/blob/master/pupil_src/shared_modules/file_methods.py <===>
#
#






# ============================================================================================================#
#                                                                                                             # 
#   Data Format                                                                                               #
#                                                                                                             #
#   timestamp - timestamp of the source image frame.                                                          #
#                                                                                                             #
#   norm_pos_x - x position in the world image frame in normalized coordinates.                               #
#   norm_pos_y - y position in the world image frame in normalized coordinates.                               #
#                                                                                                             #
#   Normalized coordinate system with the origin 0,0 at the bottom left and 1,1 at the top right.             #
#                                                                                                             #
#   Source from : https://github.com/pupil-labs/pupil/wiki/Data-Format                                        #
#                                                                                                             #
# ============================================================================================================#




#
#  Importation de l'ensemble des modules et fonctions nécessaires.
#

import pickle
import numpy as np
import sys


#
# Définition de la fonction  d'extraction et de conversion des données d'intérêt.
#


def extractionPupilData(pupil_data): # La fonction prend en paramètre le chemin du fichier à traiter.


    pupil_data = pickle.load(open(pupil_data, "rb"), encoding='latin1') # Ouverture du fichier à traiter.

    gaze_positions = pupil_data['gaze_positions'] # Sélection de la clé d'intérêt parmi les données à traiter.
  

    header0 = ['norm_pos']  
    header1 = ['timestamp']

    header_str = ','.join(header0)

    # Création de listes pour le stockage des données sélectionnées.

    filtered_positions_pupil1 = []
    filtered_positions_pupil2 = []
    filtered_timestamp = []

    #
    # Parcours et insertion des données à traiter.
    #


    # correspond aux données norm_pos_x.

    for tmp_gaze in gaze_positions: 
         filtered_positions_pupil1.append([tmp_gaze[x][0] for x in header0]) 

    # correspond aux données norm_pos_y.

    for tmp_gaze in gaze_positions:
        filtered_positions_pupil2.append([tmp_gaze[x][1] for x in header0])

     # correspond aux données timestamp.

    for tmp_gaze in gaze_positions:
         filtered_timestamp.append([tmp_gaze[x] for x in header1])

    #
    #  Sauvegarde des données traitées dans le fichier pupil_data.txt.
    #
    #      + Exemple de format de données enregistrées : 
    #  
    #      + Exe. 2.337034094803089324e-01 - <e-01> (10 puissance -1).
    #

    np.savetxt("dataTmp/pupil_data.txt", np.c_[filtered_positions_pupil1, filtered_positions_pupil2, filtered_timestamp], delimiter=",", header=('norm_pos_x' + '\t\t   ' + 'norm_pos_y' + '\t\t     ' + 'timestamp'), comments="")




if __name__ == "__main__":

    extractionPupilData('pupil_data')
    

