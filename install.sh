sudo chmod 777 *
sudo cp qr_bot.service /etc/systemd/system/
sudo systemctl enable qr_bot.service
sudo service qr_bot start
service qr_bot status
