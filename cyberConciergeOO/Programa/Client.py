#2018-2019 Programação II (LTI)
#Grupo 02
#51893 Miguel Alexandre Almeida
#53311 José Carlos Aurora da Costa Silva Ferreira

from copy import deepcopy

class Client:

    def __init__(self, name, local, start_date, start_hour, max_price, min_rep, domain, job_dur):
        """
        Receives all the parameters pertaining to a client, and creates a client object.
        Requires: Client Name, Client Localization, Client job start date, Client job start hour,
        Client's maximum budget, Client's minimum reputation required, Job domain, Job Duration.
        Ensures: Creation of clientObject
        """
        self._clientName = name
        self._clientLocal = local
        self._clientJobStartDate = start_date
        self._clientJobStartHour = start_hour
        self._clientJobMaxPrice = max_price
        self._clientMinRep = min_rep
        self._clientJobDomain = domain
        self._clientJobDuration = job_dur

        self._clientObject = [self._clientName, self._clientLocal, self._clientJobStartDate, self._clientJobStartHour,  self._clientJobMaxPrice, self._clientMinRep, self._clientJobDomain, self._clientJobDuration]



    def getClientName(self):
        """
        Returns Client Name
        """
        return self._clientName

    def getClientLocal(self):
        """
        Returns Client Location
        """
        return self._clientLocal

    def getClientJobStartDate(self):
        """
        Returns Client's Job start date
        """
        return self._clientJobStartDate

    def getClientJobStartHour(self):
        """
        Returns Client's Job start hour
        """
        return self._clientJobStartHour

    def getClientJobMaxPrice(self):
        """
        Returns Client's maximum budget
        """
        return self._clientJobMaxPrice

    def getClientMinRep(self):
        """
        Returns Client's required minimum reputation
        """
        return self._clientMinRep

    def getClientJobDomain(self):
        """
        Returns Client's Job domain
        """
        return self._clientJobDomain

    def getClientJobDuration(self):
        """
        Returns Client's Job duration
        """
        return self._clientJobDuration

    def getClientObject(self):
        """
        Returns Client Object
        """
        return self._clientObject

    #SET DOWN

    def setClientName(self, name):
        """
        Sets Client Name
        """
        self._clientName = name

    def setClientLocal(self, local):
        """
        Sets Client Location
        """
        self._clientLocal = local

    def setClientJobStartDate(self, jobStartDate):
        """
        Sets Client's Job start date
        """
        self._clientJobStartDate = jobStartDate

    def setClientJobStartHour(self, jobStartHour):
        """
        Sets Client's Job start hour
        """
        self._clientJobStartHour = jobStartHour

    def setClientJobMaxPrice(self, jobMaxPrice):
        """
        Sets Client's maximum budget
        """
        self._clientJobMaxPrice = jobMaxPrice

    def setClientMinRep(self, clientMinRep):
        """
        Sets Client's required minimum reputation
        """
        self._clientMinRep = clientMinRep

    def setClientJobDomain(self, clientJobDomain):
        """
        Sets Client's Job domain
        """
        self._clientJobDomain = clientJobDomain

    def setClientJobDuration(self, clientJobDuration):
        """
        Sets Client's Job duration
        """
        self._clientJobDuration = clientJobDuration

    #def setClientObject(self, clientObject):
         #deepcopy(self._clientObject)
