from timecard import TimeCard
from datetime import datetime
from os.path import exists
import os
import json

# TimeCard by Collin McLean
# A simple program to clock in and out of personal project sessions


class TimeFile(object):

    def __init__(self, name='myfile'):
        """Creates an object that organizes timecard objects via their clock-in
        times. The name attribute of this object is used as the savefile name
        with extension '.tc'"""

        self.file = []
        self.current = None
        self.name = name

    def find(self, time, start, end):
        """Searches the timecards with a given datetime object, will return
        a value regardless of whether or not a matching result is found.
        WORK IN PROGRESS"""

        mid = len(self.file) / 2 - 1

        if end > start:
            return start
        elif time > self.file[mid].timein:
            self.find(time, mid, end)
        elif time < self.file[mid].timein:
            self.find(time, start, mid)
        else:
            return mid

    def clockin(self):
        """Creates a new active time card and datetime object set to the user
        computer's current time, will not overwrite if a current session
        already exists"""

        if self.status() == 0:
            self.current = TimeCard(datetime.now())
        else:
            return 'Error: A session is still in progress'

        return self.current.timein

    # is this accounting for DST properly?... probably not
    def clockout(self):
        """Clocks out the active session, adds it to the list of sessions,
        and then clears it such that a new active session can start."""

        if self.status() == 0:
            return 'Error: No session found'

        # stores the current datetime to be used after current is set to null
        now = datetime.now()
        self.current.timeout = now

        # commenting for this if-statement block doesn't look right...
        # are the any overlooked possibilities that may mess with sorting?
        if not self.file:
            self.file.append(self.current)
        # if the active session's clock-in time is before the last session's
        # then search for the proper place to put it in
        elif self.file[len(self.file)-1].timein > self.current.timein:
            self.file.insert(self.find(self.current.timein, 0, len(self.file)), \
                             self.current)
        else:
            self.file.append(self.current)

        self.current = None

        return now


    def manual(self, start, end=None):
        if not start:
            print 'A manual entry requires a start time at minimum'
            return None
        elif not end:
            if self.current:
                print 'Cannot create an active manual entry with a session already in progress'
                return None
            self.current = TimeCard(start)
        else:
            pass


    def status(self):
        """Checks the current session object and returns 0 if null, 1 if
        exists but not clocked in, or 2 if exists but not clocked out."""

        if not self.current:
            return 0
        elif not self.current.timein:
            return 1
        else:
            return 2


    def save(self):
        """Saves the entire object's content, including the active session
        such that the user can retain their session without keeping a certain
        window open"""

        # sets the filename to be the object's name attribute, checks for
        # existing files
        file = '%s.tc' % self.name
        exist = False

        # if the file exists create a secondary file to prevent data loss from
        # write failures
        if exists(file):
            exist = True
            file = '%s.temp' % file

        f = open(file, 'w')

        # uses the first two lines of the file for the name followed by the
        # active session
        f.write(json.dumps(self.name) + '\n')
        if self.current:
            f.write(json.dumps(self.current.savef()) + '\n')
        else:
            f.write(json.dumps(None) + '\n')

        # remainder of the file is used to store each timecard
        for card in self.file:
            f.write(json.dumps(card.savef()) + '\n')

        f.close()

        # removes the original save file and replaces it with the secondary
        if exist == True:
            os.remove('%s.tc' % self.name)
            os.rename(file, '%s.tc' % self.name)

        print 'Saved:', self.name + '.tc'


    def load(self, name):
        """Loads any file created through this object's save function, the first
        2 lines are always assumed to be the object name and active session
        respectively"""

        file = name + '.tc'

        if not exists(file):
            print 'File not found'
            return 0

        f = open(file, 'r')

        # it is always assumed that line one of the file is the name and line 2
        # is the active session, or null if none exists
        self.name = json.loads(f.readline().rstrip('\n'))
        self.current = json.loads(f.readline().rstrip('\n'))

        # safely checks for null, then loads the active session into a timecard
        if self.current:
            hold = self.current
            self.current = TimeCard()
            self.current.loadf(hold)

        for card in f:
            # print card # for debug use
            # print json.loads(card) # for debug use

            # loads in the timecards, assumes that the file is already sorted
            # a sort may be in order
            if card.rstrip('\n').strip():
                self.file.append(TimeCard())
                self.file[len(self.file)-1].loadf(json.loads(card.rstrip('\n')))

                # self.file.append(TimeCard().loadf(json.loads(card.rstrip('\n')))) # y no work? :c

        f.close()
        print 'Loaded:', name + '.tc'


    def list(self):
        """Prints out every session stored in the object."""

        print '=' * 9, 'timein', '=' * 9, ' ', '=' * 9, 'timeout', '=' * 8
        for card in self.file:
            print card.timein.isoformat(' '), ' ', card.timeout.isoformat(' ')
