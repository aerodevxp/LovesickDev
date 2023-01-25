define ch1_wokeupforschool = True #Determined by first mini-game

label ch1:
    define persistent.dresscode = 0
    window hide
    $ quick_menu = False
    show screen quick_menu
    #Just making sure everything is silent
    stop sound fadeout .5
    stop music fadeout .5
    pause 2
    play sound alarm
    pause 3
    $ quick_menu = True
    window show dissolve
    mc "Mh..."
    window hide dissolve
    call mouseshake(1) #minigame
    if ch1_wokeupforschool:
        jump ch1_1
    else:
        jump ch1_2

label ch1_1:
    $ quick_menu = False
    window hide dissolve
    pause 3
    window show dissolve
    $ quick_menu = True
    mc "{i}*Yawn*{/i}"
    mc "Already?"
    "Well, time to wake up and go to school!"
    "I wonder if my sister is awake..."
    "...Nah!{w=.4} She would have woke me up if she was."
    stop sound fadeout 1.0 #Just in case the alarm sfx is still playing
    scene bg bedroom with trans2
    play music t3
    mc "{i}*yawns*{/i}"
    play sound knock
    "Mh?"
    show lines at pLines
    show layer screens at hshake
    show layer master at hzshake
    h "[player]!{w=.2} Hurry up!"
    hide lines
    "Oh, it's my sister!"
    "I'm surprised she woke up before me."
    mc "Um, yeah... What is it?"
    show lines at pLines
    show layer master at hzshake
    show layer screens at hshake
    h "We're late!"
    hide lines
    mc "What?{w=.4} Nah, there's no way we are-"
    "I look at my alarm clock..."
    "...and realize that, yeah, {b}we are late{/b}!"
    mc "Ah, shoot!"
    show lines at pLines
    show layer master at hzshake
    show layer screens at hshake
    h "What are you even doing?!"
    hide lines
    mc "Stop shouting like that!"
    "Hina opens the door."
    mc "Wait, wait! I'm not even dressed yet-{w=.3}{nw}"
    show hina 2c at p11
    "Before I can even finish my sentence, Hina is already in front of me."
    mc "Ah!"
    show hina 3d at hop
    h "Oh, sheesh! Dress up already!"
    mc "I was going to!"
    h "Alright, well I'll be waiting for you outside."
    show hina 2c at yeah
    h "Hurry up please!"
    mc "Yeah, yeah, I will!"
    show hina at lhide(.4)
    hide hina
    $quick_menu = False
    window hide dissolve
    pause 1.0
    #Maybe add a door sfx here?
    window auto show dissolve
    $quick_menu = True
    "Okay, so I need to dress up..."
    "Mh... What should I wear?"
    $quick_menu = False
    #Next thing to do is to redesign the choice menu.
    #Also add a hover sfx
    menu:
        "Something typical": #Leah
            $quick_menu = True
            $ persistent.dresscode = 1
            call ch1_dress1
        "Something flashy": #Emi
            $quick_menu = True
            $ persistent.dresscode = 2
            call ch1_dress2
        "Something trendy": #Pika
            $quick_menu = True
            $ persistent.dresscode = 3
            call ch1_dress3
    "Okay, well that takes care of clothing!"
    "I don't think it matters that much honestly."
    "Spring break is next week. Even if I did mess up, no one would even remember it after the break, right?"
    if persistent.dresscode is not 1:
        "Even if I somehow did get noticed today, everyone would forget about me during the break."
    "Oh, yeah! I should probably not make my sister wait for too long."
    "She's going to kill me if I do!"
    "I take my schoolbag and run out of my house."
    stop music fadeout 1
    scene bg residential_day 
    with dissolve_scene_full
    play music t4
    show hina 1a at p11
    $rpc("Going to school!", "Day 1")
    mc "Sorry! I'm here!"
    h 1d "Jeez!{w=.2} What took you so long?"
    mc "Dressing up?"
    h 3d "I didn't know boys took this long to do that."
    mc "Um, I don't! I just..."
    h 1b "What? Are you trying to dress up for someone?"
    h "Do you want to be noticed by a girl at school?"
    "Where did that came from?"
    mc "No, no!"
    mc "I surely would appreciate attention from a girl,{w=.5} {b}but{/b}{w=.4} that wasn't why I was taking so long, okay?"
    h 2a "Yeah, {i}sure.{/i}"
    mc "Anyway, let's go."
    h "Alright."
    $quick_menu = False
    scene black
    with trans1
    pause 1
    scene bg school_front
    with trans1
    $quick_menu = True
    
    mc "Here we are."
    show hina 2b  at p11
    h "Yep."
    h 1a "Well, I'll see you later, Big Brother."
    mc "See ya."
    show hina at phide
    hide hina
    pause .5
    "Alright...{w=.9} Time for class."
    stop music fadeout 1.0
    scene black with trans1
    pause .2
    scene bg class_day with trans1
    play music t5
    t "Hello, class!"
    t "Today is a special day for us as we have a new student!"
    "We do?"
    "What?{w=.8} No one told me we did..."
    "...but who would even bother to tell me anyway...?"
    t "Would you like to introduce yourself to the class?"
    "A girl next to me I didn't even notice stands up."
    show leah at p11
    "???" "\"Ah, yes.\""
    "???" "\"So... Um...\""
    "???" "\"Hello everyone. My name is Leah.\""
    l "I have recently moved in with my parents from Europe."
    l "P-Please be nice to me."
    t "Thank you, Leah.{w=.3} You may sit down now."
    show leah at phide
    hide leah
    t "Alright, so today we are going to practice en Français."
    "Oh, well..."
    "This is going to be boring."
    stop music fadeout 3
    show black:
        alpha 0
        linear 3 alpha 1
    "M-Mh..."
    window hide dissolve
    pause 5
    window auto
    scene bg class_day
    play sound bang
    show lines at pLines
    show layer master at hzshake
    show layer screens at hshake
    show teacher at p11
    t "{b}Wake up!{/b}"
    mc "{b}AH!{/b}"
    hide lines
    t "How dare you sleep during my class?"
    t "Everyone is gone. I should have let you here to die."
    play music tl fadein 5
    mc "I'm sorry!"
    mc "I wasn't sleeping...!"
    t "Okay, then, answer this."
    t "Quel âge as-tu?"
    mc "Uh..."
    mc "Bonjour! Je suis très grande baguette aujourd'hui."
    show teacher at p22
    show leah at p21
    l "Haha~!"
    "Wait, what is Leah still doing here?"
    t "Woah. T'es vraiment con."
    mc "Um... Je ne understand?"
    t "Pft... Make yourself useful and show the school to Leah, okay?"
    mc "...but I was going to the cafet-"
    t "No 'but's!"
    t "Do it."
    mc "Um, alright."
    mc "Follow me, Leah."
    l "Okay."
    #stop music fadeout .5
    scene bg corridor
    with trans1
    pause .4
    show leah at p11
    #play music t6 fadein .5
    mc "So, um, what do you want to start with?"
    l "It doesn't really matter to me..."
    mc "Okay, well, let's go eat then!"
    l "Mh...?"
    mc "I'll show you the school afterwards."
    l "You're just going to leave me here?"
    mc "No, you come eat with me."
    mc "Are you crazy? If the teacher found you alone, she would kill me."
    l "Ah! Okay!"
    mc "Do you have a lunch?"
    l "Uh... I brought money."
    mc "Oh, you can't really buy food with money here."
    l "What?"
    l "...but isn't there a cafeteria?"
    mc "Yeah, to eat what you brought."
    mc "Not to buy food."
    l "Ah, shoot..."
    l "S-Sorry..."
    mc "It's alright.{w=.5} I must have some food I can share."
    l "Really?"
    l "You don't really have to! I've seen some vending machines earlier..."
    mc "I insist. The vending machines we have won't give you a full and free meal."
    l "Alright then... T-Thanks!"
    l "I should probably have asked this way earlier, but..."
    l "What's your name?"
    mc "I'm [player]."
    l "Nice to meet you."
    l "I'm-"
    mc "Leah."
    l "U-Uh... Right."
    mc "Haha~."
    if persistent.dresscode == 1:
        l "You look nice."
        mc "Oh, thank you!"
        mc "I'm not wearing anything amazing, but..."
        l "N-No, I like it."
        $addAffection('leah', 5, 'She liked it!')
        l "I don't really like guys that try to stand out too much."
        mc "Yeah, that can be annoying sometimes..."
    elif persistent.dresscode == 2:
        l "You stand out a lot with what you're wearing..."
        mc "Yeah! I kinda like to be noticed."
        l "I mean... It's working. I noticed."
        l "Ehehe~."
        mc "Yeah, haha~."
    elif persistent.dresscode == 3:
        l "Are you popular?"
        mc "Uh, why are you asking?"
        l "Well, I don't know."
        l "The clothes you're wearing look like what the popular girl was wearing."
        mc "Which one?"
        l "The one with blue hair."
        mc "Oh, right."
        "Did she just compare me to {b}the{/b} most popular girl of this school?"
        "Anyway, we can talk about this later."
    mc "Alright, let's go now. I'm really hungry."
    l "Ah, yeah!"
    #Cafeteria Time
    stop music fadeout 1.0
    scene bg cafeteria with trans1_scene
    show leah at p11
    play music t9
    mc "Alright. Here we are."
    l "Where are we going to sit?"
    mc "Mh... I'm sure my sister has some space for us."
    l "A-Are you sure?"
    l "I wouldn't want to be an inconvenience."
    mc "Nah! Don't worry."
    mc "Follow me!"
    #CG Where the MC's face would be off screen.
    #You'd be able to see Emi and Hina sat down on the left and Leah standing up next to MC on the right
    #I would need several expressions for each character with a visible face in this image.
    scene cg caf_standup with trans1
    mc "Yo, sis?"
    h "What the-?"
    #Hina could have a bored expression in the CG here
    h "Oh, hey."
    #Emi could have an excited expression in the CG here
    e "Hiiiiiiiii [player]!"
    if persistent.dresscode == 2:
        e "Woah! Looking good!"
        mc "Me?"
        e "Yeah, of course {i}you{/i}, dummy!"
        mc "Well, thanks!"

    return

