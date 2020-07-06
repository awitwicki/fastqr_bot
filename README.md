<img src="logo.jpg">

# fastqr_bot
Qr code generator bot for Telegram messenger

## Installation
1. Clone repository `git clone https://github.com/awitwicki/fastqr_bot`
2. Insert your `TELEGRAM BOT TOKEN` in `main.py line 10` 
3. Execute `pip(3) install -r requirements.txt` to install all dependencies.
4. Since 2020, python `PIL` library has changed and we should edit some code:
   
   You need to find file `{pythondir}\Lib\site-packages\MyQr\myqr.py` and
modify 85th line. Just add `resample=Image.BOX` to
`qr.resize(...)` function:

   **line 85:** `qr.resize((qr.size[0]*3, qr.size[1]*3), resample=Image.BOX).save(qr_name)`

Run `main.py` in Python

## Dependencies
* Python >= 3.6 (using `f""` strings )
* [python-telegram-bot](https://github.com/python-telegram-bot/python-telegram-bot)
* [MyQr](https://github.com/sylnsfar/qrcode)

Also You can setup systemd service from `qr_bot.service` template.