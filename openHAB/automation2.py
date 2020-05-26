from core.rules import rule
from core.triggers import when
from core.actions import ScriptExecution as SE
from personal.logger import logDebug
from org.joda.time import DateTime
from java.lang.Thread import State
import core

from threading import Timer

timer = None                                                                                # yellow

def start_timer():                                                                          # blue
    global timer                                                                            # yellow
    timer = Timer(5, lambda: logDebug("Automation2","turning off the light ..."))           # yellow
    timer.start()                                                                           # blue


@rule("(Py) Bathroom MotionSensor changed")                                                 # green     
@when("Item Bathroom_Motion received update ON")                                            # green
def bathroom_motion(event):
    global timer                                                                            # yellow
    if timer is None or timer.getState() == State.TERMINATED:                               # blue
        start_timer()                                                                       # blue
    else:
        timer.stop()                                                                        # blue
        start_timer()                                                                       # blue
    

    