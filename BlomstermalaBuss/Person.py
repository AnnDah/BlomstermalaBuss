import QuerySQL

class Person(object):
    """description of class"""
    first_name = ''
    last_name = ''
    personal_number = ''

    def add_user(self, first_name, last_name, personal_number):
        new_person = Person()
        new_person.first_name = first_name
        new_person.last_name = last_name
        new_person.personal_number = personal_number

        QuerySQL.QuerySQL().add_user(new_person)


