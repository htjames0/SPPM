# SSPPM
# Stock Price Prediction Model

I am using TensorFlow's keras package in the Jupyter Notebook's environment to create and test a simple stock price prediction model.  I plan to make one model that
is an Artificial Neural Network (MLP) that will utilize one hidden layer.  A continuation of this project would include creating a Recurrent Neural Network (LSTM) 
as they are widely know to be useful fro time-series forcasting.  An extra interest in this project would include physic's aided learning to help with training, 
although this topic is advanced and might require more research and background knowledge and probably not as directly applicable as the MLP and LSTM models. In 
addition, I need to devise some form of fair comparison of model performace.  Maybe compare the models performace to a more traditional or theoretical forcasting 
method. 

For data, I have downloaded stock price data from Yahoo Finance on AMD, a semiconductor company, training and test data.  The data spans from January 1st, 2016 
thorough August 1, 2021.  I plan to use four year's of data (Jan 1, 2016 - December 31st, 2020) to train my model.  Then use the last half year, January 1st, 2021 -
August 1st, 2021, to test the accuracy of the model.  I need to devise a approach for forcasting, whether the model is forcasting the stock's closing price by the 
end of a certian week, or day, or month etc. The data consists of six inputs, (Open, High, Low, Close, Adj. Close and Volume). So, naturally the model would utilize
the characteristics of the data set to determine the number of inputs.  I would like to add more inputs but am hesitant to do so for overfitting purposes.  
Statistics such as Simple Moving Averages (10, 50, 100, 200 day), Beta, P/E, and % shares held by instituition could be useful metrics.  In addition to this, adding
in options activity into the model might be useful.  I plan to use one hidden layer for this model as I have read a few academic papers on Options Pricing using 
Neural Networks and all say one hidden layer is enough but quote varioius reasons why. I plan to test out several loss functions but will start with the classic 
Mean Squared Error and am undecided about which activation function to use as well.

The packages I will be using are tensorflow, pandas, numpy, and matplotlib. I used Jeff Heaton's tutorial on GitHub to install minForge and create a tensorflow 
environment to work in with Jupyter Notebooks. His tutorial can be found here and his YouTube video is also very helpful and guides you through the process of 
installation.  I don't know much about how Apple's M1 chip interacts with tensorflow, but I know it speeds up the training of models etc.  I have a 2021 MacBook Pro 
with Apple's M1 chip and eager to see how my GPU performs with these models. 

My first step will be to create methods that create and train a model.  I think this is easiest as it will allow me to manipulate and try differnt loss and 
activations functions. Next, I will manipulate and "tidy" up the data, adding in the various statistics etc. when needed. A method might be created to deal with 
this aspect.  Creating methods for these portions of the project is merely for easy to ready code and orgainization. 



