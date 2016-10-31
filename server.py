from flask import Flask, send_file, jsonify
import datetime
app = Flask(__name__)

@app.route('/')
def hello_world():
    return send_file('static/index.html')

@app.route('/api/v1/tasks')
def bleh():
    taskList = []
    for x in range(10):
        taskList += [{'Name': 'Dishes',
                      'DateTime': str(datetime.datetime.now() + datetime.timedelta(days=x)),
                      'Owner': 'Adam'}]

    return jsonify({'taskList':taskList})

if __name__ == "__main__":
    app.run(debug=True)
