import tensorflow as tf
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#import data
data = pd.read_csv(r'\Users\hughtillmanjamesjr.\Desktop\Python\SPPML\AMD.csv')
print(data)

###model function
##def model(step_size):
##
##    #defining simple Sequential model (one or more layers)
##    model = tf.keras.models.Sequential()
##    
##    #topography - single node with single layer
##    model.add(tf.keras.layers.Dense(units=1,
##                                    input_shape=(1,)))
##    
##    #compile - loss fxn MSE
##    model.compile(optimizer=tf.keras.optimizers.RMSprop(lr=step_size),
##                  loss="mean_squared_error",
##                  metrics=[tf.keras.metrics.RootMeanSquaredError()])
##    return model 
##
##
###train function
##def train_model(model, feature, label, epochs, batch_size):
##
##    #feeding features and labels to model, model iterates epoch number of times
##    #using batch_size number of data points per iteration
##    history = model.fit(x=feature,
##                        y=label,
##                        batch_size=batch_size,
##                        epochs=epochs)
##
##    #getting weights and bias
##    trained_weight = model.get_weights()[0]
##    trained_bias = model.get_bias()[1]
##
##    #getting historical data of model for each epoch
##    epochs = history.epoch
##    hist = pd.DateFram(history.history)
##
##    #gettig rmse for each epoch
##    rmse = hist["root_mean_squared_error"]
##
##    return trained_weight, trained_bias, epochs, rmse


#predict function

