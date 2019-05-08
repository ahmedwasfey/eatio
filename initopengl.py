from time import time
#from winsound import PlaySound, SND_ASYNC, SND_LOOP, SND_FILENAME

from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import pygame
def displayFunction():
    global draw
    draw()


def initOpenGl(drawParameter, onMouseKey, onKeyboardKey, onSpecialKey):
    global currentTime
    global draw

    glutInit()
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGBA | GLUT_DEPTH)
    glutInitWindowSize(500, 500)
    glutCreateWindow(b"EAT.io")
    #pygame.mixer.init(44100, -16, 2, 2048)  # intianliazion of game sound
    #pygame.mixer.music.load("/home/ahmed/Downloads/eatio-master (3)/eatio-master/resources/sounds/bg_music.wav")  # open sound file
    #pygame.mixer.music.play(-1)  # play sound to infint
    #PlaySound("resources/sounds/bg_music.wav", SND_FILENAME | SND_LOOP | SND_ASYNC)

    currentTime = time()
    draw = drawParameter

    glutDisplayFunc(displayFunction)
    glutIdleFunc(displayFunction)

    glutMouseFunc(onMouseKey)
    glutKeyboardFunc(onKeyboardKey)
    glutSpecialFunc(onSpecialKey)

    glutMainLoop()
