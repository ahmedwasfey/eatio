from gameobject import *
from math import *


def isCollided(player, obj, ):
    if obj.rotY == 90 or obj.rotY == -90:
        return testCube(player.radius, player.posX, player.posZ, obj.width, obj.Length, obj.posX, obj.posZ)
    else:
        return testCube(player.radius, player.posX, player.posZ, obj.Length, obj.width, obj.posX, obj.posZ)


def testCube (playerRadius , playerCX,playerCZ , objectLength , objectWidth , objectCX , objectCZ):

    #ObjectDimensions
    objectLength = objectLength/2
    objectWidth = objectWidth/2
    rigthX = objectCX + objectWidth
    leftX = objectCX - objectWidth
    topZ = objectCZ + objectLength
    bottomZ = objectCZ - objectLength

    if playerCX <= leftX:
         collisionX= leftX
    else:
        if playerCX >= rigthX:
            collisionX = rigthX
        else:
            collisionX = playerCX

    if playerCZ <= bottomZ:
        collisionZ = bottomZ
    else:
        if playerCZ >= topZ:
            collisionZ = topZ
        else:
            collisionZ = playerCZ

    distanceX = playerCX - collisionX
    distanceZ = playerCZ - collisionZ
    distance = sqrt(distanceX ** 2 + distanceZ ** 2)

    if distance <= playerRadius:
        return True
    else:
        return False



                    ####
                    #  #
                    #  #
                    #  #
                    #  #
                    #  #
                    #  #
                    ####





