#2018-2019 Programação II (LTI)
#Grupo 02
#51893 Miguel Alexandre Almeida
#53311 José Carlos Aurora da Costa Silva Ferreira
from SchedulingCollection import SchedulingCollection
from ScheduleItem import ScheduleItem
import dateTime

def assignTasks(expertCollection, clientCollection, currentHour):
    """
    Receives both expertCollection and clientCollection object, to create schedulingCollection object, with assigned services.
    Requires : expertCollection object ,clientCollection object and currentHour as a "HH:MM" format string
    Ensures : updated expertCollection and creation of schedulingCollection object
    """
    expertCollection = expertCollection
    clientCollection = clientCollection
    currentHour = dateTime.timeUpdate(currentHour,30)
    scheduleCollection = SchedulingCollection()


    expertCollection = expertCollection.sortExpert()
    clientCollection = clientCollection.sortClient()

    for clients in clientCollection:

        alreadyScheduled = False

        for experts in expertCollection:
            print("Is Scheduled?:", alreadyScheduled)
            if((compatibleScheduling(experts, clients)) and (alreadyScheduled == False)):
                data_tardia = dateTime.date_compare(experts.getExpertLastJobDate(), clients.getClientJobStartDate())
                print("date compare:", experts.getExpertLastJobDate(), clients.getClientJobStartDate(), "Result: ", data_tardia)

                if(data_tardia == experts.getExpertLastJobDate()):
                    data_tardia, hora_tardia = dateTime.date_time_update(experts.getExpertLastJobDate(),experts.getExpertLastJobHour(),60)
                    print("date update:", experts.getExpertLastJobDate(),experts.getExpertLastJobHour(), "Result: ", data_tardia, hora_tardia)
                    if(data_tardia != experts.getExpertLastJobDate()):
                        hora_tardia = constants.DAY_BEGIN_HOUR
                else:
                    hora_tardia = clients.getClientJobStartHour()

                print(data_tardia, "test")
                print(hora_tardia)
                scheduleCollection.appendScheduling(ScheduleItem(data_tardia, hora_tardia, clients.getClientName(), experts.getExpertName()))
                alreadyScheduled = True
                #xprt[constants.XPRT_LASTJOB_DATE], xprt[constants.XPRT_LASTJOB_HOUR] = dateTime.date_time_update(data_tardia, hora_tardia, cl[constants.CL_SERVICE_TIME].replace('h',':'))

                #xprt[constants.XPRT_LASTJOB_DATE] = xprt[constants.XPRT_LASTJOB_DATE]
                #xprt[constants.XPRT_CUMVALUE] += xprt[constants.XPRT_PRICE] * ((float(dateTime.get_hours(cl[constants.CL_SERVICE_TIME].replace('h',':')))) + float((dateTime.get_minutes(cl[constants.CL_SERVICE_TIME].replace('h',':'))))/60)

                #scheduled_clients.append(cl[constants.CL_NAME])

        if alreadyScheduled == False:
            scheduleCollection.appendScheduling(ScheduleItem(clients.getClientJobStartDate(), currentHour, clients.getClientName(), "declined"))
        scheduleCollection.sortSchedule()
#experts_updated_list = sorted(experts, key=lambda experts:(experts[constants.XPRT_LASTJOB_DATE], experts[constants.XPRT_LASTJOB_HOUR],experts[constants.XPRT_REP], experts[constants.XPRT_PRICE], experts[constants.XPRT_CUMVALUE], experts[constants.XPRT_NAME]))
#scheduling_updated_list = sorted(scheduling, key=lambda scheduling:(scheduling[constants.SCHD_DATE], scheduling[constants.SCHD_HOUR], scheduling[constants.SCHD_CL], scheduling[constants.SCHD_XPRT]))

#schedule_file_list = schedule_header + scheduling_updated_list
#xprt_file_list = xprt_header + experts_updated_list

    return scheduleCollection.getScheduleList()

def compatibleScheduling(expertObject, clientObject):
    compatibleRep = checkMinRep(expertObject, clientObject)
    compatiblePrice = checkMaxPrice(expertObject, clientObject)
    compatibleLanguage = checkLanguage(expertObject, clientObject)
    compatibleDomain = checkDomain(expertObject, clientObject)

    return compatibleRep and compatiblePrice and compatibleLanguage and compatibleDomain


def checkMinRep(expertObject, clientObject):
    return expertObject.getExpertReputation() >= clientObject.getClientMinRep()

def checkMaxPrice(expertObject, clientObject):
    return int(expertObject.getExpertPrice()) <= int(clientObject.getClientJobMaxPrice())

def checkLanguage(expertObject, clientObject):
    return expertObject.getExpertLocal() == clientObject.getClientLocal()

def checkDomain(expertObject, clientObject):
    return  clientObject.getClientJobDomain() in expertObject.getExpertDomain()
