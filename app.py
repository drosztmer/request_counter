from flask import Flask, render_template, request, redirect
app = Flask(__name__)


count_get = 0
count_post = 0
count_delete = 0
count_put = 0


@app.route('/')
def route_index():
    return render_template('index.html')

@app.route('/request-counter', methods=['GET', 'POST', 'DELETE', 'PUT'])
def request_counter():
    if request.method == 'POST':
        global count_post
        count_post += 1
    elif request.method == 'GET':
        global count_get
        count_get += 1
    elif request.method == 'DELETE':
        global count_delete
        count_delete += 1
    elif request.method == 'PUT':
        global count_put
        count_put += 1
    return redirect('/')

@app.route('/statistics')
def statistics():
    return render_template('statistics.html', count_post=count_post,
                           count_get=count_get, count_delete = count_delete, count_put=count_put)