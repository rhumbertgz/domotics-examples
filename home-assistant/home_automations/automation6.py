import appdaemon.plugins.hass.hassapi as hass
from datetime import datetime, timedelta
from functools import reduce

class Automation6(hass.Hass):

    def initialize(self):
        self.log('initializing ...')   
        self.run_daily(self.check_consumption, datetime.time(8, 00, 00))       # blue

    def check_consumption(self):
        data = self.get_history("energy_consumption", days = 21)                # yellow
        total = reduce((lambda x, y: x + y), data)                              # green
        if total > 200:                                                         # green
            self.send_notification()

    def send_notification(self):
        self.log('notiy ...') 