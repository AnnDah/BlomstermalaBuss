import QuerySQL

class Bus(object):
    """description of class"""
    
    name = ''
    seats = ''
    
    

    def add_bus(self, name, seats):
        new_bus = Bus()        
        new_bus.name = name
        new_bus.seats = seats

        QuerySQL.QuerySQL().add_bus(new_bus)
        

        
    