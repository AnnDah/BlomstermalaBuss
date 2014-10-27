import QuerySQL

class Person(object):
    """description of class"""
    first_name = ''
    last_name = ''
    personal_number = ''

    #Adds a user
    def add_user(self, new_person):
        QuerySQL.QuerySQL().add_user(new_person)

    #Get all persons
    def get_all_persons(self):
        return QuerySQL.QuerySQL().get_all_data('Person')

    #Get specific user
    def get_user(self, id):
        return QuerySQL.QuerySQL().get_person(id)

    #Edit a user with a specific id
    def edit_person(self, id, first_name, last_name, personal_number):
        new_person = Person.Person()
        new_person.first_name = first_name
        new_person.last_name = last_name
        new_person.personal_number = personal_number

        QuerySQL.QuerySQL().update_person(id, new_person)

    #Deletes a user with a specific id
    def delete_person(self, id):
        QuerySQL.QuerySQL().delete_user(id)

    #get person id on first and last name
    def get_person_id(self, first_name, last_name):
        return QuerySQL.QuerySQL().get_person_id(first_name, last_name)

    #Get id of last added person
    def get_last_id(self):
        QuerySQL.QuerySQL().get_last_person_id()


            #            query = text("""INSERT INTO HR_PunchBatch
    #(StoreID, UserID, Source,Timestamp,Status)
    #    VALUES (:StoreID,:UserID,:Source,NOW(),:Status)""")

    #g.engine.execute(query,
    #    StoreID=StoreID,
    #    UserID=session['UserID'],
    #    Source=source,
    #    Status='New')

    #batch_id = g.engine.execute('SELECT LAST_INSERT_ID() AS id').fetchone()
    #return batch_id['id']


