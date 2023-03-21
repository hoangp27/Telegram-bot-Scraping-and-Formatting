# Telegram_bot_Scraping_and_Formatting

This simple Telegram bot will scraping all the available information of trading pair on Binance website while formatting any receive trading signal from Telegram so that we can used as a signal input.

## Procedure

The overall process should be something like this:

1. The bot would access this website on Binance to retrieve data about on available trading pair, and record them as csv format
https://www.binance.com/en/futures/trading-rules/perpetual

2. The bot detect certain crypto currency worlds in the message signal, customize, and print out the standardized signal output

3. The bot will send the standardized signal to any where (here in this version I send the output to a different trading bot that read these formats!)

## Tools

I used Python particularly the following tidyverse packages: *pandas, os, telebot, requests, BeautifulSoup*. In addition, I need to create an API on *Telegram* to allow the bots to access the site. 

To prevent the bots from shutting down you will need to import the `keep_alive.py` batch into the bot and run as well. To run

## Side Notes

To run the bots 24/7, you would need a deployment platform that host the script 24/7. (Like Heroku)

## Directory

- `README.MD`: Overview and Summary of the project
- `main.py`: Telegram bot
- 'keep_alive.py`: Python Script that keep the bot alive
- `coinlist.csv`: Sample data that shows the scraping output
