#! /usr/bin/python3
# coding:utf-8


################################################################################
#                                       Auteur : Mickaël DUVAL
#                                       juillet 2017
################################################################################
import sys

################################################################################
import cgitb

cgitb.enable()
if __name__ == "__main__":
    print("Content-Type: text/html\n\n")
################################################################################
import xml.etree.ElementTree


class Page:
    def __init__(self):
        self.html = xml.etree.ElementTree.Element("html")
        self.html.set("lang","fr")
        
        self.arbo = xml.etree.ElementTree.ElementTree()
        self.arbo._setroot(self.html)
        
        self.head = self.subElement(self.html, "head")
        # self.subElement(self.head, "meta").set("charset","latin-1")
        
        self.title = self.subElement(self.head, "title")
        
        self.body = self.subElement(self.html, "body")
        
        
    def addCDN(self):
        for src in [
            "https://ajax.googleapis.com/ajax/libs/jquery/3.2.1/jquery.min.js",
            "https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css",
            "https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/js/bootstrap.min.js",
                    ]:
                    
            if src.endswith(".js"):
                self.addScr(src)
                # tmp = self.subElement(self.head, "script")
                # tmp.set("src", src)
                # tmp.text = " " 
            elif src.endswith(".css"):
                self.addCSS(src)
                # tmp = self.subElement(self.head, "link")
                # tmp.set("rel", "stylesheet")
                # tmp.set("href", src)
                
    def addScr(self, src):
        tmp = self.subElement(self.head, "script")
        tmp.set("src", src)
        tmp.text = " "
        return tmp
        
    def addCSS(self, src):
        tmp = self.subElement(self.head, "link")
        tmp.set("rel","stylesheet")
        tmp.set("href", src)
        return tmp

    def subElement(self, pere, elem):
        return xml.etree.ElementTree.SubElement(pere, elem)
        
    def rediriger(self, url):
        script = self.subElement(self.body, "script")
        script.text = """
            $(function(){
                document.location = "%s"
            });
        """ % url 
    
    def dump(self):
        sortie = "<!DOCTYPE html>\n"
        # il ne faut pas forcer l'encodage, sans quoi ça va merder au décodage
        # sortie += xml.etree.ElementTree.tostring(self.html, encoding="utf-8", method="html").decode("utf-8")
        
        # sortie += xml.etree.ElementTree.tostring(self.html, method="html").decode("utf-8")
        sortie += xml.etree.ElementTree.tostring(self.html, method="html").decode("utf-8")
        
        return sortie

if __name__ == "__main__":
    p = Page()
    p.subElement(p.body, "h1").text = "çeñior OnLïne" #.encode("utf-8").decode("latin-1")
    p.subElement(p.body, "p").text = "encoding : %s" % sys.getdefaultencoding()
    tmp = p.subElement(p.head,"meta")
    tmp.set("name","description")
    tmp.set("content","Ceci est un petit test de testation")
    
    # p.body.set("bgcolor", "black")
    # p.body.set("color", "#ffffff")
    print(p.dump())
