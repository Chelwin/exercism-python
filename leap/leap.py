def is_leap_year(year):
    #on every year that is evenly divisible by 4
    #except every year that is evenly divisible by 100
    #unless the year is also evenly divisible by 400
    leap = False

    try:
        if (year%4)==0 and not((year%100)==0):
            leap = True
        elif (year%4)==0 and (year%400)==0:
            leap = True
    except:
        raise Exception("Bad Argument: accept ints only") 
    return leap

