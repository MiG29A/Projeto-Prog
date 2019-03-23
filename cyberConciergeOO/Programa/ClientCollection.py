import constants
from copy import deepcopy

class ClientCollection:
    def __init__(self):
        self._clientCollection = []

    def appendClient(self, clientObj):
        self._clientCollection.append(clientObj)

    def sortClient(self):
        self._clientCollection = sorted(self._clientCollection, key=lambda clients:(clients.getClientJobStartHour(), clients.getClientJobStartDate()))
        pass

    def __getitem__(self, index):
        return self._clientCollection[index]

    def getClientList(self):
        return deepcopy(self._clientCollection)
