#Variables for all members (jsut for the sake of organizement)
dayTickets= 0
vipTickets = 0
superVipTickets = 0
attendeeNames = []
attendees = 0

attendeeTickets = {}
artistDict = {}

oneDayFestival = (16, 16.5, 17, 17.5, 18, 18.5, 19, 19.5, 20, 20.5, 21, 21.5, 22, 22.5, 23, 23.5, 24)
threeDayFestival = ((16, 16.5, 17, 17.5, 18, 18.5, 19, 19.5, 20, 20.5, 21, 21.5, 22, 22.5, 23, 23.5, 24), (16, 16.5, 17, 17.5, 18, 18.5, 19, 19.5, 20, 20.5, 21, 21.5, 22, 22.5, 23, 23.5, 24), (16, 16.5, 17, 17.5, 18, 18.5, 19, 19.5, 20, 20.5, 21, 21.5, 22, 22.5, 23, 23.5, 24))
artistSchedules = []

print(r'''███╗   ███╗██╗   ██╗███████╗██╗ ██████╗    ███████╗███████╗███████╗████████╗██╗██╗   ██╗ █████╗ ██╗     
████╗ ████║██║   ██║██╔════╝██║██╔════╝    ██╔════╝██╔════╝██╔════╝╚══██╔══╝██║██║   ██║██╔══██╗██║     
██╔████╔██║██║   ██║███████╗██║██║         █████╗  █████╗  ███████╗   ██║   ██║██║   ██║███████║██║     
██║╚██╔╝██║██║   ██║╚════██║██║██║         ██╔══╝  ██╔══╝  ╚════██║   ██║   ██║╚██╗ ██╔╝██╔══██║██║     
██║ ╚═╝ ██║╚██████╔╝███████║██║╚██████╗    ██║     ███████╗███████║   ██║   ██║ ╚████╔╝ ██║  ██║███████╗
╚═╝     ╚═╝ ╚═════╝ ╚══════╝╚═╝ ╚═════╝    ╚═╝     ╚══════╝╚══════╝   ╚═╝   ╚═╝  ╚═══╝  ╚═╝  ╚═╝╚══════╝
                                                                                                        ''')

#Tate Morgan venue management stuff

stages = set({})
#This is my function to add a location
def add_stage():
    name = input("What is the name of the stage: ")
    location = input("Where is it: ")
    equipment = input("Would you like to add some equipment if so add it here: ")
    stages.add( ("Stage name: ", name, "location: ", location, "equipment list: ", equipment) )
    pass


#this is my function to drop a location
def remove_stage():
    name = input("What is the name of the stage: ")
    location = input("Where is it: ")
    equipment = input("Would you like to remove some equipment if so list it here: ")
    stages.remove( ("Stage name: ", name, "location: ", location, "equipment list: ", equipment) )
    pass


#This is my main function
def venue_managementMAIN(stages):
    print('''                                                                                                         
o     o                              o     o                                                          o  
8     8                              8b   d8                                                          8  
8     8 .oPYo. odYo. o    o .oPYo.   8`b d'8 .oPYo. odYo. .oPYo. .oPYo. .oPYo. ooYoYo. .oPYo. odYo.  o8P 
`b   d' 8oooo8 8' `8 8    8 8oooo8   8 `o' 8 .oooo8 8' `8 .oooo8 8    8 8oooo8 8' 8  8 8oooo8 8' `8   8  
 `b d'  8.     8   8 8    8 8.       8     8 8    8 8   8 8    8 8    8 8.     8  8  8 8.     8   8   8  
  `8'   `Yooo' 8   8 `YooP' `Yooo'   8     8 `YooP8 8   8 `YooP8 `YooP8 `Yooo' 8  8  8 `Yooo' 8   8   8  
:::..::::.....:..::..:.....::.....:::..::::..:.....:..::..:.....::....8 :.....:..:..:..:.....:..::..::..:
:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::ooP'.:::::::::::::::::::::::::::::::::
:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::...:::::::::::::::::::::::::::::::::::''')
    while True:
        location = input("\nWould you like to add, remove, or view stages: ").lower()
        if location == "add":
            add_stage()
        elif location == "remove":
            remove_stage()
        elif location == "view":
            print(stages)
        else:
            print("\nSorry that is not a viable option, please check you spelling and try again")



