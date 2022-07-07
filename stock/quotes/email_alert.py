import os
import smtplib
from email.message import EmailMessage

import pandas as pd
from alpha_vantage.timeseries import TimeSeries

import time

EMAIL_ADDRESS = 'YOUR_REG_EMAIL'
EMAIL_PASSWORD = 'GMAIL_APP_PSWD'
ticker=''
def mailing(text):
        msg = EmailMessage()
        msg['Subject'] = 'Stock Fluctuation Alert'
        msg['From'] = EMAIL_ADDRESS
        msg['To'] =  'RECEIVER_EMAIL'
        msg.set_content(text)

        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
            smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
            smtp.send_message(msg)
def check(ticker):
    api_key = 'YOUR_API_KEY'

    # ticker = 'META'
    ts = TimeSeries(key=api_key, output_format='pandas')
    data, meta_data = ts.get_intraday(symbol=ticker,interval='1min', outputsize='full')
    # Replace daily with weekly, monthly, or intraday for different timeframes.
    # data, meta_data = ts.get_monthly(symbol='QQQ')
    print(ticker)
    print(data.head())



    open_value = data.iloc[0][0]
    close_value = data.iloc[0][3]
    # open_data = data['4. open']
    # open_value = open_data[0]
    # close_data = data['4. close'] #The close data column
    # close_value = close_data[0]

    change = 100 * ((close_value-open_value)/open_value)
    pct = '{0:.2%}'.format(abs(change)/100)

    if abs(change) > 0.1:
        message = 'Your stock\'s price has changed by more than 1%!'

        if change > 0:
            msg_detail = (message + ' Your stock has gone up by ' + pct + '.')
            print(msg_detail)
            return msg_detail

        elif change < 0:
            msg_detail = (message + ' Your stock has gone down by ' + pct + '.')
            print(msg_detail)
            return msg_detail
        
    else :
        msg_detail = ('No change in your stock price.')
        print(msg_detail)
        return msg_detail
    
# mailing(ticker + " " + check(ticker))

