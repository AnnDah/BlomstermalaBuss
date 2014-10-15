import QuerySQL

class Person(object):
    """description of class"""
    first_name = ''
    last_name = ''
    personal_number = ''

    def add_user(self, first_name, last_name, personal_number):
        self.first_name = first_name
        self.last_name = last_name
        self.personal_number = personal_number
        QuerySQL.QuerySQL().add_user(self.first_name, self.last_name, self.personal_number)


