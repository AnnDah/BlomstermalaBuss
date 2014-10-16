import QuerySQL

class Trip(object):
    """description of class"""
    bus = ''
    arrives_at = ''
    departs_from = ''

    #Get all trips
    def get_all_trips(self):
        return QuerySQL.QuerySQL().get_all_data('Trip')

