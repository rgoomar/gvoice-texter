##############################
## Google Voice Mass Texter ##
## By: Rishi Goomar         ##
##############################

from googlevoice import Voice
from googlevoice.util import input
import time

# Initialize the Google Voice object
voice = Voice()
# Ask for credentials
voice.login()
# Use login credentials to login
#voice.login("username","password")

# Initialize variables and list
numbers = []
x = False
userinput = ""

while(userinput != "c"):
    # Enter the first number
    if (not x):
        userinput = input("Enter in a number: ")
        if (userinput == "c"):
            x = False
        else:
            x = True
    # For multiple numbers after the first is entered
    else:
        userinput = input("Enter in another number or type \'c\' to continue: ")
        x = True
    # They can't enter 'c' first. They must have a number
    if (userinput == "c" and not x):
        print "You must enter in a number first!"
        # Reset values
        userinput = ""
        x = False
    # Continue on and ask for the message
    elif (userinput == "c"):
        print "Now time for the message!"
    # Add it to the list of numbers
    else:
        numbers.append(userinput)

# User input message
message = input("Please enter in a message to send to these numbers:")

# Loop through and send it to each number given
for n in numbers:
    # Send the message to the number
    voice.send_sms(n,message)
    # Show which number it was sent to
    print "Message sent to " + str(n)
    # Wait a bit before sending another
    time.sleep(3)
