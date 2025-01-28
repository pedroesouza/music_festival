tickets = 0
day_tickets = 0
vip_tickets = 0
super_vip_tickets = 0

attendee_names = []
attendees = 0

attendee_tickets = {}

def ticket_attendee_management():
    addedAtendees = 0
    attendee_name = input("Attendee Name: ").lower()
    attendee_names.append(attendee_name)
    addedAtendees += 1
    print(attendee_names)
    
    print("""
    Choose A Type
    1. 3 Day Ticket
    2. VIP Ticket
    3. Super VIP Ticket      
    """)

    ticket_type = input("Choose A Ticket: ")
    
    if ticket_type == "1":
        day_tickets +=1
        attendee_tickets.update({attendee_name: "3 Day Ticket"})
    elif ticket_type == "2":
        vip_tickets +=1
        attendee_tickets.update({attendee_name: "VIP Tickets"})
    elif ticket_type == "3":
        super_vip_tickets_added +=1
        attendee_tickets.update({attendee_name: "Super VIP Tickets"})
    else:
        print("Wrong Type")

    
    
    
    return (addedAtendees, )



while True:
    attendees += ticket_attendee_management()