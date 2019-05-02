from time import time
from CollisionDetection import test_cu
from OpenGL.GLU import *
from OpenGL.GLUT import *
from MainMap import drawMap
from gameobject import *
from gamestatus import *
from gametextures import drawImage2D, drawText2D
from initopengl import initOpenGl
from intractable_objects import createMapObjects
from objects.PlayerObject import *
player = PlayerObject()
deltaTime = 0
currentTime = 0
intractableObjects = []
currentGameStatus=0

def initCamera():
    global player, cameraZoom
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(60, 1, 0.001, 100000)
    gluLookAt(player.posX + 0, 5 + cameraZoom, player.posZ + 5 + cameraZoom,
              player.posX + 0, 0, player.posZ + 0,
              0, 1, 0)
    glMatrixMode(GL_MODELVIEW)


def draw():
    # Delta Time
    global currentTime
    global deltaTime
    newTime = time()
    frameTime = newTime - currentTime
    currentTime = newTime
    deltaTime = frameTime

    # Speed Factor
    deltaTime *= GAME_SPEED_FACTOR

    global currentGameStatus
    global currentGameScore
    glClearColor(0,0.49,0.76, 1)
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glColor3f(0, 0, 1)
    glLoadIdentity()

    if currentGameStatus >= GAME_STATUS_SCORE:
        glClearColor(0, 0 , 0 , 1 )
        glClear(GL_COLOR_BUFFER_BIT)
        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        gluOrtho2D(-5, 5, -5, 5)
        glMatrixMode(GL_MODELVIEW)
        drawImage2D("resources/images/score_title.png", 0, 2.5)
        drawText2D(str(currentGameScore), 0, -1, scaleFactor=1)
    if GAME_STATUS_PLAYING < currentGameStatus < GAME_STATUS_SCORE:
        global intractableObjects
        toBeRemoved=[]
        initCamera()
        glLoadIdentity()

        #glDisable(GL_BLEND)
        glDisable(GL_DEPTH_TEST)
        glDisable(GL_CULL_FACE)
        drawMap()
        glLoadIdentity()
        glEnable(GL_BLEND)
        glEnable(GL_CULL_FACE)
        glEnable(GL_DEPTH_TEST)
        glBlendFunc(GL_SRC_ALPHA,GL_ONE_MINUS_SRC_ALPHA)
        player.onFrameTick(deltaTime)

        player.draw()
        draw_others()
        for i in intractableObjects:
              if i.rotY == 90 or  i.rotY == -90:
                      if test_cu(player.radius, player.posX, player.posZ, i.width , i.Length, i.posX,i.posZ) == True:
                          if i.area > player.area:
                              i.a = 0.4
                              #i.startAnimation(DeltaAnimation(AnimationParams.posX, -10 ,3))
                          else :
                              if i.collision ==0:
                                      i.collision =1
                                      s =DeltaAnimation(AnimationParams.posY, -6, .5, 1 ) #toBeRemoved.append((i)))
                                      i.startAnimation(Animation(AnimationParams.posX, None, player.posX, 2))
                                      i.startAnimation(Animation(AnimationParams.posZ, None, player.posZ, 2,
                                                                 onAnimationFinished=i.startAnimation(s)))

                                      currentGameScore+=i.area/AREA_TO_SCORE
                                      print(currentGameScore)
                      else:
                          i.a =1
                          i.collision =0
              else:
                  if test_cu(player.radius, player.posX, player.posZ, i.Length, i.width, i.posX, i.posZ) == True:
                      if i.area> player.area:
                          i.a = 0.4
                      else:
                          if i.collision ==0 :
                              i.collision=1
                              s=DeltaAnimation(AnimationParams.posY, - 2 ,.1)#onAnimationFinished= toBeRemoved.append(i) )
                              i.startAnimation(Animation(AnimationParams.posX, None, player.posX, 2))
                              i.startAnimation(Animation(AnimationParams.posZ, None, player.posZ, 2,onAnimationFinished=i.startAnimation(s)))


                              currentGameScore += i.area / AREA_TO_SCORE
                              print(currentGameScore)


                  else :
                      i.a=1
                      i.collision=0
        for tbr in toBeRemoved:
            intractableObjects.remove(tbr)
        for o in intractableObjects:
            o.onFrameTick(deltaTime)
            o.draw()
        Score_update(player,currentGameScore)

    if GAME_STATUS_COUNTDOWN <= currentGameStatus < GAME_STATUS_PLAYING:
        glClearColor(0, 0 , 0 , 1 )
        glClear(GL_COLOR_BUFFER_BIT)
        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        gluOrtho2D(-5, 5, -5, 5)
        glMatrixMode(GL_MODELVIEW)
        if currentGameStatus > 3:
            drawImage2D("resources/images/countdown_1.png", 0, 0,
                        scaleFactor=0.5 + (currentGameStatus - GAME_STATUS_COUNTDOWN - 2))
        elif currentGameStatus > 2:
            drawImage2D("resources/images/countdown_2.png", 0, 0,
                        scaleFactor=0.5 + (currentGameStatus - GAME_STATUS_COUNTDOWN - 1))
        else:
            drawImage2D("resources/images/countdown_3.png", 0, 0,
                        scaleFactor=0.5 + (currentGameStatus - GAME_STATUS_COUNTDOWN))
    if currentGameStatus == GAME_STATUS_MAINMENU:
        glClearColor(0,0,0,1)
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        gluOrtho2D(-5, 5, -5, 5)
        glMatrixMode(GL_MODELVIEW)
        drawText2D("CLICK TO PLAY !", 0, 0, scaleFactor=0.5)
    if not currentGameStatus == GAME_STATUS_MAINMENU:
        currentGameStatus += deltaTime
        #print(deltaTime)
    glutSwapBuffers()

