#Seatwork 4 in DSA

#Program: Text to Speech using pyttsx3
#Video inspiration: https://www.youtube.com/watch?v=Rjk2D7XKpvI

#First Step: Import pyttsx3
import pyttsx3
#Second Step: Print the options:
                #Upload a text file
                #Type the text
print ("\n====================================================================")
print ("       Hi There! This program can read the text you want to hear.")
print ("====================================================================")
print ("\nOptions")
print ("1 --> Directly type the text")
print ("2 --> Upload a Text File\n")
print ("====================================================================\n")
#Second Step: Option Conditions
engine = pyttsx3.init()
userInputfunction = int (input ("What option do you want to try? "))
if userInputfunction == 1:
    directType = input ("Enter the text you want me to read: ")
    engine.say (directType)
    engine.runAndWait()

#Third Step: Ask user for input
#Fourth Step: Code for text to speech