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
import string

'''This first section contains the functions
that make the program convert the different number systems'''

def outputUpdate(subProgram):
    if subProgram == 1:
        pass
    elif subProgram == 2:
        value = hex_dec()
        resultText.set(value)
    elif subProgram == 3:
        value = dec_hex()
        resultText.set(value)

def hex_dec():
    hex_val = {"0":0, "1":1, "2":2, "3":3, "4":4, "5":5, "6":6, "7":7, "8":8, "9":9, "A":10, "B":11, "C":12, "D":13, "E":14, "F":15}
    number = baseNumber.get()
    number = number.upper()
    #number.rstrip()
    #number.lstrip()
    invalidChars = set(string.punctuation)
    if any(char in invalidChars for char in number):
        resultText.set("Must only contain Numbers and Letters")
    else:
        number_reverse = []
        position_val = []
        for i in range(len(number)):
            number_reverse.append(number[i])
        number_reverse.reverse()

        for i in range(len(number)):
            position_val.append(16**i)
        position_val[0] = 1
        position_val.reverse()
        print(position_val)

        value = 0

        for i in range(len(number)):
            value += hex_val[number_reverse[i]] * position_val[i]
        value = "The decimal for this number is: " + str(value)

    return value


def hex_bin():
    decValue = hex_dec()

    value = "The decimal for this number is: " + str(dec_value)

    return value


def dec_hex():
    number = baseNumber.get()
    number = int(number)
    resultText.set("The hexadecimal of " + str(number) + " is " + str(hex(number))[2:])
    number = int(baseNumber.get())
    hexConvert = hex(number)
    hexConvert = hexConvert[2:]
    value = "The hexadecimal value for " + str(number) + " is " + str(hexConvert)
    return value

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

hexBinBtn = tk.Button(buttonFrame, text="Hex to Bin", command= lambda: outputUpdate(1)).grid(row=0,column=0)
hexDecBtn = tk.Button(buttonFrame, text="Hex to Dec", command= lambda: outputUpdate(2)).grid(row=0,column=1)
decHexBtn = tk.Button(buttonFrame, text="Dec to Hex", command= lambda: outputUpdate(3)).grid(row=0,column=2)
decBinBtn = tk.Button(buttonFrame, text="Dec to Bin").grid(row=0,column=3)
binDecBtn = tk.Button(buttonFrame, text="Bin to Dec").grid(row=1,column=1)
binHexBtn = tk.Button(buttonFrame, text="Bin to Hex", command = bin_hex).grid(row=1,column=2)

root.mainloop()
