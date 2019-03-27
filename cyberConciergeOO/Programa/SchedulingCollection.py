#2018-2019 Programação II (LTI)
#Grupo 02
#51893 Miguel Alexandre Almeida
#53311 José Carlos Aurora da Costa Silva Ferreira

import constants
from copy import deepcopy

class SchedulingCollection:
    def __init__(self):
        self._scheduleCollection = []

    def appendScheduling(self, schedulingObj):
        self._scheduleCollection.append(schedulingObj)

    def sortSchedule(self):
        self._scheduleCollection = sorted(self._scheduleCollection, key=lambda scheduling:(scheduling.getJobStartDate(), scheduling.getJobStartHour(), scheduling.getClientName(), scheduling.getExpertName()))

    def __getitem__(self, index):
        return self._scheduleCollection[index]

    def getScheduleList(self):
        return deepcopy(self._scheduleCollection)
