﻿init python:
    class phone_convo:
        def __init__(self, people, con):
            self.people = people
            self.con = con
            self.sent = []
            self.typing = ""
            self.speaker = None
            self.speaking = None
            self.msg = None
            self.wait = 0
            self.choose = None
        def set_msg(self, m):
            self.msg = m
            self.choose = None
        
        
        def tick(self):
            if self.wait > 0:
                self.wait -= 0.1
            else:
                if self.msg is None:
                    self.msg = self.con.pop(0)
                    self.wait = 1.0
                    if isinstance(self.msg, (int, long)):
                        self.speaker = self.msg
                        self.speaking = self.msg
                        self.msg = None
                    elif isinstance(self.msg, list):
                        self.choose = self.msg
                elif self.choose:
                    pass
                else:
                    if self.typing == self.msg:
                        if self.speaker is not None:
                            self.sent.append([self.speaker,[self.msg]])
                            self.speaker = None
                            self.msg = None
                            Hide("phone")()
                            Show("phone")()
                            # Scroll("phone_vp", "vertical increase", 1000)()

                        else:
                            self.sent[-1][1].append(self.msg)
                            self.msg = None
                            Hide("phone")()
                            Show("phone")()
                            # Scroll("phone_vp", "vertical increase", 1000)()
                        self.typing = ""
                    else:
                        self.typing += str(self.msg[len(self.typing)])

default phone_conv_1 = phone_convo(
    [
        ["Aya", "phone/img2.png"],
        ["RiRi", "phone/img1.png"],
    ],
    [
        1,
        "hey",
        "what are you wearing?",
        "something naughty I hope :3",
        "or nothing at all",
        0,
        "stop it",
        ":(",
        1,
        "alright, alright",
        "just kidding",
        "are you ready for tomorrow? hiking, camping, marshmallows",
        "and boys :3",
        0,
        "I'm not sure...",
        "Boys can be rowdy and loud on trips like this.",
        1,
        "that's not an answer I can accept, do you want me to come over and tackle you to submission again?",
        0,
        ["no, I'll get ready", "I'll call you", "I said no"],
        1,
        "ok see you tomorrow, bye",
        0,
        "bye",
    ]
)



screen phone(c = phone_conv_1):
    modal True
    default last = 100
    # text str(c.typing) align 0.0,0.0
    if len(c.con) or c.msg:
        timer .1 repeat True action Function(c.tick)
    frame:
        xysize(600,900) padding(0,0) background "#222"
        frame:
            ysize 80 xfill True yalign 0.0 background "#333b"
            text c.people[1][0]
        frame:
            xysize 580,70 yalign 1.0 yoffset -10 background "#333b"
            if c.speaking == 0:
                text c.typing
            else:
                if c.wait > 0:
                    pass
                else:
                    text "{} is typing...".format(c.people[1][0]) size 15 yoffset -50 xalign 0.0
        frame:
            background None padding (30,80,30,110) yfill True
            viewport id "phone_vp":
                draggable True scrollbars None yinitial 1.0
                xfill False
                yfill False
                yalign 1.0
                frame:
                    padding(0,0) background None
                    vbox:
                        xfill True
                        for i in c.sent:
                            if i[0] == 0:
                                for iii,ii in enumerate(i[1]):
                                    if iii == 0:
                                        hbox:
                                            xalign 1.0 spacing 0 
                                            frame:
                                                style "phone_right" xoffset 64
                                                text ii color "#000"
                                            add c.people[i[0]] yalign 0.0
                                    else:
                                        frame:
                                            xalign 1.0
                                            style "phone_right_1"
                                            text ii color "#000"
                            else:
                                for iii,ii in enumerate(i[1]):
                                    if iii == 0:
                                        hbox:
                                            xalign 0.0 spacing 0 
                                            add c.people[i[0]] yalign 0.0
                                            frame:
                                                style "phone_left" xoffset -64
                                                text ii color "#000"
                                    else:
                                        frame:
                                            xalign 0.0
                                            style "phone_left_1"
                                            text ii color "#000"

    if c.choose:
        vbox:
            for i in c.choose:
                button:
                    xsize 600
                    text i
                    action Function(c.set_msg, i)
style phone_right:
    background Frame(im.Flip("phone/frm0.png",True), 10,20,76,10)
    padding(32,12,96,12)
    yminimum 64

style phone_left:
    background Frame("phone/frm0.png", 76,20,10,10)
    padding(96,12,32,12)
    yminimum 64

style phone_right_1:
    background Frame(im.Flip("phone/frm1.png",True), 10,20,76,10)
    padding(32,12,96,12)
    yminimum 64

style phone_left_1:
    background Frame("phone/frm1.png", 76,20,10,10)
    padding(96,12,32,12)
    yminimum 64