label ch1_dress1:
    "Well, I guess I'll just wear something typical."
    "I don't want to try to stand out at school."
    "No one would notice me anyway... as always..."
    return

label ch1_dress2:
    "I'm done being ignored!"
    "Let's wear something flashy!"
    "That way, everyone will notice me for once."
    "I know popular people who wear this kind of stuff, so..."
    "I might as well try it!"
    return

label ch1_dress3:
    "Everyone might be wearing whatever's trendy now."
    "Well, everyone meaning the people who are worth talking to."
    "Plus, if I keep up with the trends, I'm sure my reputation will skyrock after a while."
    return


label ch1_2:
    $ quick_menu = False
    window hide dissolve
    pause 8
    window show dissolve
    $ quick_menu = True
    scene bg bedroom with dissolve
    mc "Mh... {i}*Yawn*...{/i}"
    mc "Urgh, what time is it?"
    "I look at alarm clock."
    mc "OH-?!"
    "The time on the clock is 1:35 pm."
    mc "Urgh... I woke up way too late!"
    mc "Going to school isn't even worth it anymore."
    mc "...I'm super hungry as well..."
    mc "I need to eat or I'll starve to death."
    mc "I doubt Hina is home...."
    mc "...She probably went to school without me."
    mc "I can't really blame her. It was my fault I woke up so late."
    mc "Is there anything to eat?"
    scene bg menu3
    with dissolve_scene_full
    play music tl #This is the theme of Leah, you can't really use it here.
    "I walk downstairs."
    "There's a piece of paper on the table."
    mc "Uh? What's that?"
    call screen note('h', "Hey! You're hungry, aren't you? Then, go buy food! You won't wake up anytime soon anyways. I got late for school for writing this so you better listen!")
    mc "Ohh!...Umm.."
    "There was some money behind the note."
    "Thinking I won't need that much, I only take half of it."
    mc "There could be something left in the fridge."
    menu:
        "Make sure it's empty":
            mc "I'll make sure..."
            "I open the fridge."
            mc "Huh-"
            "There's another note."
            call screen note('h', "BIG BROTHER! You're dumb! I told you there was nothing in the fridge. Go buy food now! Please :3!")
            "{i}Tsk{/i}."
            

        "Assume Hina isn't exaggerating":
            mc "Oh, well..."
            mc "I'm sure it's empty."
    "I go back to my room."

    scene bg bedroom with trans2
    mc "Alright... I should get ready."
    mc "I can't let other things distract me right now."
    "She'll only come back in about the two hours, but I'm the type of person who takes a long time buying things."

    #Make dinner for Hina.
