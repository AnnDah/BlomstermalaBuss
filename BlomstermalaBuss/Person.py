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

    #Edit a user with a specific id
    def edit_person(self, id):
        print 'edit person'

    #Deletes a user with a specific id
    def delete_person(self, id):
        QuerySQL.QuerySQL().delete_user(id)
        print 'delete person'


