import QuerySQL

class City(object):
    """description of class"""
    name = ''
    country = ''
    
    #add city
    def add_city(self, new_city):
        QuerySQL.QuerySQL().add_city(new_city)

    #remove city
    def remove_city(self, id):
        QuerySQL.QuerySQL().delete_city(id)
        print 'delete city'

    #get all cities
    def get_cities(self):
        return QuerySQL.QuerySQL().get_cities()

    #Get depart cities
    def get_depart_cities(self):
        return QuerySQL.QuerySQL().get_depart_cities()
        