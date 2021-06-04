# isitDown-Telegram-Bot_heroku

Simple Telegram Bot to check the status of websites. I have integrated python-telegram-bot API in my Python code and used docker to containerize the script and deplyoed it in Heroku.Used webhooks instead of polling for data gathering.

It's done only for testing purpose. 

urllib.request module is used to fetch the URLs and and these requests are passed to urlopen to get the response. The exceptions are then handled by using the urllib.error module.
