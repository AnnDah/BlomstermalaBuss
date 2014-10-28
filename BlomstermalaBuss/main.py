import Person
import Bus
import City
import Trip
import Booking
import Address
import Phone

class main(object):
    """description of class"""

    #add person
    def add_user(self, first_name, last_name, personal_number):
        new_person = Person.Person()
        new_person.first_name = first_name
        new_person.last_name = last_name
        new_person.personal_number = personal_number

        Person.Person().add_user(new_person)

    #edit person
    def edit_person(self, id, first_name, last_name, personal_number):
        Person.Person().edit_person(id, first_name, last_name, personal_number)

    #get all persons
    def get_all_persons(self):
        return Person.Person().get_all_persons()

    #get person
    def get_person(self, id):
        return Person.Person().get_user(id)

    #get person id, search on first name and last name
    def get_person_id(self, first_name, last_name):
        return Person.Person().get_person_id(first_name, last_name)

    #get person id, search on first name and last name
    def get_person_id(self, first_name, last_name):
        return Person.Person().get_person_id(first_name, last_name)

    #Get id of last added person
    def get_last_person_id(self):
        return Person.Person().get_last_id()

    #delete person
    def delete_person(self, id):
        Person.Person().delete_person(id)
    
    #add bus
    def add_bus(self, name, seats):
        new_bus = Bus.Bus()        
        new_bus.name = name
        new_bus.seats = seats
        Bus.Bus().add_bus(new_bus)

    #edit bus
    def edit_bus(self, id, name, seats):
        Bus.Bus().edit_bus(id, name, seats)

    #get bus
    def get_bus(self, id):
        return Bus.Bus().get_bus(id)        

    #get all buses
    def get_buses(self):
        return Bus.Bus().get_buses()        

    #delete bus
    def delete_bus(self, id):
        Bus.Bus().remove_bus(id)

    #add city
    def add_city(self, name, country):
        new_city = City.City()
        new_city.name = name
        new_city.country = country

        City.City().add_city(new_city)
    
    #edit city

    #get all cities
    def get_cities(self):
        return City.City().get_cities()

    #delete city
    def delete_city(self, id):
        City.City().remove_city(id)
        
    #get all trips
    def get_all_trips(self):
        return Trip.Trip().get_all_trips()

    #add trip
    def add_trip(self, depart, arrive, start, end, weekday, price, bus):
        new_trip = Trip.Trip()
        new_trip.departs_from = depart
        new_trip.arrives_at = arrive
        new_trip.start_time = start
        new_trip.end_time = end
        new_trip.weekday = weekday
        new_trip.price = price
        new_trip.bus = bus

        Trip.Trip().add_trip(new_trip)

    #edit trip
    #delete trip
    #search trip
    def search_trip(self, search):
        return Trip.Trip().search_trip(search)

    #add booking
    def add_booking(self, date, trip, person):
        new_booking = Booking.Booking()
        new_booking.date = date
        new_booking.trip = trip
        new_booking.person = person
        Booking.Booking().add_booking(new_booking)
    #change booking
    #delete booking
    #Get all bookings
    def get_all_bookings(self):
        return Booking.Booking().get_all_bookings()

    #add address
    def add_address(self, town, zipcode, street, person_id, country):
        Address.Address().add_address(town, zipcode, street, person_id, country)
    #change adress

    #Add phone number
    def add_phone(self, phone_number, person_id):
        new_phone = Phone.Phone()
        new_phone.phone_number = phone_number
        new_phone.person_id = person_id
        Phone.Phone().add_phone(new_phone)


