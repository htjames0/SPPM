import numpy as np
import pandas as pd
import yfinance as yf
import time
import warnings
import datetime as date
import schedule

#don't show unecessary warnings
warnings.filterwarnings('ignore')

#global variables
rsi_sell = 70
rsi_buy = 30

#helper functions
#get stock price data and calculating RSI
def getData(ticker, stock_interval, time_interval, rsi_period):
    stock_data = yf.download(ticker, period = stock_interval, interval = time_interval)

    #calculating RSI
    stock_data['Up']        = np.maximum(stock_data['Close'].diff(),0)
    stock_data['Down']      = np.maximum(-stock_data['Close'].diff(),0)
    stock_data['Up SMMA']   = stock_data['Up'].rolling(rsi_period).mean()
    stock_data['Down SMMA'] = stock_data['Down'].rolling(rsi_period).mean()
    stock_data['RS']        = stock_data['Up SMMA']/stock_data['Down SMMA']
    stock_data['RSI']       = 100 - 100/(1+stock_data['RS'])

    #initializing extra columns 
    stock_data['Buy Price']  = 0.000
    stock_data['Sell Price'] = 0.000
    stock_data['Net Shares'] = 0.000

    return stock_data


#execute trade in realtime
def trade(stock_data, exec_restrict):
    #initializing variables 
    shares = 0 

    #dummy = np.zeros((10,1))
    #buy = pd.DataFrame(dummy, columns = ['Price'])
    idx = stock_data['Close'].index[-1]
    rsi = stock_data['RSI'][idx]
    close = stock_data['Close'][idx]

    #sell 
    if round(rsi, 1) >= rsi_sell and shares > 1 :
        shares = 0
        stock_data['Sell Price'][idx] = close
        stock_data['Net Shares'][idx] = shares
        print(f'{idx}, {close:0.3f}, {rsi:0.3f}, {shares}')
        print(f'I sold all shares at {close:0.2f}')
        #iterate over buy df to calculate profit
        #for k in range(0, len(buy)):
        #    if buy['Price'][k] != 0:
        #        profit = profit + (data['Close'][data.index[-1]] - buy['Price'][k])
        #        buy['Price'][k] = 0
        #j = 0

    #buy
    elif round(rsi, 1) <= rsi_buy and (shares <= exec_restrict):
        shares += 1 
        #buy call
        stock_data['Buy Price'][idx] = close 
        stock_data['Net Shares'][idx]  = shares
        print(f'{idx}, {close:0.3f}, {rsi:0.3f}')
        print(f'I bought 1 shares at {close :.2f}')
        #buy['Price'][j] = data['Close'][data.index[-1]] 
        #j += 1

    else:
        print(f'{idx}, {close:0.3f}, {rsi:0.3f}')
        print('...No Trade was Executed...')

    return 

#if __name__ == '__main__'
def execute():
    trade(getData('AMD', '30d', '5m', 6), 6)

schedule.every(5).minutes.do(execute)

while True:
    schedule.run_pending()
    time.sleep(1)
