import dbConnector

class QuerySQL(object):
    """description of class"""
    db_connection = dbConnector.dbConnector()

    #Get all data in specific table
    def get_all_data(self, table):
        query = 'SELECT * from %s' % (table)
        result = self.db_connection.get_data(query)
        return result

    #Add person
    def add_user(self, new_person):
        query = 'INSERT INTO Person (FirstName, LastName, PersonalNumber) VALUES (\'%s\', \'%s\', \'%s\')' % (new_person.first_name, new_person.last_name, new_person.personal_number)
        self.db_connection.add_data(query)

    #Delete person
    def delete_user(self, id):
        query = 'DELETE FROM Person WHERE ID=%s' % (id)
        self.db_connection.remove_data(query)

    #Delete bus
    def delete_bus(self, id):
        query = 'DELETE FROM Bus WHERE ID=%s' % (id)
        self.db_connection.remove_data(query)

    #Add bus
    def add_bus(self, new_bus):
        query = 'INSERT INTO Bus (Name, Seats) VALUES (\'%s\', \'%s\')' % (new_bus.name, new_bus.seats)
        self.db_connection.add_data(query)

    #Add city
    def add_city(self, new_city):
        query = 'INSERT INTO City (Name, Country) VALUES (\'%s\', \'%s\')' % (new_city.name, new_city.country)
        self.db_connection.add_data(query)

    #Delete city
    def delete_city(self, id):
        query = 'DELETE FROM City WHERE ID=%s' % (id)
        self.db_connection.remove_data(query)

    #Get info about specific person
    def get_person(self, id):
        query = 'SELECT ID, FirstName, LastName, PersonalNumber FROM Person WHERE ID=%s' % (id)
        result = self.db_connection.get_data(query)
        return result

    #Update information about person
    def update_person(self, id, new_person):
        query = 'UPDATE Person SET FirstName=\'%s\', LastName=\'%s\', PersonalNumber=\'%s\' WHERE ID=\'%s\'' % (new_person.first_name, new_person.last_name, new_person.personal_number, id)
        self.db_connection.add_data(query)

    #Get info about specific bus
    def get_bus(self, id):
        query = 'SELECT ID, Name, Seats FROM Bus WHERE ID=%s' % (id)
        result = self.db_connection.get_data(query)
        return result

    #Update information about bus
    def update_bus(self, id, new_bus):
        query = 'UPDATE Bus SET Name=\'%s\', Seats=\'%s\' WHERE ID=\'%s\'' % (new_bus.name, new_bus.seats, id)
        self.db_connection.add_data(query)

    #Update information about person
    def update_person(self, id, new_person):
        query = 'UPDATE Person SET FirstName=\'%s\', LastName=\'%s\', PersonalNumber=\'%s\' WHERE ID=\'%s\'' % (new_person.first_name, new_person.last_name, new_person.personal_number, id)
        self.db_connection.add_data(query)

    #Search trip on depart from
    def search_trip(self, search):
        query = 'SELECT * FROM Trip WHERE DepartsFrom=(SELECT ID FROM City WHERE Name=\'%s\')' % (search)
        return self.db_connection.get_data(query)

    def add_address(self, new_adress):
        query = 'INSERT INTO Address (Town, Zipcode, Street, PersonID, Country) (\'%s\', \'%s\', \'%s\', \'%s\', \'%s\')' % (new_address.town, new_address.zipcode, new_address.street, new_address.person_id, country)
        self.db_connection.add_data(query)

    def get_last_person_id(self, id):
        query = 'SELECT ID FROM Person ORDER BY ID DESC LIMIT 1'
        self.db_connection.add_data(query)

            #            query = text("""INSERT INTO HR_PunchBatch
    #(StoreID, UserID, Source,Timestamp,Status)
    #    VALUES (:StoreID,:UserID,:Source,NOW(),:Status)""")

    #g.engine.execute(query,
    #    StoreID=StoreID,
    #    UserID=session['UserID'],
    #    Source=source,
    #    Status='New')

    #batch_id = g.engine.execute('SELECT LAST_INSERT_ID() AS id').fetchone()
    #return batch_id['id']

    #    #Add city
    #def add_city(self, new_city):
    #    query = 'INSERT INTO City (Name, Country) VALUES (\'%s\', \'%s\')' % (new_city.name, new_city.country)
    #    self.db_connection.add_data(query)