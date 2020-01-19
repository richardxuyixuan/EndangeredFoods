from flask import Flask
from datetime import datetime
from expiryDate import checkExpiries, findExpiryTime
import json

def readFile():
    with open('foodData.txt', 'r') as f:
        foodData = json.load(f)
    #getFoodData=file.read()
    #checkIfExpired(getFoodData)
    #sortAccordingToDate(getFoodData)
    i=0
    foodList=[]
    for x in foodData:
        foodList+=[[x["Name"],x["Date"],x["Quantity"],x["Calories"]]]
    return(foodList)

foodList = readFile()
print(foodList)

def expiryList():
    outputDic = {'entries': []}
    for food in foodList:
        if checkExpiries(food[1]):
            entryDic = {'name': food[0], 'date': food[1], 'quantity': food[2], 'calories': food[3]}
            outputDic['entries'].append(entryDic)
            jsonOut = json.dumps(outputDic)
    return(jsonOut)

print("expiry List \n\n\n")
print(expiryList())

def limitedTimeFoods():
    outputDic = {'entries': []}
    for food in foodList:
        if checkExpiries(food[1]):
            entryDic = {'name': food[0], 'timeLeft': 'Expired'}
        else:
            entryDic = {'name': food[0], 'timeLeft': findExpiryTime(food[1])}
        outputDic['entries'].append(entryDic)
        jsonOut = json.dumps(outputDic)
    return(jsonOut)
print("limited time Foods \n\n\n")
print(limitedTimeFoods())