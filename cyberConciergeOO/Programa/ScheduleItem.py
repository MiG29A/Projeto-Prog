
class ScheduleItem:

    def __init__(self, jobStartDate, jobStartHour, clientName, expertName):
        self._jobStartDate = jobStartDate
        self._jobStartHour = jobStartHour
        self._clientName = clientName
        self._expertName = expertName
        self._scheduleObject = [jobStartDate, jobStartHour, clientName, expertName]

    def getClientName(self):
        return self._clientName

    def getExpertName(self):
        return self._expertName

    def getJobStartDate(self):
        return self._jobStartDate

    def getJobStartHour(self):
        return self._jobStartHour

    def setClientName(self, clientName):
        self._clientName = clientName

    def setExpertName(self, expertName):
        self._expertName = expertName

    def setJobStartDate(self, jobStartDate):
        self._jobStartDate = jobStartDate

    def setJobStartHour(self, jobStartDate):
        self._jobStartHour = jobStartHour

    def __str__(self):
        return self._jobStartDate+", "+self._jobStartHour+", "+self._clientName+" , "+ self._expertName
