from flask import Flask, jsonify, request

app = Flask(__name__)

contacts = [
    {
        "Contact": "9987644456",
        "Name": "Raju",
        "done": False, 
        "id": 1  
    },
    {
        "Contact": "9876543222",
        "Name": "Rahul",
        "done": False, 
        "id": 2
    }
]

@app.route("/")
def hello_world():
    return "Hello World"

@app.route("/add-data", methods = ["POST"])
def add_task():
    if not request.json:
        return jsonify({
            "status": "error",
            "message": "Please provide the data!"
        }, 400)
        
    contact = {
        'Contact': request.json.get('Contact', ""),
        'Name': request.json['Name'],
        'done': False,
        'id': contacts[-1]['id'] + 1
    }
    contacts.append(contact)
    return jsonify({
        "status": "success",
        "message": "Task added succesfully!"
    })

@app.route("/get-data")
def get_task():
    return jsonify({
        "data": contacts
    })

if(__name__ == "__main__"):
    app.run(debug = True)