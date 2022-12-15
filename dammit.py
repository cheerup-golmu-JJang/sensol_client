import client
import button
import sensol
import time
#각센서의 타입들
typedam = "waterLeval"#수위 센서
typelight = "light"#조도 센서
typebutton = "dambutton"#입출 버튼

def runClinetStart(sensolType,sensolNumber):
    if sensolType == "waterLeval":
        while True:
            sensolData = sensol.analog_read_WL(sensolNumber)
            client.run_client(,sensolData)      
    if sensolType == "light":
        while True:
            sensol. analog_read_light(sensolNumber)
    if sensolType == "dambutton":
        if sensolNumber == "in":
            while True:
                button.inButtonFu();
        if sensolNumber == "out":
            while True:
                button.outButtonFu();
