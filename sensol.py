import spidev, time

spi = spidev.SpiDev()
spi.open(0,0)
spi.max_speed_hz=1350000
def analog_read_WL(channel):
	if (channel > 0 and channel <4):
		r = spi.xfer2([1, (8 + channel) << 4, 0])
		adc_out = ((r[1]&3) << 8) + r[2]
		return adc_out
def analog_read_light(channel):
	if (channel > 0 and channel <4):
		r = spi.xfer2([1, (8 + channel) << 4, 0])
		adc_out = ((r[1]&3) << 8) + r[2]
		return adc_out

#while True:
#1	reading1 = analog_read(0)
#	reading2 = analog_read(1)
#	reading3 = analog_read(2)
#	reading4 = analog_read(3)
#	reading5 = analog_read(4)
#	reading6 = analog_read(5)
#	print("Re1=%d ,Re2=%d  ,Re3=%d" %(reading1,reading2,reading3))
#	print("re4=%d, re5=%d, re6=%d" %(reading4,reading5,reading6))
#	time.sleep(1)
