from datetime import datetime
import random
from flask import Flask, render_template, redirect, request, url_for
app = Flask(__name__)

# initialize global variables
account_value = 0
account_history = []

# method to update the account value and history with inputs result (response from form) and gold value (random int based on building type)
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
        date=datetime.utcnow().strftime('%Y/%m/%d %I:%M %p')
    ))

# base route where all requests redirected
@app.route('/')
def index():
    global account_value, account_history
    return render_template('home.html', account_value=account_value, account_history=account_history)

# POST request made when the "Find Gold!" button is clicked
@app.route('/process_money', methods=['POST'])
def process_money():
    # grab the value of the form's building type
    result = request.form['building']
    value = 0
    # for each bulding type, assign a gold value based on the defined limits and add to the account_value or account_history
    if result == 'farm':
        value = random.randint(10,20)
        update_account(result, value)
    elif result == 'cave':
        value = random.randint(5,10)
        update_account(result, value)
    elif result == 'house':
        value = random.randint(2,5)
        update_account(result, value)
    elif result == 'casino':
        value = random.randint(0,50)*[-1,1][random.randrange(2)]
        update_account(result, value)
    # redirect to '/' instead of staying at '/process_money'
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run()