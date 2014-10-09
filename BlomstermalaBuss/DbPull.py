class DbPull(object):
    """description of class"""

    import MySQLdb

    db = MySQLdb.connect(host="195.178.235.60", user="ad4259", db="ad4259", passwd="apa123", charset="latin1")
        
    cur = db.cursor()
    SQLString="Select * from Person"
    cur.execute(SQLString)
    result = cur.fetchall()
    
    print result


