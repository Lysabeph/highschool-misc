#Average Speed Check - Task 3 OCR GCSE Computing
#22nd August 2015
#Mr Miller

#Imports the 'math', 're' and 'time' modules.
import math
import re
import time

#This is a rule for the car registrations to follow, they must be in this format.
#[Letter][Letter][Number][Number] [Space] [Letter][Letter][Letter]
carregRule = "[a-zA-Z][a-zA-Z][\d][\d] [a-zA-Z][a-zA-Z][a-zA-Z]"

#Constant distance of 1 mile for this speed camera.
SensorDistance = 1

#Constant speed limit of 60 miles per hour for this speed camera.
SpeedLimit = 60

#List of vehicles with fines to be sent out.
Details = ''

#Opens the new file.
file = open("Fine Details.txt", "w")
file.writelines("Vehicles that will receive a fine for speeding:")
file.close()

#This is my welcome message to the user.
print ("Welcome to Mr Millers Average Speed Check Program")

#This code will run while true.
while True:

    #The variable carreg is used to collect the car registration plate of the user.
    carreg = input("Enter your car reg: ").upper()

    #Checks the carreg matches the standard format for car registrations.
    if re.match(carregRule, carreg):

        print ("Successful car reg!")

        #This code will ask the user when they passed the first sensor of the speed camera.
        print("We would like to know what time you entered the start of the " + str(SensorDistance) + " Mile Speed Camera?")
        print()
        time.sleep(1)

        #The user presses the enter button to say when they passed the first point of the speed camera.
        x = input("Press enter when your car passes the first point")
        print()

        #This code will ask the user when they passed the first sensor of the speed camera.
        print("We would like to know what time you left the end of the " + str(SensorDistance) +" Mile Speed Camera?")
        starttime = time.time()
        print()
        time.sleep(1)

        #The user presses the enter button to say when they passed the second point of the speed camera.
        x = input("Press enter when your car passes the second point")
        endtime=time.time()
        print()

        #Formula used to worked out the elapsed time.
        elapsedtime = endtime - starttime

        #Formula used to work out mph and round it down to 2 dp.  Telling the user what their speed was in mph.
        mph = (SensorDistance / elapsedtime) *3600
        mph = math.ceil(mph)
        print("Having passed through the two sensors you were travelling", str(mph), "mph")
        print()

        #Here, an IF statement is used to show if the user was speeding.
        if int(mph) > int(SpeedLimit):

            print("You were speeding.....")

            #Opens the known file with the registrations we entered manually and saves them in 'lines'.
            file = open("knownregistrations.txt", "r")
            lines = file.readlines()
            file.close()

            #Checks if the registration is in the file.
            for i in range(len(lines)):

                #Adds the registration to the Details variable if the registration is in the file.
                if carreg.upper() in lines[i]:

                    Details = lines[i].replace("\n", "")

                    #Opens the new file and adds the information to it.
                    file = open("Fine Details.txt", "a")
                    file.writelines("\n" + Details + ", " + str(mph) + " MPH")
                    file.close()

            #Prints a message if the registration was found in the file.
            if carreg in Details:

                print(carreg, "was found in the known registrations.")
                print()
                print()

            #Otherwise, print that the registration wasn't found.
            else:

                print(carreg, "was not found.")
                print()
                print()

        #Prints a message to the user if the vehicle wasn't speeding.
        else:

            print("You were not speeding.....well done")

        #The user is asked if they want to try another car.
        again = input("Do you want another car reg?")

        #If the answer is not 'y' the program will close and a list will be printed of car reg plates which were speeding and the program will break.
        if again != 'y':
            
            print("Thank you for using the Speed Camera Program ")
            time.sleep(1)
            break

        #This code will run if the user presses 'y' and the code will loop back to the beginning.       
        else:

            print ("Lets put the next car reg into the system")                

    #If the car registration doesn't follow the standard format, then it will be rejected and the use will be asked to enter another registration.
    else:

        print ("Unsuccessful car reg!")
