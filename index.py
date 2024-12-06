# import main Flask class and request object
from flask import Flask, request
from celeste import input_data

# create the Flask app
app = Flask(__name__)

# GET requests will be blocked
@app.route('/celeste', methods=['POST'])
def json_example():
    try:
        request_data = request.get_json()
        message = None
        if request_data:
            if 'message' in request_data:
                message = request_data['message']
                result = input_data(message)
            return { 'message' : result }
        return { 'message' : 'Ops! No hay mensajes para responder.' }
    except Exception as e:
        return { 'error' : str(e) }

if __name__ == '__main__':
    # run app in debug mode on port 5000
    app.run(debug=True, port=8080)