
try:
    from flask import Blueprint, render_template, redirect, url_for
    from flask import request
    from flask_login import login_required, current_user
    from . import db
    from .models import User, Price
    from ..trading_bot.constants import WEBSOCKET_URL, COIN_SYMBOL
except Exception as e:
    print(" Some pacakages are missing: {}".format(e))

main = Blueprint('main', __name__)
ticker = ""
web_url = ""

@main.route('/')
def index():
    return render_template('index.html')

@main.route('/profile')
@login_required
def profile():
    return render_template('profile.html',name=current_user.name)

@main.route('/profile', methods=['POST'])
def run_trader():
    # get ticker symbol
    global ticker
    global web_url
    ticker = request.form.get('tag').lower()
    web_url = "wss://stream.binance.com:9443/ws/{}usdt@kline_1m".format(ticker)
    return redirect(url_for('main.trader'))


@main.route('/trading')
@login_required
def trader():

    return render_template('trading.html', tick=ticker, url = web_url)
