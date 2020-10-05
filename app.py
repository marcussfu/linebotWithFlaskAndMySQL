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
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://user_name:password@IP:3306/db_name"

db.init_app(app)

# Channel Access Token
line_bot_api = LineBotApi('channel access token')
# Channel Secret
handler = WebhookHandler('channel secret')

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
    sql_cmd = """select name from users"""
    query_data = db.engine.execute(sql_cmd)
    # print(db.engine.execute(sql_cmd).fetchall())
    # print('#########   ', query_data.fetchone()[0])

    message = TextSendMessage(text=event.message.text+'   '+query_data.fetchone()[0])
    line_bot_api.reply_message(event.reply_token, message)

import os
if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
