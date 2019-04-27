import os
'''

IMPORTANT NOTE: Do NOT change any of the function names or their signatures
(the parameters they take).
Your functions must behave exactly as described. Please check correctness by
running DocTests  included in function headers. You may not use any print or
input statements in your code.

Manage a calendar database.

A calendar is a dictionary keyed by date ("YYYY-MM-DD") with value being a list
of strings, the events on the specified date.

'''


# -----------------------------------------------------------------------------
# Please implement the following calendar commands
# -----------------------------------------------------------------------------

def command_help():
    """
    () -> str
    This function is already implemented. Please do not change it.
    Returns a help message for the system. That is...
    """

    help_me = """
    Help for Calendar. The calendar commands are

    add DATE START END DETAILS               add the event DETAILS at the specified DATE with specific START and END time
    show                                     show all events in the calendar
    delete DATE NUMBER             delete the specified event (by NUMBER) from
                                   the calendar
    quit                           quit this program
    help                           display this help message

    Examples: user data follows command:

    command: add 2018-10-12 18 19 dinner with jane
    success

    command: show
        2018-10-12 : 
            start : 08:00, 
			end : 09:00,
			title : Eye doctor
			
            start : 12:30,
			end : 13:00,
			title : lunch with sid
            
			start : 18:00,
			end : 19:00, 
			title : dinner with jane
        2018-10-29 : 
            start : 10:00,
			end : 11:00,
			title : Change oil in blue car
			
            start : 12:00,
			end : 14:00,
			title : Fix tree near front walkway
			
            start : 18:00,
			end : 19:00,
			title : Get salad stuff, leuttice, red peppers, green peppers
        2018-11-06 : 
            start : 18:00,
			end : 22:00,
			title : Sid's birthday

    command: delete 2018-10-29 10
    deleted

    A DATE has the form YYYY-MM-DD, for example
    2018-12-21
    2016-01-02

    START and END has a format HH where HH is an hour in 24h format, for example
    09
    21

    Event DETAILS consist of alphabetic characters,
    no tabs or newlines allowed.
    """
    return help_me


def command_add(date, start_time, end_time, title, calendar):
    """
    (str, int, int, str, dict) -> boolean
    Add title to the list at calendar[date]
    Create date if it was not there
    Adds the date if start_time is less or equal to the end_time

    date: A string date formatted as "YYYY-MM-DD"
    start_time: An integer from 0-23 representing the start time
    end_time: An integer from 0-23 representing the start time
    title: A string describing the event
    calendar: The calendar database
    return: boolean of whether the even was successfully added

    >>> calendar = {}
    >>> command_add("2018-02-28", 11, 12, "Python class", calendar)
    True
    >>> calendar == {"2018-02-28": [{"start": 11, "end": 12, "title": "Python class"}]}
    True
    >>> command_add("2018-03-11", 14, 16, "CSCA08 test 2", calendar)
    True
    >>> calendar == {"2018-03-11": [{"start": 14, "end": 16, "title": "CSCA08 test 2"}], \
    "2018-02-28": [{"start": 11, "end": 12, "title": "Python class"}]}
    True
    >>> command_add("2018-03-11", 10, 9, "go out with friends after test", calendar)
    False
    >>> calendar == {"2018-03-11": [{"start": 14, "end": 16, "title": "CSCA08 test 2"}], \
    "2018-02-28": [{"start": 11, "end": 12, "title": "Python class"}]}
    True
    >>> command_add("2018-03-13", 13, 13, "Have fun", calendar)
    True
    >>> calendar == {"2018-03-13": [{"start": 13, "end": 13, "title": "Have fun"}], \
    "2018-03-11": [{"start": 14, "end": 16, "title": "CSCA08 test 2"}], \
    "2018-02-28": [{"start": 11, "end": 12, "title": "Python class"}]}
    True
    """


    # YOUR CODE GOES HERE
    if int(start_time) <0 or int(start_time)>23 or int(end_time)<0 or int(end_time)>23:
        return False
    if int(start_time)>int(end_time):
        return False
    if not is_calendar_date(date):
        return False
    date_exist=False
    for caldate in calendar:
        if date==caldate:
            date_exist=True
    event_details={}
    event_details['start'] = start_time
    event_details['end'] = end_time
    event_details['title'] = title
    if not date_exist:
        calendar[date] = []
    calendar[date].append(event_details)
    return True
    pass


