import pandas as pd
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

Border = "-"*40

#########################################################
# Step 1 : Get Data
#########################################################

print(Border)
print("Step 1 : Get Data")
print(Border)

df = pd.read_csv("PlayPredictor.csv")

print("Dataset loaded successfully")
print(df)

#########################################################
# Step 2 : Clean, Prepare and Manipulate data
#########################################################

print(Border)
print("Step 2 : Data Preprocessing")
print(Border)

le1 = LabelEncoder()
le2 = LabelEncoder()
le3 = LabelEncoder()

df["Whether"] = le1.fit_transform(df["Whether"])
df["Temperature"] = le2.fit_transform(df["Temperature"])
df["Play"] = le3.fit_transform(df["Play"])

X = df[["Whether","Temperature"]]
Y = df["Play"]

print("After Encoding:")
print(df)

#########################################################
# Step 3 : Train Data (Whole dataset)
#########################################################

print(Border)
print("Step 3 : Train Data")
print(Border)

model = KNeighborsClassifier(n_neighbors=3)
model.fit(X, Y)

print("Model training completed")

#########################################################
# Step 4 : Test Data
#########################################################

print(Border)
print("Step 4 : Test Data")
print(Border)

# Manual mapping
weather_map = {"Sunny":0, "Overcast":1, "Rainy":2}
temp_map = {"Hot":0, "Mild":1, "Cool":2}

test = [[weather_map["Sunny"], temp_map["Cool"]]]

prediction = model.predict(test)

# Convert result back
result = "Yes" if prediction[0] == 1 else "No"

print("Result:", result)
#########################################################
# Step 5 : Calculate Accuracy
#########################################################

print(Border)
print("Step 5 : Calculate Accuracy")
print(Border)

X_train, X_test, Y_train, Y_test = train_test_split(
    X, Y, test_size=0.5, random_state=42
)

model = KNeighborsClassifier(n_neighbors=3)
model.fit(X_train, Y_train)

Y_pred = model.predict(X_test)

accuracy = accuracy_score(Y_test, Y_pred)

print("Accuracy is :", accuracy * 100)