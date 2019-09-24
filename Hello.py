from flask import Flask, redirect, url_for, request, render_template
app = Flask(__name__)

@app.route('/name/<other>')
def hello_world(other):
    return 'Hello %s!'% other

def hello_dj():
    return 'Hello DJ!!!!'

@app.route('/warn/<name>')
def hello(name):
    if name=='dongjin':
        return redirect(url_for('qwer'))
    else:
        return redirect(url_for('hello_world',other=name))

@app.route('/success/<name>')
def success(name):
    return 'welcome %s' % name

@app.route('/login', methods = ['POST', 'GET'])
def login():
    if request.method == 'POST':
        user = request.form['myName']
        return redirect(url_for('success', name=user))
    else:
        user = request.args.get('myName')
        return redirect(url_for('success', name=user))

@app.route('/<name>')
def index(name):
    return render_template('hello.html', name=name)


if __name__ == '__main__':
    app.add_url_rule('/dj', 'qwer', hello_dj)
    app.debug=True
    app.run()

