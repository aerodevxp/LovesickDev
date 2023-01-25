#Where I define everything bla bla you've modded DDLC before you know what this is lol

#=============================================
#Config Stuff
init python:
    config.rollback_enabled = config.developer
    config.autoreload = False
    config.has_autosave = False
    config.use_cpickle = False
#=============================================
#=============================================
#Persistent Stuff
default persistent.player_name = ""
default player = persistent.player_name #Not rly persistent but necessary for the character def.
#=============================================

#=============================================
#UI Stuff
image ctc:
    xpos 1280 ypos 720
    linear 0.5 alpha 1.0 # visible
    "gui/ctc.png"
    0.75
    linear 0.5 alpha 0.0 # invisible
    0.75
    repeat

image white:
    "#ffffff"

image menu_bg1_1:
    'menu_hina'
    20
    'menu_emi'
    20
    'menu_leah'
    20
    'menu_pika'
    20
    repeat

image menu_white:
    '#FFF'
    alpha 0
    block:
        linear 1 alpha 0
        pause 18
        linear 1 alpha 1
        repeat
image menu_bg1_2:
    parallel:
        'bg menu1'
        20
        'bg menu2'
        20
        'bg menu3'
        20
        'bg menu4'
        20
        repeat
    parallel:
        #THIS took me a WHILE to set up T-T
        6.491
        block:
            1.847
            block: #OK
                ease .1 zoom 1.1
                ease .1 zoom 1
                0.262
                repeat 12
            1.645
            block: 
                ease .1 zoom 1.1
                ease .1 zoom 1
                0.262
                repeat 31
            #1.186
            block:
                ease .1 zoom 1.1
                ease .1 zoom 1
                0.262
                repeat 14
            1.102
            0.1
            repeat

image menu_bg1_2_flash:
    parallel:
        '#FFF'
        #'#ca43f7'
        #repeat
    parallel:
        alpha 0
        #THIS took me a WHILE to set up T-T
        6.491
        block:
            1.847
            block: #OK
                ease .1 zoom 1.1 alpha .5
                ease .1 zoom 1 alpha 0
                0.262
                repeat 12
            1.645
            block: 
                ease .1 zoom 1.1 alpha .5
                ease .1 zoom 1 alpha 0
                0.262
                repeat 31
            #1.186
            block:
                ease .1 zoom 1.1 alpha .5
                ease .1 zoom 1 alpha 0
                0.262
                repeat 14
            1.102
            0.1
            repeat

image menu_logo:
    "gui/logo.png"
    zoom 0.3

image white_transition:
    'white'
    dissolve_transition

image menu_hina:
    "gui/hina.png"
    menu_character(x1=1100, x2=600)

image menu_emi:
    "gui/emi.png"
    menu_character(x1=500, x2=1000)

image menu_leah:
    "gui/leah.png"
    menu_character(x1=1100, x2=600)

image menu_pika:
    "gui/pika.png"
    menu_character(x1=500, x2=1000)

image bg menu1:
    "bg/menu1.png"
    #menu_img_move(0)
image bg menu2:
    "bg/menu2.png"
    #menu_img_move(0)
image bg menu3:
    "bg/menu3.png"
    #menu_img_move(0)
image bg menu4:
    "bg/menu4.png"
    #menu_img_move(0)


#=============================================

#=============================================
#Character Defintions
define narrator = Character(ctc="ctc", ctc_position="fixed")
#Variables changing only work with DynamicChars?
define mc = DynamicCharacter('player', what_prefix='"', what_suffix='"', ctc="ctc", ctc_position="fixed")
define h = DynamicCharacter("h_name", image="hina", what_prefix='"', what_suffix='"', ctc="ctc", ctc_position="fixed")
define e = DynamicCharacter("e_name", image="emi", what_prefix='"', what_suffix='"', ctc="ctc", ctc_position="fixed")
define l = DynamicCharacter("l_name", image="leah", what_prefix='"', what_suffix='"', ctc="ctc", ctc_position="fixed")
define p = DynamicCharacter("p_name", image="pika", what_prefix='"', what_suffix='"',ctc="ctc", ctc_position="fixed")
define t = DynamicCharacter('teacher_name', what_prefix='"', what_suffix='"', ctc="ctc", ctc_position="fixed")
#Names
define h_name = 'Hina'
define e_name = 'Emi'
define l_name = 'Leah'
define p_name = 'Pika'
default teacher_name = 'Teacher' #Her name could change if the player gets to know her better later?
#=============================================

#=============================================
#Audio
define audio.t6 = "<loop 0>bgm/t6.ogg"
define audio.t1 = "<loop 6.491>bgm/t1.ogg" #by voicelessscooby
define audio.t2 = "<loop 0>bgm/t2.ogg" #by voicelessscooby
define audio.t3 = "<loop 0>bgm/t3.ogg" #by voicelessscooby
define audio.t4 = "<loop 9.221>bgm/t4.ogg" #by voicelessscooby
define audio.t5 = "<loop 0>bgm/t5.ogg" #by voicelessscooby
define audio.tp = "<loop 3.723>bgm/tp.ogg" #by voicelessscooby
define audio.t7 = "<loop 0>bgm/t7.ogg" #by Verse One
define audio.t8 = "<loop 0>bgm/t8.ogg" #by Verse One
define audio.t9 = "<loop 0>bgm/t9.ogg" #by Verse One
define audio.t10 = "<loop 0>bgm/t10.ogg" #by Verse One

