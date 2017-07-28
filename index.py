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
        
        m = self.subElement(self.head, "meta")
        m.set("charset", "utf-8")
        
        mainConteneur = self.subElement(self.body,"div")
        mainConteneur.set("class","container")
        
        jumbotron = self.subElement(mainConteneur,"div")
        jumbotron.set("class","jumbotron")
        
        self.subElement(jumbotron,"h1").text = "Ceci est le titre !"
        
        self.subElement(jumbotron,"p").text = \
            "Encoding python : %s" % sys.getdefaultencoding()
        self.subElement(jumbotron,"div").text = \
            """Quant à moi, je ne suis qu'un humble paragraphe"""
        
        
        

p = pageIndex()
tmp = p.dump()
print(tmp)
