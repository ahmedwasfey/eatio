from abc import ABC, abstractmethod
from OpenGL.GL import *

from constants import *


class Animation:

    def __init__(self, valueName, fromValue, toValue, animationTime, priority=AnimationPriority.Normal, onAnimationFinished=None):
        self.valueName = valueName
        self.fromValue = fromValue
        self.toValue = toValue
        self.animationTime = animationTime
        self.priority = priority
        self.currentProgress = 0
        self.onAnimationFinished = onAnimationFinished

class DeltaAnimation:

    def __init__(self, valueName, deltaValue, animationTime, priority=AnimationPriority.Normal, onAnimationFinished=None):
        self.valueName = valueName
        self.deltaValue = deltaValue
        self.animationTime = animationTime
        self.priority = priority
        self.currentProgress = 0
        self.fromValue = None
        self.onAnimationFinished = onAnimationFinished


class GameObject(ABC):

    def __init__(self, posX, posY, posZ, scaleX=1, scaleY=1, scaleZ=1, rotY=0):
        self.posX = posX
        self.posY = posY
        self.posZ = posZ

        self.scaleX = scaleX
        self.scaleY = scaleY
        self.scaleZ = scaleZ

        self.rotY = rotY

        self.animationList = []
        self.collision = 0
        super().__init__()

    def applyParentTransform(self):
        glLoadIdentity()
        glTranslate(self.posX, self.posY, self.posZ)
        glRotate(self.rotY, 0, 1, 0)
        glScale(self.scaleX, self.scaleY, self.scaleZ)

    @abstractmethod
    def draw(self):
        pass

    @staticmethod
    def _calculateNextValue(currentValue, animation):

        if isinstance(animation, Animation):

            if animation.fromValue is None:
                animation.fromValue = currentValue
                if animation.fromValue == animation.toValue:
                    animation.currentProgress = 1
            if animation.currentProgress >= 1:
                return animation.toValue
            return animation.fromValue + ((animation.toValue - animation.fromValue) * animation.currentProgress)

        elif isinstance(animation, DeltaAnimation):
            if animation.fromValue is None:
                animation.fromValue = currentValue
            if animation.currentProgress >= 1:
                return animation.fromValue + animation.deltaValue
            return animation.fromValue + (animation.deltaValue * animation.currentProgress)

    def onFrameTick(self, dt):
        highPriority = []
        for anim in self.animationList:
            if anim.priority == AnimationPriority.High:
                highPriority.append(anim)

        if len(highPriority) > 0:
            self.animationList.clear()
            for anim in highPriority:
                self.animationList.append(anim)

        toBeRemoved = []
        for anim in self.animationList:

            if anim.currentProgress >= 1:
                toBeRemoved.append(anim)

            if anim.valueName == AnimationParams.posX:
                self.posX = self._calculateNextValue(self.posX, anim)
            elif anim.valueName == AnimationParams.posY:
                self.posY = self._calculateNextValue(self.posY, anim)
            elif anim.valueName == AnimationParams.posZ:
                self.posZ = self._calculateNextValue(self.posZ, anim)
            elif anim.valueName == AnimationParams.scaleX:
                self.scaleX = self._calculateNextValue(self.scaleX, anim)
            elif anim.valueName == AnimationParams.scaleY:
                self.scaleY = self._calculateNextValue(self.scaleY, anim)
            elif anim.valueName == AnimationParams.scaleZ:
                self.scaleZ = self._calculateNextValue(self.scaleZ, anim)
            elif anim.valueName == AnimationParams.rotY:
                self.rotY = self._calculateNextValue(self.rotY, anim)

            anim.currentProgress += (dt / anim.animationTime)

        for tbr in toBeRemoved:
            self.animationList.remove(tbr)
            if not tbr.onAnimationFinished is None:
                tbr.onAnimationFinished()
                print("on animation finished called !!")

    def startAnimation(self, animation):
        animation.currentProgress = 0
        self.animationList.append(animation)
