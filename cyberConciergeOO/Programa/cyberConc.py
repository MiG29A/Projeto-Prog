from File import File
from Expert import Expert
from Client import Client
from collections import UserList
from ClientCollection import ClientCollection
import constants

inFileClients = File("2019y01m12clients09h00.txt") # use sys.argv[1:]
inFileClientsHeader, inFileClientsContent = inFileClients.readFileClient()
print(inFileClientsContent)
print(inFileClientsContent[0].getClientName())
#ClientUserList = ClExTest(inFileClientsContent)
inFileClientsContent.sortClient()
#testes = ClientUserList.yieldList()
#for el in testes:print(el)

inFileExperts = File("2019y01m12experts09h00.txt") # usar sys.argv[1:]
inFileExpertsHeader, inFileExpertsContent = inFileExperts.readFileExpert()

#for line in inFileClientsContent:
#    print (line.getClientObject())

#for lin in inFileExpertsContent:
#    print(lin.getExpertObject())


#print(inFileClientsHeader.getHeader())
#print(inFileExpertsHeader.getHeader())

#print(inFileClients.getFilenameInfo())
#print(inFileExperts.getFilenameInfo())


#print(inFileClients == inFileExperts) # para comparar acho que se  faz assim : inFileClients.__eq__(inFileExperts)
