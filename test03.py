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

import carousel
import os
import fw_page

# test de carousel en mode objet
lstPhotos = ["img/%s" % f for f in os.listdir("img") if f.endswith(".jpg")]
c = carousel.Carousel(lstPhotos)
p = fw_page.Page()
p.addCDN()
p.title.text = "Objet Carousel"
# p.subElement(p.body, c.rootElem)
p.body.append(c.rootElem)


print(p.dump())