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

import os
import fw_page

"""
<div id="carousel-example-generic" class="carousel slide" data-ride="carousel">
    <ol class="carousel-indicators">
      <li data-target="#carousel-example-generic" data-slide-to="0" class="active"></li>
      <li data-target="#carousel-example-generic" data-slide-to="1"></li>
      <li data-target="#carousel-example-generic" data-slide-to="2"></li>
    </ol>
    <div class="carousel-inner" role="listbox">
      <div class="item active">
        <img data-src="holder.js/1140x500/auto/#777:#555/text:First slide" alt="First slide">
      </div>
      <div class="item">
        <img data-src="holder.js/1140x500/auto/#666:#444/text:Second slide" alt="Second slide">
      </div>
      <div class="item">
        <img data-src="holder.js/1140x500/auto/#555:#333/text:Third slide" alt="Third slide">
      </div>
    </div>
    <a class="left carousel-control" href="#carousel-example-generic" role="button" data-slide="prev">
      <span class="glyphicon glyphicon-chevron-left" aria-hidden="true"></span>
      <span class="sr-only">Previous</span>
    </a>
    <a class="right carousel-control" href="#carousel-example-generic" role="button" data-slide="next">
      <span class="glyphicon glyphicon-chevron-right" aria-hidden="true"></span>
      <span class="sr-only">Next</span>
    </a>
  </div>


</div> <!-- /container -->
"""

class PageCarousel(fw_page.Page):
    def __init__(self):
        fw_page.Page.__init__(self)
        
        self.lstImg = [f for f in os.listdir("img") if f.endswith(".jpg")]
        
        # bootstrap
        self.addCDN()
        
        # titre
        tmpDiv = self.subElement(self.body,"div")
        tmpDiv.set("class", "page-header")
        self.subElement(tmpDiv,"h1").text = "Essai de carousel photo"
        self.title.text = "Carousel"
        
        # custom carousel style, si besoin
        # tmp = self.subElement(self.head, "link")
        # tmp.set("rel", "stylesheet")
        # tmp.set("href", "carousel.css")

        
        # verif
        # for f in self.lstImg:
            # self.subElement(self.body, "p").text = f
        
        # carousel
        carousel = self.subElement(self.body,"div")
        # carousel.set("id","carousel-example-generic")
        
        idCarousel = "monCarousel"
        carousel.set("id",idCarousel)
        carousel.set("class","carousel slide")
        carousel.set("data-ride","carousel")
        
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
        carouselInner = self.subElement(carousel, "div")
        carouselInner.set("class", "carousel-inner")
        carouselInner.set("role", "listbox")
        
        # items
        lstItem = []
        for f in self.lstImg:
            item = self.subElement(carouselInner, "div")
            item.set("class", "item")
            lstItem.append(item)
            
            img = self.subElement(item, "img")
            img.set("src", "img/%s" % f)
            img.set("text", f)
            img.set("alt", f)
            
            img.set("class", "img-responsive center-block")
            # img.set("class", "d-block img-fluid")
            # img.set("class", "center")
            # tmp = self.subElement(item, "p")
            # tmp.text = "Gnagnagna %s" % f
            
        
        lstItem[0].set("class", "item active")
            
        # suivant/precedent
        precedent = self.subElement(carousel, "a")
        precedent.set("class", "left carousel-control")
        precedent.set("href", "#%s" % idCarousel)
        precedent.set("role", "button")
        precedent.set("data-slide", "prev")
        
        tmp = self.subElement(precedent, "span")
        tmp.set("class", "glyphicon glyphicon-chevron-left")
        tmp.set("aria-hidden", "true")
        tmp.text = " "

        tmp = self.subElement(precedent, "span")
        tmp.set("class", "sr-only")
        tmp.text = "Précédent"
        
        # suivant
        suivant = self.subElement(carousel, "a")
        suivant.set("class", "right carousel-control")
        suivant.set("href", "#%s" % idCarousel)
        suivant.set("role", "button")
        suivant.set("data-slide", "next")
        
        tmp = self.subElement(suivant, "span")
        tmp.set("class", "glyphicon glyphicon-chevron-right")
        tmp.set("aria-hidden", "true")
        tmp.text = " "

        tmp = self.subElement(precedent, "span")
        tmp.set("class", "sr-only")
        tmp.text = "Suivant"
      
        # ?
        # scr = self.subElement(self.body, "script")
        # scr.set("language", "javascript")
        # scr.text = """
            # alert("prout");
            # $('.carousel').carousel({
                # interval: 2000
            # });
            # """
    
if __name__ == "__main__":
    p = PageCarousel()
    print(p.dump())