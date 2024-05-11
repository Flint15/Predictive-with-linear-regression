# Getting Started

## Prerequisites

* NumPy
* Matplotlib
* Scikit-learn

## Installation

First you should install numpy, matplotlib and scikit-learn with `pip`, in cmd or in code cell if you use Google Colab/Jupyter Notebook

`pip install numpy`

`pip install matplotlib`

`pip install scikit-learn`

Then you can import this libraries

```python
import numpy, matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
```
By importing the LinearRegression class from the sklearn.linear_model module, we can use it in our Python code to create linear regression models, fit them to data, make predictions, and perform other related tasks.

## Usage

```python
np.random.seed(0)

num_points = 100
```
`np.random.seed(0)` make data reproducibility, every time the code is run, the data will be the same (if you dont want't, you can delete this)

`num_points = 100` number of data points

num_points = 100
```python
x = np.random.rand(num_points) * 10 #independent variable (input values)
y = 2*X + 3 + np.random.randn(num_points) #dependent variable (output values)
```

We make predict with imaginary data, and so we should create them, but they must be interlinked with each other, they must based on a linear relationship, on this - 2*X + 3, for example

```python
x = x.reshape(-1, 1)
```
In scikit-learn, the input features (independent variables) are expected to be in a two-dimensional array format, where each row represents a sample (data point) and each column represents a feature

```python
model = LinearRegression()
model.fit(x, y)
```
Create LinearRegression() model and then perform linear regression

```python
new_X = x + 10
new_y = model.predict(new_x)
```
Create a new data to test our model, and then make a prediction

## Visualizations 

After all we can look at our data

```python
plt.scatter(x, y, label="data points")
plt.scatter(new_x, new_y, label="Future prediction")

plt.legend()
```
`plt.legend()` is used to add Legend (explanatory labels)





# Congratulate yourself that you have create prediction model by using simple linear regression
