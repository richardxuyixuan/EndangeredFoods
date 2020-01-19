from flask import Flask
from datetime import datetime
from expiryDate import checkExpiries, findExpiryTime
import json

def readFile():
    with open('foodData.txt', 'r', encoding="utf-8") as f:
        foodData = json.load(f)
    #getFoodData=file.read()
    #checkIfExpired(getFoodData)
    #sortAccordingToDate(getFoodData)
    i=0
    foodList=[]
    for x in foodData:
        foodList+=[[x["name"],x["date"],x["quantity"],x["calories"]]]
    return(foodList)

foodList = readFile()
def addFood(file):
    #[[name, date, quantity, calories]]
    open("dataStorage.txt", "w+", encoding="utf-8")
    currentFile = open("dataStorage.txt", "r", encoding="utf-8")
    currentDataList = []
    for entry in currentFile.readlines():
        finalList = []
        entryList = entry.split(",")
        for listPart in entryList:
            finalList.append(listPart.strip("[]\' \n"))  
        currentDataList.append(finalList)
    updateFile = open(str(file), "r", encoding="utf-8")
    updateData = json.load(updateFile)
    for food in updateData["entries"]:
        entry = [food["name"], food["date"], food["quantity"], food["calories"]]
        terminate = False
        for listValue in currentDataList:
            if entry[0] == listValue[0]:
                terminate = True
                break
            else:
                continue
        if terminate:
            continue
        else:
            currentDataList.append(entry)
    writing = open("dataStorage.txt", "w", encoding="utf-8")
    for update in currentDataList:
        writing.write(str(update)+"\n")

addFood('response.txt')


def expiryList():
    outputDic = {'entries': []}
    for food in foodList:
        if checkExpiries(food[1]):
            entryDic = {'name': food[0], 'date': food[1], 'quantity': food[2], 'calories': food[3]}
            outputDic['entries'].append(entryDic)
            jsonOut = json.dumps(outputDic)
    return(jsonOut)

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
