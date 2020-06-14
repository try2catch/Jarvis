import threading
import time
from datetime import datetime
from utils.alarm_utils.alarm_timing import Alarm


class ABC(threading.Thread):
    def __init__(self, logger, voice_input):
        threading.Thread.__init__(self)
        self.logger = logger
        self.input = voice_input

    def run(self):
        new = Alarm(self.logger, self.input).get_expected_time()
        self.logger.info('Current time is : ' + str(datetime.now()))
        while True:
            now = datetime.now()
            if now == new:
                print('Alarm running....')
                time.sleep(1)
                break
