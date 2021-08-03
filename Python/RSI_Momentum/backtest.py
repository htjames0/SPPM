import numpy as np
import pandas as pd
import yfinance as yf
import matplotlib.pyplot as plt
from datetime import date
import time
import warnings
warnings.filterwarnings("ignore")
#from pyrh import Robinhood

#login into Robinhood Account
#rh = Robinhood()
#rh.login(username = "____", password = "____")

#initialize parameters
rsi_buy         = 30
rsi_sell        = 70
rsi_period      = 6
sell_price      = 0
buy_price       = 0
profit          = 0
net_profit      = 0
j               = 0    #parameter for indexing buy df 
shares          = 0    #number of shares
buy_restriction = 5    #prevents buying too much of the stock (i - 1)

#getting closing price data
today = date.today()
#data = yf.download('SPCE', start='2020-06-25', end=today.strftime('%Y-%m-%d'))
data = yf.download('AMD', period = '30d', interval = '5m')

data['Up']         = 0.000
data['Down']       = 0.000
data['Up SMMA']    = 0.000
data['Down SMMA']  = 0.000
data['RS']         = 0.000
data['RSI']        = 0.000

#calculating RSI
idx = data['Close'].index[-1]
prev = data['Close'].index[-2]
data['Up'][idx]        = np.maximum(data['Close'][idx] - data['Close'][prev],0)
data['Down'][idx]      = np.maximum(-(data['Close'][idx] - data['Close'][prev]),0)
data['Up SMMA'][idx]   = data['Up'][-1].rolling(rsi_period).mean()
data['Down SMMA'][idx] = data['Down'][-1].rolling(rsi_period).mean()
data['RS'][idx]        = data['Up SMMA'][-1]/data['Down SMMA'][-1]
data['RSI'][idx]       = 100 - 100/(1+data['RS'])
print(data[RSI])


#itiializing more columns to recording buys and sells in array
data['Buy Price']  = 0.000
data['Sell Price'] = 0.000
data['Net Profit'] = 0.000
data['Profit']     = 0.000
data['Net Shares'] = 0

#itializing a new pd dataframe to keep track of the price shares were bought at
dummy = np.zeros((10,1))
buy = pd.DataFrame(dummy, columns = ['Price'])


#executing trades
for i in range(0, len(data)):    
    if round(data['RSI'][i], 1) >= rsi_sell and shares > 1 :
        shares = 0
        data['Sell Price'][i] = data['Close'][i]
        data['Net Shares'][i] = shares
        
        #iterate over buy df to calculate profit
        for k in range(0, len(buy)):
            if buy['Price'][k] != 0:
                profit = profit + (data['Close'][i] - buy['Price'][k])*10
                buy['Price'][k] = 0
        j = 0
        
    elif round(data['RSI'][i], 1) <= rsi_buy and (shares <= buy_restriction):
        shares = shares + 1 
        data['Buy Price'][i] = data['Close'][i]
        data['Net Shares'][i] = shares
        buy['Price'][j] = data['Close'][i]
        j = j + 1
        
    else:
        data['Buy Price'][i] = 0
        data['Sell Price'][i] = 0

    net_profit = net_profit + profit
    profit = 0
    data['Profit'][i] = profit
    data['Net Profit'][i] = net_profit

BNH = (data['Close'][data.index[-1]] - data['Close'][data.index[0]])*10
print(f'Buy and Hold Profit: {BNH:.2f}\nRSI Profit: {net_profit:.2f}')
print(data[['Close','RSI','Buy Price', 'Sell Price', 'Net Shares', 'Profit', 'Net Profit']].to_string())


#data['Close'].plot()
#data['RSI'].plot()
#plt.show()

# ---- ideas ----
#maybe getRSI function that when given stock ticker, rsi period, and chart period as input will produce RSI data 
#make execution helper function that will execute "trades" with one line of code
#determine correct trading frequency stock price data and RSI period

#code so that it refreshes every determined frequency to enact live trading
#print out number of buys and sells to txt sheet so that when you run it the next day you dont have to worry about
#being labled as PDT
#use a scheduler for running it every day and refreshing 
