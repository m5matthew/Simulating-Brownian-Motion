import requests
import random
import json
import time
import _thread

#BROWNIAN MOTION FUNCTION
def brownianMotion(userID, startingX = 0, startingY = 0):
    
    currentX = startingX
    currentY = startingY

    while True:
        
        xOffset = random.random()
        yOffset = random.random()
        
        if xOffset > 0.5:
            xOffset = 1
        else:
            xOffset = -1
        
        if yOffset > 0.5:
            yOffset = 1
        else:
            yOffset = -1

        currentX += xOffset
        currentY += yOffset

        #sends data
        sendData = {"X": currentX, "Y": currentY, "Z": 5, "Site":"1", "ID": userID}
        json_string = json.dumps(sendData)
        r2 = requests.post("http://marconi.sdsu.edu:8080/GeoLocation/resources/ap", json_string)
        pastebin_url = r2.text
        print("Data was posted for "+userID+"\n", end="")

        #adds one second delay between each iteration
        time.sleep(1)
    
    return;

#FUNCTION CALLS ON DIFFERENT THREADS
try:
   _thread.start_new_thread(brownianMotion, ("USER1", 12, 12) )
   _thread.start_new_thread(brownianMotion, ("USER2", 10, 0) )
   _thread.start_new_thread(brownianMotion, ("USER3", 80, 20) )
   _thread.start_new_thread(brownianMotion, ("USER4", 21, 50) )
   _thread.start_new_thread(brownianMotion, ("USER5", 33, 18) )
   _thread.start_new_thread(brownianMotion, ("USER6", 45, 45) )
   _thread.start_new_thread(brownianMotion, ("USER7", 76, 40) )
   _thread.start_new_thread(brownianMotion, ("USER8", 90, 18) )
    _thread.start_new_thread(brownianMotion, ("USER9", 14, 33) )

except:
   print("Error: unable to start thread")

#LOOP THAT KEEPS THE MAIN THREAD RUNNING
while True:
    time.sleep(10)



    



