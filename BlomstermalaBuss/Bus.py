import QuerySQL

class Bus(object):
    """description of class"""

    ID = ''   
    name = ''
    seats = ''
    
    

    def add_bus(self, ID, name, seats):
        new_bus = Bus()
        new_bus.ID = ID
        new_bus.name = name
        new_bus.seats = seats

        QuerySQL.QuerySQL().add_bus(new_bus)
        

        
    