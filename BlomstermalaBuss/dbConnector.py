#BlomstermalaBuss.py
#Created by Annika Magnusson 2014-10-13

import MySQLdb;

class dbConnector(object):
    """description of class"""

    def get_data(self, my_string):
        db = MySQLdb.connect(host="195.178.235.60", user="ad4259", db="ad4259", passwd="apa123", charset="utf8")
        cur = db.cursor()
        cur.execute(my_string)
        return cur.fetchall()
        db.close()

    def add_data(self, my_string):
        db = MySQLdb.connect(host="195.178.235.60", user="ad4259", db="ad4259", passwd="apa123", charset="utf8")
        cur = db.cursor()
        cur.execute(my_string)
        db.commit()
        db.close()

    def remove_data(self, my_string):
        db = MySQLdb.connect(host="195.178.235.60", user="ad4259", db="ad4259", passwd="apa123", charset="utf8")
        cur = db.cursor()
        cur.execute(my_string)
        db.commit()
        db.close()
