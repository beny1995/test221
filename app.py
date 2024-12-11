from flask import Flask, render_template
import requests
from datetime import datetime

app = Flask(__name__)

def get_btc_price():
    try:
        response = requests.get('https://api.coindesk.com/v1/bpi/currentprice.json')
        data = response.json()
        return {
            'price': data['bpi']['USD']['rate'],
            'updated': data['time']['updated']
        }
    except Exception as e:
        return {
            'price': 'Error fetching price',
            'updated': str(datetime.now())
        }

@app.route('/')
def home():
    btc_data = get_btc_price()
    return render_template('index.html', 
                         price=btc_data['price'],
                         last_updated=btc_data['updated'])

if __name__ == '__main__':
    app.run(debug=True)