from flask import Flask, render_template, request
from pusher import Pusher

app = Flask(__name__)

# Configure pusher object
pusher = Pusher(
    app_id = '925719',
    key = 'e423ec274d580b43c247',
    secret = 'd3381851e78bc974115e',
    cluster = 'ap2',
    ssl = True
)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')

@app.route('/order', methods=['POST'])
def order():
    data = request.form
    pusher.trigger(u'order', u'place', {u'units': data['units']
    })
    return "units logged"    

@app.route('/message', methods=['POST'])
def message():
    data = request.form
    pusher.trigger(u'message', u'send', {
        u'name': data['name'],
        u'message': data['message']
    })
    return "message sent"

@app.route('/customer', methods=['POST'])
def customer():
    data = request.form
    pusher.trigger(u'customer', u'add', {
        u'name': data['name'],
        u'position': data['position'],
        u'office': data['office'],
        u'age': data['age'],
        u'salary': data['salary']
    })
    return "customer added"

if __name__ == '__main__':
    app.run(debug=True)