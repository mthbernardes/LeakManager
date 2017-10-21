from core.models import models

class database(object):
    def insertLeak(self,username,email,password,database):
        db = models()
        db.leaks.insert(username=username,email=email,password=password,database=database)
        db.commit()

    def getEmail(self,email):
        db = models()
        results = db(db.leaks.email.contains(email,case_sensitive=False)).select()
        #results = db(db.leaks.email.like(email)).select()
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
        print("THREAD STARTED")
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
        print("END OF THREAD")
