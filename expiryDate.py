from datetime import datetime

def checkExpiries(exDate):
    datetimeExpiryDate = datetime.strptime(exDate, "%m/%d/%Y")
    if datetimeExpiryDate < datetime.now():
        return(True)
    else:
        return(False)

def findExpiryTime(exDate):
    datetimeExpiryDate = datetime.strptime(exDate, "%m/%d/%Y")
    timeDifference = datetimeExpiryDate-datetime.now()
    if timeDifference.days <= 5:
        return(str(timeDifference.days))
    else:
        return "0"