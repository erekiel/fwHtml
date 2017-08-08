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
        
        # cgi
        self.form = cgi.FieldStorage()        
        
        # test container
        self.mainCtn = self.subElement(self.body, "div")
        self.mainCtn.set("class", "container")
        
        # titre
        tmpDiv = self.subElement(self.mainCtn,"div")
        tmpDiv.set("class", "page-header")
        self.subElement(tmpDiv,"h1").text = "Essai page authentification"
        self.title.text = "Authentification"
        
        l = self.subElement(tmpDiv, "a")
        l.set("href", "fw_pageLogin.py")
        l.text = "Se Logger"
        
        # ceci dit : tout étant dans os.environ, il vaudrait mieux tester direct dans un 'isAuth()'
        # if "HTTP_COOKIE" in os.environ.keys():       
            # tmpDiv = self.subElement(self.mainCtn,"div")
            # self.subElement(tmpDiv,"h2").text = "Cookies trouvés !"
            # lstInfo = self.subElement(tmpDiv, "div")
            # lstInfo = self.subElement(lstInfo, "ul")
            # for v in os.environ["HTTP_COOKIE"].split("; "):
                # tmp = self.subElement(lstInfo, "li")
                # if "=" in v : 
                    # tmp.text = "%s : %s" % (v.split("=")[0], v.split("=")[1])
                # else : 
                    # tmp.text = v
        # else : 
            # tmpDiv = self.subElement(self.mainCtn,"div")
            # self.subElement(tmpDiv,"h2").text = "Pas de cookie"
            # self.subElement(tmpDiv,"p").text = "C'est là que tu te fais rediriger normalement"
            
        self.authentif = fw_authentification.auth(printer = False)
        if self.authentif:
            self.subElement(self.mainCtn,"h2").text = "Utilisateur autorisé !"
        else : 
            self.subElement(self.mainCtn,"h2").text = "Utilisateur pas authentifié"
            script = self.subElement(self.body, "script")
            script.text = """
                $(function(){
                    document.location = "%s"
                });
            """ % "fw_pageLogin.py"

        
        lstInfo = self.subElement(self.mainCtn, "div")
        self.subElement(lstInfo,"h2").text = "Variables d'environnement"
        lstInfo = self.subElement(lstInfo, "ul")
        for i in os.environ.items():
            tmp = self.subElement(lstInfo, "li")
            tmp.text = "%s : %s" % i        
        
        # script = self.subElement(self.body, "script")
        # script.text = """
            # $(function(){
                
            # });
        # """

        
if __name__ == "__main__" : 
    p = pageAuth()
    print(p.dump())
    
