#Seatwork 4 in DSA

#Program: Text to Speech using pyttsx3
#Video inspiration: https://www.youtube.com/watch?v=Rjk2D7XKpvI

#First Step: Import pyttsx3
import pyttsx3
#Second Step: Print the options:
                #Upload a text file
                #Type the text

engine = pyttsx3.init()
print ("\n====================================================================")
print ("    Hi There! This program can read the text you will enter.")
print ("====================================================================")
engine.say ("Hi There! This program can read the text you will enter.")
engine.runAndWait()
print ("\nOptions")
print ("1 --> Directly type the text")
print ("2 --> Open a Text File\n")
print ("====================================================================\n")

#Second Step: Option Conditions
engine.say ("What option do you want to try? Enter only the number")
engine.runAndWait()
print ("What do you want to do?")

while True:
    try:
        userInputfunction = int (input ("\nEnter only the number: ")) #Third Step: Ask user for input
        if userInputfunction not in range (1, 3):
            print ("\n\033[91mSorry, you have entered an invalid input.\033[0m\nPlease enter 1 to 2 only.\n")
            continue
    except ValueError:
            print("\n\033[91mSorry, you have entered an invalid input.\033[0m\nPlease enter a number only.\n") 
            continue    
    else:
        if userInputfunction == 1: 
            directType = input ("\nEnter the text you want me to read: ")
            engine.say (directType) #Fourth Step: code for text to speech
            engine.runAndWait()
        
            
        elif userInputfunction==2:
            inputFilename = input ("\nEnter the file name of the text file you want me to read: ")
            file = open (inputFilename, 'r', encoding = "UTF-8")
            text = file.read()
            print(f"\n========================================\n{text}\n========================================\n")
            engine.say (text)
            engine.runAndWait()
            file.close()
            
    engine.say ("Do you want to continue?")
    engine.runAndWait()
    tryAgain = input ("\nDo you want to try again? y/n: ")
    if (tryAgain == 'y' or tryAgain == "Y") or (tryAgain =="Yes"or tryAgain == "yes"):
            continue
    else:
        print ("\nThank you for using this \033[1mprogram!\033[0m\n") #End
        break
            

