#2018-2019 Programação II (LTI)
#Grupo 02
#51893 Miguel Alexandre Almeida
#53311 José Carlos Aurora da Costa Silva Ferreira
from SchedulingCollection import SchedulingCollection

def assignTasks(expertCollection, clientCollection, currentHour):
    """
    Receives both expertCollection and clientCollection object, to create schedulingCollection object, with assigned services.
    Requires : expertCollection object ,clientCollection object and currentHour as a "HH:MM" format string
    Ensures : updated expertCollection and creation of schedulingCollection object
    """
    expertCollection = expertCollection
    clientCollection = clientCollection
    currentHour = currentHour
    scheduleCollection = SchedulingCollection()


    expertCollection = expertCollection.sortExpert()
    clientCollection = clientCollection.sortClient()
