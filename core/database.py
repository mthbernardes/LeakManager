#!/usr/local/bin/python3
# coding: utf-8

from core.models import models

class database(object):
    def insertLeak(self,username,email,password,database):
        db = models()
        db.leaks.insert(username=username,email=email,password=password,database=database)
        db.commit()

    def getLeaks(self,data,searchby):
        db = models()
        if searchby == 'email':
            results = db(db.leaks.email.contains(data,case_sensitive=False)).select()
        elif searchby == 'password':
            results = db(db.leaks.password.contains(data,case_sensitive=False)).select()
        return results

    def lastEntries(self,):
        db = models()
        results = db().select(db.leaks.ALL, orderby=~db.leaks.id,limitby=(0,10))
        return results

    def deleteLeak(self,leakid):
        db = models()
        db(db.leaks.id == leakid).delete()
        db.commit()

    def getAll(self,):
        db = models()
        results = db().select(db.leaks.ALL)
        #results = db(db.leaks.id > 0).select()
        return results

    def saveMassLeaks(self,leaks):
        allLeaks = list()
        for leak in leaks:
            leak = str(leak).strip()
            if leak:
                leak = leak.strip().split(',')
                if len(leak) == 4:
                    allLeaks.append({"email":leak[0],"username":leak[1],"password":leak[2],"database":leak[3]})
        db = models()
        db.leaks.bulk_insert(allLeaks)
        db.commit()

    def updatePassword(self,oldpass,newpass):
        db = models()
        total = db(db.leaks.password == oldpass).count()
        db(db.leaks.password == oldpass).update(password=newpass)
        db.commit()
        return total
