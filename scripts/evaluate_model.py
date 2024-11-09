   # scripts/evaluate_model.py
   import pandas as pd
   from tensorflow.keras.models import load_model

   # Load test data
   test_data = pd.read_csv('../data/test_data.csv')
   X_test = test_data.drop('fuel_efficiency', axis=1).values
   y_test = test_data['fuel_efficiency'].values

   # Load the trained model
   model = load_model('fuel_efficiency_model.h5')

   # Evaluate the model
   loss = model.evaluate(X_test, y_test)
   print(f'Model Loss: {loss}')