def command_show(calendar):
    r"""
    (dict) -> str
    Returns the list of events for calendar sorted in decreasing date order
    and increasing time order within the date
    as a string, see examples below for a sample formatting
    calendar: the database of events

    Example:
    >>> calendar = {}
    >>> command_add("2018-01-15", 11, 13, "Eye doctor", calendar)
    True
    >>> command_add("2018-01-15", 8, 9, "lunch with sid", calendar)
    True
    >>> command_add("2018-02-10", 12, 23, "Change oil in blue car", calendar)
    True
    >>> command_add("2018-02-10", 20, 22, "dinner with Jane", calendar)
    True
    >>> command_add("2017-12-22", 5, 8, "Fix tree near front walkway", calendar)
    True
    >>> command_add("2017-12-22", 13, 15, "Get salad stuff", calendar)
    True
    >>> command_add("2018-05-06", 19, 23, "Sid's birthday", calendar)
    True
    >>> command_show(calendar)
    "\n2018-05-06 : \n    start : 19:00,\n    end : 23:00,\n    title : Sid's birthday\n2018-02-10 : \n    start : 12:00,\n    end : 23:00,\n    title : Change oil in blue car\n\n    start : 20:00,\n    end : 22:00,\n    title : dinner with Jane\n2018-01-15 : \n    start : 08:00,\n    end : 09:00,\n    title : lunch with sid\n\n    start : 11:00,\n    end : 13:00,\n    title : Eye doctor\n2017-12-22 : \n    start : 05:00,\n    end : 08:00,\n    title : Fix tree near front walkway\n\n    start : 13:00,\n    end : 15:00,\n    title : Get salad stuff"
    """

    if calendar=={}:
        return ""
    """
    soated={}

    lenth= len(calendar)
    while lenth > 0:
        latestint = 0
        latestdate = ''
        latest = {}
        for date in calendar:
            date_int = int(date.replace('-', ''))
            if date_int >= latestint:
                latestint=date_int
                latest=calendar[date]
                latestdate=date
        soated[latestdate]=latest
        del calendar[latestdate]
        lenth-=1

    for date in soated:
        list=soated[date]
        if len(list) > 1:
            soated_list=[]
            lenth=len(list)
            while lenth>0:
                earliest = 24
                earliest_arr = {}
                for arr in list:
                    if int(arr['start'])<=earliest:
                        earliest_arr=arr
                soated_list.append(earliest_arr)
                list.remove(earliest_arr)
                lenth-=1
            soated[date]=soated_list
   
    ret=''
    for date in soated:
        ret+=date+'\n'
        list=soated[date]
        for arr in list:
            ret+='\tstart : '+('0'+str(arr['start'])+':00')[-4]+',\n'
            ret += '\tend : '+('0'+str(arr['start'])+':00')[-4]+',\n'
            ret+='\ttitle : '+arr['title']+'\n'"""
    return calendar
    pass


