tickets = 0
day_tickets = 0
vip_tickets = 0
super_vip_tickets = 0

attendee_names = []
attendees = 0

attendee_tickets = {}

def attendee_add():
    attendee_name = input("Attendee Name: ").lower()
    attendee_names.append(attendee_name)
    print(attendee_names)
    
    print("""
    Choose A Type
    1. 3 Day Ticket
    2. VIP Ticket
    3. Super VIP Ticket      
    """)

    ticket_type = input("Choose A Ticket: ")
         
    
    if ticket_type == "1":
        day_tickets += 1
        attendee_tickets.update({attendee_name: "3 Day Ticket"})
    elif ticket_type == "2":
        vip_tickets += 1
        attendee_tickets.update({attendee_name: "VIP Tickets"})
    elif ticket_type == "3":
        super_tickets +=1
        attendee_tickets.update({attendee_name: "Super VIP Tickets"})
    else:
        print("Wrong Type")
    
    
    
    



def remove_ticket():
    

    
    print(attendee_names)
    attendee_remove = input("Whose ticket do you want to remove: ")

    if attendee_remove in attendee_names:
        del attendee_tickets[attendee_remove]
        attendees -=1
        tickets -=1
        attendee_names.remove(attendee_remove)

        if attendee_tickets[attendee_remove] == "3 Day Ticket":
            day_tickets -=1
        elif attendee_tickets[attendee_remove] == "VIP Ticket":
            vip_tickets -=1
        elif attendee_tickets[attendee_remove] == "Super VIP Tickets":
            super_vip_tickets -=1
    else:
        print("Not an Attendee")


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
            
            
            del attendee_tickets[attendee_change]
            attendee_tickets.update({attendee_change: "3 Day Ticket"})
            day_tickets +=1
        elif ticket_change == "2":
            del attendee_tickets[attendee_change]
            vip_tickets -=1
            attendee_tickets.update({attendee_change: "VIP Ticket"})
            vip_tickets +=1
        elif ticket_change == "3":
            del attendee_tickets[attendee_change]
            attendee_tickets.update({attendee_change: "Super VIP Ticket"})
            super_vip_tickets +=1
        else:
            pass



while True:
    attendee_add()