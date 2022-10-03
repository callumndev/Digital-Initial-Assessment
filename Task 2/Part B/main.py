import tkinter as tk
import tkinter.ttk as ttk
import sv_ttk
import gui
import users


root = tk.Tk()
root.withdraw() # Hide the window


# Configure the window
root.title("Library")
root.resizable(False, False)


# Set the window size based on the screen size
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

window_width = int(screen_width * 0.5)
window_height = int(screen_height * 0.5)
window_x = int((screen_width / 2) - (window_width / 2))
window_y = int((screen_height / 2) - (window_height / 2))


root.geometry(f"{window_width}x{window_height}+{window_x}+{window_y}")
root.window_width = window_width
root.window_height = window_height


# Make tabs
tab = ttk.Notebook(root)
tab.place(x=0, y=0)
root.tab = tab

# Show the login screen
gui.login(root)

# Add tabs
tab.add(gui.library_tab(root), text="Library")
tab.add(gui.account_tab(root), text="Account")



# Start the main loop
sv_ttk.set_theme("dark")
root.mainloop()
