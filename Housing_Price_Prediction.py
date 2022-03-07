from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/hello')
def hello():
    return 'Hello World!'



# https://github.com/RubixML/Housing/blob/master/data_description.txt

if __name__ == '__main__':
    app.run()
