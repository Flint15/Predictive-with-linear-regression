import numpy, matplotlib.pyplot as plt, sklearn
from sklearn.linear_model import LinearRegression

np.random.seed(0) # Set random seed for reproducibility

num_points = 100 # Number of data points

x = np.random.rand(num_points) * 10 # Generate random values for the independent variable (x)

# Generate corresponding values for the dependent variable (y)
# Assuming a linear relationship y = 2*X + 3 with some random noise
y = 2*x + 3 + np.random.randn(num_points)

x = x.reshape(-1, 1) # To match the format expected by scikit-learn

# Perform linear regression
model = LinearRegression()
model.fit(x, y)

new_x = x + 10 # Create new test data
new_y = model.predict(new_x) # Make prediction


plt.scatter(x, y, label="data points") #Visualizing initial data
plt.scatter(new_x, new_y, label="Future prediction") #Visualizing predicted data

plt.legend() #To add Legend (explanatory labels)

