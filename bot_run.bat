@echo off

call $~dp0tbot2804\venv\Scripts\activate

cd  $~dp0tbot2804

set TOKEN="ваш токен"

python tbot_2804\bot_tg_yandex.py

pause
