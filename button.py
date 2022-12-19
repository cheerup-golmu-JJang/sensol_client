import RPi.GPIO as GPIO


GPIO.setmode(GPIO.BCM)
GPIO.setup(23, GPIO.IN )
GPIO.setup(24, GPIO.IN )
#나가는 버튼의 함수
#return의 값은  0,1 
def outButtonFu() :
	try:
		signal = GPIO.input(24)
		print(signal)
		return signal
	except KeyboardInterrupt:
		GPIO.cleanup()
#들어가ㄴ는 버튼의 함수
#return 값은  0,1 
def inButtonFu() :
	try:
		signal = GPIO.input(23)
		print(signal)
		return signal
	except KeyboardInterrupt:
		GPIO.cleanup()
 