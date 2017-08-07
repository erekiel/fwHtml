#! /usr/bin/python3
# coding:utf-8


import time
import cgi
import os
import hashlib
import cgitb

cgitb.enable()


# ficSession = "sessions.txt"

def verifCle(usr, ip, cle):
    if not cle or not ip or not usr: 
        return False
    
    ficSession = os.path.join(config.repSessions, usr.replace(":","_").replace(".","_") + ".txt")
    try : 
        with open(ficSession,"r") as f : 
            for l in f.readlines():
                if l.split()[1] == ip:
                    if l.split()[2] == cle:
                        return True
    except:
        return False
    
    return False


def clef(ip, usr):
    tmp = "%s%s%s" % (ip, usr, config.clePrivee)
    tmp = tmp.encode()
    return hashlib.sha256(tmp).hexdigest()

if __name__ == "__main__" : 
    print("Content-Type: text/html\n\n")
    form = cgi.FieldStorage()
    usr = form.getvalue("usr")
    pwd = form.getvalue("pwd")
    
    if "REMOTE_ADDR" in os.environ.keys():
        ip  = os.environ["REMOTE_ADDR"]
    else :
        usr = None
    
    
    # if pwd is not None:
        # tmp = pwd.encode()
        # tmp = hashlib.sha256(tmp).hexdigest()
    
    # if usr == "erekiel" and tmp == """e601b363404e19a333aa92fc7aa2a75757325c32cfb0017abf847580d2677025""":
    
    # on envoie le psw en crypte
    if usr == "erekiel" and pwd == """e601b363404e19a333aa92fc7aa2a75757325c32cfb0017abf847580d2677025""":
        cle = clef(ip, usr)
        ficSession = os.path.join(config.repSessions, usr.replace(":","_").replace(".","_") + ".txt")
        with open(ficSession,"w") as f : 
            f.write("%s %s %s\n" % (usr, ip, cle))
        print(cle)
    else :
        print("")
    
# def setAuth(ip, nom):
    # return "zarmaOkTeslogg"
    
# form = cgi.FieldStorage()
# print("Content-Type: text/html\n\n")
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