













#Tate Morgan venue management stuff

stages = set({})
equipment = set({})
#This is my function to add a location
def add_stage():
    stages.add( input("\nWhat location would you like to add: ").lower())
    return


#this is my function to drop a location
def remove_stage():
    stages.remove( input("\nWhat location would you like to remove: ").lower())
    pass


#This is my function to check the equipment and stage name of who it owns it
def add_equipment():
    equipment.add( input("\nWhat set of equipment would you like to add: ").lower())
    pass


#This is my function to check the equipment and stage name of who it owns it
def remove_equipment():
    equipment.remove( input("\nWhat set of equipment would you like to remove: ").lower())
    pass


#This is my main function
def venue_managementMAIN(stages):
    while True:
        choice = input("Would you like to manage stages or equipment or leave: ").lower()
        if choice == "stages":
            location = input("\nWould you like to add, remove, or view stages: ").lower()
            if location == "add":
                add_stage()
            elif location == "remove":
                remove_stage()
            elif location == "view":
                print(stages)
            else:
                print("\nSorry that is not a viable option please check you spelling and try again")
        elif choice == "equipment":
            location = input("\nWould you like to add, remove, or view equipment: ").lower()
            if location == "add":
                add_equipment()
            elif location == "remove":
                remove_equipment()
            elif location == "view":
                print(equipment)
            else:
                print("\nSorry that is not a viable option please check you spelling and try again")
        elif choice == "leave":
            break
        else:
            print("\nSorry that is not a viable option please check you spelling and try again")


venue_managementMAIN(stages)
#here after used it will back to main function
