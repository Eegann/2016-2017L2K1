/*
//  clienMacOS.sql
//
//  Configure only psql DATABASE l2k1_client.
//
//
//  Created by Benjamin Cohen 24/03/2017.
//  Copyright © 2017. All rights reserved.
//
//
*/


#include <stdlib.h>
#include <stdio.h>
#include <string.h>


exec sql begin declare section;
    char patch_Ip[39];
    char patch_Ip_Mac[39];
    char patch_Os[39];
    char patch_date[39];
    int  patch_nb;

    char *select1 = "INSERT INTO L2K1_CLIENT (IP_LOG, IP_MAC_LOG, OPERATING_SYSTEM, DATE_START, DATE_END, NOMBRE_CONNEXION)"
                    "VALUES (?, ?, ?, ?, ?, ?);";

    char *select2 = "UPDATE L2K1_CLIENT SET  NOMBRE_CONNEXION = NOMBRE_CONNEXION +1, DATE_END = ? WHERE IP_LOG = ?;";
exec sql end declare section;



exec sql include sqlca;




int main(int argc, const char * argv[]) {


     FILE *pp = NULL; 

     int i=0; patch_nb=1;
     char *patch_tmp;

     patch_tmp = (char*) calloc(40, sizeof(char));


     
     
     /* Récupération de l'adresse IP de l'utilisateur. */
    
     pp = popen ("curl ipecho.net/plain", "r"); 
    
     if (pp == NULL){
         exit(22);
     }
    
     while (fgets(patch_tmp, 39, pp) != NULL)
    
     for(i=0; i<strlen(patch_tmp); i++){
         patch_Ip[i]=patch_tmp[i];
     } 

     


     /* Récupération de l'adresse Mac de l'utilisateur. */
   
     pp = popen ("ifconfig en0 | grep ether", "r");
    
     if (pp == NULL){
         exit(44);
     }
    
     while (fgets(patch_tmp, 39, pp) != NULL)
    
    
     for(i=0; i<strlen(patch_tmp); i++){
         patch_Ip_Mac[i]=patch_tmp[i+7];
     }

 


     /* Récupération de la date d'utilisation. */

     pp = popen ("date", "r");
    
     if (pp == NULL){
         exit(88);
     }
    
     while (fgets(patch_tmp, 39, pp) != NULL)
    
     for(i=0; i<strlen(patch_tmp); i++){
         patch_date[i]=patch_tmp[i];
     }
 
     

     
     /* Récupération de l'OS d'utilisation. */

     pp = popen ("sw_vers -productName", "r");
    
     if (pp == NULL){
         exit(176);
     }
    
     while (fgets(patch_tmp, 39, pp) != NULL)
    
     strcpy(patch_Os, patch_tmp);


     pp = popen ("sw_vers -productVersion", "r");
    
     if (pp == NULL){
         exit(352);
     }
    
     while (fgets(patch_tmp, 39, pp) != NULL)
    
     strcat(patch_Os, patch_tmp);





    /* Transaction sur la base de données. */

    exec sql connect to NAMEBD@localhost;


        /* Mise à jour de la base de données si l'utilisateur existe déjà. */

        exec sql prepare st_select2 from :select2;

        EXEC SQL EXECUTE st_select2 USING :patch_date, :patch_Ip; 

        exec sql set autocommit to on; 

        EXEC SQL DEALLOCATE PREPARE st_select2; 


         /* Création de l'utilisateur si celui-ci n'existait pas dans la base de données. */

        exec sql prepare st_select1 from :select1;

        EXEC SQL EXECUTE st_select1 USING :patch_Ip, :patch_Ip_Mac, :patch_Os, :patch_date, :patch_date, :patch_nb;

        exec sql set autocommit to on; 

        EXEC SQL DEALLOCATE PREPARE st_select1;

    
    /* Déconnexion de la base de données. */

    exec sql disconnect all;  

    free(patch_tmp);
    pclose(pp);

    return(0);

}