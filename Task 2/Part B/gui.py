import users
import logger
import tkinter as tk
import tkinter.ttk as ttk
import tkinter.simpledialog
import tkinter.font as font

# https://stackoverflow.com/a/44100075/10648657
def round_rectangle(canvas, x1, y1, x2, y2, radius=25, **kwargs):
    points = [
        x1+radius, y1,
        x1+radius, y1,
        x2-radius, y1,
        x2-radius, y1,
        x2, y1,
        x2, y1+radius,
        x2, y1+radius,
        x2, y2-radius,
        x2, y2-radius,
        x2, y2,
        x2-radius, y2,
        x2-radius, y2,
        x1+radius, y2,
        x1+radius, y2,
        x1, y2,
        x1, y2-radius,
        x1, y2-radius,
        x1, y1+radius,
        x1, y1+radius,
        x1, y1
    ]
    
    return canvas.create_polygon(points, **kwargs, smooth=True)


# The login screen
def login(root):
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
    
    # Show the main window
    root.deiconify()

# The library tab
def library_tab(root):
    return ttk.Frame(root.tab, width=root.window_width, height=root.window_height)

# The staff tab
def staff_tab(root):
    frame = ttk.Frame(root.tab, width=root.window_width, height=root.window_height)
    allUsers = users.get_users()
    userCount = len(allUsers)
    studentCount = 0
    staffCount = 0
    for user in allUsers:
        if users.is_staff(user["id"]):
            staffCount += 1
        else:
            studentCount += 1


    """
    Total Users
    """
    totalUsersFrame = tk.Frame(frame, bg="#2f2f2f")
    totalUsersFrame.place(x=140, y=60, width=261, height=141)

    totalUsersCanvas = tk.Canvas(frame)
    totalUsersCanvas.place(x=140, y=60, width=261, height=141)
    round_rectangle(totalUsersCanvas, 5, 5, 261-5, 141-5, radius=20, fill="#2f2f2f")

    totalUsersLabel = tk.Label(frame, bg="#2f2f2f", text="Total Users")
    totalUsersLabel["font"] = font.Font(family="Ariel", size=11, weight="bold")
    totalUsersLabel.place(x=160, y=79, width=101, height=22)

    totalUsersValue = tk.Label(frame, bg="#2f2f2f", text=userCount)
    totalUsersValue["font"] = font.Font(family="Ariel", size=11, weight="bold")
    totalUsersValue.place(x=240, y=107, width=61, height=54)


    """
    Total Students
    """
    totalStudentsFrame = tk.Frame(frame, bg="#2f2f2f")
    totalStudentsFrame.place(x=520, y=60, width=261, height=141)

    totalStudentsCanvas = tk.Canvas(frame)
    totalStudentsCanvas.place(x=520, y=60, width=261, height=141)
    round_rectangle(totalStudentsCanvas, 5, 5, 261-5, 141-5, radius=20, fill="#2f2f2f")

    totalStudentsLabel = tk.Label(frame, bg="#2f2f2f", text="Total Students")
    totalStudentsLabel["font"] = font.Font(family="Ariel", size=11, weight="bold")
    totalStudentsLabel.place(x=540, y=79, width=121, height=20)

    totalStudentsValue = tk.Label(frame, bg="#2f2f2f", text=studentCount)
    totalStudentsValue["font"] = font.Font(family="Ariel", size=11, weight="bold")
    totalStudentsValue.place(x=620, y=107, width=61, height=54)


    """
    Total Staff
    """
    totalStaffFrame = tk.Frame(frame, bg="#2f2f2f")
    totalStaffFrame.place(x=900, y=60, width=261, height=141)

    totalStaffCanvas = tk.Canvas(frame)
    totalStaffCanvas.place(x=900, y=60, width=261, height=141)
    round_rectangle(totalStaffCanvas, 5, 5, 261-5, 141-5, radius=20, fill="#2f2f2f")

    totalStaffLabel = tk.Label(frame, bg="#2f2f2f", text="Total Staff")
    totalStaffLabel["font"] = font.Font(family="Ariel", size=11, weight="bold")
    totalStaffLabel.place(x=920, y=78, width=101, height=22)

    totalStaffValue = tk.Label(frame, bg="#2f2f2f", text=staffCount)
    totalStaffValue["font"] = font.Font(family="Ariel", size=11, weight="bold")
    totalStaffValue.place(x=1000, y=107, width=61, height=54)


    """
    User List
    """
    userListFrame = tk.Frame(frame, bg="#2f2f2f")
    userListFrame.place(x=140, y=260, width=1021, height=361)

    userListCanvas = tk.Canvas(frame)
    userListCanvas.place(x=140, y=260, width=1021, height=361)
    round_rectangle(userListCanvas, 5, 5, 1021-5, 361-5, radius=20, fill="#2f2f2f")

    userListLabel = tk.Label(frame, bg="#2f2f2f", text="Users")
    userListLabel["font"] = font.Font(family="Ariel", size=11, weight="bold")
    userListLabel.place(x=160, y=280, width=61, height=20)

    userListTreeView = ttk.Treeview(frame)
    userListTreeView["columns"] = ("1", "2", "3")
    userListTreeView["show"] = "headings"

    userListTreeView.heading("1", text="id")
    userListTreeView.heading("2", text="name")
    userListTreeView.heading("3", text="type")

    userListTreeView.column("1", width=100, stretch=False)
    
    for user in allUsers:
        userListTreeView.insert("", "end", values=(user["id"], user["name"], user["type"]))

    # Block the user from editing the treeview columns
    userListTreeView.bind("<Button-1>", lambda e: userListTreeView.identify_region(e.x, e.y) == "separator" and "break")

    # Place the treeview
    userListTreeView.place(x=160, y=320, width=981, height=281)

    return frame

