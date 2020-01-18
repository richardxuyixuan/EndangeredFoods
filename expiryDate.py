from datetime import datetime

def checkExpiries(exDate):
    datetimeExpiryDate = datetime.strptime(exDate, "%m/%d/%Y")
    if datetimeExpiryDate < datetime.now():
        return(True)
    else:
        return(False)