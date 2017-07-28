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
        # m.set("charset", "latin-1")
        
        mainConteneur = self.subElement(self.body,"div")
        mainConteneur.set("class","container")
        
        jumbotron = self.subElement(mainConteneur,"div")
        jumbotron.set("class","jumbotron")
        
        self.subElement(mainConteneur,"h1").text = "ôçùàñà"
        
        
        

p = pageIndex()

print(p.dump())

# import xml.etree.ElementTree
# arbo = xml.etree.ElementTree.ElementTree()


# html = xml.etree.ElementTree.Element("html")
# head = xml.etree.ElementTree.SubElement(html, "head")
# title = xml.etree.ElementTree.SubElement(head, "title")
# title.text = "Je suis un test !"
# body = xml.etree.ElementTree.SubElement(html, "body")
# xml.etree.ElementTree.SubElement(body, "h1").text = "Je fonctionne putain êçàùö!"
# xml.etree.ElementTree.SubElement(body, "h1").text = "oh yeah"
# xml.etree.ElementTree.SubElement(body, "p").text = "C'est un truc de ouh ouh ouf"

# sortie = "<!DOCTYPE html>\n"
# sortie += xml.etree.ElementTree.tostring(html, encoding="utf-8", method="html").decode("utf-8")

# print(sortie)
