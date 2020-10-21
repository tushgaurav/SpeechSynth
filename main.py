import branding
import pyttsx3

branding.welcome()

speaker = pyttsx3.init()

choice = 'Y'
yes = choice.upper()

while choice == yes:
    text = str(input("What do you want me to say?"))
    speaker.say(text)
    speaker.runAndWait()
    choice = str(input("Try again? (Y/N)")).upper()

if choice == 'n'.upper():
    print("Thanks for using!")
    print("Aborting...")
    branding.ending()
    exit()
else:
    print("Wrong input recieved.")
    print("Aborting...")
    branding.ending()
    exit()