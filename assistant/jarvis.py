import threading

import speech_recognition as sr

from intents import music
from intents.applications import Applications
from intents.greeting import Greeting
from intents.music.itune import ITune
from utils.utils import Utils


class Jarvis(threading.Thread):
    def __init__(self, logger, config, os_name):
        threading.Thread.__init__(self)
        self.logger = logger
        self.config = config
        self.os_name = os_name
        self.utils = Utils(self.logger)
        self.speech = sr.Recognizer()

    def read_voice_cmd(self):
        voice_input = ''
        try:
            with sr.Microphone() as source:
                audio = self.speech.listen(source=source, timeout=5, phrase_time_limit=5)
            voice_input = self.speech.recognize_google(audio)
            self.logger.info('Input : {}'.format(voice_input))
        except sr.UnknownValueError:
            pass
        except sr.RequestError:
            print('Network error.')
        except sr.WaitTimeoutError:
            pass
        except TimeoutError:
            pass

        return voice_input.lower()

    def run(self):
        self.logger.info('Thread is running...')
        session = False
        self.utils.playsound('Hello Sir, Welcome to your universe.', self.os_name)
        while True:
            intent = ''

            if music.state() == 'paused' and session is False:
                music.play()

            voice_note = self.read_voice_cmd()
            for key in self.config:
                utterances = Utils.match_pattern(voice_note, self.config[key]['utterances'])
                if utterances:
                    intent = key
                    response = Utils.choose_random(self.config[key]['response'])
                    break

            if intent == 'intent_greeting':
                greeting = Greeting(self.logger, response, os_name=self.os_name)
                if music.state() == 'playing':
                    music.pause()
                    greeting.speak()
                else:
                    greeting.speak()

                session = True
                continue
            elif intent == 'intent_applications':
                if session:
                    applications = self.config[key]['applications']
                    Applications(logger=self.logger, response=response, applications=applications,
                                 command=voice_note, os_name=self.os_name).launch()
                    session = False
                    continue
            elif intent == 'intent_music':
                ITune(self.logger).launch(voice_note)
                continue
