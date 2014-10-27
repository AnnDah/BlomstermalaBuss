import main

class CLI(object):
    """description of class"""

    #Main menu
    def start(self):
        choice = -1

        while choice != '0':
            print 'Are you a:'
            print '1: User'
            print '2: Admin'
            print '0: Exit application'
            choice = raw_input('Enter choice: ')

            if choice == '1':
                self.user_menu()

            elif choice == '2':
                self.admin_menu()

            elif choice == '0':
                print ''

            else:
                print 'Invalid choice'

    #User menu
    def user_menu(self):
        self.add_new_booking()

    #Add new booking
    def add_new_booking(self):
        first_name = raw_input('Enter your first name: ')
        last_name = raw_input('Enter your last name: ')
        persons = main.main().get_person_id(first_name, last_name)
        for line in persons:
            print line
        person = raw_input('Enter your user ID: ')
        #BlomstermalaBuss().test_print()
        search = raw_input('Enter city to depart from: ')
        trips = main.main().search_trip(search)
        for line in trips:
            print line
        trip = raw_input('Enter ID for trip to book: ')
        date = raw_input('Enter wich date you would like to go: ')
        main.main().add_booking(date, trip, person)

    #Admin menu
    def admin_menu(self):
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
            choice = raw_input('Enter choice: ')

            #See all persons
            if choice == '1':
                result = main.main().get_all_persons()
                for line in result:
                    print line

            #Add person
            elif choice == '2':
                first_name = raw_input('Add first name: ')
                last_name = raw_input('Add last name: ')
                personal_number = raw_input('Add personal number: ')
                main.main().add_user(first_name, last_name, personal_number)


             



            #Delete person
            elif choice == '3':
                id = raw_input('Add ID to person to delete: ')
                main.main().delete_person(id)

            #Edit person
            elif choice == '4':
                id = raw_input('Enter person ID: ')
                print main.main().get_person(id)
                choice = raw_input('Do you want to edit this persons information? Y or N: ').upper()
                    #Yes edit
                if choice == 'Y':
                    print 'YES'
                    first_name = raw_input('Add first name: ')
                    last_name = raw_input('Add last name: ')
                    personal_number = raw_input('Add personal number: ')
                    main.main().edit_person(id, first_name, last_name, personal_number)
                
                #No don't edit
                elif choice == 'N':
                    print 'NO'

                #Invalid choice
                else:
                    print 'Invalid choice'

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
                id = raw_input('Enter bus ID: ')
                print main.main().get_bus(id)
                choice = raw_input('Do you want to edit this bus information? Y or N: ').upper()

                #Yes edit bus
                if choice == 'Y':
                    print 'YES'
                    name = raw_input('Add name: ')
                    seats = raw_input('Add seats: ')                                 
                    main.main().edit_bus(id, name, seats)                        
                
                #No don't edit bus
                elif choice == 'N':
                    print 'NO'

                #Invalid choice
                else:
                    print 'Invalid choice'


            #Delete bus
            elif choice == '3':
                print 'delete bus'
                id = raw_input('Add ID to bus to delete: ')
                main.main().delete_bus(id)

            #Invalid choice
            else:
                print 'Invalid choice!'

        #City menu
        elif choice =='3':
            print 'What do you want to do?'
            print '1: Add City'
            print '2: Edit City'
            print '3: Delete City'
            choice = raw_input('Enter choice: ')

            #Add city
            if choice == '1':                
                name = raw_input('Add Name of City: ')
                country = raw_input('Add Country ')
                main.main().add_city(name, country)                

            #Edit city
            elif choice == '2':
                print 'edit City'

            #Delete city
            elif choice == '3':
                print 'delete City'
                id = raw_input('Add ID to City to delete: ')
                main.main().delete_city(id)                

            #Invalid choice
            else:
                print 'Invalid choice!' 

        #Trip menu
        elif choice == '4':
            print 'What do you want to do?'
            print '1: See all trips'
            print '2: Add trip'
            print '3: Edit trip'
            print '4: Delete trip'
            choice = raw_input('Enter choice: ')
            
            if choice == '1':
                print main.main().get_all_trips()

            elif choice == '2':
                print main.main().get_cities()
                depart = raw_input('Enter ID for depart city: ')
                arrive = raw_input('Enter ID for arrive city: ')
                start = raw_input('Enter start time (00.00): ')
                end = raw_input('Enter end time (00.00): ')
                weekday = raw_input('Enter weekday: ')
                price = raw_input('Enter price (00.00): ')
                print main.main().get_buses()
                bus = raw_input('Enter bus ID: ')
                main.main().add_trip(depart, arrive, start, end, weekday, price, bus)

            else:
                print 'Invalid choice'

        #Booking menu
        elif choice == '5':
            print 'What do you want to do?'
            print '1: Add booking'
            print '2: Delete booking'
            print '3: See all bookings'
            print '4: See bookings on a specific date'
            print '5: See bookings for a specific user'
            choice = raw_input('Enter choice: ')
            #Add booking
            if choice == '1':
                self.add_new_booking()
            #Delete booking
            elif choice == '2':
                print '2'
            #See all bookings
            elif choice == '3':
                print main.main().get_all_bookings()
            #See bookings on a specific date
            elif choice == '4':
                print '4'
            #See bookings on specicfic user
            elif choice == '5':
                print '5'
            #Invalid choice
            else:
                print 'Invalid choice'

        #Invalid choice
        else:
            print 'Invalid choice'