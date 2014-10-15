import QuerySQL

class Trip(object):
    """description of class"""
    #Get all trips
    def get_all_trips(self):
        return QuerySQL.QuerySQL().get_all_data('Trip')

