import appdaemon.plugins.hass.hassapi as hass
from datetime import datetime, timedelta

class Automation7(hass.Hass):

    def initialize(self):
        self.log('initializing ...')
        self.events = {}                                                                    # yellow
        # self.events = {"fh_sensor_failure": 0, "i_sensor_failure": 0}
        self.last_notification = datetime.now() - timedelta(hours= 2)                       # yellow
        sensor = self.args["sensor"]
        for failure in self.args["failures"]:
            failure_name = failure["name"]
            self.events[failure_name] = 0
            self.log(f'subscribing to <{failure_name}> from <{sensor}> ')
            self.listen_state(self.on_boiler_failure, sensor, new=failure_name)             # green


    def on_boiler_failure(self, entity, attribute, old, new, kwargs):
        self.log(f'last_updated: {self.get_state(entity, attribute= "last_updated")}')
        currCount = self.events[new]                                                        # yellow
        self.events[new] = currCount+1                                                      # yellow
        self.run_in(self.__update_counter, 3.600, event = new)                              # blue
        
        notify_now = True
        for failure in self.args["failures"]:
            failure_name = failure["name"]
            failure_amount = failure["amount"]
            if self.events[failure_name] < failure_amount :                                # green
                notify_now = False                                                         # yellow

        # only check the time condition if we have the amount the failures needed.
        if notify_now and self.last_notification > (datetime.now() - timedelta(hours= 1)):  # blue
            notify_now = False                                                              # yellow

        if notify_now:                                                                      # green
            self.last_notification = datetime.now()
            self.log('Send Boiler Alert Notification')
        else: # only used for debugging purposes
            self.log('Waiting ...')   


    def __update_counter(self, kwargs):                                                     # yellow
        event = kwargs["event"]                                                             # yellow
        currCount = self.events[event]                                                      # yellow
        self.events[event] = currCount-1                                                    # yellow


    # def on_boiler_failure(self, entity, attribute, old, new, kwargs):
    #     currCount = self.events[new]
    #     self.events[new] = currCount+1
    #     self.run_in(self.__update_counter, 60, event = new)

    #     if self.events["fh_sensor_failure"] >= 3 and self.events["i_sensor_failure"] >= 1:
    #         if self.last_notification < (datetime.now() - timedelta(hours= 1)):
    #             self.last_notification = datetime.now()
    #             self.log('Send Boiler Alert Notification')
    #         else: # only used for debugging purposes
    #             self.log('Waiting ...')   
    