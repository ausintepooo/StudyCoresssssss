import random
import os

def StudyCorePrint():

    print("                       _______ _______ __   __ ______  __   __ _______ _______ ______   _______ ")
    print("                       |       |       |  | |  |      ||  | |  |       |       |    _ | |       |")
    print("                       |  _____|_     _|  | |  |  _    |  |_|  |       |   _   |   | || |    ___|")
    print( "                       | |_____  |   | |  |_|  | | |   |       |      _|  | |  |   |_||_|   |___ ")
    print("                       |_____  | |   | |       | |_|   |_     _|     | |  |_|  |    __  |    ___|")
    print("                        _____| | |   | |       |       | |   | |     |_|       |   |  | |   |___ ")
    print("                       |_______| |___| |_______|______|  |___| |_______|_______|___|  |_|_______|\n")

def descriptions():
    print("                          Welcome to studyCore! Where we create a comprehensive environment ")
    print("                                  encompassing aspects of student life and study tools.")

def save_session(username):
    with open("session.txt", "w") as sessionFile:
        sessionFile.write(username)

def is_valid_password(password):
    if len(password) < 8:
        print("  - Password must be at least:\n  - 8 characters long\n  - Include at least one number\n  - Add Highcase letter/s")

        return False
    return True

def MainMenu(username):
    print (f"""       Welcome {username}!
   1. Add Task
   2. View Tasks
   3. Mark Task as Done
   4. Add Notes
   5. Grade Calculator
   6. Virtual Pet
   7. Exit
   8. Logout""")
   
    choice = int(input("  - Select option (1-8): "))


    
def create_file(username, password, recoveryPIN):
    os.makedirs("users", exist_ok=True)
    folder_name = os.path.join("users", username)
    if not os.path.exists(folder_name):
        os.makedirs(folder_name)
        print(f"                            User folder '{folder_name}' created successfully.")
        print(f"                                    Your recovery PIN: {recoveryPIN}")
        print("                        (Keep this PIN safe, you will need it for password recovery.)")
        StudyCorePrint()
        descriptions()
        with open(os.path.join(folder_name, "credentials.txt"), "w") as file:
            file.write(f"Username: {username}\n")
            file.write(f"Password: {password}\n")
            file.write(f"PIN: {recoveryPIN}\n")

        save_session(username)
        MainMenu(username)

    else:
        print("User folder already exists for this username.")


def CreateAccount():
    print(r"""    _________                          __              _____                                   __   
    \_   ___ \_______   ____  _____  _/  |_  ____     /  _  \   ____  ____  ____  __ __  _____/  |_ 
    /    \  \/\_  __ \_/ __ \ \__  \ \   __\/ __ \   /  /_\  \_/ ___\/ ___\/  _ \|  |  \/    \   __\ 
    \     \____|  | \/\  ___/  / __ \ |  | \  ___/  /    |    \  \__\  \__(  <_> )  |  /   |  \  |  
     \______  /|__|    \___  > ____  / __|  \___  > \____|__  /\___  >___  >____/|____/|___|  /__|  
            \/             \/      \/          \/          \/     \/    \/                 \/      
    """)
    username = ""

    while username == "":
        print("(A 4-digit PIN will be generated upon creating an account.)")
        username = input("  - Enter Username: ")

        if username == "":
            print("  Username cannot be empty.")

    while True:
        password = input("  - Enter Password: ")

        if not is_valid_password(password):
            print("  Please enter a stronger password!")
            continue

        verifiedpassword = input("  - Verify Password: ")

        if password != verifiedpassword:
            print("\n  Password doesn't match\n")
            continue

        break

    recoveryPIN = random.randint(1000, 9999)

    create_file(username, password, recoveryPIN)
    
CreateAccount()
    
