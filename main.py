

tickets = 0
day_tickets = 0
vip_tickets = 0
super_vip_tickets = 0
attendee_names = []
attendees = 0

attendee_tickets = {}


def ticket_management():
    ftickets_add = []
    ftickets_remove = []


    print("Attendees: ",attendees)
    print("Total Tickets: ",tickets)
    print("3 Day Tickets: ",day_tickets)
    print("VIP Tickets: ",vip_tickets)
    print("Super VIP Tickets",super_vip_tickets)

    print("""
    1.Add an Attendee
    2.Remove an Attendee
    3.Change an Attendee's Ticket
    4.Search For an Attendee's Ticket
    """)

    ticket_manage_choice = input("Choose a Number: ")

    if ticket_manage_choice == "1":
        ftickets_add = attendee_add()
        print(attendee_names)
    elif ticket_manage_choice == "2":
        ftickets_add = remove_ticket()
        print(attendee_names)
    elif ticket_manage_choice == "3":
        change_ticket()
    elif ticket_manage_choice == "4":
        attendee_search()
    else:
        print("Not a Choice")

    return ftickets_add

def attendee_search():
    print(attendees)
    search = input("Choose an attendee to find their ticket: ")

    if search in attendee_tickets:
        print("This is", search, "ticket: ", attendee_tickets[search])
    else:
        print("Not an Attendee")

    




def attendee_add():
    attendee_name = input("Attendee Name: ").lower()
    attendee_names.append(attendee_name)
    print(attendee_names)
    
    fday_tickets = fvip_tickets = fsuper_tickets = fattendee = 0

    print("""
    Choose A Type
    1. 3 Day Ticket
    2. VIP Ticket
    3. Super VIP Ticket      
    """)
 
    ticket_type = input("Choose A Ticket: ")
         
    
    if ticket_type == "1":
        fday_tickets += 1
        fattendee +=1
        attendee_tickets.update({attendee_name: "3 Day Ticket"})
    elif ticket_type == "2":
        fvip_tickets += 1
        attendee_tickets.update({attendee_name: "VIP Tickets"})
    elif ticket_type == "3":
        fsuper_tickets +=1
        attendee_tickets.update({attendee_name: "Super VIP Tickets"})
    else:
        print("Wrong Type")

    return fday_tickets, fvip_tickets, fsuper_tickets, fattendee
    
    
    
    



def remove_ticket():
    
    fday_tickets = fvip_tickets = fsuper_tickets = fattendee = 0

    
    print(attendee_names)
    attendee_remove = input("Whose ticket do you want to remove: ").lower()

    if attendee_remove in attendee_names:
        del attendee_tickets[attendee_remove]
        fattendee -=1
        attendee_names.remove(attendee_remove)

        if attendee_tickets[attendee_remove] == "3 Day Ticket":
            fday_tickets -=1
        elif attendee_tickets[attendee_remove] == "VIP Ticket":
            fvip_tickets -=1
        elif attendee_tickets[attendee_remove] == "Super VIP Tickets":
            fsuper_tickets -=1
    else:
        print("Not an Attendee")

    return fday_tickets, fvip_tickets, fsuper_tickets, fattendee




def change_ticket():
    print(attendee_names)
    attendee_change = input("Whose ticket do you want to change: ")

    if attendee_change in attendee_names:
        print("""
        Choose a Type of Ticket
        1. 3 Day Ticket
        2. VIP Ticket
        3. Super VIP Ticket
        """)



        ticket_change = input("Choose a Ticket")

        if ticket_change == "1":
            
            if attendee_tickets[attendee_change] == "3 Day Ticket":
                day_tickets -=1
            elif attendee_tickets[attendee_change] == "VIP Ticket":
                vip_tickets -=1
            elif attendee_tickets[attendee_change] == "Super VIP Tickets":
                super_vip_tickets -=1
            
            del attendee_tickets[attendee_change]
            attendee_tickets.update({attendee_change: "3 Day Ticket"})
            day_tickets +=1
        elif ticket_change == "2":
            
            if attendee_tickets[attendee_change] == "3 Day Ticket":
                day_tickets -=1
            elif attendee_tickets[attendee_change] == "VIP Ticket":
                vip_tickets -=1
            elif attendee_tickets[attendee_change] == "Super VIP Tickets":
                super_vip_tickets -=1
            
            del attendee_tickets[attendee_change]
            attendee_tickets.update({attendee_change: "VIP Ticket"})
            vip_tickets +=1
        elif ticket_change == "3":
            
            if attendee_tickets[attendee_change] == "3 Day Ticket":
                day_tickets -=1
            elif attendee_tickets[attendee_change] == "VIP Ticket":
                vip_tickets -=1
            elif attendee_tickets[attendee_change] == "Super VIP Tickets":
                super_vip_tickets -=1
            
            
            del attendee_tickets[attendee_change]
            attendee_tickets.update({attendee_change: "Super VIP Ticket"})
            super_vip_tickets +=1
        else:
            print("Not a Ticket Type")
    else:
        print("Not an Attendee")


while True:
    tickets_add = ticket_management()
    try:
         
        day_tickets += tickets_add[0]
        vip_tickets += tickets_add[1]
        super_vip_tickets += tickets_add[2]
        attendees += tickets_add[3]
        tickets = day_tickets + vip_tickets + super_vip_tickets
    except:
        pass

    