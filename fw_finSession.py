#! /usr/bin/python3
# coding:utf-8


import time
import cgi
import os
import hashlib
import cgitb
import json

import fw_authentification

cgitb.enable()

if __name__ == "__main__":
    print("Content-Type: text/html\n\n")
    
    infSession = fw_authentification.infoSession()
    cmd = ""
    
    if os.path.isfile(os.path.join(fw_authentification.repSessions, "%s.txt" % infSession.usr)):
        cmd = "rm \"%s\"" % os.path.join(fw_authentification.repSessions, "%s.txt" % infSession.usr)
        os.system(cmd)
    
    r = {}
    
    fw_authentification.repondre(r, "Déconnecté.", True)