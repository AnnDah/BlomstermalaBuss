import QuerySQL

class City(object):
    """description of class"""


    
    name = ''
    country = ''
    
        # add
    def add_city(self, name, country):
        new_city = City()
        new_city.name = name
        new_city.country = country

        QuerySQL.QuerySQL().add_city(new_city)

        # remove
    def remove_city(self, name, country):
        QuerySQL.QuerySQL().delete_bus(id)
        