import requests
import pandas as pd
import matplotlib.pyplot as plt  # Importing matplotlib.pyplot

# Fetch data from the JSONPlaceholder API (example: users endpoint)
response = requests.get('https://jsonplaceholder.typicode.com/users')
data = response.json()

# Convert JSON data into a Pandas DataFrame
df = pd.DataFrame(data)

# Display the first few rows of the DataFrame
print("First few rows of the DataFrame:")
print(df.head())

# Perform basic data analysis
print("\nData information:")
print(df.info())

# Display descriptive statistics for numerical columns
print("\nDescriptive statistics:")
print(df.describe())

# Count unique values in categorical columns
print("\nUnique values in 'company' column:")
print(df['company'].value_counts())

# Plot a bar chart of the number of users per city
city_counts = df['address'].apply(lambda x: x['city']).value_counts()
city_counts.plot(kind='bar', color='skyblue', edgecolor='black', figsize=(8, 6))
plt.title('Number of Users per City')
plt.xlabel('City')
plt.ylabel('Number of Users')
plt.xticks(rotation=45)
plt.grid(True)
plt.show()
