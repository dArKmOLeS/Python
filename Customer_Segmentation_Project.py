#------------------------------------------------------------------------------------------------------------------------------------------------------
#Code By :- Anmol Kumar Srivastava (dArKmOLeS)
#------------------------------------------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------------------------------------------
#Generates synthetic customer data with CustomerID, Age, Gender, Annual Income, Total Spend, Purchase Frequency.
#Performed various visualisations and used K-means Clustering.
#------------------------------------------------------------------------------------------------------------------------------------------------------

# Import necessary libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans

# Set a seed for reproducibility
np.random.seed(56)

# Generate synthetic customer data
total_customers = 500
customer_id = np.arange(1001, 1001 + total_customers)  # Unique customer IDs
customer_age = np.random.randint(18, 70, size=total_customers)  # Random ages between 18 and 70
gender = np.random.choice(["Male", "Female"], size=total_customers)  # Randomly assign gender
annual_income = np.random.randint(25000, 200000, size=total_customers)  # Random annual income
total_spending = annual_income * np.random.uniform(0.05, 0.2, size=total_customers)  # Spending as a fraction of income
purchase_frequency = np.random.randint(1, 40, size=total_customers)  # Random purchase frequency

# Create a DataFrame to store the generated data
customer_df = pd.DataFrame({
    "Customer ID": customer_id,
    "Age": customer_age,
    "Gender": gender,
    "Annual Income": annual_income,
    "Total Spending": total_spending,
    "Purchase Frequency": purchase_frequency
})

# Save the data to a CSV file
customer_df.to_csv("customers.csv", index=False)

# Load the data from the CSV file to ensure correctness
df = pd.read_csv("customers.csv")

# Check for any missing values
print(df.isnull().sum())  # Ensure there are no missing values

# Scale the numerical features using StandardScaler
scaler = StandardScaler()
df[["Age", "Annual Income", "Total Spending", "Purchase Frequency"]] = scaler.fit_transform(
    df[["Age", "Annual Income", "Total Spending", "Purchase Frequency"]])

# Visualize the age distribution before and after scaling
plt.figure(figsize=(14, 4))

# Original age distribution
plt.subplot(1, 2, 1)
plt.hist(customer_df["Age"], bins=53, color="skyblue", edgecolor="black")
plt.title("Age Distribution - Original")
plt.xlabel("Age")
plt.ylabel("Number of Customers")

# Scaled age distribution
plt.subplot(1, 2, 2)
plt.hist(df["Age"], bins=53, color="skyblue", edgecolor="black")
plt.title("Age Distribution - Scaled")
plt.xlabel("Age (Scaled)")
plt.ylabel("Number of Customers")

plt.tight_layout()
plt.show()

# Visualize gender distribution using a pie chart
df["Gender"].value_counts().plot(kind="pie", autopct='%1.1f%%', colors=["lightblue", "pink"])
plt.title("Gender Distribution")
plt.ylabel("")  # Remove y-axis label for a cleaner look
plt.show()

# Visualize the relationship between Annual Income and Total Spending before and after scaling
plt.figure(figsize=(14, 4))

# Original data
plt.subplot(1, 2, 1)
plt.scatter(customer_df['Annual Income'], customer_df['Total Spending'], alpha=0.5)
plt.title('Income vs. Total Spending - Original')
plt.xlabel('Annual Income')
plt.ylabel('Total Spending')

# Scaled data
plt.subplot(1, 2, 2)
plt.scatter(df['Annual Income'], df['Total Spending'], alpha=0.5)
plt.title('Income vs. Total Spending - Scaled')
plt.xlabel('Annual Income')
plt.ylabel('Total Spending')

plt.tight_layout()
plt.show()

# Visualize additional relationships between features
plt.figure(figsize=(14, 4))

# Purchase Frequency vs. Annual Income (Original)
plt.subplot(1, 2, 1)
plt.scatter(customer_df["Purchase Frequency"], customer_df["Annual Income"], alpha=0.5)
plt.title('Purchase Frequency vs. Annual Income - Original')
plt.xlabel('Purchase Frequency')
plt.ylabel('Annual Income')

# Total Spend vs. Purchase Frequency (Original)
plt.subplot(1, 2, 2)
plt.scatter(customer_df["Total Spending"], customer_df["Purchase Frequency"], alpha=0.5)
plt.title('Total Spend vs. Purchase Frequency - Original')
plt.xlabel('Total Spend')
plt.ylabel('Purchase Frequency')

plt.tight_layout()
plt.show()

# Apply K-Means clustering to the scaled data
k = 4  # Number of clusters
kmeans = KMeans(n_clusters=k, random_state=42)
df['Cluster'] = kmeans.fit_predict(customer_df[['Age', 'Annual Income', 'Purchase Frequency', 'Total Spending']])

# Visualize customer segments based on clustering results
plt.scatter(customer_df['Annual Income'], customer_df['Total Spending'], c=df['Cluster'], cmap='viridis', alpha=0.5)
plt.title('Customer Segments')
plt.xlabel('Annual Income')
plt.ylabel('Total Spending')
plt.show()

# Use Seaborn to create a pair plot of the features, colored by cluster
sns.pairplot(df, hue='Cluster', vars=['Age', 'Annual Income', 'Total Spending', 'Purchase Frequency'], palette='viridis')
plt.suptitle('Pair Plot of Features by Cluster', y=1.02)
plt.show()

# Use Seaborn's FacetGrid to visualize the relationship between Income and Spending by Cluster and Gender
g = sns.FacetGrid(df, col='Cluster', hue='Gender', height=4, aspect=1.2)
g.map(sns.scatterplot, 'Annual Income', 'Total Spending')
g.add_legend()
g.set_axis_labels('Annual Income', 'Total Spending')
g.fig.suptitle('Income vs Spending by Cluster and Gender', y=1.02)
plt.show()
