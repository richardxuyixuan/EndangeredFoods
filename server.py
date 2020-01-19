from flask import Flask, request
from main import expiryList,limitedTimeFoods,change_dict_to_txt

app = Flask(__name__,
            static_url_path='', 
            static_folder='static',)

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
@app.route('/returnList',methods=['POST','GET'])
def return_list_data():
    #e_list = expiryList()
    selected_item_name = request.form.to_dict()
    change_dict_to_txt(selected_item_name)
    return selected_item_name


# send removefood list
@app.route('/removeList',methods=['POST','GET'])
def remove_list_data():
    #e_list = expiryList()
    selected_item_name = request.form.to_dict()
    change_dict_to_txt(selected_item_name)
    return selected_item_name

# root page
@app.route('/')
def index():
    return app.send_static_file("index.html")
    

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000)
