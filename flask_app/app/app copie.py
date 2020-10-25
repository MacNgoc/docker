from flask import Flask, request, jsonify, render_template

import mysql.connector




app = Flask(__name__)



connection = mysql.connector.connect( user = 'root', password = 'Abc123az', db = 'db_flask')

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == "POST":
        data = request.form
        first_name = data['fname']
        last_name = data['lname']
        cursor = connection.cursor()
        cursor.execute("INSERT INTO user(lastname, firstname) VALUES (%s, %s)", (last_name, first_name))
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
    app.run(debug=True)
    #app.run(debug=True)