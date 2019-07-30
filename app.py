from flask import Flask, render_template, request, redirect
app = Flask(__name__)


count_get = 0
count_post = 0


@app.route('/')
def route_index():
    return render_template('index.html')

@app.route('/request-counter', methods=['GET', 'POST'])
def request_counter():
    if request.method == 'POST':
        global count_post
        count_post += 1
    else:
        global count_get
        count_get += 1
    return redirect('/')

@app.route('/statistics')
def statistics():
    return render_template('statistics.html')