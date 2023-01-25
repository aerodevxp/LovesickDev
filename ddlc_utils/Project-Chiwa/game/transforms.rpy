#=============================================
#Transforms
transform main_menu_frame_anim:
    parallel:
        ypos 0
        linear 20 ypos -720
        repeat
    #parallel:
    #    xpos 0
    #    9
    #    ease 2 xpos 90 
    #    ease xpos 0
    #    repeat
transform dissolve_transition:
    xpos 0
    ypos 0
    alpha 0
    linear 2 alpha 1
    linear 2 alpha 0

transform bounce_transition:
    alpha 1
    on show:
        zoom 0
        ease_bounce 2 zoom 1
    on show:
        zoom 1
        ease 2 zoom 0
    

transform menu_character(x1, x2):
    parallel:
        xpos x1
        linear 20 xpos x2
    # parallel:
    #     alpha 0
    #     linear 1 alpha 1
    #     18
    #     linear 1 alpha 0



transform pcommon(x=640, z=1.05):
    yanchor 1.0 subpixel True
    on show:
        ypos 1.4
        zoom z*0.95 alpha 0.00
        xcenter x yoffset -20
        easein .15 yoffset 0 zoom z*1.00 alpha 1.00
    on replace:
        alpha 1.00
        parallel:
            easein .25 xcenter x zoom z*1.00
        parallel:
            easein .15 yoffset -20 yoffset .03

transform phide(z=0.80):
    on hide:
        easein .2 alpha 0.00 yoffset -20

transform lhide(speed):
    on hide:
        easeout speed xcenter -300


transform hop: #I would have used jump, but it's a keyword so I can't T-T
    easein .1 yoffset -20
    easeout .1 yoffset 0

transform yeah:
    easein .3 yoffset 10
    easeout .2 yoffset 0

transform nope:
    easein .3 xoffset 5
    ease .2 xoffset -5
    easeout .2 xoffset 0

transform pinstant(x=640, z=0.80):
    xcenter x yoffset 0 zoom z*1.00 alpha 1.00 yanchor 1.0 ypos 1.03

transform p41:
    pcommon(200)
transform p42:
    pcommon(493)
transform p43:
    pcommon(786)
transform p44:
    pcommon(1080)
transform p31:
    pcommon(240)
transform p32:
    pcommon(640)
transform p33:
    pcommon(1040)
transform p21:
    pcommon(400)
transform p22:
    pcommon(880)
transform p11:
    pcommon(640)

transform i41:
    pinstant(200)
transform i42:
    pinstant(493)
transform i43:
    pinstant(786)
transform i44:
    pinstant(1080)
transform i31:
    pinstant(240)
transform i32:
    pinstant(640)
transform i33:
    pinstant(1040)
transform i21:
    pinstant(400)
transform i22:
    pinstant(880)
transform i11:
    pinstant(640)

transform vshake:
    linear .05 yoffset 8
    linear .05 yoffset -8
    linear .05 yoffset 8
    linear .05 yoffset -8
    linear .05 yoffset 8
    linear .05 yoffset -8
    linear .05 yoffset 8
    linear .05 yoffset -8
    linear .05 yoffset 8
    linear .05 yoffset -8
    linear .05 yoffset 8
    linear .05 yoffset -8
    linear .05 yoffset 8
    linear .05 yoffset -8
    linear .05 yoffset 8
    linear .05 yoffset -8
    linear .05 yoffset 0

transform hshake:
    linear .05 xoffset 8
    linear .05 xoffset -8
    linear .05 xoffset 8
    linear .05 xoffset -8
    linear .05 xoffset 8
    linear .05 xoffset -8
    linear .05 xoffset 8
    linear .05 xoffset -8
    linear .05 xoffset 8
    linear .05 xoffset -8
    linear .05 xoffset 8
    linear .05 xoffset -8
    linear .05 xoffset 8
    linear .05 xoffset -8
    linear .05 xoffset 8
    linear .05 xoffset -8
    linear .05 xoffset 0

transform hzshake:
    xanchor .5
    yanchor .5
    ypos .5
    xpos .5
    ease .02 zoom 1.2
    hshake
    ease .02 zoom 1.0

transform vzshake: #for backgrounds only
    xanchor .5
    yanchor .5
    ypos .5
    xpos .5
    ease .02 zoom 1.2
    vshake
    ease .02 zoom 1.0
#=============================================