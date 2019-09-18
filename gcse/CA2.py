#Average Speed Check - Task 2 OCR GCSE Computing
#6th July 2015
#Mr Miller

#importing of the time module
import time
import re
import math

#This is a rule for the car registrations to follow, they must be in this format
carregRule = "[a-zA-Z][a-zA-Z][\d][\d] [a-zA-Z][a-zA-Z][a-zA-Z]"

#constant distance of 1 mile for this speed camera
SensorDistance = 1

#constant speed limit of 60 miles per hour for this speed camera
SpeedLimit = 60

#An initial empty list of speeding cars
NonStandardReg = []

NonStandardSpeed = []

#This is my welcome message to the user
print ("Welcome to Mr Millers Average Speed Check Program")


#This code will run while true
while True:

    
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

    mph = math.ceil(mph)
    print ("Having passed through the two sensors you were travelling",str(mph),"mph")

#Here an IF statement is used to show if the user was speeding.  If so the car reg is added to the empty list
    print()
    if int(mph)>int(SpeedLimit):
        print ("You were speeding.....slow down, we need to take your car reg for our records")
            
#The variable carreg is used to collect the car registration plate of the user
        carreg = input("Enter your car reg ")
        
#re.search is used to check the car reg against the set pattern
        if re.match(carregRule,carreg):

            print ("Successful car reg!")
            print ("However as you were speeding we need to add 3 points to your driving license")

        else:

            print ("Unsuccessful car reg!")
            print ("As well as speeding you also have a none standard car reg of ",carreg)
            print ("We need to send your details to the DVLA")
            NonStandardReg.append(carreg)
            NonStandardSpeed.append(mph)

    else:
        print ("You were not speeding.....")           

           

    #The user is asked if they want to try another car       
    again = input("Do you want another car reg?")

    #If the answer is not 'y' the program will close and a list will be printed of car reg plates which were speeding and the program will break

    if again !='y':
        print ("Thank you for using the Speed Camera Program ")
        time.sleep(1)
        
        combined=[]

        for x in range(len(NonStandardReg)):
            combined.append(NonStandardReg[x])
            combined.append(NonStandardSpeed[x])
             
        text_file = open("speedrecords.txt","w")
        text_file.write("The DVLA records show :\n")
        text_file.write("\n")
        text_file.write("Non Standard Registration and (mph)\t"+(str(combined)))
        text_file.close()

        break
    
    #This code will run if the user presses 'y' and the code will loop back to the beginning        
    else:
        print ("Lets put the next car reg into the system")


                

                
                



