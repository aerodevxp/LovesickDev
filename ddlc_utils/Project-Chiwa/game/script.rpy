# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

#define e = Character("Eileen")


# The game starts here.

label main_menu:
    stop music
    stop sound fadeout .3
    show white onlayer overlay:
        alpha 1
        linear 1 alpha 0
    play music audio.menu
    show menu_bg1_2 
    show menu_bg1_2_flash 
    show menu_bg1_1 
    #show menu_white
    call screen main_menu
    return

#DISCORD Rich Presence
init -20 python:
    import discord_rpc
    import time
    start = time.time()

    def readyCallback(current_user):
        print('Our user: {}'.format(current_user))

    def disconnectedCallback(codeno, codemsg):
        print('Disconnected from Discord rich presence RPC. Code {}: {}'.format(
            codeno, codemsg
        ))

    def errorCallback(errno, errmsg):
        print('An error occurred! Error {}: {}'.format(
            errno, errmsg
        ))
    
    def rpc(details, state, img='hina',t=False):
        discord_rpc.update_connection()
        discord_rpc.run_callbacks()
        global start
        if not t:
            pass
        else:
            start = time.time()
        discord_rpc.update_presence(
            **{
                'details': details,
                'state': state,
                'large_image_key': img,
                'start_timestamp': start
            }
        )
        discord_rpc.update_connection()
        discord_rpc.run_callbacks()

label before_main_menu:
    python:
        # Note: 'event_name': callback
        callbacks = {
            'ready': readyCallback,
            'disconnected': disconnectedCallback,
            'error': errorCallback,
        }
        rpc("Main Menu", "Vibing to the beat!")
        discord_rpc.update_connection()
        discord_rpc.run_callbacks()

    return

label start:

    python:
        callbacks = {
            'ready': readyCallback,
            'disconnected': disconnectedCallback,
            'error': errorCallback,
        }
        discord_rpc.initialize('782017295106572339', callbacks=callbacks, log=False)
        rpc('Just woke up!', 'Day 1')

    jump ch1

    return

