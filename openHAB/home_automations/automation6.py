from core.rules import rule
from core.triggers import when
from personal.logger import logDebug
from org.joda.time import DateTime
from core.actions import PersistenceExtensions


@rule("Power: Main energy monitor")                                                                                                         # green
@when("Item HEM1_Total_Energy_Cleaned changed")                                                                                             # green
def mainsEnergyMonitor(event):
    lastThreeWeeksUsage = float(str(PersistenceExtensions.sumSince(ir.getItem("HEM1_Total_Energy_Delta"), DateTime.now().minusDays(21))))   # blue yellow
    if lastThreeWeeksUsage > 200:                                                                                                           # green  
       logDebug("Demo8","Send alert - {} => {}".format(event.itemName, str(event.itemState)))
            
    