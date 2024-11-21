from flask import Flask, jsonify, request

app = Flask(__name__)


@app.route('/hello', methods=['GET'])
def helloworld():
	if(request.method == 'GET'):
		data = {"data": "Hello World!"}
		return jsonify(data)

@app.route('/')
def base():
    return 'Hello world'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=9001)