import threading
from datetime import datetime
from utils.alarm_utils.alarm_timing import AlarmTiming
from utils.utils import Utils


class Reminder(threading.Thread):
    def __init__(self, logger, voice_input, reminder, response, os):
        threading.Thread.__init__(self)
        self.logger = logger
        self.input = voice_input
        self.os = os
        self.response = response
        self.utils = Utils(self.logger)
        self.reminder = reminder

    def run(self):
        new = AlarmTiming(self.logger, self.input).get_expected_time()
        new = datetime.strptime(new, "%Y-%m-%d %H:%M:00")

        self.logger.info('Current time is : ' + str(datetime.now()))
        self.utils.playsound(self.response, self.os)
        while True:
            now = datetime.now().strftime('%Y-%m-%d %H:%M:00')
            now = datetime.strptime(now, "%Y-%m-%d %H:%M:00")
            if now > new:
                self.utils.playsound('Alarm time is greater than current time sir.', self.os)
                break
            elif now == new:
                self.utils.playsound(self.reminder, self.os)
                break
