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
        #search trip
        #book trip

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
            self.person_menu()

        #Bus menu
        elif choice == '2':
            self.bus_menu()

        #City menu
        elif choice =='3':
            self.city_menu() 

        #Trip menu
        elif choice == '4':
            self.trip_menu()

        #Booking menu
        elif choice == '5':
            self.booking_menu()

        #Invalid choice
        else:
            print 'Invalid choice'

    #Add new booking
    def add_new_booking(self):
        first_name = raw_input('Enter your first name: ')
        last_name = raw_input('Enter your last name: ')
        persons = main.main().get_person_id(first_name, last_name)
        print '{:<4}'.format('ID'), '{:<20}'.format('Name'), '{:<10}'.format('Personal number')
        for line in persons:
            print '{:<4}'.format(line['ID']), '{:<20}'.format(line['FirstName'] + ' ' + line['LastName']), '{:<10}'.format(line['PersonalNumber'])
        person = raw_input('Enter your user ID: ')
        search = raw_input('Enter city to depart from: ')
        trips = main.main().search_trip(search)
        print 'Departures from: %s' %(search)
        print '{:<4}'.format('ID'), '{:<6}'.format('Starts'), '{:<5}'.format('Ends'), '{:<8}'.format('Weekday'), '{:<6}'.format('Price'), '{:<10}'.format('Departs'), '{:<10}'.format('Arrives')
        for line in trips:
            print '{:<4}'.format(line['ID']), '{:<6}'.format(line['Start']), '{:<5}'.format(line['Ends']), '{:<8}'.format(line['Weekday']), '{:<6}'.format(line['Price']), '{:<10}'.format(line['DepartsFrom']), '{:<10}'.format(line['ArrivesAt'])
        trip = raw_input('Enter ID for trip to book: ')
        date = raw_input('Enter wich date you would like to go: ')
        main.main().add_booking(date, trip, person)

    #Person menu
    def person_menu(self):
            print 'What do you want to do?'
            print '1: See list of persons'
            print '2: Add person'
            print '3: Delete person'
            print '4: Edit person'
            choice = raw_input('Enter choice: ')

            #See all persons
            if choice == '1':
                result = main.main().get_all_persons()
                print '{:<4}'.format('ID'), '{:<20}'.format('Name'), '{:<10}'.format('Personal number')
                for line in result:
                    print '{:<4}'.format(line['ID']), '{:<20}'.format(line['FirstName'] + ' ' + line['LastName']), '{:<10}'.format(line['PersonalNumber'])

            #Add user
            elif choice == '2':
                #add person
                first_name = raw_input('Add first name: ')
                last_name = raw_input('Add last name: ')
                personal_number = raw_input('Add personal number: ')
                main.main().add_user(first_name, last_name, personal_number)
                
                #get last added person id 
                reslist = main.main().get_last_person_id()
                for line in reslist:
                    last_added = line['ID']
                
                #add address
                street = raw_input('Add street: ')
                zipcode = raw_input('Add your zipcode: ')
                town = raw_input('Add town of recidence: ')
                person_id = last_added
                country = raw_input('Add Country: ')
                main.main().add_address(town, zipcode, street, person_id, country)
                
                #add phone nummber
                phone_number = raw_input('Enter phone number: ')
                main.main().add_phone(phone_number, last_added)   

            #Delete person
            #Doesn't work yet
            elif choice == '3':
                id = raw_input('Add ID to person to delete: ')
                main.main().delete_person(id)

            #Edit person
            elif choice == '4':
                id = raw_input('Enter person ID: ')
                result = main.main().get_person(id)
                print '{:<4}'.format('ID'), '{:<20}'.format('Name'), '{:<10}'.format('Personal number')
                for line in result:
                    print '{:<4}'.format(line['ID']), '{:<20}'.format(line['FirstName'] + ' ' + line['LastName']), '{:<10}'.format(line['PersonalNumber'])
                choice = raw_input('Do you want to edit this persons information? Y or N: ').upper()
                #Yes edit
                if choice == 'Y':
                    print 'Please enter information about the selected person'
                    first_name = raw_input('Add first name: ')
                    last_name = raw_input('Add last name: ')
                    personal_number = raw_input('Add personal number: ')
                    main.main().edit_person(id, first_name, last_name, personal_number)
                
                #No don't edit
                elif choice == 'N':
                    print 'You choose not to edit the information.'

                #Invalid choice
                else:
                    print 'Invalid choice'

            #Invalid choice
            else:
                print 'Invalid choice'

    #Bus menu
    def bus_menu(self):
        print 'What do you want to do?'
        print '1: Add bus'
        print '2: Edit bus'
        print '3: Delete bus'
        print '4: See list of available buses'
        choice = raw_input('Enter choice: ')

        #Add bus
        if choice == '1':
            name = raw_input('Add Name: ')
            seats = raw_input('Add Seats ')
            main.main().add_bus(name, seats)

        #Edit bus
        elif choice == '2':                            
            id = raw_input('Enter bus ID: ')
            result = main.main().get_bus(id)
            print '{:<4}'.format('ID'), '{:<12}'.format('Name'), '{:<5}'.format('Seats')
            for line in result:
                print '{:<4}'.format(line['ID']), '{:<12}'.format(line['Name']), '{:<5}'.format(line['Seats'])
            choice = raw_input('Do you want to edit this bus information? Y or N: ').upper()

            #Yes edit bus
            if choice == 'Y':
                print 'Please enter information about the selected bus.'
                name = raw_input('Add name: ')
                seats = raw_input('Add seats: ')                                 
                main.main().edit_bus(id, name, seats)                        
                
            #No don't edit bus
            elif choice == 'N':
                print 'You choose not to edit the information.'

            #Invalid choice
            else:
                print 'Invalid choice'


        #Delete bus
        #Doesn't work yet
        elif choice == '3':
            print 'delete bus'
            id = raw_input('Add ID to bus to delete: ')
            main.main().delete_bus(id)

        #See list of buses
        elif choice == '4':
            result = main.main().get_buses()
            print '{:<4}'.format('ID'), '{:<12}'.format('Name'), '{:<5}'.format('Seats')
            for line in result:
                print '{:<4}'.format(line['ID']), '{:<12}'.format(line['Name']), '{:<5}'.format(line['Seats'])

        #Invalid choice
        else:
            print 'Invalid choice!'

    #City menu
    def city_menu(self):
        print 'What do you want to do?'
        print '1: Add city'
        print '2: Edit city'
        print '3: Delete city'
        print '4: See list of citys'
        choice = raw_input('Enter choice: ')

        #Add city
        if choice == '1':                
            name = raw_input('Add Name of City: ')
            country = raw_input('Add Country ')
            main.main().add_city(name, country)                

        #Edit city
        #Doesn't work yet
        elif choice == '2':
            print 'edit City'

        #Delete city
        #Doesn't work yet
        elif choice == '3':
            print 'delete City'
            id = raw_input('Add ID to City to delete: ')
            main.main().delete_city(id)  
            
        #See list of cities
        #Doesn't work yet
        elif choice == '4':
            print 'See list of citys'
            result = main.main().get_cities()
            print '{:<4}'.format('ID'), '{:<20}'.format('Name'), '{:<20}'.format('Country')
            for line in result:
                print '{:<4}'.format(line['ID']), '{:<20}'.format(line['Name']), '{:<20}'.format(line['Country'])        

        #Invalid choice
        else:
            print 'Invalid choice!'

    #Trip menu
    def trip_menu(self):
        print 'What do you want to do?'
        print '1: See all trips'
        print '2: Add trip'
        print '3: Edit trip'
        print '4: Delete trip'
        choice = raw_input('Enter choice: ')
            
        if choice == '1':
            trips = main.main().get_all_trips()
            print '{:<4}'.format('ID'), '{:<6}'.format('Starts'), '{:<5}'.format('Ends'), '{:<8}'.format('Weekday'), '{:<6}'.format('Price'), '{:<10}'.format('Departs'), '{:<10}'.format('Arrives')
            for line in trips:
                print '{:<4}'.format(line['ID']), '{:<6}'.format(line['Start']), '{:<5}'.format(line['Ends']), '{:<8}'.format(line['Weekday']), '{:<6}'.format(line['Price']), '{:<10}'.format(line['DepartsFrom']), '{:<10}'.format(line['ArrivesAt'])

        elif choice == '2':
            cities = main.main().get_cities()
            for line in cities:
                print line
            depart = raw_input('Enter ID for depart city: ')
            arrive = raw_input('Enter ID for arrive city: ')
            start = raw_input('Enter start time (00.00): ')
            end = raw_input('Enter end time (00.00): ')
            weekday = raw_input('Enter weekday: ')
            price = raw_input('Enter price (00.00): ')
            buses = main.main().get_buses()
            for line in buses:
                print line
            bus = raw_input('Enter bus ID: ')
            main.main().add_trip(depart, arrive, start, end, weekday, price, bus)

        #Edit trip
        #Doesn't work yet
        elif choice == '3':
            print 'Edit trip'

        #Delete trip
        #Doesn't work yet
        elif choice == '4':
            print 'Delete trip'

        #Invalid choice
        else:
            print 'Invalid choice'

    #Booking menu
    def booking_menu(self):
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
        #Doesn't work yet
        elif choice == '2':
            print 'Delete booking'

        #See all bookings
        elif choice == '3':
            bookings = main.main().get_all_bookings()
            for line in bookings:
                print line
        
        #See bookings on a specific date
        #Doesn't work yet
        elif choice == '4':
            print 'See bookings on a specific date'

        #See bookings on specicfic user
        #Doesn't work yet
        elif choice == '5':
            print 'See bookings on specicfic user'

        #Invalid choice
        else:
            print 'Invalid choice'
