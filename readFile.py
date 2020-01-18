import json

def readFile():
    with open('foodData.json', 'r') as f:
        foodData = json.load(f)
    #getFoodData=file.read()
    #checkIfExpired(getFoodData)
    #sortAccordingToDate(getFoodData)
    i=0
    foodList=[]
    for x in foodData:
        foodList+=[[x["Name"],x["Date"],x["Quantity"],x["Calories"]]]
    print(foodList)
    return True

readFile()
