import main

class BlomstermalaBuss(object):
    
    print 'Are you a:'
    print '1: User'
    print '2: Admin'
    choice = raw_input('Enter choice: ')

    if choice == '1':
        print 'user menu'

    elif choice == '2':
        print 'Enter menu to go to'
        print '1: Person'
        print '2: Bus'
        print '3: City'
        print '4: Trip'
        print '5: Booking'
        choice = raw_input('Enter choice: ')
        #Person menu
        if choice == '1':
            print 'Vad vill du göra?'
            print '1: Se alla personer'
            print '2: Lägga till person'
            print '3: Ta bort person'
            choice = raw_input('Val: ')
            #See all persons
            if choice == '1':
                #print all persons
                print QuerySQL.QuerySQL().get_all_users()
            #Add person
            elif choice == '2':
                #add person
                first_name = raw_input('Add firstname: ')
                last_name = raw_input('Add last name: ')
                personal_number = raw_input('Add personal number: ')
                main.main().add_user(first_name, last_name, personal_number)
            #Delete person
            elif choice == '3':
                #delete person
                id = raw_input('Add ID to person to delete: ')
                main.main().delete_person(id)
            #Invalid choice
            else:
                print 'Det var inget giltligt val :)'
        #Bus menu
        elif choice == '2':
            print 'What do you want to do?'
            print '1: Add bus'
            print '2: Edit bus'
            print '3: Delete bus'
            choice = raw_input('Enter choice: ')

            if choice == '1':
                #Add bus                 
                name = raw_input('Add Name: ')
                seats = raw_input('Add Seats ')
                main.main().add_bus(name, seats)

            elif choice == '2':
                print 'edit bus'

            elif choice == '3':
                print 'delete bus'

            else:
                print 'Invalid choice!'

        elif choice =='3':
            print 'trip menu' 

        elif choice == '4':
            print 'booking menu'