# SSPPM
Stock Price Prediction Model

I am using TensorFlow's keras package in the Jupyter Notebook's environment to create and test a simple stock price prediction model.  Currently, I have code to use one input and output to create the network but plan on developing the network further.  An interest in this project would include physic's aided learning to help with training, although this topic is advanced and might require more research and background knowledge. 

For data, I have downloaded stock price data from Yahoo Finance on AMD, a semiconductor company, training and test data.  The data spans from January 1st, 2016 thorough August 1, 2021.  I plan to use four year's of data (Jan 1, 2016 - December 31st, 2020) to train my model.  Then use the last half year, January 1st, 2021 - August 1st, 2021, to test the accuracy of the model.  I need to devise a approach for forcasting, whether the model is forcasting the stock's closing price by the end of a certian week, or day, or month etc.  Thought needs to go into this portion of prediction and analysis.

In terms of the model's topology itself, I am unsure of how many layers and inputs it will have.  The data consists of six inputs, (Open, High, Low, Close, Adj. Close and Volume). So, naturally the model would utilize the characteristics of the data set.  I would like to add more inputs but am hesitant to do so.  Statistics such as Beta, P/E, and % shares held by instituition could be useful metrics.  In addition to this, adding in options activity into the model might be useful.  I plan to use one hidden layer for this model as I have read a few academic papers on Options Pricing using Neural Networks and all say one hidden layer is enough but quote varioius reasons why.  The number of neurons in the hidden layer is currently undetermined. I plan to test out several loss functions but will start with the classic Mean Squared Error and am undecided about which activation function to use as well.  
