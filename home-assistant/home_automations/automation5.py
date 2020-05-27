# import appdaemon.plugins.hass.hassapi as hass
import hassapi as hass
from datetime import datetime, timedelta

class Automation5(hass.Hass):

    def initialize(self):
        self.log('initializing ...')
        
        sensors =  list(self.args["sensors"])                                                   
        trigger1 = sensors[0]                                                                   # yellow
        trigger2 = sensors[-1]                                                                  # yellow
       
        default_time = datetime.now() - timedelta(hours= 2)                                     # yellow

        # init times dictionary
        self.times = {trigger1["name"]: default_time, trigger2["name"]: default_time }           # yellow

        # subscribe and register callbacks for both triggers
        self.listen_state(self.on_trigger1, trigger1["name"], new= trigger1["state"])            # green
        self.listen_state(self.on_trigger2, trigger2["name"], new= trigger2["state"])            # green

        self.log(f'subscribed to trigger1: {trigger1["name"]} with state: {trigger1["state"]}')
        self.log(f'subscribed to trigger2: {trigger2["name"]} with state: {trigger2["state"]}')

        # remove trigger sensors
        del sensors[0]                                                                          # yellow
        del sensors[-1]                                                                         # yellow

        # subscribe and register callbacks for the remaining sensors 
        for sensor in sensors:                                                                  
            sensor_name = sensor["name"]
            self.times[sensor_name] = default_time                                              # yellow
            self.listen_state(self.on_sensor_update, sensor_name, new= sensor["state"])         # green
            self.log(f'subscribed to: {sensor_name} with state: {sensor["state"]}')

    def on_trigger1(self, entity, attribute, old, new, kwargs):
        self.log('on_trigger1 ...')
       
        last_update_trigger1 = datetime.now()                                                   # yellow
        last_update_trigger2 = self.times[self.args["sensors"][-1]["name"]]                     # blue
        self.times[entity] = last_update_trigger1                                               # blue
        # stop if the the last motion detected by the trigger2 is older than TIME_DELTA sec
        if  last_update_trigger2 < (last_update_trigger1 - timedelta(seconds= int(self.args["time_delta"]))): # blue
            return

        sensors = self.args["sensors"]
        if all((lambda i: self.times[sensors[i]["name"]] > self.times[sensors[i+1]["name"]]) for i in sensors): #purple
            self.log('leaving home ....')  
            # code logic for leaving home 

    def on_trigger2(self, entity, attribute, old, new, kwargs):
        self.log('on_trigger2 ...')
       
        last_update_trigger1 = self.times[self.args["sensors"][0]["name"]]                                      # blue
        last_update_trigger2 = datetime.now()                                                                   # yellow
        self.times[entity] = last_update_trigger2                                                               # blue

        # stop if the the last motion detected by the trigger1 is older than TIME_DELTA sec
        if  last_update_trigger1 < (last_update_trigger2 - timedelta(seconds= int(self.args["time_delta"]))):   # blue
            return

        sensors = self.args["sensors"]
        if all((lambda i: self.times[sensors[i]["name"]] < self.times[sensors[i+1]["name"]]) for i in sensors): # purple
            self.log('arriving home ...')  
            # code logic for arriving home 

             
    def on_sensor_update(self, entity, attribute, old, new, kwargs):
        self.log('on_sensor_update ...')
        self.times[entity] = datetime.now()                                                                     # yellow


    
# import appdaemon.plugins.hass.hassapi as hass
# from datetime import datetime, timedelta

# class HomePresence(hass.Hass):

#     def initialize(self):
#         self.log('initializing ....')
#         default_time = datetime.now() - timedelta(hours= 2)
#         self.last_update_trigger2 = default_time
#         self.last_update_sensor3 = default_time
#         self.last_update_trigger1 = default_time
#         self.listen_state(self.on_sensor_update, self.args["hall_motion"], new="on")
#         self.listen_state(self.on_trigger1, self.args["door_motion"], new="on")
#         self.listen_state(self.on_trigger2, self.args["door_contact"], new="on")

#     def on_trigger2(self, entity, attribute, old, new, kwargs):
#         self.log('on_trigger2ed ...')
#         self.last_update_trigger2 = datetime.now()

#     def on_sensor_update(self, entity, attribute, old, new, kwargs):
#         self.log('on_sensor_update_detected ...')
#         self.last_update_sensor3 = datetime.now()

#         # stop if the the last motion detected by the door_motion_sesor is older than 60 sec
#         if  self.last_update_trigger1 < (self.last_update_sensor3 - timedelta(seconds= 60)):
#             return

#         if self.last_update_sensor3 > self.last_update_trigger2 and self.last_update_trigger2 > self.last_update_trigger1:
#             self.log('arriving home ...')  
#             # code logic for arriving home  
             
    
#     def on_trigger1(self, entity, attribute, old, new, kwargs):
#         self.log('on_trigger1_detected ...')
#         self.last_update_trigger1 = datetime.now()
#         # stop if the the last motion detected by the hall_motion_sesor is older than 60 sec
#         if  self.last_update_sensor3 < (self.last_update_trigger1 - timedelta(seconds= 60)):
#             return

#         if self.last_update_trigger1 > self.last_update_trigger2 and self.last_update_trigger2 > self.last_update_sensor3:
#             self.log('leaving home ...')  
#             # code logic for arriving home 