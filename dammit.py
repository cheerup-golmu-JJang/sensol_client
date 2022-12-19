import client
import button
import sensol
import datetime
import threading
import time

typedam = "waterLeval"
typelight = "light"
typebutton = "dambutton"
setDelayTime =  1

def ClinetDataSet(sensolType,sensolNumber):
    ##client.send_data의 인자
    ##(Type,id,Data) 
    ##Type: 1의 자리: 데이터 종류 
    ##1:수위 2:조도 3:들어오는 스위치 4:나가는 스위치
    resultTimeWL = 1
    resultTimeLight = 1
    number = 1000;
    while True:
        now=datetime.datetime.now() 
        print(str(now.second)+": wl :"+str(resultTimeWL)+": li :"+str(resultTimeLight))
        
        
        if sensolType == 1: 
            
            if now.second == resultTimeWL:
                sensolData = sensol.analog_read_WL(sensolNumber-1)
                client.send_data(1,sensolNumber+number,sensolData)
                resultTimeWL = resultTimeWL + setDelayTime     
                if resultTimeWL >= 60:
                    resultTimeWL = 1
        if sensolType == 2:
            now=datetime.datetime.now()
            if now.second == resultTimeLight:
                sensolData = sensol.analog_read_light(sensolNumber+2)
                client.send_data(2,sensolNumber+number,sensolData)   
                resultTimeLight = resultTimeLight + setDelayTime  
                if resultTimeLight >= 60:
                    resultTimeLight = 1  
def buttonSet(damNum):
    if damNum == 1:
        while True:
            if button.outButtonFu() == 0:
                client.send_data(4,1001,1)
                time.sleep(0.3)
            if button.inButtonFu() == 0 :
                client.send_data(3,1001,1)
                time.sleep(0.3)
def ThreadRun():
    threading.Thread(target=ClinetDataSet,args=(1,1,),daemon=True).start()
    threading.Thread(target=ClinetDataSet,args=(1,2,),daemon=True).start()
    threading.Thread(target=ClinetDataSet,args=(1,3,),daemon=True).start()
    threading.Thread(target=ClinetDataSet,args=(2,1,),daemon=True).start()
    threading.Thread(target=ClinetDataSet,args=(2,2,),daemon=True).start()
    threading.Thread(target=ClinetDataSet,args=(2,3,),daemon=True).start()
    threading.Thread(target=buttonSet,args=(1,)).start()
   
ThreadRun()