# The account tab
def account_tab(root):
    frame = ttk.Frame(root.tab, width=root.window_width, height=root.window_height)

    userID = root.user["id"]
    userName = root.user["name"]
    userType = root.user["type"]


    """
    ID
    """
    userIDFrame = tk.Frame(frame, bg="#2f2f2f")
    userIDFrame.place(x=140, y=60, width=261, height=141)

    userIDCanvas = tk.Canvas(frame)
    userIDCanvas.place(x=140, y=60, width=261, height=141)
    round_rectangle(userIDCanvas, 5, 5, 261-5, 141-5, radius=20, fill="#2f2f2f")

    userIDLabel = tk.Label(frame, bg="#2f2f2f", text="ID")
    userIDLabel["font"] = font.Font(family="Ariel", size=11, weight="bold")
    userIDLabel.place(x=160, y=79, width=101, height=22)

    userIDValue = tk.Label(frame, bg="#2f2f2f", text=userID)
    userIDValue["font"] = font.Font(family="Ariel", size=11, weight="bold")
    userIDValue.place(x=240, y=107, width=61, height=54)


    """
    Name
    """
    userNameFrame = tk.Frame(frame, bg="#2f2f2f")
    userNameFrame.place(x=520, y=60, width=261, height=141)

    userNameCanvas = tk.Canvas(frame)
    userNameCanvas.place(x=520, y=60, width=261, height=141)
    round_rectangle(userNameCanvas, 5, 5, 261-5, 141-5, radius=20, fill="#2f2f2f")

    userNameLabel = tk.Label(frame, bg="#2f2f2f", text="Total Students")
    userNameLabel["font"] = font.Font(family="Ariel", size=11, weight="bold")
    userNameLabel.place(x=540, y=79, width=121, height=20)

    userNameValue = tk.Label(frame, bg="#2f2f2f", text=userName)
    userNameValue["font"] = font.Font(family="Ariel", size=11, weight="bold")
    userNameValue.place(x=620, y=107, width=61, height=54)


    """
    Account Type
    """
    userAccountTypeFrame = tk.Frame(frame, bg="#2f2f2f")
    userAccountTypeFrame.place(x=900, y=60, width=261, height=141)

    userAccountTypeCanvas = tk.Canvas(frame)
    userAccountTypeCanvas.place(x=900, y=60, width=261, height=141)
    round_rectangle(userAccountTypeCanvas, 5, 5, 261-5, 141-5, radius=20, fill="#2f2f2f")

    userAccountTypeLabel = tk.Label(frame, bg="#2f2f2f", text="Total Staff")
    userAccountTypeLabel["font"] = font.Font(family="Ariel", size=11, weight="bold")
    userAccountTypeLabel.place(x=920, y=78, width=101, height=22)

    userAccountTypeValue = tk.Label(frame, bg="#2f2f2f", text=userType)
    userAccountTypeValue["font"] = font.Font(family="Ariel", size=11, weight="bold")
    userAccountTypeValue.place(x=1000, y=107, width=61, height=54)


    """
    My Books
    """
    myBooksFrame = tk.Frame(frame, bg="#2f2f2f")
    myBooksFrame.place(x=140, y=260, width=1021, height=361)

    myBooksCanvas = tk.Canvas(frame)
    myBooksCanvas.place(x=140, y=260, width=1021, height=361)
    round_rectangle(myBooksCanvas, 5, 5, 1021-5, 361-5, radius=20, fill="#2f2f2f")

    myBooksLabel = tk.Label(frame, bg="#2f2f2f", text="My Books")
    myBooksLabel["font"] = font.Font(family="Ariel", size=11, weight="bold")
    myBooksLabel.place(x=160, y=280, width=71, height=20)

    myBooksTreeView = ttk.Treeview(frame)
    myBooksTreeView["columns"] = ("1", "2", "3")
    myBooksTreeView["show"] = "headings"

    myBooksTreeView.heading("1", text="id")
    myBooksTreeView.heading("2", text="name")
    myBooksTreeView.heading("3", text="type")

    myBooksTreeView.column("1", width=100, stretch=False)
    
    # for user in allUsers:
    #     myBooksTreeView.insert("", "end", values=(user["id"], user["name"], user["type"]))
    myBooksTreeView.insert("", "end", values=(root.user["id"], root.user["name"], root.user["type"]))

    # Block the user from editing the treeview columns
    myBooksTreeView.bind("<Button-1>", lambda e: myBooksTreeView.identify_region(e.x, e.y) == "separator" and "break")

    # Place the treeview
    myBooksTreeView.place(x=160, y=320, width=981, height=281)

    return frame
