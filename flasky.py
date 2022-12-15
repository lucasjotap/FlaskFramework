from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
	return '<h1>Hello World, this is a flask project!</h1>'
