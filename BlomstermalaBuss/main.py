import Person
import Bus
import City

class main(object):
    """description of class"""

    #add person
    def add_user(self, first_name, last_name, personal_number):
        Person.Person().add_user(first_name, last_name, personal_number)

    #edit person
    def edit_person(self, id, first_name, last_name, personal_number):
        return Person.Person().edit_person(id, first_name, last_name, personal_number)

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
        
    #add trip
    #edit trip
    #delete trip

    #add booking
    #change booking
    #delete booking


