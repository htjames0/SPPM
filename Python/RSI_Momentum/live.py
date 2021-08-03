import numpy as np
import pandas as pd
import yfinance as yf
import sched
from datetime import date
import time
import warnings
warnings.filterwarnings("ignore")

s = sched.scheduler(time.time,time.sleep)

def RSI(rsi_period, stock_interval, time_interval, restriction) :
    #initialize parameters
    rsi_buy         = 30
    rsi_sell        = 70
    rsi_period      = rsi_period
    sell_price      = 0
    buy_price       = 0
    profit          = 0
    net_profit      = 0
    j               = 0    #parameter for indexing buy df 
    shares          = 0    #number of shares
    buy_restriction = restriction    #prevents buying too much of the stock (i - 1)

    #**getting closing price data
    today = date.today()
    #data = yf.download('SPCE', start='2020-06-25', end=today.strftime('%Y-%m-%d'))
    data = yf.download('AMD', period = stock_interval, interval = time_interval)

    #**calculating RSI
    data['Up']        = np.maximum(data['Close'].diff(),0)
    data['Down']      = np.maximum(-data['Close'].diff(),0)
    data['Up SMMA']   = data['Up'].rolling(rsi_period).mean()
    data['Down SMMA'] = data['Down'].rolling(rsi_period).mean()
    data['RS']        = data['Up SMMA']/data['Down SMMA']
    data['RSI']       = 100 - 100/(1+data['RS'])


    #itiializing more columns to recording buys and sells in array
    data['Buy Price']  = 0.000
    data['Sell Price'] = 0.000
    data['Net Profit'] = 0.000
    data['Profit']     = 0.000
    data['Net Shares'] = 0

    #itializing a new pd dataframe to keep track of the price shares were bought at
    dummy = np.zeros((10,1))
    buy = pd.DataFrame(dummy, columns = ['Price'])
    print(data['RSI'][data.index[-1]])

    #executing trades    
    if round(data['Close'][data.index[-1]], 1) >= rsi_sell and shares > 1 :
        #sell call
        shares = 0
        data['Sell Price'][data.index[-1]] = data['Close'][data.iloc[-1]]
        data['Net Shares'][data.index[-1]] = shares
        
        #iterate over buy df to calculate profit
        for k in range(0, len(buy)):
            if buy['Price'][k] != 0:
                profit = profit + (data['Close'][data.index[-1]] - buy['Price'][k])
                buy['Price'][k] = 0
        j = 0
        
    elif round(data['RSI'][data.index[-1]] , 1) <= rsi_buy and (shares <= buy_restriction):
        shares = shares + 1 
        #buy call
        data['Buy Price'][data.index[-1]] = data['Close'][data.index[-1]] 
        data['Net Shares'][data.index[-1]]  = shares
        buy['Price'][j] = data['Close'][data.index[-1]] 
        j = j + 1

    net_profit = net_profit + profit
    profit = 0
    data['Profit'][data.index[-1]]  = profit
    data['Net Profit'][data.index[-1]]  = net_profit
    s.enter(300, 1, RSI, (rsi_period, stock_interval, time_interval, restriction, ))

s.enter(300, 1, RSI, (6, '30d', '5m', 5, ))
s.run()
