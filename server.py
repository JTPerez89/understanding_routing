from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/dojo')
def say_dojo():
    return 'Dojo!'

@app.route('/say/<string:name>')

def say(name):
    if name.isalpha():
        return 'Hi ' + name + '!'
    else:
        return 'Improper input'

@app.route('/repeat/<num>/<input>')

def repeat(num, input):
    if input.isalpha() & num.isdigit():
        return f'<p>{input}</p>' * int(num)
    else:
        return 'Improper input'


@app.route('/<path:path>')

def wrong_route(path):
    return 'Sorry! No response. Try again.'





















    
if __name__=="__main__":
    app.run(debug=True)