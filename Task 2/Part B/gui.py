import users
import logger
import tkinter.ttk as ttk
import tkinter.simpledialog

# The login screen
def login(root):
    print(users.get_users())

    # Show a dialog box to get the username
    username = tkinter.simpledialog.askstring("Login", "Username")
    if users.get_user_by_name(username) == None:
        logger.log_fatal("User not found")
        
    # Show a dialog box to get the password
    password = tkinter.simpledialog.askstring("Login", "Password")
    if users.get_user_by_name(username)["password"] != password:
        logger.log_fatal("Incorrect password")

    # Get the user object and add it to the root
    user = users.get_user_by_name(username)
    root.user = user

    # Add the staff tab if the user is a staff member
    if users.is_staff(user["id"]):
        root.tab.add(staff_tab(root), text="Staff")
        # root.menu.add_command(label="Staff", command=lambda: staff_tab(root))
    
    # Show the main window
    root.deiconify()

# The library tab
def library_tab(root):
    return ttk.Frame(root.tab, width=root.window_width, height=root.window_height)

# The staff tab
def staff_tab(root):
    return ttk.Frame(root.tab, width=root.window_width, height=root.window_height)

# The account tab
def account_tab(root):
    return ttk.Frame(root.tab, width=root.window_width, height=root.window_height)
