from File import File


inFileClients = File("2019y01m12clients09h00.txt")
inFileExperts = File("2019y01m12experts09h00.txt")
inFileClientsHeader, inFileClientsContent = inFileClients.readFileClient()


inFileClientsHeader.getHeader()
for line in inFileClientsContent:
    print (line.getClientObject())

print(inFileClients.getFilenameInfo())
print(inFileExperts.getFilenameInfo())
print(inFileClients == inFileExperts)
#inFileExperts = File("2019y01m12experts09h00.txt")
