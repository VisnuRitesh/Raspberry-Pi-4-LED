from Tkinter import *
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setup(19,GPIO.OUT)
GPIO.setup(26,GPIO.OUT)
GPIO.setup(21,GPIO.OUT)
GPIO.setup(20,GPIO.OUT)

GPIO.output(19,GPIO.LOW)
GPIO.output(26,GPIO.LOW)
GPIO.output(21,GPIO.LOW)
GPIO.output(20,GPIO.LOW)

mw=Tk()

def ledOn():
    if GPIO.input(19):
        GPIO.output(19,GPIO.LOW)
        button["text"]="LED 1 ON"
    else:
        GPIO.output(19,GPIO.HIGH)
        button["text"]="LED 1 OFF"

def ledOn2():
    if GPIO.input(26):
        GPIO.output(26,GPIO.LOW)
        button2["text"]="LED 2 ON"
    else:
        GPIO.output(26,GPIO.HIGH)
        button2["text"]="LED 2 OFF"

def ledOn3():
    if GPIO.input(21):
        GPIO.output(21,GPIO.LOW)
        button3["text"]="LED 3 ON"
    else:
        GPIO.output(21,GPIO.HIGH)
        button3["text"]="LED 3 OFF"

def ledOn4():
    if GPIO.input(20):
        GPIO.output(20,GPIO.LOW)
        button4["text"]="LED 4 ON"
    else:
        GPIO.output(20,GPIO.HIGH)
        button4["text"]="LED 4 OFF"


def exit():
    GPIO.cleanup()
    mw.quit()

mw.title("4 LED Control")

button=Button(mw,text="LED 1 ON",command=ledOn).grid(row=0,column=0)
button2=Button(mw,text="LED 2 ON",command=ledOn2).grid(row=0,column=2)
button3=Button(mw,text="LED 3 ON",command=ledOn3).grid(row=1,column=0)
button4=Button(mw,text="LED 4 ON",command=ledOn4).grid(row=1,column=2)

ex=Button(mw,text="QUIT",command=exit).grid(row=3,column=1)

mainloop()
