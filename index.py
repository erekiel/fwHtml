#! /usr/bin/python3
# coding:utf-8


################################################################################
#                                       Auteur : Mickaël DUVAL
#                                       juillet 2017
################################################################################
import sys

################################################################################
# tous les scripts devraient commencer comme ça pour afficher les emmerdes
import cgitb

cgitb.enable()
print("Content-Type: text/html\n\n")
################################################################################


import fw_page

class pageIndex(fw_page.Page):
    def __init__(self):
        fw_page.Page.__init__(self)
        
        self.addCDN()
        
        # m = self.subElement(self.head, "meta")
        # m.set("charset", "utf-8")
        
        mainConteneur = self.subElement(self.body,"div")
        mainConteneur.set("class","container")
        
        jumbotron = self.subElement(mainConteneur,"div")
        jumbotron.set("class","jumbotron")
        
        self.subElement(jumbotron,"h1").text = "Ceci est le titre !"
        
        self.subElement(jumbotron,"p").text = \
            "Encoding python : %s" % sys.getdefaultencoding()
        self.subElement(jumbotron,"p").text = \
            """Quant à moi, je ne suis qu'un humble paragraphe P."""
        self.subElement(jumbotron,"div").text = \
"""Moi je ne suis qu'un div, et je permet de tester l'encodage : ùàïôçù."""
        tmp = self.subElement(jumbotron,"a")
        tmp.text = "Page de test 2" 
        tmp.set("href", "test02.py")
        
        tmp = self.subElement(jumbotron,"p")
        tmp = self.subElement(tmp,"a")
        tmp.text = "Les oignons de twine" 
        tmp.set("href", "oignons.html")
        
        

p = pageIndex()
tmp = p.dump()
print(tmp)
