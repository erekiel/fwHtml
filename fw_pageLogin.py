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


"""<div class="row">
    <div class="col-md-4"></div>
    <div class="col-md-3">
        <div class="bloc" id="blockLogin">
            <h2>Login</h2>
            <form action="" method="POST">
            <div class="form-group">
              <label for="usr">Utilisateur :</label>
              <input type="text" class="form-control" id="usr" name="usr">
            </div>
            <div class="form-group">
              <label for="pwd">Mot de passe :</label>
              <input type="password" class="form-control" id="pwd" name="pwd">
            </div>
            <div>
                <input type="submit" class="btn" value="go" id="btGoLogin">
            </div>
            
        </div>
        
    </div>
</div>
"""

class pageAuth(fw_page.Page):
    def __init__(self):
        fw_page.Page.__init__(self)
        
        self.addCDN()
        
        self.addScr("js/cookies.js")
        self.addScr("js/crypto.js")
        self.addScr("js/auth.js")
        
        # cgi
        self.form = cgi.FieldStorage()        
        
        # test container
        self.mainCtn = self.subElement(self.body, "div")
        self.mainCtn.set("class", "container")
        
        # formulaire
        tmp = self.subElement(self.mainCtn, "row")
        tmp = self.subElement(tmp, "div")
        tmp.set("class", "col-md-4")
        
        tmp = self.subElement(self.mainCtn, "div")
        tmp.set("class", "col-md-4")
        blockLogin = self.subElement(tmp, "div")
        blockLogin.set("class", "bloc")
        blockLogin.set("id", "blockLogin")
        
        ligneLogin = self.subElement(blockLogin, "div")
        ligneLogin.set("class", "row")
        tmp = self.subElement(ligneLogin, "div")
        tmp.set("class", "col-md-10")
        self.subElement(tmp, "h2").text = "Login"
        
        # block déco
        tmp = self.subElement(ligneLogin, "div")
        tmp.set("class", "col-md-2")
        tmp = self.subElement(tmp, "div")
        tmp.text = "Se déconnecter"
        tmp.set("id", "btUnLog")
        tmp.set("class", "btn")
        ###########
        
        formulaire = self.subElement(blockLogin, "form")
        
        formulaire.set("action", "")
        formulaire.set("method", "POST")
        
        self.formInput(formulaire, "Utilisateur", "text", "usr")
        self.formInput(formulaire, "Mot de passe", "password", "pwd")
        self.formInput(formulaire, "", "submit", "btGoLogin", classCSS = "btn")
        
        tmp = self.subElement(formulaire, "input")
        tmp.set("type", "hidden")
        tmp.set("name", "redirige")
        tmp.set("id", "redirige")
        
        if self.form.getvalue("redirige") :
            self.redirection = self.form.getvalue("redirige")
        else : 
            self.redirection = ""
        tmp.set("value", self.redirection)
   
        
        tmp = self.subElement(blockLogin, "div")
        tmp.set("id", "resultat")
        # tmp.text = "resultat"
        # scr = self.subElement(self.body, "script")
    
    
    
    def formInput(self, blockParent, libelle, type, nom, classCSS="form-control"):
        tmp = self.subElement(blockParent, "div")
        tmp.set("class", "form-group")
        
    
        tmp = self.subElement(blockParent, "label")
        tmp.set("for", "%s" % nom)
        tmp.text = libelle
        
        tmp = self.subElement(blockParent, "input")
        tmp.set("type", type)
        tmp.set("class", classCSS)
        
        tmp.set("id", nom)
        tmp.set("name", nom)
        
        return tmp
        
        
if __name__ == "__main__":
    p = pageAuth()
    print(p.dump())