import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestRegressor  
from sklearn.metrics import r2_score
from sklearn.metrics import accuracy_score, classification_report
import seaborn as sns
import matplotlib.pyplot as plt
import csv
from sklearn.preprocessing import LabelEncoder

data = pd.read_csv('Students Social Media Addiction.csv')
print(data.head())
data = data.dropna()
data = data.drop(['Country','Most_Used_Platform','Gender','Student_ID'], axis=1)
le = LabelEncoder()
data['Academic_Level'] = le.fit_transform(data['Academic_Level'])
data['Relationship_Status'] = le.fit_transform(data['Relationship_Status'])
data['Affects_Academic_Performance'] = le.fit_transform(data['Affects_Academic_Performance'])

y = data['Addicted_Score']
X = data[['Age','Academic_Level','Avg_Daily_Usage_Hours','Affects_Academic_Performance','Sleep_Hours_Per_Night','Mental_Health_Score','Relationship_Status','Conflicts_Over_Social_Media']]

model = RandomForestRegressor(n_estimators=100, random_state=42)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)
model.fit(X_train, y_train)
y_pred = model.predict(X_test)
r2 = r2_score(y_test, y_pred)
print(f'R² Score: {r2}')