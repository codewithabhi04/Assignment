import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

# Step 1 : Dataset
X = np.array([[1],[2],[3],[4],[5]])
Y = np.array([3,4,2,4,5])

# Step 2 : Create model
model = LinearRegression()

# Step 3 : Train model
model.fit(X, Y)

# Step 4 : Predict all Y values
Y_pred = model.predict(X)

print("Predicted Y values : ")
print(Y_pred)

# Step 5 : Calculate MSE
mse = mean_squared_error(Y, Y_pred)
print("Mean Squared Error (MSE) : ", mse)

# Step 6 : Calculate R2 Score
r2 = r2_score(Y, Y_pred)
print("R2 Score : ", r2)