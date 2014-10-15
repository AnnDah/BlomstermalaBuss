import QuerySQL #ta bort
import dbConnector #ta bort
import main

class BlomstermalaBuss(object):
    print 'Vad vill du göra?'
    print '1: Se alla personer'
    print '2: Lägga till person'
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
        main.main().add_user(first_name, last_name, personal_number)

    elif choice == '3':
        #delete person
        id = raw_input('Add ID to person to delete: ')
        main.main().delete_person(id)

    elif choice == '4':
        #Add bus                 
        name = raw_input('Add Name: ')
        seats = raw_input('Add Seats ')
        main.main().add_bus(name, seats)
        


    else:
        print 'Det var inget giltligt val :)'

    

