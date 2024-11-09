import pandas as pd

# Loading the dataset
df = pd.read_csv('./data/heart-disease-health-indicators-dataset.csv')

#Required columns
df = df[['HeartDiseaseorAttack', 'HighBP', 'BMI', 'Smoker', 'Sex']]
print(df.head())
