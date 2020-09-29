from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import *

from flask_sqlalchemy import SQLAlchemy

import random
import os

db = SQLAlchemy()
app = Flask(__name__)

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://sql12367906:Khl3ZDcMda@sql12.freemysqlhosting.net:3306/sql12367906"

db.init_app(app)

# Channel Access Token
line_bot_api = LineBotApi('N6EH/sRKbfIQO6moywQ11ZDhhu4tLp2Vq8KZLeQeXojim+jfkdVHCdbuSRy4Bh+ZzXF/sGH4Q1ruqdxVFd39/6GA3uf4pF2hzfq9msmKHjnD1HTC5Xyz7LjatSO2zxzgEtXAz0ZqYT3Kk5ih0m315QdB04t89/1O/w1cDnyilFU=')
# Channel Secret
handler = WebhookHandler('2c03d2503de5fa94a58018c4857d4499')

# 監聽所有來自 /callback 的 Post Request
@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']
    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)
    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)
    return 'OK'

# 處理訊息
@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    # sql_cmd = """select * from users"""
    # query_data = db.engine.execute(sql_cmd)
    # print(query_data)
    # return 'ok'
    # query_data = db.engine.execute("""select * from users""")

    sql = """
        select * from users
    """

    message = TextSendMessage(text=event.message.text)
    line_bot_api.reply_message(event.reply_token, message+sql)

import os
if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
