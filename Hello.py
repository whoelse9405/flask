from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!'

def hell_dj():
    return 'Hello DJ!'

if __name__ == '__main__':
    app.run()

