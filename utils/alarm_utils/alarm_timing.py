import re
import dateparser
from utils import alarm_utils


class AlarmTiming:
    def __init__(self, logger, text):
        self.logger = logger
        self.text = text

    @staticmethod
    def match(string, regex):
        compiled = re.compile(regex)
        result = compiled.search(string)
        if result:
            return result.group()
        else:
            return ''

    def get_expected_time(self):

        date_time_str = ''
        time = AlarmTiming.match(self.text, alarm_utils.time_regex)
        date_time_str += time

        day_night = AlarmTiming.match(self.text, alarm_utils.day_night_regex)
        date_time_str += day_night

        day = AlarmTiming.match(self.text, alarm_utils.days_regex)
        date_time_str += day

        date = AlarmTiming.match(self.text, alarm_utils.date_regex)
        # date_time_str += date

        period = AlarmTiming.match(self.text, alarm_utils.period_regex)
        date_time_str += period
        self.logger.info('Timing String from regex :' + date_time_str)

        value = dateparser.parse(date_time_str)
        self.logger.info('Parsed text to datetime :' + str(value))

        return value
