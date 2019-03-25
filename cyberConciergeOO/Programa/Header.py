#2018-2019 Programação II (LTI)
#Grupo 02
#51893 Miguel Alexandre Almeida
#53311 José Carlos Aurora da Costa Silva Ferreira

from copy import deepcopy

class Header:
    def __init__(self, date, time, scope):
        """
        """
        self._headerDate = date
        self._headerTime = time
        self._headerScope = scope
        self._headerList=[self._headerDate, self._headerTime, self._headerScope]

    def getHeader(self):
        return deepcopy(self._headerList)

    def getHeaderDate(self):
        return self._headerDate

    def getHeaderTime(self):
        return self._headerTime

    def getHeaderScope(self):
        return self._headerScope

    def setHeaderDate(self, date):
        self._headerDate = date

    def setHeaderTime(self, time):
        self._headerTime = time

    def setHeaderScope(self, scope):
        self._headerScope = scope

    def __getitem__(self):
        return self._headerScope