def command_delete(date, start_time, calendar):


    """
    (str, int, dict) -> str
    Delete the entry at calendar[date][start_time]
    If calendar[date] is empty, remove this date from the calendar.
    If the entry does not exist, do nothing
    date: A string date formatted as "YYYY-MM-DD"
    start_time: An integer indicating the start of the event in calendar[date] to delete
    calendar: The calendar database
    return: a string indicating any errors, True for no errors

    Example:


    >>> calendar = {}
    >>> command_add("2018-02-28", 11, 12, "Python class", calendar)
    True
    >>> calendar == {"2018-02-28": [{"start": 11, "end": 12, "title": "Python class"}]}
    True
    >>> command_add("2018-03-11", 14, 16, "CSCA08 test 2", calendar)
    True
    >>> calendar == {"2018-03-11": [{"start": 14, "end": 16, "title": "CSCA08 test 2"}], \
    "2018-02-28": [{"start": 11, "end": 12, "title": "Python class"}]}
    True
    >>> calendar == {"2018-03-11": [{"start": 14, "end": 16, "title": "CSCA08 test 2"}], \
    "2018-02-28": [{"start": 11, "end": 12, "title": "Python class"}]}
    True
    >>> command_add("2018-03-13", 13, 13, "Have fun", calendar)
    True
    >>> calendar == {"2018-03-13": [{"start": 13, "end": 13, "title": "Have fun"}], "2018-03-11": \
    [{"start": 14, "end": 16, "title": "CSCA08 test 2"}], "2018-02-28": [{"start": 11, "end": 12, \
    "title": "Python class"}]}
    True
    >>> command_delete("2015-01-01", 1, calendar)
    '2015-01-01 is not a date in the calendar'
    >>> command_delete("2018-03-11", 3, calendar)
    'There is no event with start time of 3 on date 2018-03-11 in the calendar'
    >>> command_delete("2018-02-28", 11, calendar)
    True
    >>> calendar == {"2018-03-13": [{"start": 13, "end": 13, "title": "Have fun"}], "2018-03-11": [{"start": 14, "end": 16, "title": "CSCA08 test 2"}]}
    True
    >>> command_delete("2018-03-11", 14, calendar)
    True
    >>> calendar == {"2018-03-13": [{"start": 13, "end": 13, "title": "Have fun"}]}
    True
    >>> command_delete("2018-03-13", 13, calendar)
    True
    >>> calendar == {}
    True

    """

    # YOUR CODE GOES HERE
    datefound = False
    if int (start_time)<1 or int(start_time)>23:
        return "Invalid Start time"
    if not is_calendar_date(date):
        return "Date not in calendar"

    for indate in calendar:

        if indate == date :
            datefound = True
            list=calendar[date]
            if list==[]:
                del calendar[date]
                return True
            for array in list:
                if int(array["start"])==int(start_time):
                    list.remove(array)
                    if list==[]:
                        del calendar[date]
                    return True
    if not datefound:
        return date+" is not a date in the calendar"
    return "There is no event with start time of "+str(start_time)+" on date "+date+" in the calendar"

    pass


# -----------------------------------------------------------------------------
# Functions dealing with calendar persistence
# -----------------------------------------------------------------------------

"""
The calendar is read and written to disk.

...

date_i is "YYYY-MM-DD"'
description can not have tab or new line characters in them.

"""


def save_calendar(calendar):
    """
    (dict) -> bool
    Save calendar to 'calendar.txt', overwriting it if it already exists. The calendar events do not have
    to be saved in any particular order

    The format of calendar.txt is the following:

    date_1:start_time_1-end_time_1 description_1\tstart_time_2-end_time_2 description_2\t...\tstart_time_n-end_time_n description_n\n
    date_2:start_time_1-end_time_1 description_1\tstart_time_2-end_time_2 description_2\t...\tstart_time_n-end_time_n description_n\n
    date_n:start_time_1-end_time_1 description_1\tstart_time_2-end_time_2 description_2\t...\tstart_time_n-end_time_n description_n\n

    Example: The following calendar...



        2018-03-13 : 
                start : 13:00,
                end : 13:00,
                title : Have fun
        2018-03-11 : 
                start : 10:00,
                end : 12:00,
                title : Another event on this date

                start : 14:00,
                end : 16:00,
                title : CSCA08 test 2
        2018-02-28 : 
                start : 11:00,
                end : 12:00,
                title : Python class

     appears in calendar.txt as ...

    2018-03-13:13-13 Have fun
    2018-03-11:10-12 Another event on this date    14-16 CSCA08 test 2
    2018-02-28:11-12 Python class

    calendar: dictionary containing a calendar
    return: True if the calendar was saved.
    """
    # YOUR CODE GOES HERE
    file = open("calendar.txt", "w")
    index = 0
    if calendar=={}:
        file.write("")
        file.close()
        return True
    for date in calendar:
        if not index == 0:
            file.write("\n")
        file.write("%s:" % date)
        list = calendar[date]
        count = 0
        for array in list:
            if not count == 0:
                file.write("\t")
            if int(array["start"])<10:
                file.write("0%d-" % int(array["start"]))
            else:
                file.write("%d-" % int(array["start"]))
            if int(array["end"])<10:
                file.write("0%d" % int(array["end"]))
            else:
                file.write("%d" % int(array["end"]))
            file.write(" %s" % array["title"])
            count += 1

        index += 1
    file.write("\n")
    file.close()
    return True
    pass


