
import serial
import time


class Display:
    def showTemperature(self, temp_str):
        pass
    def showDutyCycle(self, duty_cycle):
        pass
    def showAutoMode(self, set_point):
        pass
    def showBoilMode(self):
        pass
    def showManualMode(self):
        pass
    def showOffMode(self):
        pass

class LCD(Display):
    def __init__(self, tempUnits):
        self.tempUnits = tempUnits
        ser = serial.Serial("/dev/ttyAMA0", 9600)
        ser.write(b"?BFF")
        time.sleep(.1) #wait 100msec
        ser.write("?f?a")
        ser.write(b"?y0?x00PID off      ")
        ser.write(b"?y1?x00HLT:")
        ser.write(b"?y3?x00Heat: off      ")
        ser.write(b"?D70609090600000000") #define degree symbol
        time.sleep(.1) #wait 100msec

    def showTemperature(self, temp_str):
        #write to LCD
        ser.write(b"?y1?x05")
        ser.write(temp_str)
        ser.write(b"?7") #degree
        time.sleep(.005) #wait 5msec
        if (self.tempUnits == 'F'):
            ser.write("F   ")
        else:
            ser.write("C   ")

    def showDutyCycle(self, duty_cycle):
        #write to LCD
        ser.write(b"?y2?x00Duty: ")
        ser.write(b"%3.1f" % duty_cycle)
        ser.write(b"%     ")

    def showAutoMode(self, set_point):
        ser.write(b"?y0?x00Auto Mode     ")
        ser.write(b"?y1?x00HLT:")
        ser.write(b"?y3?x00Set To: ")
        ser.write(b"%3.1f" % set_point)
        ser.write(b"?7") #degree
        time.sleep(.005) #wait 5msec
        if (self.tempUnits == 'F'):
            ser.write("F   ")
        else:
            ser.write("C   ")

    def showBoilMode(self):
        ser.write(b"?y0?x00Boil Mode     ")
        ser.write(b"?y1?x00BK: ")
        ser.write(b"?y3?x00Heat: on       ")

    def showManualMode(self):
        ser.write(b"?y0?x00Manual Mode     ")
        ser.write(b"?y1?x00BK: ")
        ser.write(b"?y3?x00Heat: on       ")

    def showOffMode(self):
        ser.write(b"?y0?x00PID off      ")
        ser.write(b"?y1?x00HLT:")
        ser.write(b"?y3?x00Heat: off      ")

class NoDisplay(Display):
    def __init__(self):
        pass
