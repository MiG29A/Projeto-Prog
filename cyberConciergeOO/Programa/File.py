import constants
from Header import *
from Client import  Client
from Expert import Expert

class File:
    def __init__(self, fileName):
        """
        Reiceve a file and open it
        Requires: fileName is str with txt extension
        Ensures: a list with fileName data
        """
        self._fileName = fileName

    def getFileName (self):
        """
        Get the name of the file
        """
        return self._fileName

    def setFileName(self, newFileName):
        """
        Set the name of the file
        Requires: newFileName is str with txt extension
        """
        self._fileName = newFileName

    def openFile(self):
        """
        Opens the file that has the provided filename
        Requires: Filename of file
        Ensures: If file exists, it is opened.
        """
        inFile = open(self.getFileName(), "r")
        return inFile

    def readFileClient(self):
        """
        Reads, and returns the Client's Header and File Content, both in a list
        using the file object which is opened and closed inside the function
        Requires: Filename (Already received)
        Ensures: return of list of Header parameters, and list of Client objects
        """
        inFile = self.openFile()
        clHeader = self.readFileHeader(inFile)
        clContent = self.readFileContentCli(inFile)
        inFile.close()

        return clHeader, clContent

    def readFileExpert(self):
        """
        Reads, and returns the Expert's Header and File Content, both in a list
        using the file object which is opened and closed inside the function
        Requires: Filename (Already received)
        Ensures: return of list of Header parameters, and list of Expert objects
        """
        inFile = self.openFile()
        expHeader = self.readFileHeader(inFile)
        expContent = self.readFileContentExp(inFile)
        inFile.close()

        return expHeader, expContent

    def readFileHeader(self, inFile):
        """
        Read the header of the open file
        """
        for line_counter in range(constants.HEADER_LINES):
            line_read = inFile.readline()
            if(line_counter == constants.HEADER_DATE):
                date = line_read
            elif(line_counter == constants.HEADER_HOURS):
                time = line_read
            elif(line_counter == constants. HEADER_FILETYPE):
                scope = line_read

        return Header(date, time, scope)

    def readFileContentCli(self, inFile):
        """
        Reads client's file content after header, creates an object with the data that was read
        and puts all the objects into a list.
        Requires: File Object, with the opened file
        Ensures: Return of List of Client Objects
        """
        clientList = []
        for line in inFile:
            name, local, start_date, start_hour, max_price, min_rep, domain, job_dur = line.strip().split(', ')
            clientList.append(Client(name, local, start_date, start_hour, max_price, min_rep, domain, job_dur))

        return clientList

    def readFileContentExp(self, inFile):
        """
        Reads expert's file content after header, creates an object with the data that was read
        and puts all the objects into a list.
        Requires: File Object, with the opened file
        Ensures: Return of List of Expert Objects
        """
        expertList = []
        for line in inFile:
            name, local, domains, reputation, price, date, hour, total_renum = line.strip().split(', ')
            expertList.append(Expert(name, local, domains, reputation, price, date, hour, total_renum))

        return expertList

    def __str__(self):
        return "File name: "+str(self.getFileName())


    def __eq__ (self,other):
        fileOne = self.getFileName
        fileTwo = other.getFileName
        return fileOne == FileTwo

    def countLines(self):
        """
        count the number of lines in the file
        """
        fileIn = open(self.getFileName(),"r")

        numberLines = 0
        for lines in fileIn:
            numberLines +=1

        fileIn.close()
        return numberLines


    def __lt__(self,other):
        """
        Tell if one file is less than other
        Requires: Other is the name of  file with txt extesion
        """
        fileOne = self.countLines()
        fileTwo = other.countLines()

        return fileOne < fileTwo

    def getFilenameInfo(self):
        """
        Gets the Filename information, date, scope, and hour, for comparison with header, for exception throwing.
        Requires: Filename (already defined as Class attribute)
        Ensures: return of filename data
        """
        self._formattedFilename = self.getFileName().strip('.txt').replace('y','-').replace('m','-')
        return self._formattedFilename
