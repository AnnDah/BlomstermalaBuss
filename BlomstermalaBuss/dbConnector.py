#BlomstermalaBuss.py
#Created by Annika Magnusson 2014-10-13

import MySQLdb;

class dbConnector(object):
    """description of class"""
    db
    def __init__(self):
        self.db = MySQLdb.connect(host="195.178.235.60", user="ad4259", db="ad4259", passwd="apa123", charset="latin1")

    def create_db_connection():
        return db

    def close_db_connection():
        print "Closing connection"