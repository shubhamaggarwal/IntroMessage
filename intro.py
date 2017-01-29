#!/usr/bin/python
import pygame
import time
import os


pygame.mixer.init()
pygame.mixer.music.load("intro.ogg")
pygame.mixer.music.play()
while pygame.mixer.music.get_busy() == True:
    continue
pygame.mixer.music.stop()

pygame.mixer.init()
pygame.mixer.music.load("sys_rad.ogg")
pygame.mixer.music.play()
while pygame.mixer.music.get_busy() == True:
    continue
pygame.mixer.music.stop()

pygame.mixer.init()
pygame.mixer.music.load("5.ogg")
pygame.mixer.music.play()
while pygame.mixer.music.get_busy() == True:
    continue
pygame.mixer.music.stop()

time.sleep(1)

pygame.mixer.init()
pygame.mixer.music.load("4.ogg")
pygame.mixer.music.play()
while pygame.mixer.music.get_busy() == True:
    continue
pygame.mixer.music.stop()

time.sleep(1)

pygame.mixer.init()
pygame.mixer.music.load("3.ogg")
pygame.mixer.music.play()
while pygame.mixer.music.get_busy() == True:
    continue
pygame.mixer.music.stop()

time.sleep(1)

pygame.mixer.init()
pygame.mixer.music.load("2.ogg")
pygame.mixer.music.play()
while pygame.mixer.music.get_busy() == True:
    continue
time.sleep(1)
pygame.mixer.music.stop()

pygame.mixer.music.load("1.ogg")
pygame.mixer.music.play()
while pygame.mixer.music.get_busy() == True:
    continue
time.sleep(1)
pygame.mixer.music.stop()

pygame.mixer.music.load("end.ogg")
pygame.mixer.music.play()
while pygame.mixer.music.get_busy() == True:
    continue
pygame.mixer.music.stop()

pygame.mixer.music.load("Kiss.ogg")
pygame.mixer.music.play()
while pygame.mixer.music.get_busy() == True:
    continue
pygame.mixer.music.stop()
