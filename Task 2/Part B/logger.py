from tkinter import messagebox

# Log an error to the console
def log_error(error):
    print("[ERROR] {}".format(error))

# Log a fatal error to the console, show a message box, and exit the program
def log_fatal(error):
    log_error("[FATAL] {}".format(error))
    messagebox.showerror("Fatal Error", error)
    exit()
