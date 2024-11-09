   # scripts/evaluate_model.py
import pandas as pd
import can  # Ensure you have python-can installed
from tensorflow.keras.models import load_model

# Load CAN BUS data
def load_can_data(file_path):
    can_data = []
    with can.open_msgbus(file_path) as bus:
        for msg in bus:
            can_data.append({
                'timestamp': msg.timestamp,
                'id': msg.arbitration_id,
                'data': msg.data.hex()  # Convert data to hex string for easier handling
            })
    return pd.DataFrame(can_data)

# Example usage
can_file_path = 'path/to/your/can_data.log'  # Update with your CAN data file path
can_df = load_can_data(can_file_path)

# Load test data
test_data = pd.read_csv('../data/test_data.csv')
X_test = test_data.drop('fuel_efficiency', axis=1).values
y_test = test_data['fuel_efficiency'].values

# Load the trained model
model = load_model('fuel_efficiency_model.h5')

# Evaluate the model
loss = model.evaluate(X_test, y_test)
print(f'Model Loss: {loss}')