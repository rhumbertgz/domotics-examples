import appdaemon.plugins.hass.hassapi as hass
from datetime import datetime, timedelta

class Automation4(hass.Hass):

    def initialize(self):
        self.log('initializing')
        res = self.get_now_ts()
        self.log(f'state: {res}')
        # initialize last_ring variable to avoid extra `If` condition
        self.last_ring = datetime.now() - timedelta(seconds= 35)                    # yellow
        self.listen_state(self.on_doorbell_press, self.args["sensor"], new="on")    # green

    def on_doorbell_press(self, entity, attribute, old, new, kwargs):
        if self.last_ring < datetime.now() - timedelta(seconds= 35):                 # blue
            self.last_ring = datetime.now()                                          # yellow
            self.log('sending notification')
        else:
            self.log('Waiting ...')    

