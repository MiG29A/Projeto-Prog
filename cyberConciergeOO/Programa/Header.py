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
