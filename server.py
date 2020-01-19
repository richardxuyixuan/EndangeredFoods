from flask import Flask, request
from main import *

app = Flask(__name__)

# send expiry list
@app.route('/elist',methods=['POST','GET'])
def send_elist_data():
    e_list = expiryList()
    return e_list

# send limited time food list
@app.route('/ltf',methods=['POST','GET'])
def send_ltf_data():
    ltf = limitedTimeFoods()
    return ltf

# send addFood list
@app.route('/returnList', methods=['POST','GET'])
def return_list_data():
    #e_list = expiryList()
    selected_item_name = request.form.to_dict()
    change_dict_to_txt(selected_item_name)
    return selected_item_name

#Get recipe request
@app.route('/getRecipe', methods=['POST', 'GET'])
def send_ingredients():
    response = request.form.to_dict()
    recipe = getRecipe(response)
    print(recipe)
    return recipe

# send removefood list
@app.route('/removeList',methods=['POST','GET'])
def remove_list_data():
    #e_list = expiryList()
    print('inside remove list')
    selected_item_name = request.form.to_dict()
    print('form data is', selected_item_name)
    removeFood(selected_item_name['name'], selected_item_name['quantity'])
    return selected_item_name

# root page
@app.route('/')
def index():
    return app.send_static_file("index.html")
    

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000)