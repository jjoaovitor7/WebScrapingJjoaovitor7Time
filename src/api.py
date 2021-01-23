from flask_api import FlaskAPI
from getTime import getTime

app = FlaskAPI(__name__)

@app.route('/time/', methods=['GET'])
def time():
    return { 'time': getTime()}

if __name__ == "__main__":
    app.run(debug=True)