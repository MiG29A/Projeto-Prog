from copy import deepcopy
class Client:

    def __init__(self, name, local, start_date, start_hour, max_price, min_rep, domain, job_dur):
        """
        Receives all the parameters pertaining to a client, and creates a client object.
        Requires: Client Name, Client Localization, Client job start date, Client job start hour,
        Client's maximum budget, Client's minimum reputation required, Job domain, Job Duration.
        Ensures: Client Object
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
        return self._clientName

    def getClientLocal(self):
        return self._clientLocal

    def getClientJobStartDate(self):
        return self._clientJobStartDate

    def getClientJobStartHour(self):
        return self._clientJobStartHour

    def getClientJobMaxPrice(self):
        return self._clientJobMaxPrice

    def getClientMinRep(self):
        return self._clientMinRep

    def getClientJobDomain(self):
        return self._clientJobDomain

    def getClientJobDuration(self):
        return self._clientJobDuration

    def getClientObject(self):
        return deepcopy(self._clientObject)
