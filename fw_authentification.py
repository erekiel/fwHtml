#! /usr/bin/python3
# coding:utf-8


import time
import cgi
import os
import hashlib
import cgitb
import json

cgitb.enable()

clefDuSite = "J'aimeraisEtreUneLibelluleEtMePoserSurTonPull"
repSessions = "sessions"

if __name__ == "__main__":
    print("Content-Type: text/html\n\n")
    

def clef(ip, usr):
    tmp = "%s%s%s" % (ip, usr, clefDuSite)
    tmp = tmp.encode()
    return hashlib.sha256(tmp).hexdigest()


# utilise le os.environ et fait tout le nécessaire, ou renvoie du vide si c'est non
def auth(redirige = ""):
    # bon, il me faut un usr, une ip, et soit un idSession, soit un pwd
    idSession = None
    usr = None
    pwd = None
    ip = None
    
    # si tu m'envoie un pwd, je renvoie un idSession
    reponse = {}
    reponse["idSession"] = ""
    reponse["commentaire"] = ""
    reponse["redirige"] = redirige
    
    
    # déjà, a-t-on un cookie avec un id session ?
    if "HTTP_COOKIE" in os.environ.keys():
        for c in os.environ["HTTP_COOKIE"].split("; "):
            if c.startswith("usr") and "=" in c:
                usr = c.split("=")[1]
            elif c.startswith("idSession") and "=" in c:
                idSession = c.split("=")[1]
    
    if "REMOTE_ADDR" in os.environ.keys():
        ip  = os.environ["REMOTE_ADDR"]
    
    # sinon, t'es qui toi ?    
    form = cgi.FieldStorage()
    
    if not usr: 
        usr = form.getvalue("usr")
    if not pwd:     
        pwd = form.getvalue("pwd")
        
    if not os.path.isdir(repSessions):
        os.system("mkdir %s" % repSessions)
    
    # ton idSession est correk
    if idSession : 
        if os.path.isfile(os.path.join(repSessions, "%s.txt" % idSession)):
            reponse["commentaire"] = "Je vois que Monsieur %s est déjà logg" % usr
            print(json.dumps(reponse))
            return True
        else : 
            reponse["commentaire"] = "idSession moisi dis donc"
            print(json.dumps(reponse))
            return False
    
    # pas de session en cours, t'en veux ?
    else :
        if usr and pwd and ip :
            if usr == "erekiel" and pwd == """e601b363404e19a333aa92fc7aa2a75757325c32cfb0017abf847580d2677025""":
                k = clef(ip, usr)
                ficSession = os.path.join(repSessions, k + ".txt")
                with open(ficSession,"w") as f : 
                    f.write("%s %s %s\n" % (usr, ip, k))
                    
                reponse["commentaire"] = "Bienvenue %s" % usr
                reponse["idSession"] = k
                print(json.dumps(reponse))
                
                return True
            else : 
                reponse["commentaire"] = "mot de passe incorrect %s : %s " % (usr, pwd)
                print(json.dumps(reponse))
                return False
        else : 
            print(json.dumps(reponse))
            reponse["commentaire"] = "pas usr ou pas pwd ou pas ip : [%s] [%s] [%s]" % (usr, pwd, ip)
            return False
    
    reponse["commentaire"] = "J'aurais pas du arriver ici"
    print(json.dumps(reponse))
    

if __name__ == "__main__":
    auth()

    
# def setAuth(ip, nom):
    # return "zarmaOkTeslogg"
    
# form = cgi.FieldStorage()

# print("<h3>Ma réponse sera la suivante : </h3>")

# if "HTTP_COOKIE" in os.environ.keys():
    # print("j'ai trouvé un cookie  :"  + os.environ["HTTP_COOKIE"])
    # if not os.environ["REMOTE_ADDR"]:
        # print("Pas d'adresse IP ?!")
    # elif isAuth(os.environ["REMOTE_ADDR"], os.environ["HTTP_COOKIE"]):
        # print("<h2>YAY Baybay !</h2>\n<p>Tu es identifié !</p>")
    # else : 
        # print("<p>Identification incorrecte</p>")
    
# else : 
    # print("<p>Pas de cookie d'identification</p>")


# if __name__ == "__main__":
    # c = http.cookies.SimpleCookie()
    # c["superCle"] = "leBoutDeMonZboub"
    # c.update({"expires":"31/12/2017"})
    # print(str(c.js_output()))
    
# if __name__ == "__main__":
    # form = cgi.FieldStorage()
    # print("Content-Type: text/html\n\n")
    # print("envoyé : ")

    # infoCGI = "<ul>"
    # for champ in form:
        # infoCGI += "<li>%s : %s</li>" % (champ, form.getvalue(champ))
    # infoCGI += "</ul>"
    # print(infoCGI)

    # if form.getvalue("zeCle") == "salagadouLaMagickaBou":
        # print("<h2>T'es trop officiel cousin !</h2>")
    # else :
        # print("<h2>tu vaux pas de la merde</h2>")