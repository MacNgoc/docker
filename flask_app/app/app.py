from flask import Flask, request, jsonify, render_template

import mysql.connector

import time


time.sleep(5)


app = Flask(__name__)


connection = mysql.connector.connect( host='mysql-product', port= '3306', user = 'root', password = 'Abc123az',\
                                        database = 'db_flask', auth_plugin='mysql_native_password')

# For connect to mysql server from this container, we have to be careful about some parameters:
# 1) "host" is container-name of mysql, 
# 2) "port" by defaut is 3306
# 3) auth_plugin for the new version of mysql (8.0)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == "POST":
        data = request.form
        first_name = data['fname']
        last_name = data['lname']
        print("fist name", first_name)
        print("last name", last_name)
        cursor = connection.cursor()
        cursor.execute("INSERT INTO user (lastname, firstname) VALUES (%s, %s)", (last_name, first_name))
        print("it has been executed")
        connection.commit()

        cursor.close()
        
        return 'Success'

    return render_template('index.html')


@app.route('/predict', methods=['POST'])

def predict():
    recieved_value = request.get_json()
    print("Here recieved-value", recieved_value)
    if recieved_value and 'data' in recieved_value:
        data = recieved_value['data']
    else:
        data = "There's nothing in data"
    return jsonify(str(data))






if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
    #app.run(debug=True)