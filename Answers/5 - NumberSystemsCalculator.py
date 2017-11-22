'''Creator: S Rogers
Title: NumberSystemsCalculator
Created: July 2017
Purpose: Demonstration of how to create a GUI for a simple APP.
This app allows the user to enter a number in Decimal, Binary or Hex and convert
to a number system of their choice

To Do: Test with normal and extreme values
To Do: Adapt the app so that there is a home screen, num converter screen and test screen.
'''

# This line imports the class "tkinter" and all of its methods
# The "as tk" is a common approach to make calling methods faster
import tkinter as tk


def menu():
    def menuChoice(choice):
        if choice == 1:
            calculator(menuWindow)
        else:
            quizMenu(menuWindow)

    menuWindow = tk.Tk()
    menuWindow.title("Main Menu")
    heading = tk.Label(menuWindow,text="GUI Example")
    heading.pack()

    calcBtn = tk.Button(menuWindow, text = "Calculator", command = lambda: menuChoice(1))
    calcBtn.pack()

    quizBtn = tk.Button(menuWindow, text = "Quiz", command = lambda: menuChoice(2))
    quizBtn.pack()

    menuWindow.mainloop()

def calculator (menuWindow):
    """This first section contains the functions
    that make the program convert the different number systems"""

    #This procedure accepts the parameter subProgram which will tell it which conversion function
    #to call. These functions will then return a value to outputUpdate and
    #set resultText to the appropriate message"""
    def popUP(message):
        pop = tk.Tk()
        pop.title("Error")
        #resultText.set(message)
        tk.Label(pop, text=message).pack()
        pop.mainloop()

    def outputUpdate(subProgram):
        #Selection block that will run the appropriate function based upon
        #the button the user pushes
        #It first obtains the entered value in the input box
        number = baseNumber.get()
        if subProgram == 1:
            value = hex_bin()
            if value != "Must only contain numbers and letters in the Hex set\n" \
                    "0,1,2,3,4,5,6,7,8,9,a,b,c,d,e,f":
                resultText.set("The binary for this number is: " + str(value)[2:].upper())
            else:
                popUP(value)

        elif subProgram == 2:
            #The function is run within a variable to that the returned
            #value is stored and usable
            value = hex_dec()
            if value != "Must only contain numbers and letters in the Hex set\n" \
                    "0,1,2,3,4,5,6,7,8,9,a,b,c,d,e,f":
                resultText.set("The decimal for this number is: " + str(value).upper())
            else:
                popUP(value)
        elif subProgram == 3:
            value = dec_hex()
            #using the is digit method to see if the returned value is a number.
            #If the value is a number the user has entered a valid decimal value
            if value != "Must only enter whole numbers e.g. 1, 10, 14":
                resultText.set("The decimal for this number is: " + str(value).upper())
            else:
                #If the user did not enter a valid decimal value
                #The function will have returned an appropriate error message
                popUP(value)
        elif subProgram == 4:
            value = dec_bin()
            test = value.replace(" ","")
            if test.isalpha():
                popUP(value)
            else:
                #string slicing used to remove the leading 0b from the binary value
                resultText.set("The binary value of " + str(number) + " is " + str(value)[2:])
        elif subProgram == 5:
            value = bin_dec()
            if value != "Must enter a valid binary number i.e. only containint 1 or 0":
                resultText.set("The decimal value of " + str(number) + " is " + str(value))
            else:
                popUP(value)
        else:
            value = bin_hex()
            if value != "Must enter a valid binary number i.e. only containint 1 or 0":
                resultText.set("The hexadecimal value of " + str(number) + " is " + str(value)[2:].upper())
            else:
                popUP(value)

    def hex_bin():
        #This makes use of the hex_dec function to get the decimal value of the hex number
        #This means I don't have to re-write code
        number = hex_dec()
        try:
            binValue = bin(number)
            #Returning the value to the output function
            return binValue
        except:
            return "Must only contain numbers and letters in the Hex set\n" \
                    "0,1,2,3,4,5,6,7,8,9,a,b,c,d,e,f"

    def hex_dec():
        #Establish a dictionary to store the hex value of each position
        number = baseNumber.get()
        try:
            value = int(number,16)
            return value
        except:
            value = "Must only contain numbers and letters in the Hex set\n" \
                    "0,1,2,3,4,5,6,7,8,9,a,b,c,d,e,f"
            return value

    def dec_hex():
        #As before this is getting the entered value
        number = baseNumber.get()

        if number.isdigit():

            #Converting the input to an integer so that we can use it in calculations
            number = int(number)
            #Making use of the inbuilt hex function that returns the hex value of a decimal
            hexConvert = hex(number)
            #hex() returns this with a leading 0x
            #I have used string slicing to remove the elements I do not want
            hexConvert = hexConvert[2:]
            #As with the other functions this returns the numerical value
        else:
            hexConvert = "Must only enter whole numbers e.g. 1, 10, 14"
        return hexConvert

    '''Completed Not Commented'''
    def dec_bin():
        #Retrieving the value entered by the user to the GUI
        number = baseNumber.get()
        #Selection statement testing if the value etered was a digit
        if number.isdigit():
            #If a digit is entered the conversion is carried out
            number = bin(int(number))
        else:
            #If the user enters a non-digit, the error message is returned
            number = "Must enter a valid digit"
        return number

    def bin_hex():
        #the bin_dec() function is called to obtain a decimal value for conversion
        decValue = bin_dec()
        #Error checking takes place in an attempt to carry out the conversion
        try:
            #the hex and int functions are used to convert the returned decValue
            #If no error is caused the conversion is carried out and returned
            hexVal = hex(int(decValue))
            return hexVal
        except:
            #Any errors are caught and returned to the output procedure
            return "Must enter a valid binary number i.e. only containint 1 or 0"

    def bin_dec():
        #The entered number is retrieved and stored in a variable for use
        number = baseNumber.get()
        #Error checking to stop the program crashing
        try:
            #Attempt to convert the entered value into an int with base 2
            #If no error is caused the value is returned
            value = int(number , 2)
            return value
        except:
            #If an error occurs the error is caught and the appropriate message
            #returned to the output function
            return "Must enter a valid binary number i.e. only containint 1 or 0"

    #Procedure to convert the text the user enters in the entry box to upper case
    def caps(event):
        entryText.set(entryText.get().upper())

    def close():

        root.destroy()
        menu()

    #Setting the tk environment to start the GUI
    menuWindow.destroy()
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
    menuFrame = tk.Frame(root, width=400, height=200)
    menuFrame.pack()
    #Creating a label to display text on the screen
    title = tk.Label(titleFrame, text="BinHexDec Converter").pack()
    entryText = tk.Label(entryFrame, text="Enter the number to convert and select the conversion below").grid(row=0, columnspan=3)
    #Creatingan entry widget that will allow the user to enter a value
    entryText = tk.StringVar()
    baseNumber = tk.Entry(entryFrame, textvariable=entryText)
    baseNumber.grid(row=1, column=1)
    baseNumber.bind("<KeyRelease>",caps)

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
    decBinBtn = tk.Button(buttonFrame, text="Dec to Bin", command= lambda: outputUpdate(4)).grid(row=0,column=3)
    binDecBtn = tk.Button(buttonFrame, text="Bin to Dec", command= lambda: outputUpdate(5)).grid(row=1,column=1)
    binHexBtn = tk.Button(buttonFrame, text="Bin to Hex", command = lambda: outputUpdate(6)).grid(row=1,column=2)

    closeBtn = tk.Button(menuFrame, text = "Return to Menu", command = close).grid(row=2,column=2)
    #This initialises the window and keeps it running constantly
    root.mainloop()

