from collections import namedtuple
from flask import Flask, render_template, redirect, url_for, request
from random import randint


app = Flask(__name__)
show = namedtuple('show', 'ad soyad')

messages = []
messages2 = []
a="Huh.You lose.My number is greater than yours."
b="Wow.You win.Your number is greater than mine."
c="A tie!"

@app.route('/', methods=['GET'])
def hello_world():
    return render_template('index.html')


@app.route('/main', methods=['GET'])
def main():
    return render_template('main.html', messages=messages)


@app.route('/introduce', methods=['POST'])
def introduce():
    if len(messages)>0:
        messages.clear()
    ad = request.form['ad']
    soyad = request.form['soyad']
    messages.append(show(ad, soyad))
    return redirect(url_for('main'))
    

@app.route('/facts', methods=['GET'])
def facts():
    return render_template('citysfacts.html')


@app.route('/factsfind', methods=['POST'])
def facts2():
    text2 = request.form['text2']
    if text2=="Moscow":
        return moscow()
    elif text2=="Berlin":
        return berlin()
    elif text2=="Amsterdam":
        return amsterdam()
    elif text2=="Jerusalem":
        return jerusalem()

    
@app.route('/moscow', methods=['GET'])
def moscow():
    return render_template('Moscow.html')

@app.route('/berlin', methods=['GET'])
def berlin():
    return render_template('Berlin.html')

@app.route('/amsterdam', methods=['GET'])
def amsterdam():
    return render_template('Amsterdam.html')

@app.route('/jerusalem', methods=['GET'])
def jerusalem():
    return render_template('Jerusalem.html')

@app.route('/random', methods=['GET'])
def random():
    return render_template('random.html',messages2=messages2)

@app.route('/add_num', methods=['POST'])
def add_num():
    if len(messages2)>0:
        messages2.clear()
    mynum=randint(0, 1000)
    yournum = request.form['yournum']
    if mynum>int(yournum):
        result=a
    if mynum==int(yournum):
        result=c
    if mynum<int(yournum):
        result=b
    Message2={
        'first':mynum,
        'second':yournum,
        'third':result
    }
    messages2.append(Message2)
    return redirect(url_for('random'))

if __name__=='__main__':
    app.run(debug=True)