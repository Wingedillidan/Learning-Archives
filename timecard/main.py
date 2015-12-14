from datetime import datetime
from timefile import TimeFile
from sys import exit
from os.path import exists

def init():
    print '\n\n\nWelcome to TimeCard! A simple way of tracking how much time y-'
    print 'ou spent doing personal projects!\n\n'
    
    print 'Enter a filename (if loading a save, then enter the name minus'
    print 'the extension, case sensitive)'
    filename = raw_input('> ')
    
    activefile = TimeFile(filename)
    
    if activefile.load(filename) == 0:
        print 'Created a new file!\n\n'
    else:
        if activefile.current:
            print '\n\nA session is still active, it is clocked in at:', \
                  activefile.current.timein.strftime('%b %d, %Y %H:%M:%S.%f')
    
    main_menu(activefile)

def changename(timefile):
    print 'Input a new desired file name:'
    response = raw_input('> ')
    
    if exists(response + '.tc'):
        print 'File already exists, are you sure you want to overwrite & continue? Y\N'
        if not 'y' in raw_input('> ').lower():
            return 0
    
    timefile.name = response
    
    timefile.save()
    return timefile
    
def main_menu(timefile):
    while True:
        print 'Input a command via a corresponding numbers:'
        print ' [1] Clock in'
        print ' [2] Clock out'
        print ' [3] List all sessions'
        print ' [4] Change filename'
        print ' [5] Save & quit'
        
        try:
            response = int(raw_input('> '))
        except ValueError:
            print '\n\nError: Input was not a number.\n\n\n'
            continue
        
        print '\n'
        
        if response == 1:
            time = timefile.clockin()
            
            if type(time) is datetime:
                print 'Clocked in at time:', time.strftime('%b %d, %Y %H:%M:%S.%f')
            else:
                print time
                
        elif response == 2:
            time = timefile.clockout()
            
            if type(time) is datetime:
                print 'Clocked out at time:', time.strftime('%b %d, %Y %H:%M:%S.%f')
            else:
                print time
                
        elif response == 3:
            timefile.list()
        elif response == 4:
            timefile = changename(timefile)
        elif response == 5:
            timefile.save()
            exit(0)
        else:
            'Error: Number outside range of menu values.'
            
        print '\n\n'

init()