import Person
import Bus
import City
import Trip

class main(object):
    """description of class"""

    #add person
    def add_user(self, first_name, last_name, personal_number):
        Person.Person().add_user(first_name, last_name, personal_number)

    #edit person
    def edit_person(self, id, first_name, last_name, personal_number):
        Person.Person().edit_person(id, first_name, last_name, personal_number)

    #get all persons
    def get_all_persons(self):
        return Person.Person().get_all_persons()

    #get person
    def get_person(self, id):
        return Person.Person().get_user(id)

    #delete person
    def delete_person(self, id):
        Person.Person().delete_person(id)
    
    #add bus
    def add_bus(self, name, seats):
        Bus.Bus().add_bus(name, seats)

    #edit bus
    def edit_bus(self, id, name, seats):
        Bus.Bus().edit_bus(id, name, seats)


    #get bus
    def get_bus(self, id):
        return Bus.Bus().get_bus(id)        

    #delete bus
    def delete_bus(self, id):
        Bus.Bus().remove_bus(id)

    #add city
    def add_city(self, name, country):
        City.City().add_city(name, country)
    #edit city

    #delete city
    def delete_city(self, id):
        City.City().remove_city(id)
        
    #get all trips
    def get_all_trips(self):
        return Trip.Trip().get_all_trips()
    #add trip
    #edit trip
    #delete trip

    #add booking
    #change booking
    #delete booking


