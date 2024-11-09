   # scripts/train_model.py
import pandas as pd
from models.neural_network import create_model

# Load data
data = pd.read_csv('../data/fuel_data.csv')
X = data.drop('fuel_efficiency', axis=1).values  # Features
y = data['fuel_efficiency'].values  # Target variable

# Create and train model
model = create_model((X.shape[1],))
model.fit(X, y, epochs=100, batch_size=32, validation_split=0.2)

# Save the model
model.save('fuel_efficiency_model.h5')