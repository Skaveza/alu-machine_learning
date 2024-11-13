import pandas as pd
from sklearn.linear_model import SGDRegressor
from sklearn.linear_model import DecisionTreeRegressor
from sklearn.linear_model import RandomForestRegressor
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import train_test_split
import joblib

# 
df = pd.read_csv('./data/heart_disease_health_indicators_BRFSS2015.csv')
df = df[['HeartDiseaseorAttack', 'HighBP', 'BMI', 'Smoker', 'Sex']]  
# Defining X and y
X = df[['HighBP', 'BMI', 'Smoker', 'Sex']]  
y = df['HeartDiseaseorAttack']  
# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
# Initialize the Linear Regression model
model = LinearRegression()
# Train the model
model.fit(X_train, y_train)
# Make predictions
y_pred_continuous = model.predict(X_test)
# Apply a threshold to convert continuous predictions to binary (0 or 1)
threshold = 0.5
y_pred_binary = [1 if pred >= threshold else 0 for pred in y_pred_continuous]
# Evaluate the model
accuracy = accuracy_score(y_test, y_pred_binary)
print("Model Accuracy:", accuracy)

joblib.dump(model, 'heart_disease_model.joblib')
print ("Model saved successfully")