import QuerySQL

class Bus(object):
    """description of class"""
    
    name = ''
    seats = 0
    
    #add bus
    def add_bus(self, new_bus):
        QuerySQL.QuerySQL().add_bus(new_bus)

    #Get specific bus
    def get_bus(self, id):
        return QuerySQL.QuerySQL().get_bus(id)

    #edit
    def edit_bus(self, id, name, seats):
        new_bus = Bus.Bus()        
        new_bus.name = name
        new_bus.seats = seats

        QuerySQL.QuerySQL().update_bus(id, new_bus)

    #remove bus
    def remove_bus(self, id):
        QuerySQL.QuerySQL().delete_bus(id)
        print 'delete bus'
    
    #get buses
    def get_buses(self):
        return QuerySQL.QuerySQL().get_buses()
        

        
    