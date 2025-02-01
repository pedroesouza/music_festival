















































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



venue_managementMAIN(stages)
#here after used it will go to ticket sales and admission
