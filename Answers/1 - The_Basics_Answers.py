'''Creator: S Rogers
Title: 1 - The Basics

Description: This program is to be used with Year 12 students to introduce them
to the basics of Tkinter GUI.

They will learn about importing the module, initialising a window
and how to use some basic widgets'''

# This line imports the class "tkinter" and all of its methods
# The "as tk" is a common approach to make calling methods faster
import tkinter as tk

# root could be called anything and simply provides an identifier for the main window
root = tk.Tk()

# Create your first label
myFirstLabel = tk.Label(root, text="Creating my first label")
myFirstLabel.pack()

# Create your first text entry widget
myFirstEntry = tk.Entry(root)
myFirstEntry.pack()

# Create your first button
myFirstButton = tk.Button(root, text="Submit")
myFirstButton.pack()

# This method initiates the loop that allows the GUI to actually run
root.mainloop()
