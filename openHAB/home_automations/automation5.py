from core.rules import rule
from core.triggers import when
from personal.logger import logDebug
from java.time import ZonedDateTime as ZDateTime

lastDoorOpen = ZDateTime.now().minusHours(24)                                                   # yellow
lastEHallMotion = ZDateTime.now().minusHours(24)                                                # yellow
lastFDoorMotion = ZDateTime.now().minusHours(24)                                                # yellow

@rule("(Py) Front Door Opened")                                                                 # green
@when("Item Front_Door_Contact changed to OPEN")                                                # green
def front_door_opened(event):
    global lastDoorOpen                                                                         # yellow
    lastDoorOpen = ZDateTime.now()                                                              # yellow
    logDebug("Automation5", "The Front Door was opened")

@rule("(Py) Motion Detected - Entrance Hall")                                                   # green
@when("Item Entrance_Hall_Motion changed to ON")                                                # green
def entrance_hall_motion(event):
    global lastEHallMotion, lastFDoorMotion                                                     # yellow
    lastEHallMotion = ZDateTime.now()                                                           # yellow
    logDebug("Automation5", "Motion detected in the Entrance Hall")

    if lastFDoorMotion.isBefore(lastEHallMotion.minusSeconds(10)):                              # blue
        logDebug("Automation5", "Discarding old Motion Detected in the Front Door")
        return                                                                                  # blue
    
    if lastEHallMotion.isAfter(lastDoorOpen) and lastDoorOpen.isAfter(lastFDoorMotion):         # purple
        logDebug("Automation5", "Arriving Home!")


@rule("(Py) Motion Detected - Front Door")                                                      # green
@when("Item Front_Door_Motion changed to ON")                                                   # green
def front_door_motion(event):
    global lastEHallMotion, lastFDoorMotion                                                     # yellow
    lastFDoorMotion = ZDateTime.now()                                                           # yellow
    logDebug("Automation5", "Motion detected in the Front Door")

    if lastEHallMotion.isBefore(lastFDoorMotion.minusSeconds(10)):                              # blue
        logDebug("Automation5", "Discarding old Motion Detected in the Entrance Hall")
        return                                                                                  # blue
    
    if lastFDoorMotion.isAfter(lastDoorOpen) and lastDoorOpen.isAfter(lastEHallMotion):         # purple
        logDebug("Automation5", "Leaving Home!")    
    