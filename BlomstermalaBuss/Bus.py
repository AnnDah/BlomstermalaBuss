import QuerySQL

class Bus(object):
    """description of class"""
    
    name = ''
    seats = ''
    
    
        #add
    def add_bus(self, name, seats):
        new_bus = Bus()        
        new_bus.name = name
        new_bus.seats = seats

        QuerySQL.QuerySQL().add_bus(new_bus)

        #Get specific bus
    def get_bus(self, id):
        return QuerySQL.QuerySQL().get_bus(id)

        #edit
    def edit_bus(self, id, name, seats):
        new_bus = Bus()        
        new_bus.name = name
        new_bus.seats = seats

        QuerySQL.QuerySQL().update_bus(id)

    ##Edit a user with a specific id
    #def edit_person(self, id, first_name, last_name, personal_number):
    #    new_person = Person()
    #    new_person.first_name = first_name
    #    new_person.last_name = last_name
    #    new_person.personal_number = personal_number
        
    #    QuerySQL.QuerySQL().update_person(id, new_person)

        #remove 
    def remove_bus(self, id):
        QuerySQL.QuerySQL().delete_bus(id)
        print 'delete bus'
        

        
    