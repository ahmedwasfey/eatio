from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import numpy as np
from math import *
from random import *
from gameobject import *


class LightingObject(GameObject):

    def __init__(self, posX, posY, posZ, scaleX=1, scaleY=1, scaleZ=1, rotY=0, al=1):
        super().__init__(posX, posY, posZ, scaleX, scaleY, scaleZ, rotY)
        self.Length = 0
        self.width = 0
        self.alpha = al
        self.area = 1.5

    def draw(self):
        self.applyParentTransform()
        glColor4f(0.51, 0.72, 0.91, self.alpha)
        glScale(.4, 1, 0.5)
        glutSolidCube(0.5)

        self.applyParentTransform()
        glTranslate(0, 1.5, 0)
        glScale(.2, 5, 0.2)
        glutSolidCube(0.5)

        self.applyParentTransform()
        glTranslate(0.5, 2.65, 0)
        glScale(2, 0.1, 0.1)
        glutSolidCube(0.5)

        self.applyParentTransform()
        glTranslate(1.2, 2.58, 0)
        glScale(.9, 0.2, 0.5)
        glutSolidCube(0.5)


class ConeObject(GameObject):

    def __init__(self, posX, posY, posZ, scaleX=1, scaleY=1, scaleZ=1, rotY=0, al=1):
        super().__init__(posX, posY, posZ, scaleX, scaleY, scaleZ, rotY)
        self.Length = 0
        self.width = 0
        self.area = 1
        self.alpha = 1

    def draw(self):
        glColor4f(0.99, 0.6, 0.1, self.alpha)
        self.applyParentTransform()
        glScale(1, 0.1, 1)
        glutSolidCube(.8)

        glColor4f(0.89, 0.51, 0.1, self.alpha)
        self.applyParentTransform()
        glRotate(-90, 1, 0, 0)
        glutSolidCone(.4, 1.2, 10, 10)


class CylinderObject_1(GameObject):
    def __init__(self, posX, posY, posZ, scaleX=1, scaleY=1, scaleZ=1, rotY=0):
        super().__init__(posX, posY, posZ, scaleX, scaleY, scaleZ, rotY)
        self.Length = 0
        self.width = 0
        self.area = 1
        self.alpha = 1

    def draw(self):
        self.applyParentTransform()
        glColor4f(0.67, 0.65, 0.54, self.alpha)
        glRotate(-90, 1, 0, 0)
        glutSolidCylinder(.12, .5, 10, 10)


class CylinderObject_2(GameObject):
    def __init__(self, posX, posY, posZ, scaleX=1, scaleY=1, scaleZ=1, rotY=0):
        super().__init__(posX, posY, posZ, scaleX, scaleY, scaleZ, rotY)
        self.Length = 0
        self.width = 0
        self.area = 1
        self.alpha = 1

    def draw(self):
        glColor4f(0.36, 0.59, 0.23, self.alpha)
        self.applyParentTransform()
        glRotate(-90, 1, 0, 0)
        glutSolidCylinder(0.4, 0.7, 6, 5)

        glColor4f(0.83, 1, 0.97, self.alpha)
        self.applyParentTransform()
        glTranslate(0, .7, 0)
        glRotate(-90, 1, 0, 0)
        glutSolidCylinder(0.4, 0.08, 6, 5)


class BarrierObject(GameObject):
    def __init__(self, posX, posY, posZ, scaleX=1, scaleY=1, scaleZ=1, rotY=0):
        super().__init__(posX, posY, posZ, scaleX, scaleY, scaleZ, rotY)
        self.Length = 0
        self.width = 0
        self.area = 1
        self.alpha = 1

    def draw(self):
        glColor4f(0.38, 0.58, 0.76, self.alpha)
        self.applyParentTransform()
        glTranslate(0, 1, 0)
        glScale(0.06, 2, 0.06)
        glutSolidCube(1)

        self.applyParentTransform()
        glTranslate(0.4, 1, 0)
        glScale(0.06, 2, 0.06)
        glutSolidCube(1)

        self.applyParentTransform()
        glTranslate(0.8, 1, 0)
        glScale(0.06, 2, 0.06)
        glutSolidCube(1)

        self.applyParentTransform()
        glTranslate(1.2, 1, 0)
        glScale(0.06, 2, 0.06)
        glutSolidCube(1)

        self.applyParentTransform()
        glTranslate(-0.4, 1, 0)
        glScale(0.06, 2, 0.06)
        glutSolidCube(1)

        self.applyParentTransform()
        glTranslate(-0.8, 1, 0)
        glScale(0.06, 2, 0.06)
        glutSolidCube(1)

        self.applyParentTransform()
        glTranslate(-1.2, 1, 0)
        glScale(0.06, 2, 0.06)
        glutSolidCube(1)

        self.applyParentTransform()
        glTranslate(0, 0.2, 0)
        glRotate(-90, 0, 0, 1)
        glScale(0.06, 2.5, 0.06)
        glutSolidCube(1)

        self.applyParentTransform()
        glTranslate(0, 1.8, 0)
        glRotate(-90, 0, 0, 1)
        glScale(0.06, 2.5, 0.06)
        glutSolidCube(1)


