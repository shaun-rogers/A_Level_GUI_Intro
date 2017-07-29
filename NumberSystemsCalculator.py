'''Creator: S Rogers
Title: NumberSystemsCalculator
Created: July 2017
Purpose: Demonstration of how to create a GUI for a simple APP.
This app allows the user to enter a number in Decimal, Binary or Hex and convert
to a number system of their choice
'''

# This line imports the class "tkinter" and all of its methods
# The "as tk" is a common approach to make calling methods faster
import tkinter as tk

'''This first section contains the functions
that make the program convert the different number systems'''


def hex_dec():
    hex_val = {"1":1, "2":2, "3":3, "4":4, "5":5, "6":6, "7":7, "8":8, "9":9, "A":10, "B":11, "C":12, "D":13, "E":14, "F":15}
    number = baseNumber.get()
    number = number.upper()
    value = 0
    index = -1
    for i in range(len(number)):
        if len(number)>1:
            if i == 1:
                value +=  hex_val[number[index]]
            else:
                value += hex_val[number[index]] * (16 * (abs(i-1)))
        elif len(number)== 1:
            value += hex_val[number[index]]
        else:
            value = "You must enter a number to convert"
        index -= 1
    resultText.set("The binary for this number is: " + str(value))


def hex_bin():
    pass


def dec_hex():
    pass


def dec_bin():
    pass


def bin_hex():
    pass


def bin_dec():
    pass


root = tk.Tk()
root.title("BinHexDec Calculator")

titleFrame = tk.Frame(root, width=400, height=50)
titleFrame.pack()
entryFrame = tk.Frame(root, width=400, height=200)
entryFrame.pack()
resultFrame = tk.Frame(root, width=400, height=200)
resultFrame.pack()
buttonFrame = tk.Frame(root, width=400, height=200)
buttonFrame.pack()

title = tk.Label(titleFrame, text="BinHexDec Converter").pack()

entryText = tk.Label(entryFrame, text="Enter the number to convert and select the conversion below").grid(row=0, columnspan=3)
baseNumber = tk.Entry(entryFrame)
baseNumber.grid(row=1, column=1)

resultText = tk.StringVar()
displayResult = tk.Label(resultFrame, textvariable=resultText).grid(row=0, column=1)
resultText.set("The result of the calculation will appear here")

hexBinBtn = tk.Button(buttonFrame, text="Hex to Bin", command=hex_bin).grid(row=0,column=0)
hexDecBtn = tk.Button(buttonFrame, text="Hex to Dec", command=hex_dec).grid(row=0,column=1)
decHexBtn = tk.Button(buttonFrame, text="Dec to Hex").grid(row=0,column=2)
decBinBtn = tk.Button(buttonFrame, text="Dec to Bin").grid(row=0,column=3)
binDecBtn = tk.Button(buttonFrame, text="Bin to Dec").grid(row=1,column=1)
binHexBtn = tk.Button(buttonFrame, text="Bin to Hex").grid(row=1,column=2)

root.mainloop()