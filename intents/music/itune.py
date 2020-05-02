from intents import music


class ITune:
    def __init__(self, logger):
        self.logger = logger

    def launch(self, key):
        if 'play music' in key:
            self.logger.info('Playing music...')
            music.launch()
            music.play()
        elif 'next song' in key or 'change' in key:
            self.logger.info('Playing next song...')
            music.next()
        elif 'previous' in key or 'last' in key:
            self.logger.info('Playing previous song...')
            music.previous()
        elif 'stop' in key:
            self.logger.info('Stop music.')
            music.stop()
        elif 'mute' in key:
            self.logger.info('Mute music.')
            music.mute()
        elif 'unmute' in key:
            self.logger.info('Un Mute music.')
            music.un_mute()
