from core.rules import rule
from core.triggers import when
from core.actions import ScriptExecution as SE
from personal.logger import logDebug
import core

@rule("(Py) Bathroom MotionSensor changed")                                                     # green                                                    
@when("Item Bathroom_Motion received update ON")                                                # green  
def bathroom_motion(event):
    if items.Bathroom_AmbientLight.intValue() <= 40 and items.Bathroom_Lamp == OFF:             # green  
        logDebug("Demo2","Turning ON Bathroom Lamp")
        events.sendCommand("Bathroom_Lamp", "ON")
      


    