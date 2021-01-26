from flask_api import FlaskAPI
from getTime import getTime
from flasgger import Swagger
from flasgger.utils import swag_from

app = FlaskAPI(__name__)

@app.route('/time/', methods=['GET'])
@swag_from('./time.yml') # http://localhost:5000/apidocs/
def time():
    return { 'time': getTime()}

swag = Swagger(app)

if __name__ == "__main__":
    app.run(debug=True)