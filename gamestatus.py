#from game import currentTime
from objects.PlayerObject import *
from gametextures import  drawText2D
cameraZoom = 0
GAME_STATUS_MAINMENU = 0
GAME_STATUS_COUNTDOWN = 1
GAME_STATUS_PLAYING = 4
GAME_STATUS_SCORE = 200
GAME_SPEED_FACTOR = 1
AREA_TO_SCORE= 2
PLAYER_MINIMUM_MOVEMENT = 1
refrenceGameScore =0
toMakeBiger=10
def Score_update(player,currGameScore):
    global refrenceGameScore ,toMakeBiger
    global currentGameScore
    if currGameScore - refrenceGameScore >= toMakeBiger :
        player.radius += player.radius *(1/player.radius)
        player.update_area()
        refrenceGameScore = currGameScore
        drawText2D("Size Up!", player.posX, 2, player.posZ, scaleFactor=1)
        toMakeBiger*=3
