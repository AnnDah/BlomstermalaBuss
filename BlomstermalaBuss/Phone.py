import QuerySQL
class Phone(object):
    """description of class"""

    phone_number = ''
    person_id = 0

    def add_phone(self, new_phone):
        QuerySQL.QuerySQL().add_phone(new_phone)



