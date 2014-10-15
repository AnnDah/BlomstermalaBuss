import dbConnector

class QuerySQL(object):
    """description of class"""
    db_connection = dbConnector.dbConnector()

    def get_all_users(self):
        query = 'SELECT * FROM Person'
        result = self.db_connection.get_data(query)
        return result

    def add_user(self, new_person):
        query = 'INSERT INTO Person (FirstName, LastName, PersonalNumber) VALUES (\'%s\', \'%s\', \'%s\')' % (new_person.first_name, new_person.last_name, new_person.personal_number)
        self.db_connection.add_data(query)

    def delete_user(self, id):
        query = 'DELETE FROM Person WHERE ID=%s' % (id)
        self.db_connection.remove_data(query)

    def delete_bus(self, id):
        query = 'DELETE FROM Bus WHERE ID=%s' % (id)
        self.db_connection.remove_data(query)

    def add_bus(self, new_bus):
        query = 'INSERT INTO Bus (Name, Seats) VALUES (\'%s\', \'%s\')' % (new_bus.name, new_bus.seats)
        self.db_connection.add_data(query)

    def add_city(self, new_city):
        query = 'INSERT INTO City (Name, Country) VALUES (\'%s\', \'%s\')' % (new_city.name, new_city.country)
        self.db_connection.add_data(query)