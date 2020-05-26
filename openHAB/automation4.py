# Debounce patterns
from core.rules import rule
from core.triggers import when
from java.time import ZonedDateTime as DT
from personal.logger import logDebug
from datetime import datetime, timedelta


lastRing = DT.now().minusSeconds(35)                        # yellow

@rule("(Py) Doorbell notification")                         # green
@when("Item Doorbell changed to PRESSED")                   # green
def doorbell_notification(event): 
    global lastRing                                         # yellow
    if(lastRing.isBefore(DT.now().minusSeconds(30))):       # blue
       lastRing = DT.now()                                  # yellow
       # send the doorbell notification
       logDebug("Demo1","Doorbeell Alert")
    else:
        logDebug("Demo1","Waiting ...")
    
    
