# Line Bot 教學

本教程介紹如何使用 Python LINE Bot SDK 在 Heroku 上架設一個簡單的回話機器人，並透過Flask讀取MySQL資料。

## 在你開始之前

確保您具有以下內容：

- 擁有 Line 帳號
- 擁有 [Heroku](https://www.heroku.com) 帳戶（可以免費創建一個）

## 建立 Heroku 專案
1. 登入 Heroku 後，
  在 [Heroku](https://dashboard.heroku.com/apps) 頁面中，點選 New -> Create New App
  ![image](https://github.com/marcussfu/linebotWithFlaskAndMySQL/blob/main/image/intro1.png)
2. 輸入自己喜歡的 App name ，然後點擊 Create app
  ![image](https://github.com/marcussfu/linebotWithFlaskAndMySQL/blob/main/image/intro2.png)

3. 可以看到建置完成的畫面
  ![image](https://github.com/marcussfu/linebotWithFlaskAndMySQL/blob/main/image/intro3.png)

## 創建 Line Bot 頻道
1.  進入 [Line 控制台](https://developers.line.me/console/)

2.  Create Channel
    ![iamge](https://github.com/marcussfu/linebotWithFlaskAndMySQL/blob/main/image/intro4.png)
3. 填入 Bot 資訊
    ![image](https://github.com/marcussfu/linebotWithFlaskAndMySQL/blob/main/image/intro5.png)
4. 填入 Bot 資訊 1
    ![image](https://github.com/marcussfu/linebotWithFlaskAndMySQL/blob/main/image/intro6.png)
5. 同意 Line 條款，並按 Create
    ![image](https://github.com/marcussfu/linebotWithFlaskAndMySQL/blob/main/image/intro7.png)

## 設定機器人

按照以下步驟架設一個回話機器人。

1. 進入 [Line 控制台](https://developers.line.me/console/)，選擇你剛剛創建的機器人
    ![image](https://github.com/marcussfu/linebotWithFlaskAndMySQL/blob/main/image/intro8.png)
2. 關閉預設罐頭回覆訊息，點擊edit
    ![image](https://github.com/marcussfu/linebotWithFlaskAndMySQL/blob/main/image/intro9.png) 
   也開啟Webhook
    ![image](https://github.com/marcussfu/linebotWithFlaskAndMySQL/blob/main/image/intro10.png)
   儲存後修改結果
    ![image](https://github.com/marcussfu/linebotWithFlaskAndMySQL/blob/main/image/intro11.png)
3. 點擊"Channel access token"的issue產生 **Channel access token**
    ![image](https://github.com/marcussfu/linebotWithFlaskAndMySQL/blob/main/image/intro12.png)
4. 取得 **Channel secret**
    ![image](https://github.com/marcussfu/linebotWithFlaskAndMySQL/blob/main/image/intro13.png)

5. 使用編輯器開啟範例程式碼資料夾內的 app.py，將剛剛取得的 **channel secret** 和 **channel access token** 填入
  ```shell＝
  // Channel Access Token
  line_bot_api = LineBotApi('channel access token')
  // Channel Secret
  handler = WebhookHandler('channel secret')
  ```

## 設定連結MySQL

這邊要測試連結MySQL，藉由使用者詢問資訊，去資料庫中搜尋相關字詞資料。
連結MYSQL有很多種方式，可以在aws等網路空間建置，或者在heroku使用"ClearDB MySQL"服務
這邊是為了測試功能，使用了MySQL免費網路服務 "https://www.freemysqlhosting.net/"
在freemysqlhosting申請一個測試用的MySQL資料庫，就可以將這個資料庫的帳號密碼和資料庫名稱等輸入至app.py的"app.config['SQLALCHEMY_DATABASE_URI']"

```shell＝
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://user_name:password@IP:3306/db_name"

ex: app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://sql12345:password@sql12.freemysqlhosting.net:3306/sql12345"

// user_name: database登入使用者名稱
// password: database登入使用者密碼
// db_name: database名稱
// IP:3306 PortNumber
```

## 將程式推到 Heroku 上

1. 下載並安裝 [Heroku CLI](https://devcenter.heroku.com/articles/heroku-cli)、[Git](https://git-scm.com/)
2. 開啟下載的此程式碼資料夾，在路徑上輸入 cmd
3. 使用終端或命令行應用程序(Terminal)登錄到 Heroku
    ```shell＝
    heroku login
    ```
4. 初始化 git
    ``` shell=
    $ git config --global user.name "你的名字"
    $ git config --global user.email 你的信箱
    ```
    注意：**你的名字** 和 **你的信箱** 要換成各自的 **名字** 和 **信箱**

5. 初始化 git
    ```shell＝
    git init
    ```
    注意：僅第一次使用時要輸入

6. 用 git 將資料夾與 heroku 連接
    ```shell＝
    heroku git:remote -a {HEROKU_APP_NAME}
    ```
    注意：{HEROKU_APP_NAME} 是 Heroku 應用的名稱
    
7. 輸入以下指令，將程式碼推上 Heroku，**如果有跳出錯誤請重新輸入**
    ```shell
    git add .
    git commit -m "Add code"
    git push -f heroku master
    ```
    **每當需要更新 Bot 時，請重新輸入上述指令**

## 將 Heroku 與 Line 綁定
1. 進入 [Line 控制台](https://developers.line.me/console/)，選擇你剛剛創建的 Bot
    ![](https://i.imgur.com/6ocsOBW.png)
2. 在 webhook URL 中輸入 Heroku 網址

    ```shell
    {HEROKU_APP_NAME}.herokuapp.com/callback
    ```
    ![](https://i.imgur.com/EkDhAgb.png)
    注意：{HEROKU_APP_NAME} 是 Heroku 應用的名稱
    
    在linebot上verify沒過沒關係，因為我們要透過加入linebot到手機實際測試。

  
## 測試範例成果
1. 進入 [Line 控制台](https://developers.line.me/console/)，選擇你剛剛創建的 Bot
    ![](https://i.imgur.com/6ocsOBW.png)
2. 通過在控制台的 “Channel settings” 頁面上掃描 QR Code，將您的 Bot 添加到 LINE 的朋友中
3. 在 Line 上向您的 Bot 發送文字訊息，並確認它會學你說話

## 錯誤尋找

> 當程式遇到問題時，可查看日誌以找出錯誤

要查看您的 Bot 在 Heroku 的日誌，請按照以下步驟。

1. 如果沒登入，請先透過 Heroku CLI 登入
    ```shell
    heroku login
    ```

2. 顯示 app 日誌
    ```shell
    heroku logs --tail --app {HEROKU_APP_NAME}
    ```
    注意：{HEROKU_APP_NAME} 是上述步驟2中的應用名稱。
    ```shell
    --tail                     # 持續打印日誌
    --app {HEROKU_APP_NAME}    # 指定 App
    ```

## 程式檔案解說

> 資料夾裡需含有兩份文件來讓你的程式能在 heroku 上運行

- Procfile：heroku 執行命令，web: {語言} {檔案}，這邊語言為 python，要自動執行的檔案為 app.py，因此我們改成 **web: python app.py**。
- requirements.txt：列出所有用到的套件，heroku 會依據這份文件來安裝需要套件

### app.py (主程式)
可透過修改程式裡的 handle_message() 方法內的程式碼來控制機器人的訊息回覆

![](https://i.imgur.com/DNeNbpV.png)

新版範例程式碼內附註解
如想更多了解此程式，可以去研究 Git、Python3、[Flask 套件](http://docs.jinkan.org/docs/flask/)、[Line bot sdk](https://github.com/line/line-bot-sdk-python)


## 進階操作
[官方文件](https://github.com/line/line-bot-sdk-python#api)
### 回覆訊息
只有當有訊息傳來，才能回覆訊息
```python
line_bot_api.reply_message(reply_token, 訊息物件)
```
### 主動傳送訊息
Bot 需要有開啟 push 功能才可以做，否則程式會出錯
```python
line_bot_api.push_message(push_token, 訊息物件)
```

### 參考資料
lineBot教學
(https://github.com/yaoandy107/line-bot-tutorial/

如何 使用flask 連結 MySQL
(https://www.maxlist.xyz/2019/11/10/flask-sqlalchemy-setting/)

MySQL的免費網路測試服務(freemysqlhosting.net)
(https://www.freemysqlhosting.net/)


