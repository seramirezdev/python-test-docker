from flask import Flask, jsonify
from users import usersList

app = Flask(__name__)

@app.route('/', methods=['GET'])
def ping():
    return jsonify({"response": "Hello World"})

@app.route('/users')
def usersHandlet():
    return jsonify({"users": usersList})

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=4000, debug=True)



