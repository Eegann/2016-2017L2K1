/* Processed by ecpg (4.12.0) */
/* These include files are added by the preprocessor */
#include <ecpglib.h>
#include <ecpgerrno.h>
#include <sqlca.h>
/* End of automatic include section */

#line 1 "clientMacOS.sql"
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


/* exec sql begin declare section */
     
     
     
     
      

       
                    

       

#line 20 "clientMacOS.sql"
 char patch_Ip [ 39 ] ;
 
#line 21 "clientMacOS.sql"
 char patch_Ip_Mac [ 39 ] ;
 
#line 22 "clientMacOS.sql"
 char patch_Os [ 39 ] ;
 
#line 23 "clientMacOS.sql"
 char patch_date [ 39 ] ;
 
#line 24 "clientMacOS.sql"
 int patch_nb ;
 
#line 26 "clientMacOS.sql"
 char * select1 = "INSERT INTO L2K1_CLIENT (IP_LOG, IP_MAC_LOG, OPERATING_SYSTEM, DATE_START, DATE_END, NOMBRE_CONNEXION)" "VALUES (?, ?, ?, ?, ?, ?);" ;
 
#line 29 "clientMacOS.sql"
 char * select2 = "UPDATE L2K1_CLIENT SET  NOMBRE_CONNEXION = NOMBRE_CONNEXION +1, DATE_END = ? WHERE IP_LOG = ?;" ;
/* exec sql end declare section */
#line 30 "clientMacOS.sql"





#line 1 "/Applications/Postgres.app/Contents/Versions/9.6/include/sqlca.h"
#ifndef POSTGRES_SQLCA_H
#define POSTGRES_SQLCA_H

#ifndef PGDLLIMPORT
#if  defined(WIN32) || defined(__CYGWIN__)
#define PGDLLIMPORT __declspec (dllimport)
#else
#define PGDLLIMPORT
#endif   /* __CYGWIN__ */
#endif   /* PGDLLIMPORT */

#define SQLERRMC_LEN	150

#ifdef __cplusplus
extern		"C"
{
#endif

struct sqlca_t
{
	char		sqlcaid[8];
	long		sqlabc;
	long		sqlcode;
	struct
	{
		int			sqlerrml;
		char		sqlerrmc[SQLERRMC_LEN];
	}			sqlerrm;
	char		sqlerrp[8];
	long		sqlerrd[6];
	/* Element 0: empty						*/
	/* 1: OID of processed tuple if applicable			*/
	/* 2: number of rows processed				*/
	/* after an INSERT, UPDATE or				*/
	/* DELETE statement					*/
	/* 3: empty						*/
	/* 4: empty						*/
	/* 5: empty						*/
	char		sqlwarn[8];
	/* Element 0: set to 'W' if at least one other is 'W'	*/
	/* 1: if 'W' at least one character string		*/
	/* value was truncated when it was			*/
	/* stored into a host variable.             */

	/*
	 * 2: if 'W' a (hopefully) non-fatal notice occurred
	 */	/* 3: empty */
	/* 4: empty						*/
	/* 5: empty						*/
	/* 6: empty						*/
	/* 7: empty						*/

	char		sqlstate[5];
};

struct sqlca_t *ECPGget_sqlca(void);

#ifndef POSTGRES_ECPG_INTERNAL
#define sqlca (*ECPGget_sqlca())
#endif

#ifdef __cplusplus
}
#endif

#endif

#line 34 "clientMacOS.sql"





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

    { ECPGconnect(__LINE__, 0, "NAMEBD@localhost" , NULL, NULL , NULL, 0); }
#line 133 "clientMacOS.sql"



        /* Mise à jour de la base de données si l'utilisateur existe déjà. */

        { ECPGprepare(__LINE__, NULL, 0, "st_select2", select2);}
#line 138 "clientMacOS.sql"


        { ECPGdo(__LINE__, 0, 1, NULL, 0, ECPGst_execute, "st_select2", 
	ECPGt_char,(patch_date),(long)39,(long)1,(39)*sizeof(char), 
	ECPGt_NO_INDICATOR, NULL , 0L, 0L, 0L, 
	ECPGt_char,(patch_Ip),(long)39,(long)1,(39)*sizeof(char), 
	ECPGt_NO_INDICATOR, NULL , 0L, 0L, 0L, ECPGt_EOIT, ECPGt_EORT);}
#line 140 "clientMacOS.sql"
 

        { ECPGsetcommit(__LINE__, "on", NULL);}
#line 142 "clientMacOS.sql"
 

        { ECPGdeallocate(__LINE__, 0, NULL, "st_select2");}
#line 144 "clientMacOS.sql"
 


         /* Création de l'utilisateur si celui-ci n'existait pas dans la base de données. */

        { ECPGprepare(__LINE__, NULL, 0, "st_select1", select1);}
#line 149 "clientMacOS.sql"


        { ECPGdo(__LINE__, 0, 1, NULL, 0, ECPGst_execute, "st_select1", 
	ECPGt_char,(patch_Ip),(long)39,(long)1,(39)*sizeof(char), 
	ECPGt_NO_INDICATOR, NULL , 0L, 0L, 0L, 
	ECPGt_char,(patch_Ip_Mac),(long)39,(long)1,(39)*sizeof(char), 
	ECPGt_NO_INDICATOR, NULL , 0L, 0L, 0L, 
	ECPGt_char,(patch_Os),(long)39,(long)1,(39)*sizeof(char), 
	ECPGt_NO_INDICATOR, NULL , 0L, 0L, 0L, 
	ECPGt_char,(patch_date),(long)39,(long)1,(39)*sizeof(char), 
	ECPGt_NO_INDICATOR, NULL , 0L, 0L, 0L, 
	ECPGt_char,(patch_date),(long)39,(long)1,(39)*sizeof(char), 
	ECPGt_NO_INDICATOR, NULL , 0L, 0L, 0L, 
	ECPGt_int,&(patch_nb),(long)1,(long)1,sizeof(int), 
	ECPGt_NO_INDICATOR, NULL , 0L, 0L, 0L, ECPGt_EOIT, ECPGt_EORT);}
#line 151 "clientMacOS.sql"


        { ECPGsetcommit(__LINE__, "on", NULL);}
#line 153 "clientMacOS.sql"
 

        { ECPGdeallocate(__LINE__, 0, NULL, "st_select1");}
#line 155 "clientMacOS.sql"


    
    /* Déconnexion de la base de données. */

    { ECPGdisconnect(__LINE__, "ALL");}
#line 160 "clientMacOS.sql"
  

    free(patch_tmp);
    pclose(pp);

    return(0);

}