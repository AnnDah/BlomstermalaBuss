import QuerySQL

class Person(object):
    """description of class"""
    first_name = ''
    last_name = ''
    personal_number = ''

    #Adds a user
    def add_user(self, first_name, last_name, personal_number):
        new_person = Person()
        new_person.first_name = first_name
        new_person.last_name = last_name
        new_person.personal_number = personal_number

        QuerySQL.QuerySQL().add_user(new_person)

    #Get all persons
    def get_all_persons(self):
        return QuerySQL.QuerySQL().get_all_persons()

    #Get specific user
    def get_user(self, id):
        return QuerySQL.QuerySQL().get_person(id)

    #Edit a user with a specific id
    def edit_person(self, id, first_name, last_name, personal_number):
        new_person = Person()
        new_person.first_name = first_name
        new_person.last_name = last_name
        new_person.personal_number = personal_number
        
        QuerySQL.QuerySQL().update_person(id, new_person)

    #Deletes a user with a specific id
    def delete_person(self, id):
        QuerySQL.QuerySQL().delete_user(id)
        print 'delete person'


