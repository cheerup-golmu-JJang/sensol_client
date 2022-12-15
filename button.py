import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setup(23, GPIO.IN )
GPIO.setup(24, GPIO.IN )
#나가는 버튼의 함수
#return의 값은  0,1 
def outButtonFu() :
	try:
		return GPIO.input(24)
	except KeyboardInterrupt:
		GPIO.cleanup()
#들어가ㄴ는 버튼의 함수
#return 값은  0,1 
def inButtonFu() :
	try:
		return GPIO.input(23)
	except KeyboardInterrupt:
		GPIO.cleanup()
 