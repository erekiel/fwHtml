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

    
class infoSession:
    def __init__(self):
        self.usr = ""
        self.pwd = ""
        self.ip = ""
        self.idSession = ""
                
        # déjà, a-t-on un cookie avec un id session ?
        if "HTTP_COOKIE" in os.environ.keys():
            for c in os.environ["HTTP_COOKIE"].split("; "):
                if c.startswith("usr") and "=" in c:
                    self.usr = c.split("=")[1]
                elif c.startswith("idSession") and "=" in c:
                    self.idSession = c.split("=")[1]
        
        if "REMOTE_ADDR" in os.environ.keys():
            self.ip  = os.environ["REMOTE_ADDR"]
        
        # sinon, t'es qui toi ?    
        form = cgi.FieldStorage()
               
        if not self.usr:
            self.usr = form.getvalue("usr")
        if not self.pwd:     
            self.pwd = form.getvalue("pwd")
                    

# pour gratter quelques lignes de code
def repondre(reponse, comm, bRetour, printer = True):
    if "commentaire" not in reponse.keys():
        reponse["commentaire"] = ""
    reponse["commentaire"] += comm
    if printer:
        print(json.dumps(reponse))
    return bRetour
        
                    
# utilise le os.environ et fait tout le nécessaire, ou renvoie du vide si c'est non
def auth(redirige = "", printer = True):
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
    
    
    if not os.path.isdir(repSessions):
        os.system("mkdir %s" % repSessions)
        
    # if reponse["redirige"] == "":
        # reponse["redirige"]
        
    i = infoSession()
    
    # ton idSession est correk
    if i.idSession : 
        if os.path.isfile(os.path.join(repSessions, "%s.txt" % i.usr)):
            with open(os.path.join(repSessions, "%s.txt" % i.usr), "r") as f:
                u,ip,k = f.readline().split()
                
            if k != clef(ip, u):
                return repondre(reponse, "Ecoute %s, ça correspond pas à la session sur le serveur..." % i.usr, False, printer)
            else :
                return repondre(reponse, "Je vois que Monsieur %s est déjà logg" % i.usr, True, printer)
        else : 
            return repondre(reponse, "idSession moisi dis donc : le fichier %s.txt existe pas" % i.usr, False, printer)
            
    # pas de session en cours, t'en veux ?
    # else :
    if i.usr and i.pwd and i.ip :
        if i.usr == "erekiel" and i.pwd == """e601b363404e19a333aa92fc7aa2a75757325c32cfb0017abf847580d2677025""":
            reponse["idSession"] = clef(i.ip, i.usr)
            ficSession = os.path.join(repSessions, i.usr + ".txt")
            with open(ficSession,"w") as f : 
                f.write("%s %s %s\n" % (i.usr, i.ip, reponse["idSession"]))
            return repondre(reponse, "Bienvenue %s" % i.usr, True, printer)
        else : 
            return repondre(reponse, "mot de passe incorrect %s : %s " % (i.usr, i.pwd), False, printer)
            
    else : 
        
        # for it in os.environ.items():
            # reponse["commentaire"] += "%s : %s" % it
        
        return repondre(reponse, "pas usr ou pas pwd ou pas ip : [%s] [%s] [%s]" % (i.usr, i.pwd, i.ip), False, printer)
    
    return repondre(reponse,"J'aurais pas du arriver ici : [usr:%s] [pwd:%s] [ip:%s]" % (i.usr, i.pwd, i.ip), False, printer)

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