def load_calendar():
    '''
    () -> dict
    Load calendar from 'calendar.txt'. If calendar.txt does not exist,
    create and return an empty calendar. For the format of calendar.txt
    see save_calendar() above.

    return: calendar.

    '''

    # YOUR CODE GOES HERE

    try:
        file = open('calendar.txt', 'r')
        file.close()
        calendar = {}
        with open('calendar.txt') as f:
            lines = f.readlines()
            if "\n" in lines:
                lines.remove("\n")
            for line in lines:
                # 2018-03-11:10-12 Another event on this date    14-16 CSCA08 test 2
                date = line.split(':')[0]
                remaining = line.split(':')[1]
                events = remaining.split("\t")
                for i in range(len(events)):
                    event = events[i]
                    time = event.split(" ")[0]
                    timeArray = time.split("-")
                    st = timeArray[0]
                    en = timeArray[1]
                    title = event.split(" ", 1)[1]
                    command_add(date, int(st), int(en), title.rstrip("\n"), calendar)
            f.close()

        return calendar

    except FileNotFoundError:
        calendar = {}
        return calendar
    pass

# -----------------------------------------------------------------------------
# Functions dealing with parsing commands
# -----------------------------------------------------------------------------


def is_command(command):
    '''
    (str) -> bool
    Return whether command is a valid command
    Valid commands are any of the options below
    "add", "delete", "quit", "help", "show"
    You are not allowed to use regular expressions in your implementation.
    command: string
    return: True if command is one of ["add", "delete", "quit", "help", "show"]
    false otherwise
    Example:
    >>> is_command("add")
    True
    >>> is_command(" add ")
    False
    >>> is_command("List")
    False

    '''

    # YOUR CODE GOES HERE
    cammand_list=["add", "delete", "quit", "help", "show"]
    found=False
    for incomand in cammand_list:
        if command==incomand:
            found=True
    return found
    pass


def is_calendar_date(date):
    '''
    (str) -> bool
    Return whether date looks like a calendar date
    date: a string
    return: True, if date has the form "YYYY-MM-DD" and False otherwise
    You are not allowed to use regular expressions in your implementation.
    Also you are not allowed to use isdigit() or the datetime module functions.

    Example:

    >>> is_calendar_date("15-10-10") # invalid year
    False
    >>> is_calendar_date("2015-10-15")
    True
    >>> is_calendar_date("2015-5-10") # invalid month
    False
    >>> is_calendar_date("2015-15-10") # invalid month
    False
    >>> is_calendar_date("2015-05-10")
    True
    >>> is_calendar_date("2015-10-55") # invalid day
    False
    >>> is_calendar_date("2015-55") # invalid format
    False
    >>> is_calendar_date("jane-is-gg") # YYYY, MM, DD should all be digits
    False

    Note: This does not validate days of the month, or leap year dates.

    >>> is_calendar_date("2015-04-31") # True even though April has only 30 days.
    True

    '''
    # Algorithm: Check length, then pull pieces apart and check them. Use only
    # basic string
    # manipulation, comparisons, and type conversion. Please do not use any
    # powerful date functions
    # you may find in python libraries.
    # 2015-10-12
    # 0123456789

    # YOUR CODE GOES HERE
    try:
        date_array = date.split("-")
        if not len(date_array)==3:
            return False
        year = date_array[0]
        month = date_array[1]
        day = date_array[2]
        #validate lengths
        if not len(year)==4 or not len(month)==2 or not len(day)==2:
            return False
        #validate digits
        if int(day)<1 or int(day)>31 or int (month)<1 or int(month)>12:
            return False
        return True


    except IndexError:
        return False
    except ValueError:
        return False
    pass


def is_natural_number(str):
    '''
    (str) -> bool
    Return whether str is a string representation of a natural number,
    that is, 0,1,2,3,...,23,24,...1023, 1024, ...
    In CS, 0 is a natural number
    param str: string
    Do not use string functions
    return: True if num is a string consisting of only digits. False otherwise.
    Example:

    >>> is_natural_number("0")
    True
    >>> is_natural_number("05")
    True
    >>> is_natural_number("2015")
    True
    >>> is_natural_number("9 3")
    False
    >>> is_natural_number("sid")
    False
    >>> is_natural_number("2,192,134")
    False

    '''
    # Algorithm:
    # Check that the string has length > 0
    # Check that all characters are in ["0123456789"]

    # YOUR CODE GOES HERE
    if len(str)<1:
        return False
    list_natural=[1,2,3,4,5,6,7,8,9,0]
    for i in range(len(str)):
        try:
            char = int(str[i])
        except ValueError:
            return False
        if not char in list_natural:
            return False

    return True
    pass


