from core.rules import rule
from core.triggers import when
from personal.logger import logDebug
import core

#Items
#Switch Bathroom_Window_Timer (gWindowTimers) { expire="1h,command=OFF" } # blue


@rule("(Py) Window open for more than an hour")                     # green                             
@when("Member of gWindows changed")                                 # green  
def window_x_open(event):
    timerX = ir.getItem(event.itemName+"_Timer")                    # yellow  
    if event.itemState == OPEN:                                     # green
        events.sendCommand(timerX, ON)                              # blue
        logDebug("Demo6","Set/Reset timer for "+event.itemName)
    else:
        if timerX.state == ON:                                      # green
            events.postUpdate(timerX, OFF)                          # blue
            logDebug("Demo6","Timer canceled for " +event.itemName )


@rule("(Py) Timer expired for a Window Contact Sensor")              # blue
@when("Member of gWindowTimers received command OFF")                # blue
def timer_expired(event):                                            # blue
    logDebug("Demo6","Timer expired for " +event.itemName )
    