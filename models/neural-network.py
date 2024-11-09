   # models/neural_network.py
   import numpy as np
   from tensorflow import keras
   from tensorflow.keras import layers

   def create_model(input_shape):
       model = keras.Sequential([
           layers.Dense(64, activation='relu', input_shape=input_shape),
           layers.Dense(64, activation='relu'),
           layers.Dense(1)  # Output layer for fuel efficiency prediction
       ])
       model.compile(optimizer='adam', loss='mean_squared_error')
       return model