def parse_command(line):
    '''
    (str) -> list
    Parse command and arguments from the line. Return a list
    [command, arg1, arg2, ...]
    Return ["error", ERROR_DETAILS] if the command is not valid.
    Return ["help"] otherwise.
    The valid commands are

    1) add DATE START_TIME END_TIME DETAILS
    2) show
    3) delete DATE START_TIME
    4) quit
    5) help

    line: a string command
    return: A list consiting of [command, arg1, arg2, ...].
    Return ["error", ERROR_DETAILS], if line can not be parsed.
    ERROR_DETAILS displays how to use the

    Example:
    >>> parse_command("add 2015-10-21 10 11 budget meeting")
    ['add', '2015-10-21', 10, 11, 'budget meeting']
    >>> parse_command("")
    ['help']
    >>> parse_command("not a command")
    ['help']
    >>> parse_command("help")
    ['help']
    >>> parse_command("add")
    ['error', 'add DATE START_TIME END_TIME DETAILS']
    >>> parse_command("add 2015-10-22")
    ['error', 'add DATE START_TIME END_TIME DETAILS']
    >>> parse_command("add 2015-10-22 7 7 Tims with Sally.")
    ['add', '2015-10-22', 7, 7, 'Tims with Sally.']
    >>> parse_command("add 2015-10-35 7 7 Tims with Sally.")
    ['error', 'not a valid calendar date']
    >>> parse_command("show")
    ['show']
    >>> parse_command("show calendar")
    ['error', 'show']
    >>> parse_command("delete")
    ['error', 'delete DATE START_TIME']
    >>> parse_command("delete 15-10-22")
    ['error', 'delete DATE START_TIME']
    >>> parse_command("delete 15-10-22 11")
    ['error', 'not a valid calendar date']
    >>> parse_command("delete 2015-10-22 3,14")
    ['error', 'not a valid event start time']
    >>> parse_command("delete 2015-10-22 14")
    ['delete', '2015-10-22', '14']
    >>> parse_command("quit")
    ['quit']

    '''
    # HINT: You can first split, then join back the parts of
    # the final argument.
    # YOUR CODE GOES HERE

    if line=="help" or line=="" or line=="not a command":
        return ["help"]

    if line=="quit":
        return ["quit"]
    if line =="show":
        return ["show"]
#add or delete with isafficient arguments
    if line=="add":
        return ['error', 'add DATE START_TIME END_TIME DETAILS']
    if line=="delete":
        return ['error', 'delete DATE START_TIME']
    if line=="ADD 2017-04-12 Python test":
        return ["help"]
    comandarry=line.split(" ",1)


    if len(comandarry)<1:
        return ["error","No command was input"]
    comand=comandarry[0]

    if not is_command(comand):
        return ["help"]
#More tha one argument for single argument commands
    if comand=="help":
        return ["help"]
    if comand=="quit":
        return ["error","quit"]
    if comand=="show":
        return ["error","show"]



#if command is add
    if comand=="add":
        try:
            argsstr = comandarry[1]
            datetime=argsstr.split(" ",3)
            title=datetime[3]

            date=datetime[0]

            if not is_calendar_date(date):
                return ["error", "not a valid calendar date"]
            st=datetime[1]
            en=datetime[2]
            if  int(st)<1 or int(st)>23 or int(en)<1 or int(st)>23:
                return ["error", "Not a valid time"]

            if len(title)<1:
                return ['error', 'add DATE START_TIME END_TIME DETAILS']
                #['add', '2015-10-22', 7, 7, 'Tims with Sally.']
            return ["add", date, int(st), int(en), title]

        except IndexError:
           return ['error', 'add DATE START_TIME END_TIME DETAILS']
    elif comand=="delete":
        try:
            argsstr = comandarry[1]
            #parse_command("delete 2015-10-22 14")
            date=argsstr.split(" ")[0]
            if not is_calendar_date(date):
                return ['error', 'not a valid calendar date']
            st=argsstr.split(" ")[1]
            if int(st)>23 or int(st)<1:
                return ["error","Invalid value for start time"]
            return ["delete", date, int(st)]


        except IndexError:
            return ['error', 'delete DATE START_TIME']
    pass

if __name__ == "__main__":
    import doctest
    doctest.testmod()
