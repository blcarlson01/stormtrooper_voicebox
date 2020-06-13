from datetime import datetime
import pygame
import RPi.GPIO as GPIO
from time import sleep
import os

pygame.mixer.init()
buttonA = 13 
buttonB = 15
buttonC = 37
buttonD = 16
buttonE = 36
music_path = "/home/pi/Music/audio_files/"
queue = ''

GPIO.setmode(GPIO.BOARD)
GPIO.setup(buttonA,GPIO.IN,pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(buttonB,GPIO.IN,pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(buttonC,GPIO.IN,pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(buttonD,GPIO.IN,pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(buttonE,GPIO.IN,pull_up_down=GPIO.PUD_DOWN)

GPIO.add_event_detect(buttonA, GPIO.RISING, push_message, bouncetime=50)
GPIO.add_event_detect(buttonB, GPIO.RISING, push_message, bouncetime=50)
GPIO.add_event_detect(buttonC, GPIO.RISING, push_message, bouncetime=50)
GPIO.add_event_detect(buttonD, GPIO.RISING, push_message, bouncetime=50)

#TODO: refactor
def push_message(channel):
    press_time = datetime.now().strftime("%A, %d %B %Y at %H:%M:%S %Z")
    button = get_button(channel)
    msg = "Button %s pressed on %s"%(button,press_time)
    global queue
    if button in queue:
        queue += button
        if queue == 'AA':
            pygame.mixer.music.load(music_path+"Follow_me.mp3")
            pygame.mixer.music.play(0)
        if queue == 'BB':
            pygame.mixer.music.load(music_path+"Arent_the_droids.mp3")
            pygame.mixer.music.play(0)
        if queue == 'CC':
            pygame.mixer.music.load(music_path+"Dont_need_to_see_ID.mp3")
            pygame.mixer.music.play(0)
        if queue == 'DD':
            pygame.mixer.music.load(music_path+"No_one_here.mp3")
            pygame.mixer.music.play(0)
        queue = ''
    else:
        if button == 'A':
            pygame.mixer.music.load(music_path+"Whats_goin_on.mp3")
            pygame.mixer.music.play(0)
            queue = 'A'
        if button == 'B':
            pygame.mixer.music.load(music_path+"How_long_had_the_droids.mp3")
            pygame.mixer.music.play(0)
            queue = 'B'
        if button == 'C':
            pygame.mixer.music.load(music_path+"Let_me_see_your_ID.mp3")
            pygame.mixer.music.play(0)
            queue = 'C'
        if button == 'D':
            pygame.mixer.music.load(music_path+"Move_along.mp3")
            pygame.mixer.music.play(0)
            queue = 'D'
     
    print(msg)

def get_button(channel):
    return{
            13: 'A',
            15: 'B',
            37: 'C',
            16: 'D'
            }[channel]

print("Waiting for button press")
while GPIO.input(buttonE) == GPIO. LOW:
    sleep(0.01)

GPIO.cleanup()