import os
import hardwareSet
from flask import Flask, send_from_directory

app = Flask(__name__, static_url_path='', static_folder='ui/build/')


proj_dict = {'a':hardwareSet.HWSet(250,'a'), 'b':hardwareSet.HWSet(350,'b'), 'c':hardwareSet.HWSet(50, 'c')}

@app.route('/')
def index():
    return send_from_directory('ui/build/', 'index.html')

@app.route('/test')
def test():
    return 'testing stupid app'

@app.route('/checkIn/<projectId>/<qty>')
def checkIn_hardware(projectId, qty):
    return '%s hardware checked in' %qty

@app.route('/checkOut/<projectId>/<qty>')
def checkOut_hardware(projectid, qty):
    return '%s hardware checked out' %qty

@app.route('/join/<projectId>')
def joinProject(projectId):
    return 'Joined %s' %projectId

@app.route('/leave/<projectId>')
def leaveProject(projectId):
    return 'Left %s' %projectId


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=False, port=os.environ.get('PORT', 80))