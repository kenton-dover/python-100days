'''Extract datetimes from log entries and calculate the time
   between the first and last shutdown events'''
from datetime import datetime
import os
import urllib.request

SHUTDOWN_EVENT = 'Shutdown initiated'

# prep: read in the logfile
logfile = os.path.join('/tmp', 'log')
urllib.request.urlretrieve('http://bit.ly/2AKSIbf', logfile)

with open(logfile) as f:
    loglines = f.readlines()

# for you to code:


'''my solution'''
def convert_to_datetime(line):
    '''TODO 1:
       Given a log line extract its timestamp and convert it to a datetime object. 
       For example calling the function with:
       INFO 2014-07-03T23:27:51 supybot Shutdown complete.
       returns:
       datetime(2014, 7, 3, 23, 27, 51)'''
    parts = line.split(' ')
    date = parts[1]
    date = date.replace('T', ':')
    date = datetime.strptime(date, '%Y-%m-%d:%H:%M:%S')
    return date


def time_between_shutdowns(loglines):
    '''TODO 2:
       Extract shutdown events ("Shutdown initiated") from loglines and calculate the 
       timedelta between the first and last one. 
       Return this datetime.timedelta object.'''
    temp = []
    for line in loglines:
        if "Shutdown initiated" in line:
            temp.append(line)
    temp[0] = convert_to_datetime(temp[0])
    temp[1] = convert_to_datetime(temp[1])
    timedelta = temp[1] - temp[0]
    return timedelta





'''their solution 
def convert_to_datetime(line):
    TODO 1:
       Given a log line extract its timestamp and convert it to a datetime object.
       For example calling the function with:
       INFO 2014-07-03T23:27:51 supybot Shutdown complete.
       returns:
       datetime(2014, 7, 3, 23, 27, 51)
    timestamp = line.split()[1]
    date_str = '%Y-%m-%dT%H:%M:%S'
    return datetime.strptime(timestamp, date_str)


def time_between_shutdowns(loglines):
    TODO 2:
       Extract shutdown events ("Shutdown initiated") from loglines and
       calculate the timedelta between the first and last one.
       Return this datetime.timedelta object.
    shutdown_entries = [line for line in loglines if SHUTDOWN_EVENT in line]
    shutdown_times = [convert_to_datetime(event) for event in shutdown_entries]
    return max(shutdown_times) - min(shutdown_times)
    '''