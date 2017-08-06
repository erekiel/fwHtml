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
        
        tmp = self.subElement(self.head, "script")
        tmp.set("src", "js/cookies.js")
        tmp.text = " " 
        tmp = self.subElement(self.head, "script")
        tmp.set("src", "js/crypto.js")
        tmp.text = " " 
        
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
        tmp.set("class", "col-md-3")
        blockLogin = self.subElement(tmp, "div")
        blockLogin.set("class", "bloc")
        blockLogin.set("id", "blockLogin")
        
        self.subElement(blockLogin, "h2").text = "Login"
        
        formulaire = self.subElement(blockLogin, "form")
        formulaire.set("action", "")
        formulaire.set("method", "POST")
        
        self.formInput(formulaire, "Utilisateur", "text", "usr")
        self.formInput(formulaire, "Mot de passe", "password", "pwd")
        self.formInput(formulaire, "", "submit", "btGoLogin", classCSS = "btn")
        
        
        scr = self.subElement(self.body, "script")
        
        scr.text = """
function getAuth(){ 
    //alert(SHA256($("#pwd").val()));
    $.ajax({
            method: "POST",
                url: "fw_authentification.py",
                data: { 
                    pwd: SHA256($("#pwd").val()),
                    usr: $("#usr").val(),
                }
        })
        .done(
            function(reponse) {
                if($.trim(reponse) != ""){
                    setCookie("idSession", $.trim(reponse), 1);
                    setCookie("usr", $("#usr").val(), 1);
                    $("#resultat").html("Bienvenue " + $("#usr").val());
                    
                    // $("#resultat").html("idSession : " + reponse);
                    // $("#resultat").html($("#resultat").html() + "<p>cookie : " + document.cookie + "</p>");
                    
                    var p = getCookie("origine");
                    //alert("cookie origine : " + p);
                    
                    if(p){
                        deleteCookie("origine");
                        document.location = p;
                    }
                    
                }
                else{
                    $("#resultat").html("identification incorrecte...");
                }
        });
        
    return false;
}

$("#btGoLogin").click(getAuth);
$("#usr").focus();
"""
    
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