import QuerySQL
import Bus
import City

class Trip(object):
    """description of class"""
    bus = ''
    arrives_at = ''
    departs_from = ''
    price = 0.00
    weekday = ''
    start_time = ''
    end_time = ''

    #Get all trips
    def get_all_trips(self):
        return QuerySQL.QuerySQL().get_all_data('Trip')

    #add trip

    #edit trip

    #delete trip

    #search trip on depart from
    def search_trip(self, search):
        return QuerySQL.QuerySQL().search_trip(search)

