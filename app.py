from datetime import datetime
import math
import random
import numpy as np
from flask import Flask, render_template, redirect, request, url_for
app = Flask(__name__)

account_value = 0
account_history = []

def update_account(result, value):
    global account_value, account_history
    temp = account_value
    account_value += value

    if value < 0 and account_value < 0:
        value = temp*(-1)
        account_value = 0

    account_history.append(dict(
        result=result,
        value=value,
        date=datetime.utcnow()
    ))


@app.route('/', methods=['GET'])
def index():
    global account_value, account_history
    print('History: ', account_history)
    return render_template('home.html', account_value=account_value, account_history=account_history)

@app.route('/process_money', methods=['POST'])
def process_money():
    result = request.form['building']
    value = 0
    if result == 'farm':
        value = random.randint(10,20)
        print(value)
        update_account(result, value)
    elif result == 'cave':
        value = random.randint(5,10)
        print(value)
        update_account(result, value)
    elif result == 'house':
        value = random.randint(2,5)
        print(value)
        update_account(result, value)
    elif result == 'casino':
        value = random.randint(0,50)*[-1,1][random.randrange(2)]
        print(value)
        update_account(result, value)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)