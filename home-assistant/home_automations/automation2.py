import appdaemon.plugins.hass.hassapi as hass

class Automation2(hass.Hass):

    def initialize(self):
        self.log('initializing ...')
        self.timer = None                                                                       # yellow
        self.listen_state(self.on_motion_detected, self.args["sensors"]["motion"], new="on")    # green

    def on_motion_detected(self, entity, attribute, old, new, kwargs):
        if self.timer == None:                                                                  # blue
            self.log('starting timer ...')   
            self.__start_timer()                                                                # blue
        else:
            self.log('rescheduling timer ...')  
            self.cancel_timer(self.timer)                                                       # blue
            self.__start_timer()                                                                # blue    


    def __start_timer(self):
        self.timer = self.run_in(self.__turn_off_light, 10)                                    # yellow


    def __turn_off_light(self, kwargs):
        self.log('Timer expired, turning off the light ...')  
        self.turn_off(self.args["lights"]["bathroom"])         