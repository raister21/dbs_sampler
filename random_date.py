import time
import random
import string

date_dic = {1:"JAN", 2:"FEB", 3:"MAR", 4:"APR", 5:"MAY", 6:"JUN", 7:"JUL", 8:"AUG", 9:"SEPT", 10:"OCT",11:"NOV",12:"DEC"}

def str_time_prop(start, end, format, prop):
    """Get a time at a proportion of a range of two formatted times.

    start and end should be strings specifying times formated in the
    given format (strftime-style), giving an interval [start, end].
    prop specifies how a proportion of the interval to be taken after
    start.  The returned time will be in the specified format.
    """

    stime = time.mktime(time.strptime(start, format))
    etime = time.mktime(time.strptime(end, format))

    ptime = stime + prop * (etime - stime)

    return time.strftime(format, time.localtime(ptime))

def proper_date(date_obj):
    date_obj = date_obj.split('/')
    p_date = ""
    p_date =  date_obj[0] + "-" + date_dic[int(date_obj[1])] + "-" +  date_obj[2]

    return p_date    
        

def random_date(start, end, prop):
    date_output = str_time_prop(start, end, '%d/%m/%Y', prop)
    date_output = proper_date(date_output)

    return date_output



