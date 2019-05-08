from OpenGL.GLUT import *
from gameobject import *
from random import randrange

class CharacterObject(GameObject):

    def __init__(self, posX, posY, posZ, scaleX=1, scaleY=1, scaleZ=1, rotY=0, r=0, g=0, b=0):
        super().__init__(posX, posY, posZ, scaleX, scaleY, scaleZ, rotY)
        self.Length=0
        self.width=0
        self.area=1
        self.HeadDeltaY = 0
        self.HeadUpDown = 1
        self.r=r/255
        self.g=g/255
        self.b=b/255
        Straight(self)

    def draw(self):
        self.applyParentTransform()
        glColor3f(self.r, self.g, self.b)
        glTranslate(0, 1.5, 0)
        glScale(.6, .9, .4)
        glutSolidCube(.976)

        self.applyParentTransform()
        glColor3f(241 / 255, 195 / 255, 125 / 255)
        glTranslate(0, 2.0 + self.HeadDeltaY, 0)
        glScale(.6, .3, .4)
        glutSolidCube(1.03)

        self.applyParentTransform()
        glColor3f(0, 0, 0.1)
        glTranslate(0, 2.25 + self.HeadDeltaY, 0)
        glScale(.6, .2, .4)
        glutSolidCube(1.03)

    def onFrameTick(self, dt):
        super().onFrameTick(dt)
        if self.HeadDeltaY > 0.1:
            self.HeadUpDown = 0
        if self.HeadDeltaY < -0.1:
            self.HeadUpDown = 1
        if self.HeadUpDown:
            self.HeadDeltaY += dt * 0.5
        else:
            self.HeadDeltaY -= dt * 0.5

#movement
def Straight(obj):
    obj.rotY=360
    a20 = DeltaAnimation(AnimationParams.posZ, 3 , 3)
    a20.onAnimationFinished = lambda: partX1(obj)
    obj.startAnimation(a20)
def partX1(obj):
    obj.rotY=90
    a9 = DeltaAnimation(AnimationParams.posX,-3 , 3)
    a9.onAnimationFinished = lambda : Straight2(obj)
    obj.startAnimation(a9)
def partX2(obj):
    obj.rotY=270
    a9 = DeltaAnimation(AnimationParams.posX,3 , 3)
    a9.onAnimationFinished = lambda : Straight(obj)
    obj.startAnimation(a9)

def Straight2(obj):
    obj.rotY=180
    a21 = DeltaAnimation(AnimationParams.posZ,-3 , 3)
    a21.onAnimationFinished = lambda: partX2(obj)
    obj.startAnimation(a21)
