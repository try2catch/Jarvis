from utils.utils import Utils


class Greeting:
    def __init__(self, logger, response, os_name):
        self.logger = logger
        self.response = response
        self.os_name = os_name
        self.utils = Utils(self.logger)

    def speak(self):
        self.utils.playsound(self.response, self.os_name)
