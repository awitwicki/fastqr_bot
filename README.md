<img src="logo.jpg">

# fastqr_bot
Qr code generator bot for Telegram messenger

## Installation

### 1. Env

Use next environment variables:

* `FASTQR_TOKEN={YOUR_TOKEN}` - telegram token
* `FASTQR_INFLUX_QUERY={url}` - url to your influxDB server for storing logs, you choose not to define that env variable, if you don't need to log bot events

<hr>

### 2. Docker compose:
create `.env` file and fill it with that variables and run

```
docker-compose up -d
```
## OR
### 2. use Python

1. Clone repository `git clone https://github.com/awitwicki/fastqr_bot`
2. Execute `pip(3) install -r requirements.txt` to install all dependencies.
3. Since 2020, python `PIL` library has changed and we should edit some code:
   
   You need to find file `{pythondir}\Lib\site-packages\amzqr\amzqr.py` and
modify 85th line. Just add `resample=Image.BOX` to
`qr.resize(...)` function:
qr.resize((qr.size[0]*3, qr.size[1]*3)).save(qr_name) -> qr.resize((qr.size[0]*3, qr.size[1]*3), resample=Image.BOX).save(qr_name)
   **line 85:** `qr.resize((qr.size[0]*3, qr.size[1]*3), resample=Image.BOX).save(qr_name)`

Run `main.py` in Python

## Dependencies
* Python >= 3.6 (using `f""` strings )
* [python-telegram-bot](https://github.com/python-telegram-bot/python-telegram-bot)
* [Amazing-QR](https://github.com/x-hw/amazing-qr)
