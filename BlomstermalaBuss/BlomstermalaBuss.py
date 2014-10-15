import main

class BlomstermalaBuss(object):
    
    print 'Are you a:'
    print '1: User'
    print '2: Admin'
    choice = raw_input('Enter choice: ')

    #User menu
    if choice == '1':
        print 'user menu'

    #Admin menu
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
            print 'What do you want to do?'
            print '1: See list of persons'
            print '2: Add person'
            print '3: Delete person'
            print '4: Edit person'
            choice = raw_input('Val: ')

            #See all persons
            if choice == '1':
                print QuerySQL.QuerySQL().get_all_users()

            #Add person
            elif choice == '2':
                first_name = raw_input('Add firstname: ')
                last_name = raw_input('Add last name: ')
                personal_number = raw_input('Add personal number: ')
                main.main().add_user(first_name, last_name, personal_number)

            #Delete person
            elif choice == '3':
                id = raw_input('Add ID to person to delete: ')
                main.main().delete_person(id)

            #Edit person
            elif choice == '4':
                print 'edit person'

            #Invalid choice
            else:
                print 'Invalid choice'

        #Bus menu
        elif choice == '2':
            print 'What do you want to do?'
            print '1: Add bus'
            print '2: Edit bus'
            print '3: Delete bus'
            choice = raw_input('Enter choice: ')

            #Add bus
            if choice == '1':                
                name = raw_input('Add Name: ')
                seats = raw_input('Add Seats ')
                main.main().add_bus(name, seats)

            #Edit bus
            elif choice == '2':
                print 'edit bus'

            #Delete bus
            elif choice == '3':
                print 'delete bus'
                id = raw_input('Add ID to person to delete: ')
                main.main().delete_bus(id)

            #Invalid choice
            else:
                print 'Invalid choice!'

        #City menu
        elif choice =='3':
            print 'city menu' 

        #Trip menu
        elif choice == '4':
            print 'trip menu'

        #Booking menu
        elif choice == '5':
            print 'Booking menu'

        #Invalid choice
        else:
            print 'Invalid choice'