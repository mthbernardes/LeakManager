#!/usr/local/bin/python3
# coding: utf-8

from pydal import DAL, Field

class models(object):
    def __new__(self,):
        #dalString  = 'mongodb://localhost/leakManager' #uncomment to use mongodb
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
