#Average Speed Check - Task 1 OCR GCSE Computing
#30th June 2015
#Mr Miller

#importing of the time module
import time

#constant distance of 1 mile for this speed camera
SensorDistance = 1

#constant speed limit of 60 miles per hour for this speed camera
SpeedLimit = 60

#An initial empty list of speeding cars
SpeedingCars = []

#This is my welcome message to the user
print ("Welcome to Mr Millers Average Speed Check Program")

#This code will run while true
while True:

#A variable of car reg to ask the user their input for the car reg plate
    carreg = input("Please enter your car reg plate\n")

#If the car reg input has been entered the program will continue and will thank the user
    if carreg != "":
        print ("Thank you, your car reg is ",carreg)
        print()
        print()

#this code will ask the user when they passed the first sensor of the speed camera

        print("We would like to know what time you entered the start of the " + str(SensorDistance) +" Mile Speed Camera?")
        print()
        time.sleep(1)

#The user presses the enter button to say when they passed the first point of the speed camera
        
        x = input("Press enter when your car passes the first point")
        print()

#this code will ask the user when they passed the first sensor of the speed camera

        print("We would like to know what time you left the end of the " + str(SensorDistance) +" Mile Speed Camera?")
        starttime=time.time()
        print()
        time.sleep(1)

#The user presses the enter button to say when they passed the second point of the speed camera

        x=input("Press enter when your car passes the second point")
        endtime=time.time()
        print()

#Formula used to worked out the elapsed time

        elapsedtime=endtime-starttime

#Formula used to work out mph and round it down to 2 dp.  Telling the user what their speed was in mph
        
        mph = (SensorDistance/elapsedtime)*3600

        mph = round(mph,2)
        print ("Having passed through the two sensors you were trvelling",str(mph),"mph")

#Here an IF statement is used to show if the user was speeding.  If so the car reg is added to the empty list
        print()
        if int(mph)>int(SpeedLimit):
            print ("You were speeding.....slow down, you have been added to the list")
            SpeedingCars.append(carreg)
#Here the use is told if they are within the speed limit
        else:
            print ("You were not speeding......well done, always keep within the speed limit")

#The user is asked if they want to try another car       
        again = input("Do you want another car reg?")

#If the answer is not 'y' the program will close and a list will be printed of car reg plates which were speeding and the program will break
        if again !='y':
            print ("Thank you for using the Speed Camera Program ")
            time.sleep(1)
            print ("The cars speeding were ",(SpeedingCars))

            break
#This code will run if the user presses 'y' and the code will loop back to the beginning        
        else:
            print ("Lets put the next car reg into the system")
#This code runs if the user does not enter a car reg plate at the beginning and the program loops back to the start               
    else:
        print ("You have not entered a car reg plate")
        time.sleep(1)

        print()
        print()
        print()

    

   
