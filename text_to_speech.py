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
print ("    Hi There! This program can read the text you want to hear.")
print ("====================================================================")
engine.say ("Hi There! This program can read the text you want to hear.")
engine.runAndWait()
print ("\nOptions")
print ("1 --> Directly type the text")
print ("2 --> Upload a Text File\n")
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
            break
            
        elif userInputfunction==2:
            inputFilename = input ("\nEnter the file name of the text file you want me to read: ")
            file = open (inputFilename, 'r', encoding = "UTF-8")
            text = file.read()
            print(f"\n{text}")
            engine.say (text)
            engine.runAndWait()
            file.close()
            break
            

