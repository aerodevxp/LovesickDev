label splashscreen:
    python:
        callbacks = {
            'ready': readyCallback,
            'disconnected': disconnectedCallback,
            'error': errorCallback,
        }
        discord_rpc.initialize('782017295106572339', callbacks=callbacks, log=False)
        start = time.time()
        print(start)
        discord_rpc.update_connection()
        discord_rpc.run_callbacks()
        discord_rpc.update_presence(
            **{
                'details': 'Main Menu',
                'start_timestamp': start,
                'large_image_key': 'hina'
            }
        )
    stop music
    stop sound
    scene black
    $ renpy.movie_cutscene("gui/intro.mpg")
    scene white