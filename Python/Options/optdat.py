import numpy as np
import pandas as pd
import yfinance as yf

aapl = yf.Ticker("AAPL")
opt = aapl.option_chain('2021-07-27')
