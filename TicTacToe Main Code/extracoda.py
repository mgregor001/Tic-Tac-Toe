import tkinter as tk

def open_window():
    new_window = tk.Toplevel()
    new_window.title("New Window")
    new_window.geometry("200x200")
    label = tk.Label(new_window, text="This is a new window!")
    label.pack()

# Main window
root = tk.Tk()
root.title("Main Window")

# Button to open a new window
button = tk.Button(root, text="Open New Window", command=open_window)
button.pack()

root.mainloop()