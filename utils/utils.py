import os
import random
import re

import pyttsx3


class Utils:
    def __init__(self, logger):
        self.logger = logger
        self.engine = pyttsx3.init()

    @staticmethod
    def normalize_utterances(utterances):
        normalized = ''
        for u in utterances:
            u = re.sub('\\W+', ' ', u)
            normalized += u.lower().strip() + "|"

        return normalized[:-1]

    @staticmethod
    def match_pattern(voice_note, pattern):
        data = Utils.normalize_utterances(pattern)
        compiled = re.compile(data)
        value = compiled.search(voice_note)
        if value:
            return True
        else:
            False

    @staticmethod
    def choose_random(response):
        return random.choice(response)

    def playsound(self, response, os_name):
        if os_name == 'Darwin':
            os.system('say "{}"'.format(response))
        else:
            self.engine.say(response)
            self.engine.runAndWait()
