import os

from utils.utils import Utils


class Applications:
    def __init__(self, logger, response, applications, command, os_name):
        self.logger = logger
        self.response = response
        self.os_name = os_name
        self.utils = Utils(self.logger)
        self.applications = applications
        self.command = command

    def get_name(self):
        return self.command.split(' ')[1]

    def get_path(self):
        name = self.get_name()
        self.logger.info('App Name : {}'.format(name))

        for app, path in self.applications.items():
            if name.lower() == app.lower():
                return path

    def launch(self):
        path = self.get_path()
        self.logger.info('App path : {}'.format(path))
        if path:
            self.utils.playsound(self.response, self.os_name)
            if self.os_name == 'Darwin':
                os.system('open {}'.format(path))
            else:
                os.system('explorer {}'.format(path))
        else:
            self.utils.playsound('I am sorry Sir. The app which you are looking for, is not register into my database.',
                                 self.os_name)
