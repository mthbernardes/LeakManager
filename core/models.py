#!/usr/local/bin/python3
# coding: utf-8

from pydal import DAL, Field

class models(object):
    def __new__(self,):
        #dalString  = 'mongodb://localhost/leakManager' # New counter solution does not work with mongo, because the id of a entry is not predictable, use sqlite, it works fine, even with more then 1Mi leaks.
        dalString  = 'sqlite://leakManager.db'  #uncomment to use sqlite
        db = DAL(dalString,migrate=True)
        db.define_table('leaks',
            Field('username'),
            Field('email'),
            Field('password'),
            Field('database'))
        db.define_table('counter',
            Field('total','integer'))
        return db