def onKeyboardKeyDown(key, x, y):
    global currentGameStatus
    if key == b'r':
        print('Restarting the game..')
        currentGameStatus = GAME_STATUS_MAINMENU

    if key == b'p':
        quit()
    global cameraZoom
    if key == b'[':
        cameraZoom += 1
    if key == b']':
        cameraZoom -= 1


def onSpecialKeyDown(key, x, y):
    global player
    global angle
    if key == GLUT_KEY_RIGHT:
        if player.posX < 100-player.radius:
            player.startAnimation(DeltaAnimation(AnimationParams.posX,+PLAYER_MINIMUM_MOVEMENT ,.001))
        player.rotY = 90
        player.x = player.radius +.2
        player.z = 0


    elif key == GLUT_KEY_LEFT:
        if player.posX > -100 +player.radius:
            player.startAnimation(DeltaAnimation(AnimationParams.posX,-PLAYER_MINIMUM_MOVEMENT ,.001))
        player.rotY = -90
        player.x = -player.radius-.2
        player.z = 0

    elif key == GLUT_KEY_DOWN:
        if player.posZ < -player.radius:
            player.startAnimation(DeltaAnimation(AnimationParams.posZ, +PLAYER_MINIMUM_MOVEMENT , .001))
        player.rotY = 0
        player.z = player.radius+.2
        player.x = 0
    elif key == GLUT_KEY_UP:

        if player.posZ > -100+player.radius:
            player.startAnimation(DeltaAnimation(AnimationParams.posZ, -PLAYER_MINIMUM_MOVEMENT, .001))
        player.rotY = 180
        player.z = - player.radius-.2
        player.x = 0
def onMouseKeyDown(button, state, x, y):
    global currentGameStatus
    if button == GLUT_LEFT_BUTTON and currentGameStatus == GAME_STATUS_MAINMENU:
        currentGameStatus = GAME_STATUS_COUNTDOWN
        global intractableObjects
        intractableObjects = createMapObjects()

initOpenGl(draw, onMouseKeyDown, onKeyboardKeyDown, onSpecialKeyDown)
