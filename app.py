import yfinance as yf
from flask import request, render_template, jsonify, Flask

app = Flask(__name__ template_folder='templates')


@app.route('/')
def index(): 
    return render_template('index.html')

@app.route(rule: '/get_stock_data', methods=['POST'])