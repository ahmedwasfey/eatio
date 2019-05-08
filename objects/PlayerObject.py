from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import numpy as np
from math import *
from random import *
from gameobject import *
from gametextures import  drawText2D

def draw_circle(r=0.5, z=0):
    glBegin(GL_POLYGON)

    for theta in np.arange(0, 2 * pi, .1):
        x = r * sin(theta)
        y = r * cos(theta)
        glVertex(x, 0.05 + z, y)
    glEnd()


class PlayerObject(GameObject):

    def __init__(self, posX=randrange(-100, 100), posY=0, posZ=randrange(-100, 0), scaleX=1, scaleY=1, scaleZ=1, rotY=0, radius=1, r=0, g=1,
                 b=0):
        super().__init__(posX, posY, posZ, scaleX, scaleY, scaleZ, rotY)
        self.radius = radius
        self.xdis = randrange(-100, 100)
        self.zdis = randrange(-100, 0)
        self.r = r
        self.g = g
        self.b = b
        self.arrowPosX = 0
        self.arrowPosZ = 0
        self.area = (pi * self.radius * self.radius) /2
        self.score =0
        self.currentGameScore=0
        self.refrenceGameScore=0
        self.toMakeBig =15

    def update_area(self):
        self.area = pi * self.radius * self.radius * .5

    def draw(self):
        self.applyParentTransform()
        glColor(0, 0, 0)
        draw_circle(self.radius, 0.03)
        draw_circle(self.radius)

        glColor(0, 1, 0)
        draw_circle(self.radius + self.radius * 0.1, -0.02)

        glLoadIdentity()
        glTranslate(self.posX +self.arrowPosX, 0.05, self.posZ +self.arrowPosZ)
        glRotate(self.rotY, 0, 1, 0)
        glBegin(GL_POLYGON)
        glColor(0, 1, 0)
        glVertex(.2 + self.radius * 0.1, 0, self.radius * 0.1 * 2)
        glVertex(- .2 - self.radius * 0.1, 0, self.radius * 0.1 * 2)
        glVertex(0, 0, .346 + self.radius * 0.1 * 4)
        glEnd()

    def Score_update(self ):
        if self.currentGameScore - self.refrenceGameScore >= self.toMakeBig:
            self.radius += 1.5
            self.update_area()
            self.refrenceGameScore = self.currentGameScore
            drawText2D("Size Up!", self.posX, 2, self.posZ, scaleFactor=1)
            self.toMakeBig *= 3
            print("He is Bigggg")



others = 3
listOfallPlayers= []

for i in range(others):
    listOfallPlayers.append(PlayerObject())

for i in range(others):
    listOfallPlayers.append(PlayerObject())
    listOfallPlayers[i].posZ = randrange(-100, 0)
    listOfallPlayers[i].posX = randrange(-100, 100)


def draw_others():
    global others
    global listOfallPlayers
    for i in range(others):
        if listOfallPlayers[i].posX == listOfallPlayers[i].xdis and listOfallPlayers[i].posZ == listOfallPlayers[i].zdis:
            listOfallPlayers[i].xdis = randrange(-100, 100)
            listOfallPlayers[i].zdis = randrange(-100, 0)
        else:
            if listOfallPlayers[i].posX < listOfallPlayers[i].xdis:
                listOfallPlayers[i].posX += .5
                if listOfallPlayers[i].posZ < listOfallPlayers[i].zdis:
                    listOfallPlayers[i].posZ += .5
                    listOfallPlayers[i].rotY = 45
                    listOfallPlayers[i].arrowPosX = listOfallPlayers[i].radius + .2
                    listOfallPlayers[i].arrowPosZ = listOfallPlayers[i].radius + .2
                elif listOfallPlayers[i].posZ > listOfallPlayers[i].zdis:
                    listOfallPlayers[i].posZ -= .5
                    listOfallPlayers[i].rotY = 135
                    listOfallPlayers[i].arrowPosX = listOfallPlayers[i].radius + .2
                    listOfallPlayers[i].arrowPosZ = -listOfallPlayers[i].radius - .2
                else:
                    listOfallPlayers[i].rotY = 90
                    listOfallPlayers[i].arrowPosX = listOfallPlayers[i].radius + .2
                    listOfallPlayers[i].arrowPosZ = 0

            elif listOfallPlayers[i].posX > listOfallPlayers[i].xdis:
                listOfallPlayers[i].posX -= .5
                if listOfallPlayers[i].posZ > listOfallPlayers[i].zdis:
                    listOfallPlayers[i].posZ -= .5
                    listOfallPlayers[i].rotY = 225
                    listOfallPlayers[i].arrowPosX = -listOfallPlayers[i].radius - .2
                    listOfallPlayers[i].arrowPosZ = -listOfallPlayers[i].radius - .2
                elif listOfallPlayers[i].posZ < listOfallPlayers[i].zdis:
                    listOfallPlayers[i].posZ += .5
                    listOfallPlayers[i].rotY = -45
                    listOfallPlayers[i].arrowPosX = -listOfallPlayers[i].radius - .2
                    listOfallPlayers[i].arrowPosZ = listOfallPlayers[i].radius + .2
                else:
                    listOfallPlayers[i].rotY = - 90
                    listOfallPlayers[i].arrowPosX = -listOfallPlayers[i].radius - .2
                    listOfallPlayers[i].arrowPosZ = 0
            else:
                if listOfallPlayers[i].posZ > listOfallPlayers[i].zdis:
                    listOfallPlayers[i].posZ -= .5
                    listOfallPlayers[i].rotY = 180
                    listOfallPlayers[i].arrowPosX = 0
                    listOfallPlayers[i].arrowPosZ = -listOfallPlayers[i].radius - .2
                elif listOfallPlayers[i].posZ < listOfallPlayers[i].zdis:
                    listOfallPlayers[i].posZ += .5
                    listOfallPlayers[i].rotY = 0
                    listOfallPlayers[i].arrowPosX = 0
                    listOfallPlayers[i].arrowPosZ = listOfallPlayers[i].radius + .2

        listOfallPlayers[i].draw()
