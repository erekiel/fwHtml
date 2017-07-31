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
if __name__ == "__main__":
    print("Content-Type: text/html\n\n")
################################################################################

import xml.etree.ElementTree

class Carousel:
    def __init__(self, lstImg = None):
        self.rootElem = xml.etree.ElementTree.Element("div")
        self.lstImg = lstImg
        
        self.hauteur = "500px"
        
        self.rootElem.set("class", "page-header")
        
        # tmp = 
        # xml.etree.ElementTree.SubElement(self.rootElem,"h1").text = "Ceci est le titre du carousel"
        
        # self.rootElem = self.subElement(self.body,"div")
        # self.rootElem = xml.etree.ElementTree.SubElement(carousel, "div")
        # self.rootElem.set("id","carousel-example-generic")
        
        idCarousel = "monCarousel"
        self.rootElem.set("id",idCarousel)
        self.rootElem.set("class","carousel slide")
        self.rootElem.set("data-ride","carousel")
        
        # barre d'indicateur en dessous
        # ctnIndicateurs = self.subElement(carousel, "ol")
        # ctnIndicateurs.set("class", "carousel-indicators")
        
        # lstIndicateurs = []
        
        # for i in range(len(self.lstImg)):
            # tmp = self.subElement(ctnIndicateurs, "li")
            # tmp.set("data-target","#%s" % idCarousel)
            # tmp.set("data-slide-to", str(i))
            # tmp.text = " "
            # lstIndicateurs.append(tmp)
        
        # lstIndicateurs[0].set("class", "item active")
        
        # inner truc 
        
        carouselInner = xml.etree.ElementTree.SubElement(self.rootElem, "div")
        carouselInner.set("class", "carousel-inner")
        carouselInner.set("role", "listbox")
        
        # items
        lstItem = []
        for f in self.lstImg:        
            item = xml.etree.ElementTree.SubElement(carouselInner, "div")
            item.set("class", "item")
            lstItem.append(item)
            
            img = xml.etree.ElementTree.SubElement(item, "img")
            # img.set("src", "img/%s" % f)
            img.set("src", f)
            img.set("text", f)
            img.set("alt", f)
            
            img.set("class", "img-responsive center-block")
            img.set("style", "height:%s" % self.hauteur)
            # img.set("class", "d-block img-fluid")
            # img.set("class", "center")
            # tmp = self.subElement(item, "p")
            # tmp.text = "Gnagnagna %s" % f
            
        
        lstItem[0].set("class", "item active")
            
        # suivant/precedent
        precedent = xml.etree.ElementTree.SubElement(self.rootElem, "a")
        precedent.set("class", "left carousel-control")
        precedent.set("href", "#%s" % idCarousel)
        precedent.set("role", "button")
        precedent.set("data-slide", "prev")
        
        tmp = xml.etree.ElementTree.SubElement(precedent, "span")
        tmp.set("class", "glyphicon glyphicon-chevron-left")
        tmp.set("aria-hidden", "true")
        tmp.text = " "

        tmp = xml.etree.ElementTree.SubElement(precedent, "span")
        tmp.set("class", "sr-only")
        tmp.text = "Précédent"
        
        # suivant
        suivant = xml.etree.ElementTree.SubElement(self.rootElem, "a")
        suivant.set("class", "right carousel-control")
        suivant.set("href", "#%s" % idCarousel)
        suivant.set("role", "button")
        suivant.set("data-slide", "next")
        
        tmp = xml.etree.ElementTree.SubElement(suivant, "span")
        tmp.set("class", "glyphicon glyphicon-chevron-right")
        tmp.set("aria-hidden", "true")
        tmp.text = " "

        tmp = xml.etree.ElementTree.SubElement(suivant, "span")
        tmp.set("class", "sr-only")
        tmp.text = "Suivant"
