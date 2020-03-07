def isYearLeap(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                
                return True
                
            else:
                return False
        else:
            
            return True
        
    else:
       return False
Months31=[1,3,5,7,8,10,12]
Months30=[4,6,9,11]
def daysInMonth(year, month):
    if month<1 or month>12:
        return None
    elif month in Months31:
        return 31
    elif month in Months30:
        return 30
    elif isYearLeap(year)==True and month==2:
        return 29
    else:
        return 28


total_days=[]
def dayOfYear(year, month, day):
    #current_day_in_month=daysInMonth(year,month)-day-1
    #return current_day_in_month
    if day<1 and day>31:
        print("Day is wrong")
    for j in range(month,0,-1):
        x=daysInMonth(year, month-j)
        total_days.append(x)
    total_days.append(day)
    del total_days[0]
    print(total_days)
    print(sum(total_days))
    return ""
    
    
print(dayOfYear(2019,3,2))

"""
testYears = [1900, 2000, 2016, 1987]
testMonths = [2, 2, 1, 11]
testResults = [28, 29, 31, 30]
for i in range(len(testYears)):
	yr = testYears[i]
	mo = testMonths[i]
	print(yr, mo, "->", end="")
	result = daysInMonth(yr, mo)
	if result == testResults[i]:
		print("OK")
	else:
		print("Failed")
"""