class TrafficlightsObject(GameObject):
    def __init__(self, posX, posY, posZ, scaleX=1, scaleY=1, scaleZ=1, rotY=0):
        super().__init__(posX, posY, posZ, scaleX, scaleY, scaleZ, rotY)
        self.Length = 0
        self.width = 0
        self.area = 1
        self.alpha = 1

    def draw(self):
        glColor4f(0.38, 0.58, 0.76, self.alpha)
        self.applyParentTransform()
        glScale(0.2, 0.7, 0.2)
        glutSolidCube(1)

        self.applyParentTransform()
        glTranslate(0, 1.5, 0)
        glScale(0.1, 2.5, 0.1)
        glutSolidCube(1)

        glColor4f(0.68, 0.69, 0.73, self.alpha)
        self.applyParentTransform()
        glTranslate(0.1, 2, 0)
        glScale(0.1, 1, 0.4)
        glutSolidCube(1)

        glColor4f(0.32, 0.49, 0.17, self.alpha)
        self.applyParentTransform()
        glTranslate(0.2, 1.8, 0)
        glScale(0.1, 0.15, 0.15)
        glutSolidCube(1)

        glColor4f(0.77, 0.43, 0.07, self.alpha)
        self.applyParentTransform()
        glTranslate(0.2, 2.1, 0)
        glScale(0.1, 0.15, 0.15)
        glutSolidCube(1)

        glColor4f(0.46, 0.18, 0.19, self.alpha)
        self.applyParentTransform()
        glTranslate(0.2, 2.4, 0)
        glScale(0.1, 0.15, 0.15)
        glutSolidCube(1)


class IceManObject(GameObject):
    def __init__(self, posX, posY, posZ, scaleX=.5, scaleY=.5, scaleZ=.5, rotY=0):
        super().__init__(posX, posY, posZ, scaleX, scaleY, scaleZ, rotY)
        self.Length = 0
        self.width = 0
        self.area = 2
        self.alpha = 1

    def draw(self):
        self.applyParentTransform()
        glColor4f(0.93359, 0.9492, 0.984375, self.alpha)  # Base_Sphere
        glutSolidSphere(2, 15, 10)
        self.applyParentTransform()
        glColor4f(0.996, 0.40625, 0.3007, self.alpha)
        glTranslate(0, 1.3, 0)
        glScale(2.6, 1.7, 2.3)
        glutSolidSphere(0.6, 10, 10)
        self.applyParentTransform()
        glColor4f(0.93359, 0.9492, 0.984375, self.alpha)
        glTranslate(0, 2.2, 0)
        glutSolidSphere(1.4, 20, 25)
        self.applyParentTransform()
        glColor4f(0.996, 0.40625, 0.3007, self.alpha)
        glTranslate(0, 3, 0)
        glScale(2.6, 1.7, 2.3)
        glutSolidSphere(0.4, 10, 10)
        self.applyParentTransform()
        glTranslate(0, 3.6, 0)
        glRotate(-90, 1, 0, 0)
        glutSolidCone(0.4, 0.8, 5, 5)
        self.applyParentTransform()
        glTranslate(1.2, 2.3, 0)
        glRotate(90, 0, 1, 0)
        glutSolidCone(0.2, 0.7, 10, 10)


class TreeObject(GameObject):
    def __init__(self, posX, posY, posZ, scaleX=1, scaleY=1, scaleZ=1, rotY=0):
        super().__init__(posX, posY, posZ, scaleX, scaleY, scaleZ, rotY)
        self.Length = 0
        self.width = 0
        self.area = 2
        self.alpha = 1

    def draw(self):
        self.applyParentTransform()
        glColor4f(0.64843, 0.4140625, 0.26953125, self.alpha)
        glScale(1, 3, 1)
        glutSolidCube(0.5)
        self.applyParentTransform()
        glColor4f(0.66796875, 0.8554, 0.18359, self.alpha)
        glScale(1.5, 1, 1.5)
        glTranslate(0, 1.5, 0)
        glutSolidCube(1.5)
        self.applyParentTransform()
        glColor4f(0.74218, 0.9453125, 0.20703125, self.alpha)
        glScale(3, 0.8, 2)
        glTranslate(0, 3, 0)
        glutSolidCube(0.5)
        self.applyParentTransform()
        glColor4f(0.74218, 0.9453125, 0.20703125, self.alpha)
        glScale(3, 2, 0.8)
        glTranslate(0, 0.75, 1.125)
        glutSolidCube(0.5)
