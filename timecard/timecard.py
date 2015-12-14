from datetime import datetime

# TimeCard by Collin McLean
# A simple program to clock in and out of personal project sessions

class TimeCard(object):
    
    def __init__(self, timein=None, timeout=None):
        """Creates an object that stores when the user starts and ends
        their session"""
        
        self.timein = timein
        self.timeout = timeout
    
    
    def savef(self):
        """Creates a json serializable format for saving."""
        if self.timeout == None:
            return [self.timein.strftime('%b %d, %Y %H:%M:%S.%f'), None]
        else:
            return [self.timein.strftime('%b %d, %Y %H:%M:%S.%f'), \
                    self.timeout.strftime('%b %d, %Y %H:%M:%S.%f')]
        
        
    def loadf(self, strtimes):
        """Loads a json serialized format, must be in the exact datetime
        format as the savef function."""
        
        if strtimes[0] == None:
            self.timein == None
        else:
            self.timein = datetime.strptime(strtimes[0], '%b %d, %Y %H:%M:%S.%f')
        
        if strtimes[1] == None:
            self.timeout = None
        else:
            self.timeout = datetime.strptime(strtimes[1], '%b %d, %Y %H:%M:%S.%f')
    
    
    def seconds(self):
        """Returns the total amount of time of the session if the timecard
        has been completed properly (contains both a time-in and time-out
        datetime object)"""
        
        if self.timein == None:
            print 'This timecard has not been clocked in yet.'
            return 0
        elif self.timeout == None:
            print 'This timecard has not been clocked out yet.'
            return 0
        else:
            return (self.timeout - self.timein).total_seconds()

    
    ### in hindsight, these probably aren't needed, perhaps a similar function
    ### to the above but returns a straight up timedelta object instead
    def minutes(self):
        return self.seconds() / 60
    
    def hours(self):
        return self.minutes() / 60
    
    def days(self):
        return self.hours() / 24