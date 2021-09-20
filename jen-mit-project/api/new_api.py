from flask import Flask, jsonify, render_template
import requests
import random

app = Flask(__name__, template_folder='../templates')
app.config["DEBUG"] = True


@app.route('/', methods=['GET'])
def getquotes():
    url = 'https://type.fit/api/quotes'
    r= requests.get(url)
    response = r.json()
    one = response[random.randint(0, len(response))]
    return render_template('index.html', content = one.get('text'))

app.run()
