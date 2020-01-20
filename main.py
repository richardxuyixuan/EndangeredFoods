from datetime import datetime
from expiryDate import checkExpiries, findExpiryTime
import json
import requests

#Reads file, simples
def readFile():
    with open('dataStorage.txt', 'r+', encoding="utf-8") as f:
        foodList = []
        for line in f:
            foodList.append(eval(line))
        return foodList

#Removes a quantity of food, deletes if quantity <= 0
def removeFood(name, quantity):
    open("dataStorage.txt", "w", encoding="utf-8")
    with open('dataStorage.txt', 'r+', encoding="utf-8") as f:
        foodList = []
        for line in f:
            foodList.append(eval(line))
        for food in foodList:
            if food[0] == name:
                newQuant = int(food[2]) - quantity
                indexPos = foodList.index(food)
                if newQuant > 0:
                    foodList[indexPos] = [food[0], food[1], newQuant, food[3], food[4]]
                else:
                    del foodList[indexPos]
            else:
                continue
    o = open("dataStorage.txt", "w", encoding="utf-8")
    for food in foodList:
        o.write(str(food) + "\n")


def addFood(file):
    #Copying the data stored into a list
    open("dataStorage.txt", "a", encoding="utf-8")
    currentFile = open("dataStorage.txt", "r+", encoding="utf-8")
    finalList = []
    currentDataList = []
    for entry in currentFile.readlines():
        currentDataList.append(eval(entry))

    #Adding new foods to current list
    updateFile = open(str(file), "r", encoding="utf-8")
    updateData = json.load(updateFile)
    for food in updateData["entries"]:
        #Preventing duplicates
        entry = [food["name"], food["date"], food["quantity"], food["calories"], food["pic"]]
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
            finalList.append(entry)

    #Output
    with open("dataStorage.txt", "a", encoding="utf-8") as myFile:
        for update in finalList:
            myFile.write(str(update)+"\n")

#Returns list of expired food
def expiryList():
    foodList = readFile() 
    outputDic = {'entries': []}
    for food in foodList:
        if checkExpiries(food[1]):
            entryDic = {'name': food[0], 'date': food[1], 'quantity': food[2], 'calories': food[3], 'pic': food[4]}
            outputDic['entries'].append(entryDic)
            jsonOut = json.dumps(outputDic)
    return(jsonOut)

#Accepting json request to add specific food object
def change_dict_to_txt(jsonObject):
    jsonArray = {"entries": [jsonObject]}
    with open('json_return_data.txt', 'w', encoding="utf-8") as outfile:
      json.dump(jsonArray, outfile)
    addFood('json_return_data.txt')
    return jsonObject

#Returns list of foods about to expire, and expired foods
def limitedTimeFoods():
    foodList = readFile()
    outputDic = {'entries': []}
    for food in foodList:
        if (int(findExpiryTime(food[1])) <= 5):
            if checkExpiries(food[1]):
                entryDic = {'name': food[0], 'timeLeft': 'Expired'}
            else:
                entryDic = {'name': food[0], 'timeLeft': findExpiryTime(food[1])}
        else:
            continue
        outputDic['entries'].append(entryDic)
        jsonOut = json.dumps(outputDic)
    return(jsonOut)

#Function that uses spoonacular's API to return a recipe when given a list of food names
def getRecipe(clientRequest):
    ingredients = ""
    ingredientList = [clientRequest["name"]]
    for food in ingredientList:
        if ingredientList.index(food) == 0:
            ingredients += str(food)
        else:
            ingredients +=  (", + " + str(food))    
    response = requests.get("https://api.spoonacular.com/recipes/findByIngredients?apiKey=50bc728be7ce4ce2a00c793ff7baa63e&ingredients="+ingredients+"&number=1&ignorePantry=true")
    recipeData={"name": response.json()[0]['title'], "url": response.json()[0]['image'], "quantity": response.json()[0]['usedIngredientCount']}
    recipeDataTheOtherHalf=[]
    return recipeData