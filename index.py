#!/usr/local/bin/python3
# coding: utf-8

import hug
import time
import threading
from core.database import database
from core.templates import get_template

user,passwd = open('etc/leakManager.conf').read().split(':')
admin_area = hug.http(requires=hug.authentication.basic(hug.authentication.verify(user.strip(), passwd.strip())))


@admin_area.post('/massInsert',output=hug.output_format.html)
def massInsert(body,request,response):
    leaks = str(body['leakmass']).replace("'b","").split('\\n')
    count = len(leaks)
    db = database()
    thread = threading.Thread(target=db.saveMassLeaks, args=(leaks,))
    thread.start()
    message = 'You have loaded %d new leaks the process to register will happen in bakground!' % count
    return "<script>alert('%s');document.location = '/'</script>" % message

@admin_area.get('/delete/{leakid}',output=hug.output_format.html)
def deleteLeak(leakid):
    db = database()
    db.deleteLeak(int(leakid))
    message = 'leak deleted'
    return "<script>alert('%s');document.location = '/'</script>" % message

@admin_area.post('/singleInsert')
def singleInsert(body):
    checks = ['username','password','email','database']
    for c in checks:
        if c not in body:
            return False
    db = database()
    db.insertLeak(username=body['username'],email=body['email'],password=body['password'],database=body['database'])
    message = 'New leak created for e-mail %s' % body['email']
    return {'message':message}

@admin_area.post('/search')
def search(body):
    db = database()
    results = list()
    leaks = db.getEmail(body['email-search'])
    for leak in leaks:
        results.append({'id':leak.id,'email':leak.email,'username':leak.username,'password':leak.password,'database':leak.database})
    return results

@admin_area.get('/',output=hug.output_format.html)
def index():
    template = get_template('index.html')
    db = database()
    totalLeaks = len(db.getAll())
    lastLeaks = db.lastEntries()
    return template.render({'total':totalLeaks,'leaks':lastLeaks})

@admin_area.get('/static/img/{img_file}',output=hug.output_format.image('png'))
def staticimg(img_file):
    if '..' in img_file:
        raise
    return open('static/img/{}'.format(img_file),'rb')

@admin_area.get('/static/js/{static_file}',output=hug.output_format.html)
def staticjs(static_file):
    if '..' in static_file:
        raise
    print(static_file)
    return open('static/js/{}'.format(static_file)).read()

@admin_area.get('/static/css/{static_file}',output=hug.output_format.html)
def staticcss(static_file):
    if '..' in static_file:
        raise
    print(static_file)
    return open('static/css/{}'.format(static_file)).read()
