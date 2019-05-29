from random import *

import numpy as np
from math import *

from gameobject import *
from gametextures import drawText2D


def draw_circle(r=0.5, z=0.0):
    glBegin(GL_POLYGON)

    for theta in np.arange(0, 2 * pi, .1):
        x = r * sin(theta)
        y = r * cos(theta)
        glVertex(x, 0.05 + z, y)
    glEnd()


class PlayerObject(GameObject):

    def __init__(self, posX=randrange(-100, 100), posY=0, posZ=randrange(-100, 0), scaleX=1, scaleY=1, scaleZ=1, rotY=0,
                 radius=1, r=0, g=1,
                 b=0, isAI=True):
        super().__init__(posX, posY, posZ, scaleX, scaleY, scaleZ, rotY)
        self.radius = radius
        self.xdis = randrange(-100, 100)
        self.zdis = randrange(-100, 0)
        self.r = r
        self.g = g
        self.b = b
        self.arrowPosX = 0
        self.arrowPosZ = 0
        self.area = (pi * self.radius * self.radius) / 2
        self.score = 0
        self.currentGameScore = 0
        self.refrenceGameScore = 0
        self.toMakeBig = 5
        self.isAI = isAI

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
        glTranslate(self.posX + self.arrowPosX, 0.05, self.posZ + self.arrowPosZ)
        glRotate(self.rotY, 0, 1, 0)
        glBegin(GL_POLYGON)
        glColor(0, 1, 0)
        glVertex(.2 + self.radius * 0.1, 0, self.radius * 0.1 * 2)
        glVertex(- .2 - self.radius * 0.1, 0, self.radius * 0.1 * 2)
        glVertex(0, 0, .346 + self.radius * 0.1 * 4)
        glEnd()

    def Score_update(self):
        if self.currentGameScore - self.refrenceGameScore >= self.toMakeBig:
            self.radius += 1.5
            self.update_area()
            self.refrenceGameScore = self.currentGameScore
            drawText2D("Size Up!", self.posX, 2, self.posZ, scaleFactor=1)
            self.toMakeBig *= 3
            # print("He is Bigggg")
            return True
        return False


others = 3


def move_others(listOfallPlayers):
    for obj in listOfallPlayers:
        if obj.isAI:
            if obj.posX == obj.xdis and obj.posZ == obj.zdis:
                obj.xdis = randrange(-100, 100)
                obj.zdis = randrange(-100, 0)
            else:
                if obj.posX < obj.xdis:
                    obj.posX += .5
                    if obj.posZ < obj.zdis:
                        obj.posZ += .5
                        obj.rotY = 45
                        obj.arrowPosX = obj.radius + .2
                        obj.arrowPosZ = obj.radius + .2
                    elif obj.posZ > obj.zdis:
                        obj.posZ -= .5
                        obj.rotY = 135
                        obj.arrowPosX = obj.radius + .2
                        obj.arrowPosZ = -obj.radius - .2
                    else:
                        obj.rotY = 90
                        obj.arrowPosX = obj.radius + .2
                        obj.arrowPosZ = 0

                elif obj.posX > obj.xdis:
                    obj.posX -= .5
                    if obj.posZ > obj.zdis:
                        obj.posZ -= .5
                        obj.rotY = 225
                        obj.arrowPosX = -obj.radius - .2
                        obj.arrowPosZ = -obj.radius - .2
                    elif obj.posZ < obj.zdis:
                        obj.posZ += .5
                        obj.rotY = -45
                        obj.arrowPosX = -obj.radius - .2
                        obj.arrowPosZ = obj.radius + .2
                    else:
                        obj.rotY = - 90
                        obj.arrowPosX = -obj.radius - .2
                        obj.arrowPosZ = 0
                else:
                    if obj.posZ > obj.zdis:
                        obj.posZ -= .5
                        obj.rotY = 180
                        obj.arrowPosX = 0
                        obj.arrowPosZ = -obj.radius - .2
                    elif obj.posZ < obj.zdis:
                        obj.posZ += .5
                        obj.rotY = 0
                        obj.arrowPosX = 0
                        obj.arrowPosZ = obj.radius + .2
