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

'''This procedure accepts the parameter subProgram which will tell it which conversion function
to call. These functions will then return a value to outputUpdate and
set resultText to the appropriate message'''
def outputUpdate(subProgram):
    #Selection block that will run the appropriate function based upon
    #the button the user pushes
    if subProgram == 1:
        pass
    elif subProgram == 2:
        #The function is run within a variable to that the returned
        #value is stored and usable
        value = hex_dec()
        resultText.set(value)
    elif subProgram == 3:
        value = dec_hex()
        resultText.set(value)

def hex_dec():
    #Establish a dictionary to store the hex value of each position
    hex_val = {"0":0, "1":1, "2":2, "3":3, "4":4, "5":5, "6":6, "7":7, "8":8, "9":9, "A":10, "B":11, "C":12, "D":13, "E":14, "F":15}
    #Get the value that has been entered into input field in the GUI stored in the
    #baseNumber variable
    number = baseNumber.get()
    #Input Sanitisation ensuring that we are working with upper case text
    number = number.upper()
    #VALIDATION - ensuring the user has not entered an invalid character into the input field
    #i.e. no symbols such as !@#$ etc
    invalidChars = set(string.punctuation)
    #Selection statement that outputs an error message should the user enter an invalid value
    if any(char in invalidChars for char in number):
        resultText.set("Must only contain Numbers and Letters")
    else:
        #If the entry is valid the rest of the algorithm runs
        #Establishing a list to hold the entered value in reverse
        #This is so that we can work from right to left i.e. as numbers work
        number_split = []
        #This list will store the decimal exponent of that position in a number
        #e.g. 16,1 for a two digit Hex value
        position_val = []
        #Count controlled loop initiated to build the list of Hex items
        #Count controlled used to allow it to expand for any length of entered value
        for i in range(len(number)):
            #.append method adds value to number_split
            number_split.append(number[i])
        #This process is repeated for the position values
        for i in range(len(number)):
            #The exponent operator is used as each position will
            position_val.append(16**i)
        #Mathematically the first appended value would be 0, it needs to be 1
        #So the index of 0 is changed to 1
        position_val[0] = 1
        #As the position values work from right to left
        position_val.reverse()
        #Initialising a variable to store the actual decimal value of the number
        value = 0
        #Again, count controlled iteration to add the value of each position to the total
        for i in range(len(number)):
            value += hex_val[number_reverse[i]] * position_val[i]
        #Concatenating the value into a string that can be presented in the output
        value = "The decimal for this number is: " + str(value)
    #Returning the value to the calling function to be used there
    return value


def hex_bin():
    #This makes use of the hex_dec function to get the decimal value of the hex number
    #This means I don't have to re-write code
    decValue = hex_dec()
    #This is then carried out using the dec_bin function
    binValue = dec_bin()
    #Setting the string to be returned and concatenating with the binary value
    value = "The binary for this number is: " + str(bin_value)
    #Returning the value to the output function
    return value


def dec_hex():
    #As before this is getting the entered value
    number = baseNumber.get()
    '''Here I will build the validation and error checking later'''

    #Converting the input to an integer so that we can use it in calculations
    number = int(number)
    #Making use of the inbuilt hex function that returns the hex value of a decimal
    hexConvert = hex(number)
    #hex() returns this with a leading 0x
    #I have used string slicing to remove the elements I do not want
    hexConvert = hexConvert[2:]
    #As with the other functions the output message is being concatenated
    #and returned to the output procedure
    value = "The hexadecimal value for " + str(number) + " is " + str(hexConvert)
    return value

def dec_bin():
    pass


def bin_hex():
    pass


def bin_dec():
    pass

#Setting the tk environment to start the GUI
root = tk.Tk()
'''I have set up different frames to allow for different grid layouts'''
#Setting the title that will appear at the top of the window
root.title("BinHexDec Calculator")
#Creating a frame that will hold the top text of the window
titleFrame = tk.Frame(root, width=400, height=50)
titleFrame.pack()
#Creating a frame that will hold the entry widget
entryFrame = tk.Frame(root, width=400, height=200)
entryFrame.pack()
resultFrame = tk.Frame(root, width=400, height=200)
resultFrame.pack()
buttonFrame = tk.Frame(root, width=400, height=200)
buttonFrame.pack()
#Creating a label to display text on the screen
title = tk.Label(titleFrame, text="BinHexDec Converter").pack()
entryText = tk.Label(entryFrame, text="Enter the number to convert and select the conversion below").grid(row=0, columnspan=3)
#Creatingan entry widget that will allow the user to enter a value
baseNumber = tk.Entry(entryFrame)
baseNumber.grid(row=1, column=1)

#Initialising a variable as a "string variable" this allows me
#to change this value dynamically within the program
resultText = tk.StringVar()
#This creates a label that will display whatever is in resultText
#To create this dynamic label I don't set it with a text, it has a textVariable
displayResult = tk.Label(resultFrame, textvariable=resultText).grid(row=0, column=1)
resultText.set("The result of the calculation will appear here")

#Here I am creating a series of buttons.
#These will all run the outputUpdate procedure
#So that the correct function is run a value is passed into outputUpdate
hexBinBtn = tk.Button(buttonFrame, text="Hex to Bin", command= lambda: outputUpdate(1)).grid(row=0,column=0)
hexDecBtn = tk.Button(buttonFrame, text="Hex to Dec", command= lambda: outputUpdate(2)).grid(row=0,column=1)
decHexBtn = tk.Button(buttonFrame, text="Dec to Hex", command= lambda: outputUpdate(3)).grid(row=0,column=2)
decBinBtn = tk.Button(buttonFrame, text="Dec to Bin").grid(row=0,column=3)
binDecBtn = tk.Button(buttonFrame, text="Bin to Dec").grid(row=1,column=1)
binHexBtn = tk.Button(buttonFrame, text="Bin to Hex", command = bin_hex).grid(row=1,column=2)
#This initialises the window and keeps it running constantly
root.mainloop()
