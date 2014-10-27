import QuerySQL
import Bus
import City

class Trip(object):
    """description of class"""
    bus = 0
    arrives_at = 0
    departs_from = 0
    price = 0.00
    weekday = ''
    start_time = 00.00
    end_time = 00.00

    #Get all trips
    def get_all_trips(self):
        return QuerySQL.QuerySQL().get_all_data('Trip')

    #add trip

    def add_trip(self, new_trip):
        QuerySQL.QuerySQL().add_trip(new_trip)


    #edit trip

    #delete trip

    #search trip on depart from
    def search_trip(self, search):
        return QuerySQL.QuerySQL().search_trip(search)

