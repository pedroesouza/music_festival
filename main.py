artistDict = {"example": ["examp", "Genre", "Duration"]}

print(r''' █████╗ ██████╗ ████████╗██╗███████╗████████╗    ███╗   ███╗ █████╗ ███╗   ██╗ █████╗  ██████╗ ███████╗███╗   ███╗███████╗███╗   ██╗████████╗
██╔══██╗██╔══██╗╚══██╔══╝██║██╔════╝╚══██╔══╝    ████╗ ████║██╔══██╗████╗  ██║██╔══██╗██╔════╝ ██╔════╝████╗ ████║██╔════╝████╗  ██║╚══██╔══╝
███████║██████╔╝   ██║   ██║███████╗   ██║       ██╔████╔██║███████║██╔██╗ ██║███████║██║  ███╗█████╗  ██╔████╔██║█████╗  ██╔██╗ ██║   ██║   
██╔══██║██╔══██╗   ██║   ██║╚════██║   ██║       ██║╚██╔╝██║██╔══██║██║╚██╗██║██╔══██║██║   ██║██╔══╝  ██║╚██╔╝██║██╔══╝  ██║╚██╗██║   ██║   
██║  ██║██║  ██║   ██║   ██║███████║   ██║       ██║ ╚═╝ ██║██║  ██║██║ ╚████║██║  ██║╚██████╔╝███████╗██║ ╚═╝ ██║███████╗██║ ╚████║   ██║   
╚═╝  ╚═╝╚═╝  ╚═╝   ╚═╝   ╚═╝╚══════╝   ╚═╝       ╚═╝     ╚═╝╚═╝  ╚═╝╚═╝  ╚═══╝╚═╝  ╚═╝ ╚═════╝ ╚══════╝╚═╝     ╚═╝╚══════╝╚═╝  ╚═══╝   ╚═╝   
                                                                                                                                             ''')

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

artist_management()