define audio.th = "<loop 0>bgm/th.ogg" #by voicelessscooby
define audio.tl = "<loop 0>bgm/tl.ogg" #by voicelessscooby
define audio.tp = "<loop 0>bgm/tp.ogg" #by voicelessscooby

define audio.menu = audio.t1


init python:
    import os #Probably already imported, but just making sure.
    import random
    def playMiniGameMusic():
        if random.randint(1, 1) == 1: #For creepy music later
            renpy.music.play('<from 0 to 41.148>bgm/mg_n1.ogg', channel='music', loop=True)

define audio.alarm = "sfx/alarm.ogg"
define audio.knock = "sfx/knock.ogg"
define audio.bang = "sfx/bang.ogg"
#=============================================

#=============================================
#Images
init -10:
    image main_menu_frame_img:
        "gui/overlay/main_menu.png"
        main_menu_frame_anim

image bg bedroom = "bg/bedroom.png"
image bg school = "bg/school.png"

image bg residential_afternoon = "bg/residential/1_afternoon.png"
image bg residential_day = "bg/residential/1_day.png"
image bg residential_night = "bg/residential/1_night.png"

image bg school_front = "bg/school_front.png"
image bg school_yard = "bg/school_yard.png"

image bg class_day = "bg/class_day.png"

image bg cafeteria = "bg/cafeteria.png" #Okay um so u really have to replace this art.

image lines:
    "fx/line1.png"
    .1
    "fx/line2.png"
    .1
    "fx/line3.png"
    .1
    repeat

transform pLines(a=1):
    on show:
        alpha 0
        linear .5 alpha a
    on hide:
        alpha a
        linear .5 alpha 0

image bg corridor = "bg/school_corridor.png" 

image bg sky1 = "bg/skies/1.png"
image bg sky2 = "bg/skies/2.png"
image bg sky3 = "bg/skies/3.png"
image bg sky4 = "bg/skies/4.png"
image bg sky5 = "bg/skies/5.png"
image bg sky6 = "bg/skies/6.png"

#Characters
#Hina

image hina 1a = im.Composite((640, 1280),(0, 0), "hina/1.png",(0, 0), "hina/a.png")
image hina 1b = im.Composite((640, 1280),(0, 0), "hina/1.png",(0, 0), "hina/b.png")
image hina 1c = im.Composite((640, 1280),(0, 0), "hina/1.png",(0, 0), "hina/c.png")
image hina 1d = im.Composite((640, 1280),(0, 0), "hina/1.png",(0, 0), "hina/d.png")

image hina 2a = im.Composite((640, 1280),(0, 0), "hina/2.png",(0, 0), "hina/a.png")
image hina 2b = im.Composite((640, 1280),(0, 0), "hina/2.png",(0, 0), "hina/b.png")
image hina 2c = im.Composite((640, 1280),(0, 0), "hina/2.png",(0, 0), "hina/c.png")
image hina 2d = im.Composite((640, 1280),(0, 0), "hina/2.png",(0, 0), "hina/d.png")

image hina 3a = im.Composite((640, 1280),(0, 0), "hina/3.png",(5, 0), "hina/a.png")
image hina 3b = im.Composite((640, 1280),(0, 0), "hina/3.png",(5, 0), "hina/b.png")
image hina 3c = im.Composite((640, 1280),(0, 0), "hina/3.png",(5, 0), "hina/c.png")
image hina 3d = im.Composite((640, 1280),(0, 0), "hina/3.png",(5, 0), "hina/d.png")
#=============================================
#vfx



#=============================================
#Notes

style note:
    color "#000"
    size 50

style h_note is note:
    font "gui/font/hina.ttf"

transform note_intro:
    yoffset 1500
    ease 1 yoffset 0
    on hide:
        yoffset 0
        ease 1 yoffset 1500

transform note_click(n):
    alpha 0
    xalign .5
    yalign .5
    xanchor .5
    yanchor .5
    yoffset 0 
    10
    alpha 1
    ease_bounce 2 yoffset -265 * n
    on hide:
        ease 1 yoffset 1500



screen note(author, txt, sign=True):
    python:
        _window_hide(dissolve)
        multipleNotes = isinstance(txt, list)

    text 'Click on the note' outlines [ (3, "#000", 0, 0) ] at note_click(1)
    text 'when you are done.' outlines [ (3, "#000", 0, 0) ] at note_click(-1)

    frame:
        at note_intro
        background Image("gui/notes/"+author+"_note.png", xpos=640, ypos=360, xanchor=.5, yanchor=.5)
        #at truecenter
        #xanchor .5
        #yanchor .5
        xpadding 410
        ypadding 150
        button action Function(Return)
        text txt xalign .5 yalign .4 yoffset -20 style 'h_note'
        if author == 'h':
            text '- Hina' xalign .9 yalign .9 yoffset 40 style 'h_note'