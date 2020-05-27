import appdaemon.plugins.hass.hassapi as hass

class Automation1(hass.Hass):

    def initialize(self):
        self.log('initializing ...')
        self.listen_state(self.on_motion_detected, self.args["sensors"]["motion"], new="on")  # green

    def on_motion_detected(self, entity, attribute, old, new, kwargs):
        light_entity = self.args["lights"]["bathroom"]                                        # yellow
        ambient_light = int(self.get_state(self.args["sensors"]["light"]))                    # yellow
        bathroom_light = self.get_state(light_entity)                                         # yellow
        if ambient_light <= 35 and bathroom_light == "off":                                   # green
            self.log('turning on the bathroom light')
            self.turn_on(light_entity)
                