def quizMenu(menuWindow):
    def choice(option):
        if option == 1:
            login(quizWindow)
        elif option == 2:
            registration(quizWindow)
        else:
            menuWindow.destroy()
            menu()

    menuWindow.destroy()
    quizWindow = tk.Tk()
    quizWindow.title = "Quiz Menu"

    logIn = tk.Button(quizWindow, text = "Log In", command = lambda: choice(1))
    logIn.pack()

    register = tk.Button(quizWindow, text = "Register", command = lambda: choice(2))
    register.pack()

    menu = tk.Button(quizWindow, text="Register", command=lambda: choice(3))
    menu.pack()

    quizWindow.mainloop()

def login(quizWindow):
    def logInCheck(correctUsername, correctPassword):
        username = usernameEntry.get()
        password = passwordEntry.get()
        if username == correctUsername and password == correctPassword:
            runQuiz(loginWindow,username)
        else:
            print("ERROR")
    correctUsername = "Test"
    correctPassword = "Test"

    quizWindow.destroy()
    loginWindow = tk.Tk()
    loginWindow.title = "Login"

    tk.Label(loginWindow, text = "Username").grid(row=1, column=0)
    usernameEntry = tk.Entry(loginWindow)
    usernameEntry.grid(row = 1, column = 2)
    usernameEntry.bind("<KeyRelease>")
    tk.Label (loginWindow,text = "Password").grid(row=2, column=0)
    passwordEntry = tk.Entry(loginWindow)
    passwordEntry.grid(row = 2, column = 2)
    passwordEntry.bind("<KeyRelease>")

    tk.Button(loginWindow, text="Login", command = lambda: logInCheck(correctUsername, correctPassword)).grid(row = 3, column = 0)

    loginWindow.mainloop()

def registration(quizWindow):
    pass
def runQuiz(closeWindow, username):
    global score
    pass
    def importQuestions():
        return None

    def answerCheck(answer, correctAnswer):
        global score
        pass

    closeWindow.destroy()
    runWindow = tk.Tk()
    questions = importQuestions

    runWindow.mainloop()
global score
score = 0
menu()