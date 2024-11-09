# models/neural_network.py
import tensorflow as tf
from tensorflow.keras import layers
import numpy as np

def create_model(input_shape: tuple[int, ...]) -> tf.keras.Sequential:
    model = keras.Sequential([
        layers.Dense(64, activation='relu', input_shape=input_shape),
        layers.Dense(64, activation='relu'),
        layers.Dense(1)  # Output layer for fuel efficiency prediction
    ])
    model.compile(optimizer='adam', loss='mean_squared_error')
    return model