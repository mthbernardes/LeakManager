#!/usr/local/bin/python3
# coding: utf-8

from core.models import models

class database(object):
    def insertLeak(self,username,email,password,database):
        db = models()
        db.leaks.insert(username=username,email=email,password=password,database=database)
        db.commit()
        self.addCounter(1)

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
        self.delCounter()

    def getAll(self,):
        db = models()
        results = db().select(db.leaks.ALL)
        return results

    def saveMassLeaks(self,leaks):
        allLeaks = list()
        counter = 0
        for leak in leaks:
            leak = str(leak).strip()
            if leak:
                leak = leak.strip().split(',')
                if len(leak) == 4:
                    counter += 1
                    allLeaks.append({"email":leak[0],"username":leak[1],"password":leak[2],"database":leak[3]})
        db = models()
        db.leaks.bulk_insert(allLeaks)
        db.commit()
        self.addCounter(counter)

    def addCounter(self,n):
        db = models()
        total = db(db.counter.id == 1).select().first()
        totalLeaks = total.total if total else 0
        db.counter.update_or_insert(db.counter.id==1,total=totalLeaks+n)
        db.commit()

    def delCounter(self,):
        db = models()
        total = db(db.counter.id == 1).select().first()
        totalLeaks = total.total if total else 0
        if totalLeaks > 0:
            db(db.counter.id == 1).update(total=totalLeaks-1)
            db.commit()

    def getTotal(self,):
        db = models()
        total = db(db.counter.id == 1).select().first()
        return total.total if total else 0

    def updatePassword(self,oldpass,newpass):
        db = models()
        total = db(db.leaks.password == oldpass).count()
        db(db.leaks.password == oldpass).update(password=newpass)
        db.commit()
        return total
