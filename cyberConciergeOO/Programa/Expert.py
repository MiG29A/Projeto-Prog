#2018-2019 Programação II (LTI)
#Grupo 02
#51893 Miguel Alexandre Almeida
#53311 José Carlos Aurora da Costa Silva Ferreira

from copy import deepcopy
from ExpertCollection import ExpertCollection

class Expert:

    def __init__(self,name, local, domain, reputation, price, lastJob_date, lastJob_hour, amount):
        """
        Receives all the parameters pertaining to a expert, and creates a client object.
        Requires: Expert Name, Expert Localization, Expert Domain, Expert reputation,
        Expert's last job date, Expert's last job hour , Expert's amount.
        Ensures: Experts Object
        """
        self._expertName = name
        self._expertLocal= local
        self._expertDomain = domain
        self._expertReputation = reputation
        self._expertPrice = price
        self._expertLastJobDate = lastJob_date
        self._expertLastJobHour = lastJob_hour
        self._expertAmount = amount

        self._expertObject = [self._expertName, self._expertLocal, self._expertDomain, self._expertReputation,
                             self._expertPrice, self._expertLastJobDate, self._expertLastJobHour,  self._expertAmount]


    def getExpertName(self):
        """
        Returns Expert Name
        """
        return self._expertName

    def getExpertLocal(self):
        """
        Returns Expert Location
        """
        return self._expertLocal

    def getExpertDomain(self):
        """
        Returns Expert Domain
        """
        return self._expertDomain

    def getExpertReputation (self):
        """
        Returns Expert Reputation
        """
        return self._expertReputation

    def getExpertPrice(self):
        """
        Returns Expert Price
        """
        return self._expertPrice

    def getExpertLastJobDate (self):
        """
        Returns Expert Last Job Date
        """
        return self._expertLastJobDate

    def getExpertLastJobHour (self):
        """
        Returns Expert Last Job Hour
        """
        return self._expertLastJobHour

    def getExpertAmount (self):
        """
        Returns Expert Amount
        """
        return self._expertAmount

    def __str__(self):
        return self._expertName+ "," +self._expertLocal+ "," +str(self._expertDomain)+ "," +self._expertReputation+ "," +self._expertPrice+ "," +self._expertLastJobDate+ "," +self._expertLastJobHour+ "," +self._expertAmount

    def getExpertObject(self):
        return deepcopy(self._expertObject)
