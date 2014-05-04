##################################
#                                #
# Spam Texter Using Google Voice #
# Created by: Rishi Goomar       #
#                                #
##################################
from googlevoice import Voice
from googlevoice.util import input
import time

# Initialize Google Voice
voice = Voice()
# Ask for credentials
voice.login()
# Use login credentials to login
#voice.login("username","password")

userinput = ""
# Get a number to send to
while (userinput == ""):
    userinput = input("Enter in a phone number: ")
    # If there is no valid input, ask again
    if (userinput == ""):
        print "You must enter in a phone number first!"
# The message to send
message = input("Please enter in a message to send: ")
# Get the amount of times to send the message
times = input("Enter in the amount of times to send the message: ")
# Send the message as many times as put in
for i in range(int(times)):
    # Send the txt message
    voice.send_sms(userinput,message)
    # Give a little message to show that it sent
    print "Message Sent " + str(i+1) + " time(s)."
    # Wait 5 seconds before doing it again
    time.sleep(5);
