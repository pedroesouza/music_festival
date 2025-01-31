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
    del artistDict[artistName]

def edit_artist(artistName, whatToEdit, change):
    if whatToEdit == "name":
        artistDict[artistName][0] = change
        artistDict[change] = artistDict.pop(artistName)
    
        
    if whatToEdit == "genre":
        artistDict[artistName][1] = change


def search_artist(artistName):
    pass

def artist_management():
    print(r'''   ___             _        _              _              __  __                            __ _                                    _     
  /   \     _ _   | |_     (_)     ___    | |_      o O O|  \/  |  __ _    _ _     __ _    / _` |   ___    _ __     ___    _ _     | |_   
  | - |    | '_|  |  _|    | |    (_-<    |  _|    o     | |\/| | / _` |  | ' \   / _` |   \__, |  / -_)  | '  \   / -_)  | ' \    |  _|  
  |_|_|   _|_|_   _\__|   _|_|_   /__/_   _\__|   TS__[O]|_|__|_| \__,_|  |_||_|  \__,_|   |___/   \___|  |_|_|_|  \___|  |_||_|   _\__|  
_|"""""|_|"""""|_|"""""|_|"""""|_|"""""|_|"""""| {======|_|"""""|_|"""""|_|"""""|_|"""""|_|"""""|_|"""""|_|"""""|_|"""""|_|"""""|_|"""""| 
"`-0-0-'"`-0-0-'"`-0-0-'"`-0-0-'"`-0-0-'"`-0-0-'./o--000'"`-0-0-'"`-0-0-'"`-0-0-'"`-0-0-'"`-0-0-'"`-0-0-'"`-0-0-'"`-0-0-'"`-0-0-'"`-0-0-' ''')
    
    print(artistDict)


    artistListInteraction = input("\nWould you like to add, edit, remove artist and info or search? ").lower()
    if artistListInteraction == "add":
        add_artist(input("What is the artists name? "), input("What is the artists genre? "), input("What is the duration of the performance? "))
    if artistListInteraction == "remove":
        remove_artist(input("What artist would you like to remove? "))
    if artistListInteraction == "edit":
        edit_artist(input("What artist do you want to edit? "), input("Would you like to edit the name, genre, or duration? ").lower(), input("What do you want to change it to? "))
    if artistListInteraction == "search":
        search_artist(input("What is your artist's name? "))

while True:
    artist_management()