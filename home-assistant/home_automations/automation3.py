import appdaemon.plugins.hass.hassapi as hass

class Automation3(hass.Hass):

    def initialize(self):
        self.log('initializing ....')

        group = self.get_state(self.args["windows"], attribute = "all")                     #yellow
        # get all sensors of the group
        sensors = group["attributes"]["entity_id"]                                          #yellow
       
        for sensor in sensors:
            self.log(f'subscribing to: {sensor}')
            self.listen_state(self.on_windows_open, sensor, new= 'on', duration= 3.600)     #green blue

    def on_windows_open(self, entity, attribute, old, new, kwargs):
        window_name = self.friendly_name(entity)    
        self.log(f'Alert! The {window_name} has been open for more than one hour.') 
        # send your notification   
        
                    

# import appdaemon.plugins.hass.hassapi as hass

# class WindowAlert(hass.Hass):

#     def initialize(self):
#         self.log('initializing ...')
#         self.timers = {}
#         group = self.get_state(self.args["windows"], attribute = "all")
#         # get all sensors of the group
#         sensors = group["attributes"]["entity_id"]
       
#         for sensor in sensors:
#             self.log('subscribing to: ' + str(sensor))
#             # init timer dictionary, each entry represents a window (name->timer) 
#             self.timers[str(sensor)] = None
#             self.listen_state(self.on_windows_open, sensor)

#     def on_windows_open(self, entity, attribute, old, new, kwargs):
#         self.log('on_windows_open ' + str(entity))
#         timer_key = str(entity)
#         friendly_name = self.friendly_name(entity)
#         if new == "on":
#             self.log(f'Start timer for {friendly_name}')
#             self.timers[timer_key] = self.run_in(self.send_notification, 3.600, window= friendly_name, timer= timer_key )
#         else:
#             timer = self.timers[timer_key]
#             if timer != None:
#                 self.log(f'Canceling timer for {friendly_name}')
#                 self.timers[timer_key] = self.cancel_timer(timer) 
     

#     def send_notification(self, kwargs):
#         window_name = kwargs["window"]
#         timer_key = kwargs["timer"]
#         # forget timer reference
#         self.timers[timer_key] = None
#         # send your notification   
#         self.log(f'Alert! The {window_name} has been open for more than one hour.') 
                    
