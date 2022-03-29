days_of_months = [31,28,31,30,31,30,31,31,30,31,30,31]
days_in_standard_year = sum(days_of_months)

def isLeapYear(year):
    if year % 4 != 0:
        return False
    elif year % 100 != 0:
        return True
    elif year % 400 != 0:
        return False
    else:
        return True

def nextDay(year, month, day):
    """Simple version: assume every month has 30 days"""
    len_month = days_of_months[month-1] # we're going to pretend the list is 1-indexed
    if month == 2 and isLeapYear(year):
        len_month += 1
    if day < len_month:
        return year, month, day + 1
    else:
        if month == 12:
            return year + 1, 1, 1
        else:
            return year, month + 1, 1
        
def dateIsBefore(year1, month1, day1, year2, month2, day2):
    """Returns True if year1-month1-day1 is before
       year2-month2-day2. Otherwise, returns False."""
    if year1 < year2:
        return True
    if year1 == year2:
        if month1 < month2:
            return True
        if month1 == month2:
            return day1 < day2
    return False

def daysBetweenDates(year1, month1, day1, year2, month2, day2):
    """Returns the number of days between year1/month1/day1
       and year2/month2/day2. Assumes inputs are valid dates
       in Gregorian calendar."""
    # program defensively! Add an assertion if the input is not valid!
    assert not dateIsBefore(year2, month2, day2, year1, month1, day1)

    days = 0
    while dateIsBefore(year1, month1, day1, year2, month2, day2):
        year1, month1, day1 = nextDay(year1, month1, day1)
        days += 1
    return days   

def testDaysBetweenDates():
    assert isLeapYear(1996)
    assert not isLeapYear(1996 + 1)
    assert isLeapYear(2000)
    assert not isLeapYear(2000 + 1)
    assert isLeapYear(2004)

    # test same day
    assert(daysBetweenDates(2017, 12, 30, 2017, 12, 30) == 0)
    # test adjacent days
    assert(daysBetweenDates(2017, 12, 30,  2017, 12, 31) == 1)
    # test new year
    assert(daysBetweenDates(2017, 12, 30,  2018, 1,  1)  == 2)
    # test full year difference
    assert(daysBetweenDates(2012, 6, 29, 2013, 6, 29)  == 365)
    
    print("Congratulations! Your daysBetweenDates")
    print("function is working correctly!")
    
testDaysBetweenDates()