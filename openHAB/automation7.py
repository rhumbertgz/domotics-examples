from core.rules import rule
from core.triggers import when
from core.actions import ScriptExecution
from org.joda.time import DateTime
from personal.logger import logDebug
from threading import Timer
from java.time import ZonedDateTime as ZDateTime
import core

events = {"FHS_FAILURE": 0, "IS_FAILURE": 0}                        # yellow
lastNotification = ZDateTime.now().minusSeconds(5)                  # yellow

def update_counter(event):                                          # yellow
    global events                                                   # yellow
    currCount = events[event]                                       # yellow
    events[event] = currCount-1                                     # yellow
    logDebug("Demo4","Timeout - New State {}".format(events))


@rule("(Py) Boiler alert notification")                             # green
@when("Item BoilerAlarm received update FHS_FAILURE")               # green
@when("Item BoilerAlarm received update IS_FAILURE")                # green
def boiler_alert(event):
    global events, lastNotification                                 # yellow
    logDebug("Demo4","States: {}".format(events))
    eventStr = str(items.BoilerAlarm)                               # yellow
    currCount = events[eventStr]                                    # yellow
    events[eventStr] = currCount+1                                  # yellow
    #  //now.plusHours(1) -  We don't ever need to cancel the Timer so we don't need to keep a handle on it 
    # ScriptExecution.createTimer(DateTime.now().plusSeconds(5), lambda e=eventStr: update_counter(e))
    Timer(5, lambda e=eventStr: update_counter(e)).start()          # blue

    if events["FHS_FAILURE"] >= 3 and events["IS_FAILURE"] >= 1:            # green
        if lastNotification.isBefore(ZDateTime.now().minusSeconds(5)):      # blue
            lastNotification = ZDateTime.now()                              # yellow
            logDebug("Demo4", "Sending Boiler Alert Notification")
        else:
            logDebug("Demo4", "Waiting ...")
        


    