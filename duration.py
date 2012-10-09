'''
Created on Oct 9, 2012

@author: timo
'''
from datetime import timedelta
import math

def duration(value, arg = "%h:%m"):
    """
    Renders a timedelta in human-readable format. Each format identifier is
    preceded by a '%' and is one of:

    s -- seconds, 00...59
    S -- seconds, integer, values > 59 possible
    m -- minutes, 00...59
    M -- minutes, integer, values > 59 possible
    h -- hours, 0...23
    H -- hours, integer, values > 23 possible
    o -- hours, 2 decimals, 0...23.99
    O -- hours, 2 decimals, values > 23 possible
    D -- days, integer
    """
    
    # Fail silently if the value is not a timedelta.
    if not isinstance(value, timedelta):
        return ""
    
    # Dissect value
    totalSeconds = (value.microseconds + (value.seconds + value.days * 24 * 3600) * 10**6) / float(10**6)
    totalDays, remainder = divmod(totalSeconds, 86400)
    modHours, remainder = divmod(remainder, 3600)
    modMinutes, modSeconds = divmod(remainder, 60)
    totalHours = math.floor(totalSeconds / 3600)
    totalMinutes = math.floor(totalSeconds / 60)

    # Pass 1: Determine which is the smallest unit we have to display
    awaitingFormatIdentifier = False
    seconds_smallest_unit = minutes_smallest_unit = hours_smallest_unit = days_smallest_unit = False
    for c in arg:
        if c == "%":
            if awaitingFormatIdentifier:
                awaitingFormatIdentifier = False
            else:
                awaitingFormatIdentifier = True
        else:
            if awaitingFormatIdentifier:
                if c == "s"or c == "S":
                    seconds_smallest_unit = True
                    minutes_smallest_unit = hours_smallest_unit = days_smallest_unit = False
                elif c == "m" or c == "M":
                    minutes_smallest_unit = not seconds_smallest_unit
                    hours_smallest_unit = days_smallest_unit = False
                elif c == "h" or c == "H" or c == "o" or c == "O":
                    hours_smallest_unit = not minutes_smallest_unit and not seconds_smallest_unit
                    days_smallest_unit = False
                elif c == "D":
                    days_smallest_unit = not hours_smallest_unit and not minutes_smallest_unit and not seconds_smallest_unit
                else:
                    pass
                awaitingFormatIdentifier = False
            else:
                pass
    
    print("seconds_smallest_unit: " + str(seconds_smallest_unit))
    print("minutes_smallest_unit: " + str(minutes_smallest_unit))
    print("hours_smallest_unit: " + str(hours_smallest_unit))
    print("days_smallest_unit: " + str(days_smallest_unit))
    
    # Pass 2: Assemble the output
    niceOutput = ""
    awaitingFormatIdentifier = False
    for c in arg:
        if c == "%":
            if awaitingFormatIdentifier:
                niceOutput = niceOutput + "%"
                awaitingFormatIdentifier = False
            else:
                awaitingFormatIdentifier = True
        else:
            if awaitingFormatIdentifier:
                if c == "s":
                    niceOutput = niceOutput + ("%02d" % modSeconds)
                elif c == "S":
                    niceOutput = niceOutput + ("%02d" % totalSeconds)
                elif c == "m":
                    niceOutput = niceOutput + ("%02d" % modMinutes)
                elif c == "M":
                    niceOutput = niceOutput + ("%02d" % totalMinutes)
                elif c == "h":
                    niceOutput = niceOutput + str(int(modHours))
                elif c == "H":
                    niceOutput = niceOutput + str(int(totalHours))
                elif c == "o":
                    decimalModHours = modHours + (modMinutes / 60)
                    niceOutput = niceOutput + ("%.2f" % decimalModHours)
                elif c == "O":
                    decimalTotalHours = totalHours + (modMinutes / 60)
                    niceOutput = niceOutput + ("%.2f" % decimalTotalHours)
                elif c == "D":
                    niceOutput = niceOutput + str(int(totalDays))
                else:
                    pass
                awaitingFormatIdentifier = False
            else:
                niceOutput = niceOutput + c
    return niceOutput

td1 = timedelta(1, 3631)
# print(duration(td1, " %m %h %S  %M %H %O"))
print(duration(td1))
