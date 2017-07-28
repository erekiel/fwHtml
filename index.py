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



import xml.etree.ElementTree
# arbo = xml.etree.ElementTree.ElementTree()


html = xml.etree.ElementTree.Element("html")
head = xml.etree.ElementTree.SubElement(html, "head")
title = xml.etree.ElementTree.SubElement(head, "title")
title.text = "Je suis un test !"
body = xml.etree.ElementTree.SubElement(html, "body")
xml.etree.ElementTree.SubElement(body, "h1").text = "Je fonctionne putain êçàùö!"

sortie = "<!DOCTYPE html>\n"
sortie += xml.etree.ElementTree.tostring(html, encoding="utf-8", method="html").decode("utf-8")

print(sortie)
