import datetime
import client
import time
import sensol
import threading

def timeTest(number):
    resultTime = 1
    while True:
        now=datetime.datetime.now()
        print(str(now.second)+":"+str(resultTime))
        if now.second == resultTime:
            resultTime = resultTime + 5
            print(str(now.second)+":"+str(resultTime))
            sensolData = sensol.analog_read_WL(number-1)
            client.send_data(1,1001,sensolData)  
            time.sleep(1)
            print(str(now.second))
            if resultTime >= 60:    
                resultTime = 0
             
while True:
    now=datetime.datetime.now() 
    lae = now.second
    print(lae)
    if lae == 10:
        print("HHHHHHHHHHH")