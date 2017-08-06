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
        
        if "HTTP_COOKIE" in os.environ.keys():       
            tmpDiv = self.subElement(self.mainCtn,"div")
            self.subElement(tmpDiv,"h1").text = "Cookie trouvé !"
            lstInfo = self.subElement(tmpDiv, "div")
            lstInfo = self.subElement(lstInfo, "li")
            for v in os.environ["HTTP_COOKIE"].split("; "):
                tmp = self.subElement(lstInfo, "ul")
                tmp.text = "%s : %s" % v.split("=")
        
        
        lstInfo = self.subElement(self.mainCtn, "div")
        lstInfo = self.subElement(lstInfo, "ul")
        for i in os.environ.items():
            tmp = self.subElement(lstInfo, "li")
            tmp.text = "%s : %s" % i        
        
        script = self.subElement(self.body, "script")
        script.text = """
            $(function(){
                
            });
        """

        
if __name__ == "__main__" : 
    p = pageAuth()
    print(p.dump())
    
