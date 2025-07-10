import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
df = pd.read_csv("traffic_violation_accident_analysis.csv")  # Replace with actual path

# Basic info
print(df.info())
print(df.describe())

# Accident count by state
accidents_by_state = df['State'].value_counts().head(10)
accidents_by_state.plot(kind='bar', title='Top 10 States by Accident Count')
plt.xlabel("State")
plt.ylabel("Accident Count")
plt.show()

# Accidents by time of day
df['Start_Time'] = pd.to_datetime(df['Start_Time'])
df['Hour'] = df['Start_Time'].dt.hour
sns.histplot(df['Hour'], bins=24, kde=False)
plt.title("Accidents by Hour of Day")
plt.xlabel("Hour")
plt.ylabel("Number of Accidents")
plt.show()

# Weather condition impact
sns.countplot(y='Weather_Condition', data=df, order=df['Weather_Condition'].value_counts().iloc[:10].index)
plt.title("Top Weather Conditions During Accidents")
plt.show()
