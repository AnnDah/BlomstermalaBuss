import QuerySQL
import dbConnector

class BlomstermalaBuss(object):
    print 'Vad vill du g�ra?'
    print '1: Se alla personer'
    print '2: L�gga till person'
    print '3: Ta bort person'
    choice = raw_input('Val: ')

    if choice == '1':
        #print all persons
        print QuerySQL.QuerySQL().get_all_users()

    elif choice == '2':
        #add person
        first_name = raw_input('Add firstname: ')
        last_name = raw_input('Add last name: ')
        personal_number = raw_input('Add personal number: ')
        QuerySQL.QuerySQL().add_user(first_name, last_name, personal_number)

    elif choice == '3':
        #delete person
        id = raw_input('Add ID to person to delete: ')
        QuerySQL.QuerySQL().delete_user(id)

    else:
        print 'Det var inget giltligt val :)'

    

