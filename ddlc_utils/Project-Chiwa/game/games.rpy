#games.rpy - Where mini-games are made.

#=======================================
#1. Mouse Shake Game
#=======================================

label mouseshake(n):
    $skipgame = False
    if config.developer:
        menu:
            "Do you want to skip this mini-game?"
            "Yes":
                $skipgame = True
                menu:
                    "Consider mini-game as..."
                    "Won":
                        $last_ms_success = True
                    "Lost":
                        $last_ms_success = False

            "No":
                pass
    if not skipgame:
        $renpy.show('mouseshake_intro' + str(n))
        $renpy.pause(3.5, hard=True)
        if n is 1: #Difficulty (The higher = The easier)
            $mouseGameSensitivity = 7
        call screen mouseshake
    if n is 1: #Where is the victory or failure stored
        $ch1_wokeupforschool = last_ms_success
    return
    
label ms_end(success):
    stop music fadeout .2
    play sound "sfx/whistle.mp3"
    if success:
        show mouseshake_end
        $ last_ms_success = True
        $renpy.pause(2, hard=True)
    else:
        show mouseshake_fail
        $ last_ms_success = False
        $renpy.pause(5, hard=True)
    return

define last_ms_success = False

screen mouseshake:
    on 'show' action Function(playMiniGameMusic)
    add im.Flip("gui/mousegame_charge_empty.png", vertical=True)
    add DynamicDisplayable(MouseSlider) at left
    hbox:
        at truecenter
        
        add DynamicDisplayable(MouseDist) at ms_num
    
#                      [ (x,y pos), time, total dist]
default mouse_values = [(None, None), 0.0, 0.0]

transform ms_num:
    xalign .5
    yalign .5
    zoom 1
    block:
        linear .3 zoom 1.4 
        linear .3 zoom 1
        repeat

style ms_intro:
    size 45
    font "gui/font/button.ttf"

style ms_intro2 is ms_intro:
    size 100

image mouseshake_intro1:
    xalign .5
    yalign .5
    zoom 0
    Text("You're late! Wake up!", style='ms_intro')
    ease 1 rotate 360 zoom 1
    1.5
    Text("GO!", style='ms_intro2')
    ease 1 rotate 0 zoom 0

image mouseshake_end:
    xalign .5
    yalign .5
    Text("Got it!", style='ms_intro')
    zoom 0 
    ease_bounce .6 zoom 1
    2
    linear 1 alpha 0

image mouseshake_fail:
    xalign .5
    yalign .5
    Text("...Aw... You didn't finish quickly enough...", style='ms_intro')
    zoom 0 
    ease .6 zoom 1
    5
    linear 1 alpha 0

transform mouseslider(x):
    alpha x

init -10 python:
    import pygame
    import time
    import math
    mouseGamePtns = 0 #Finishes at 1380
    mouseGameTime = time.time()
    mouseGameTime2 = time.time()
    mouseGameTimeLimit = 45
    mouseTxtSize = 30
    mouseGameSensitivity = 2

    def MouseSlider(st, at):
        img = im.Flip(Image("gui/mousegame_charge_full.png"), vertical=True)
        try:
            if 720*2 < mouseGamePtns:
                #img = im.Scale("gui/mousegame_charge_full.png", 0, 0, 0, 100*mouseGamePtns)
                pass
            else:
                img = im.Flip(im.Crop("gui/mousegame_charge_full.png", (0, 0, 1280, mouseGamePtns/2)), vertical=True)
        except:
            pass
        if mouseGamePtns == 0:
            img = im.Crop("gui/mousegame_charge_full.png", (0, 0, 1280, 0))
        return img, 0.0


    def MouseDist(st, at):
        global mouseGameTimeLimit
        global mouseGameTime2
        if mouseGameTimeLimit == 0:
            renpy.hide_screen('mouseshake')
            renpy.call('ms_end', success=False)
        if time.time() >= mouseGameTime2 + 1:
            mouseGameTime2 = time.time()
            mouseGameTimeLimit = mouseGameTimeLimit - 1
        mp = [abs(k) for k in renpy.get_mouse_pos()]
        dist = (0.0 if mouse_values[0][0] is None 
                else math.hypot(mouse_values[0][0]-mp[0], 
                                mouse_values[0][1]-mp[1]))
        speed = 0.0 if not st else dist / (st-mouse_values[1])
        store.mouse_values = [mp, st, mouse_values[2]+dist]
        global mouseGamePtns
        global mouseGameTime
        global mouseTxtSize
        global mouseGameSensitivity
        losingPtns = False
        if time.time() > mouseGameTime + 0.1 and speed < 1000/mouseGameSensitivity :
            
            mouseGameTime = time.time()
            mouseGamePtns = (mouseGamePtns - int(1/mouseGameSensitivity) if int(1/mouseGameSensitivity) is not 0
                            else mouseGamePtns - 1)
        elif speed > 2500/mouseGameSensitivity:
            mouseGamePtns = mouseGamePtns + 3
        elif speed >= 1000/mouseGameSensitivity:
            mouseGamePtns = mouseGamePtns + 1
        
        if mouseGamePtns < 0:
            mouseGamePtns = 0
        elif mouseGamePtns < 1500/mouseGameSensitivity:
            #           Base Size         Sensitivty
            mouseTxtSize = 30 + mouseGamePtns/15*mouseGameSensitivity
        #elif mouseGamePtns =< 100:
        #    mouseTxtSize = 30
        
        if mouseGamePtns >= 1380:
            renpy.hide_screen('mouseshake')
            renpy.call('ms_end', success=True)
        if mouseGameTimeLimit == 15:
            return Text("15 seconds left!",font="gui/font/button.ttf", size=40, outlines=[ (3, "#000", 0, 0) ]), 0.0
        if mouseGameTimeLimit <= 5:
            return Text("5 seconds left! Hurry up!",font="gui/font/button.ttf", size=40, outlines=[ (3, "#000", 0, 0) ]), 0.0
        if mouseGamePtns == 0:
            if renpy.mobile:
                return Text("Touch the screen and shake your finger!",font="gui/font/button.ttf", size=30, outlines=[ (3, "#000", 0, 0) ]), 0.0
            else:
                return Text("Shake your mouse!",font="gui/font/button.ttf", size=30, outlines=[ (3, "#000", 0, 0) ]), 0.0
        elif mouseGamePtns > 1200:
            return Text("Almost there!",font="gui/font/button.ttf", size=40, outlines=[ (3, "#000", 0, 0) ]), 0.0
        return Text(str(mouseGamePtns),font="gui/font/button.ttf", size=mouseTxtSize, outlines=[ (3, "#000", 0, 0) ]), 0.0

