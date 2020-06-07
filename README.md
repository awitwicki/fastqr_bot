<img src="logo.jpg">

# fastqr_bot
Qr code generator bot for Telegram messenger

## Installation
1. Clone repository `git clone https://github.com/awitwicki/fastqr_bot`
3. Insert your `TELEGRAM BOT TOKEN` in `main.py line 10` 
4. Execute `pip(3) install -r requirements.txt` to install all dependencies.
5. Run `main.py` in Python

## Dependencies
* Python >= 3.6 (using `f""` strings )
* [python-telegram-bot](https://github.com/python-telegram-bot/python-telegram-bot)
* [MyQr](https://github.com/sylnsfar/qrcode)

Also You can setup systemd service from `qr_bot.service` template.