def add_artist(artistName, artistGenre, performaceDuration):
    artistDict[artistName] = [artistName, artistGenre, performaceDuration]

def remove_artist(artistName):
    if artistName in artistDict:
        del artistDict[artistName]
    
    print("Your artist was removed from the artist list, if there was no artist of that name, we have not changed the list at all")

def edit_artist(artistName, whatToEdit, change):
    if artistName in artistDict:
        if whatToEdit == "name":
            artistDict[artistName][0] = change
            artistDict[change] = artistDict.pop(artistName)
        
        elif whatToEdit == "genre":
            artistDict[artistName][1] = change

        elif whatToEdit == "duration":
            artistDict[artistName][2] = change

        else:
            print("ERROR, your choice of what to edit is invalid!, please reselect your choices and try again!, remember, in this question, your only aoptions are name, genre, and duration.")
    else:
        print("ERROR, artist in not in the list of artist!, please reselect your choices and try again!")

def search_artist(artistName):
    if artistName in artistDict:
        print(f"Your artist is in the dictionary, their information is name:{artistDict[artistName][0]}, genre:{artistDict[artistName][1]}, duration:{artistDict[artistName][2]}")
    else:
        print("Your artist is not yet in the list.")

def artist_management():
    while True:
        print(r'''   ___             _        _              _              __  __                            __ _                                    _     
  /   \     _ _   | |_     (_)     ___    | |_      o O O|  \/  |  __ _    _ _     __ _    / _` |   ___    _ __     ___    _ _     | |_   
  | - |    | '_|  |  _|    | |    (_-<    |  _|    o     | |\/| | / _` |  | ' \   / _` |   \__, |  / -_)  | '  \   / -_)  | ' \    |  _|  
  |_|_|   _|_|_   _\__|   _|_|_   /__/_   _\__|   TS__[O]|_|__|_| \__,_|  |_||_|  \__,_|   |___/   \___|  |_|_|_|  \___|  |_||_|   _\__|  
_|"""""|_|"""""|_|"""""|_|"""""|_|"""""|_|"""""| {======|_|"""""|_|"""""|_|"""""|_|"""""|_|"""""|_|"""""|_|"""""|_|"""""|_|"""""|_|"""""| 
"`-0-0-'"`-0-0-'"`-0-0-'"`-0-0-'"`-0-0-'"`-0-0-'./o--000'"`-0-0-'"`-0-0-'"`-0-0-'"`-0-0-'"`-0-0-'"`-0-0-'"`-0-0-'"`-0-0-'"`-0-0-'"`-0-0-' ''')
    
        print(f"\nYour artist list is: {artistDict}")


        artistListInteraction = input("\nWould you like to add, edit, remove artist and info, search, or leave artist management? ").lower()
        if artistListInteraction == "add":
            add_artist(input("What is the artists name? "), input("What is the artists genre? "), input("What is the duration of the performance? "))
        elif artistListInteraction == "remove":
            remove_artist(input("What artist would you like to remove? "))
        elif artistListInteraction == "edit":
            edit_artist(input("What artist do you want to edit? "), input("Would you like to edit the name, genre, or duration? ").lower(), input("What do you want to change it to? "))
        elif artistListInteraction == "search":
            search_artist(input("What is your artist's name? "))
        elif artistListInteraction == "leave":
            break
        else: 
            print("ERROR, your answer was not in the options, please only answer with add, remove, edit, search, or leave")

global tickets
tickets = 0


#Asher Wangia, Ticket Sales and Attendee Management

