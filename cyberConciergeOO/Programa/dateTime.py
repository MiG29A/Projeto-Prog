#2018-2019 Programação II (LTI)
#Grupo 02
#51893 Miguel Alexandre Almeida
#53311 José Carlos Aurora da Costa Silva Ferreira

import constants



def get_date(filename):
    """
        This function will receive the filename of a file and return the date in YYYYyMMmDD format, in a string

        Requires: Filename of file

        Ensures: String with date in YYYYyMMmDD format
    """
    return filename[0:10]


def get_hours(hours):
    """
        This function will receive the hours and minutes string in a HH:MM format and return only the hours

        Requires: String with the time in hours and minutes(HH:MM)

        Ensures: String with the number of hours
    """

    return str(hours.split(':')[0])

def get_minutes(hours):
    """
        This function will receive the hours and minutes string in a HH:MM format and return only the minutes

        Requires: String with the time in hours and minutes(HH:MM)

        Ensures: String with the number of minutes
    """
    minutes_update = int(hours.split(':')[1])
    if minutes_update<=9:
        minutes_update = str(minutes_update)
        minutes_update = '0'+minutes_update
    else:
        minutes_update = str(minutes_update)

    return minutes_update

def timeUpdate(hours, inc):
    """
    This function increments the given hour, 'inc' ammount of minutes
    Requires : Time STR in HH:MM format, and positive integer INC
    Ensures : Updated hour
    """

    hour_update = int(get_hours(hours))
    minutes_update = int(get_minutes(hours))

    if(isinstance(inc, str)):
        increment = int(get_minutes(inc)) + (int(get_hours(inc))*60)

    minutes_update += inc

    days_to_update=0

    while minutes_update>=60:
        hour_update+=1
        minutes_update-=60

    while hour_update>=20:
        hour_update=hour_update-12
        days_to_update+=1

    if(hour_update<10):
        hour_update=str(hour_update)
        hour_update='0'+ hour_update

    if(minutes_update<10):
        minutes_update=str(minutes_update)
        minutes_update= '0'+ minutes_update

    updated_time = str(hour_update)+':'+str(minutes_update)

    return updated_time


def date_compare(first_date, second_date):
    """
        This function will compare two dates, and output the latest of the two.

        Requires: Two strings with dates either in YYYYyMMmDD or YYYY-MM-DD format

        Ensures : String with the latest date
    """
    first_date_year=int(first_date[0:4])
    first_date_month=int(first_date[5:7])
    first_date_day=int(first_date[8:10])

    second_date_year=int(second_date[0:4])
    second_date_month=int(second_date[5:7])
    second_date_day=int(second_date[8:10])

    if((first_date_year >= second_date_year and first_date_month >= second_date_month and first_date_day > second_date_day) or (first_date_year >= second_date_year and first_date_month > second_date_month ) or (first_date_year > second_date_year)):
        return first_date
    else:
        return second_date


def date_time_update(date,hours,increment):
    """
        This function will update the date and the hour received from 'hours' with the value received in 'update' which will be in either string or integer

        Requires: String with the date, other with the current hour and minutes and another one with the minutes to update.

        Ensures: Updated date and hour in string
    """
    #time update

    hour_update = int(get_hours(hours))
    minutes_update = int(get_minutes(hours))

    if(isinstance(increment, str)):
        increment = int(get_minutes(increment)) + (int(get_hours(increment))*60)

    minutes_update += increment

    days_to_update=0

    while minutes_update>=60:
        hour_update+=1
        minutes_update-=60

    while hour_update>=20:
        hour_update=hour_update-12
        days_to_update+=1

    if(hour_update<10):
        hour_update=str(hour_update)
        hour_update='0'+ hour_update

    if(minutes_update<10):
        minutes_update=str(minutes_update)
        minutes_update= '0'+ minutes_update

    updated_time = str(hour_update)+':'+str(minutes_update)

    ##date update
    year_update=int(date[0:4])
    month_update=int(date[5:7])
    day_update=int(date[8:10])

    while(days_to_update>0):
        day_update+=1

        if(day_update>30):
            month_update+=1
            day_update=1

            if(month_update>12):
                year_update+=1
                month_update=1

        days_to_update-=1

    if(day_update<10):
        day_update=str(day_update)
        day_update= '0'+day_update

    if(month_update<10):
        month_update=str(month_update)
        month_update= '0'+month_update


    updated_date= str(year_update)+'-'+str(month_update)+'-'+str(day_update)

    return updated_date, updated_time
