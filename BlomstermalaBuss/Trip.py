import QuerySQL

class Trip(object):
    """description of class"""
    bus = ''
    arrives_at = ''
    departs_from = ''
    price = 0.00
    weekday = '' #kanske kan man solve detta med en algoritm och bara ha en datetime som man sen tar ut veckodag, tid, datum etc
    start_time = ''
    end_time = ''

    #Get all trips
    def get_all_trips(self):
        return QuerySQL.QuerySQL().get_all_data('Trip')

