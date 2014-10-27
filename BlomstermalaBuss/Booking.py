import QuerySQL

class Booking(object):
    """description of class"""

    trip = 0
    date = ''
    person = 0

    #Add booking on Trip.ID
    def add_booking(self, new_booking):
        QuerySQL.QuerySQL().add_booking(new_booking)

    #Edit booking

    #Delete booking on ID

    #See all bookings on specific date and specific trip

    #See bookings on Person.ID




