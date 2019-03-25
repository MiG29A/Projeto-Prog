#2018-2019 Programação II (LTI)
#Grupo 02
#51893 Miguel Alexandre Almeida
#53311 José Carlos Aurora da Costa Silva Ferreira

import constants
from copy import deepcopy

class ExpertCollection:
    def __init__(self):
        self._expertCollection = []

    def appendExpert(self, expertObj):
        self._expertCollection.append(expertObj)

    
##    def sortExpert(self):   # NÃO ENTENDI A ORDENÇÃO
##        self._expertCollection = sorted (self._expertCollection, key = lambda )

    def __getExpertItem__(self, index):
        return self._expertCollection [index]

    def getExpertList (self):
        return deepcopy(self._expertCollection)
