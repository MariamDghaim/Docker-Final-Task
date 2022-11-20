from flask import Flask
import bitCoin
import redis

app = Flask(__name__)
btcData = redis.Redis(host='redis', port=6379)


@app.route("/")

def home():
    # True loop used for getting the price in less than minute
    while True:

        price = float("{:.2f}".format(bitCoin.gitCurBTCPrice()))
        avgPrice = float("{:.2f}".format(bitCoin.gitAvgBtCPrice()))

        # save it in btcData redis file
        btcData.set('CurrPrice', price)
        btcData.set('AvgPrice', avgPrice)

        #refresh to update the content in page without clicking refresh each time
        return """
        <meta http-equiv="refresh" content="1" /><h2>--DOCKER TASK-- \n Bitcoin Price:</h2><br> <h3>The Current Bitcoin Price is: {}$</h3><br> <h3>the Average Bitcoin Price: {}$ </h3><br> """.format(price,avgPrice)