#This Function asks for how the user would like to manage attendees and tickets
def ticket_management():
    ftickets_add = []
    


    print("Attendees Amount: ",attendees)
    print("Total Tickets: ",tickets)
    print("3 Day Tickets: ",dayTickets)
    print("VIP Tickets: ",vipTickets)
    print("Super VIP Tickets",superVipTickets)

    print("""
    1.Add an Attendee
    2.Remove an Attendee
    3.Search For an Attendee's Ticket
    """)

    ticketManageChoice = input("Choose a Number: ")

    if ticketManageChoice == "1":
        ftickets_add = attendee_add()
        print(attendeeNames)
    elif ticketManageChoice == "2":
        ftickets_add = remove_ticket()
        print(attendeeNames)
    elif ticketManageChoice == "3":
        attendee_search()
    else:
        print("Not a Choice")

    return ftickets_add


#This function adds an attendee to the festival and gives them a ticket
def attendee_add():
    attendeeName = input("Attendee Name: ").lower()
    attendeeNames.append(attendeeName)
    print("Attendees:",attendeeNames)
    
    fDayTickets= fVipTickets = fSuperTickets = fattendee = 0

    print("""
    Choose A Type
    1. 3 Day Ticket
    2. VIP Ticket
    3. Super VIP Ticket      
    """)
 
    ticket_type = input("Choose A Number: ")
         
    
    if ticket_type == "1":
        fDayTickets+= 1
        fattendee +=1
        attendeeTickets.update({attendeeName: "3 Day Ticket"})
    elif ticket_type == "2":
        fVipTickets += 1
        fattendee +=1
        attendeeTickets.update({attendeeName: "VIP Tickets"})
    elif ticket_type == "3":
        fSuperTickets +=1
        fAttendee +=1
        attendeeTickets.update({attendeeName: "Super VIP Tickets"})
    else:
        print("Wrong Type")


    return fDayTickets, fVipTickets, fSuperTickets, fAttendee
       

#This function removes an attendee from the festival
def remove_ticket():
    
    fDayTickets= fVipTickets = fSuperTickets = fAttendee = 0

    
    print("Attendees:",attendeeNames)
    attendeeRemove = input("Whose ticket do you want to remove: ").lower()

    if attendeeRemove in attendeeNames:
        fAttendee -=1
        attendeeNames.remove(attendeeRemove)

        if attendeeTickets[attendeeRemove] == "3 Day Ticket":
            fDayTickets-=1
        elif attendeeTickets[attendeeRemove] == "VIP Ticket":
            fVipTickets -=1
        elif attendeeTickets[attendeeRemove] == "Super VIP Tickets":
            fSuperTickets -=1

        del attendeeTickets[attendeeRemove]
        
    else:
        print("Not an Attendee")

    return fDayTickets, fVipTickets, fSuperTickets, fAttendee


#This function searches for an attendees ticket
def attendee_search():
    print("Attendees:",attendeeNames)
    search = input("Choose an attendee to find their ticket: ").lower()

    if search in attendeeTickets:
        print("This is", search, "ticket: ", attendeeTickets[search])
    else:
        print("Not an Attendee")


#This part adds the tickets and amount of attendees while running the ticket management function
def main_ticket_management():
    while True:
        tickets_add = ticket_management()
        try:
            
            dayTickets+= tickets_add[0]
            vipTickets += tickets_add[1]
            superVipTickets += tickets_add[2]
            attendees += tickets_add[3]
            tickets = dayTickets+ vipTickets + superVipTickets
        except:
            pass

#Loclin schedule management


def schedule_edit():
    


def schedule_management():
    scheduleChoice = input("Would you like to (edit) time slots, assign (artists), or (leave)?")
    if scheduleChoice == "edit":
        schedule_edit(input("Would you like to have an all "))

def main():
    whatToDo = input("Would you like to manage tickets, artists, venue or leave? ").lower()

    if whatToDo == "tickets":
        main_ticket_management()
    elif whatToDo == "artists":
        artist_management()
    elif whatToDo == "venue":
        venue_managementMAIN()
    elif whatToDo == "leave":
        exit()
    else:
        print("ERROR, please only answer with ticktets, artist, venue or leave")

while True:
    main()


