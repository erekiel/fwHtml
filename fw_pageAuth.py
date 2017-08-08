#! /usr/bin/python3
# coding:utf-8

################################################################################
#                                       Auteur : Mickaël DUVAL
#                                       juillet 2017
################################################################################
import sys
import os
import cgi

################################################################################
# tous les scripts devraient commencer comme ça pour afficher les emmerdes
import cgitb

cgitb.enable()
if __name__ == "__main__" : 
    print("Content-Type: text/html\n\n")
################################################################################


import fw_page
import fw_authentification

class pageAuth(fw_page.Page):
    def __init__(self):
        fw_page.Page.__init__(self)
        
        self.addCDN()
        self.addScr("js/cookies.js")
        self.addScr("js/crypto.js")
        self.addScr("js/auth.js")
        
        self.mainCtn = self.subElement(self.body, "div")
        self.mainCtn.set("class", "container")
        
        # titre
        tmpDiv = self.subElement(self.mainCtn,"div")
        tmpDiv.set("class", "page-header")
        self.subElement(tmpDiv,"h1").text = "Essai page authentification"
        self.title.text = "Authentification"
        
        
        # self.authentif = True si t'es ok
        self.authentif = fw_authentification.auth(printer = False)
        if self.authentif:
            self.subElement(self.mainCtn,"h2").text = "Utilisateur autorisé !"
        else : 
            self.subElement(self.mainCtn,"h5").text = "Redirection en cours..."
            # passer la page en param redirige après login
            self.rediriger("fw_pageLogin.py?redirige=fw_pageAuth.py")
            # ne plus rien afficher sur la page
            return
                
        # block déconnexion
        tmp = self.subElement(tmpDiv, "div")
        tmp.set("class", "col-md-2")
        tmp = self.subElement(tmp, "div")
        tmp.text = "Se déconnecter"
        tmp.set("id", "btUnLog")
        tmp.set("class", "btn")
        ###########
        
        # lstInfo = self.subElement(self.mainCtn, "div")
        # self.subElement(lstInfo,"h2").text = "Variables d'environnement"
        # lstInfo = self.subElement(lstInfo, "ul")
        # for i in os.environ.items():
            # tmp = self.subElement(lstInfo, "li")
            # tmp.text = "%s : %s" % i        
        

        
if __name__ == "__main__" : 
    p = pageAuth()
    print(p.dump())
    
