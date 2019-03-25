#2018-2019 Programação II (LTI)
#Grupo 02
#51893 Miguel Alexandre Almeida
#53311 José Carlos Aurora da Costa Silva Ferreira

import sys
from File import File
from Expert import Expert
from Client import Client
from collections import UserList
from ClientCollection import ClientCollection
from ExpertCollection import ExpertCollection 
import constants



def assign(fileNameExperts, fileNameClients):
    """
    Assign given experts given to given clients.
    Requires: fileNameExperts, fileNameClients are str
    """
    inFileExperts = File(fileNameExperts)
    inFileExpertsHeader, inFileExpertsContent = inFileExperts.readFileExpert()
    
    inFileClients = File(fileNameClients)
    inFileClientsHeader, inFileClientsContent = inFileClients.readFileClient()


inputFileName1, inputFileName2 = sys.argv[1:]

assign(inputFileName1, inputFileName2)

######## TEST 
inFileClients = File("2019y01m12clients09h00.txt") 
inFileClientsHeader, inFileClientsContent = inFileClients.readFileClient()

print(inFileClientsHeader.getHeader())

inFileClientsContent.sortClient()

#for line in inFileClientsContent:
#    print (line.getClientObject())

#for lin in inFileExpertsContent:
#    print(lin.getExpertObject())

#print(inFileClientsHeader.getHeader())
#print(inFileExpertsHeader.getHeader())

#print(inFileClients.getFilenameInfo())
#print(inFileExperts.getFilenameInfo())
#print(inFileClients == inFileExperts) # para comparar acho que se  faz assim : inFileClients.__eq__(inFileExperts)
