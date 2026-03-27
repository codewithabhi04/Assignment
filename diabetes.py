import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import StandardScaler,MinMaxScaler
from sklearn.metrics import (
    accuracy_score,
    confusion_matrix,
    ConfusionMatrixDisplay,
    precision_score,
    recall_score,
    f1_score
)

#########################################################
# Step 1 :Exploratory Data Analysis (EDA)
#########################################################
print("Step 1 : Load the dataset")

DatasetPath = "diabetes.csv"

df = pd.read_csv(DatasetPath)

print("Dataset gets loaded succesfully...")
print("Initial entries from dataset :")

#Display the first 5 rows
print(df.head())


#Display summery of statistic
print(df.describe())


print("Class Distribution (Outcome count)")
print(df["Outcome"].value_counts())

#countplot

sns.countplot(x="Outcome", data=df)
plt.title("Distribution of Outcome")
plt.show()

#Histogram

df["Outcome"].hist()
plt.title("Histogram of Outcome")
plt.xlabel("Outcome")
plt.ylabel("Frequency")
plt.show()

#Boxplot

sns.boxplot(x=df["Outcome"])
plt.title("Boxplot of Outcome")
plt.show()

#########################################################
# Step 2 : Data Preprocessing
#########################################################


#Split the dataset
feture_cols = [
    "Pregnancies",
    "Glucose",
    "BloodPressure",
    "SkinThickness",
    "Insulin",
    "BMI",
    "DiabetesPedigreeFunction",
    "Age"
]

X = df[feture_cols]
Y = df["Outcome"]

print("X shape : ",X.shape)
print("Y shape : ",Y.shape)

X_train, X_test, Y_train, Y_test = train_test_split( X,Y,test_size=0.5,random_state=42)


#Show column info and check for null values
print("Missing values (Per Column)")
print(df.isnull().sum())

#StandardScaler 
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)
print("StandardScaler is :",X_scaled)

#MinMaxScaler
scaler = MinMaxScaler()
X_scaled = scaler.fit_transform(X)
print("MinMaxScaler is :",X_scaled)

#########################################################
# Step 3 : Model Buliding
#########################################################

model_lr =LogisticRegression(max_iter=100)
model_dt =DecisionTreeClassifier(random_state=42)
model_knn =KNeighborsClassifier(n_neighbors=5)

#########################################################
# Step 4 : Train models
#########################################################

model_lr.fit(X_train,Y_train)
model_dt.fit(X_train,Y_train)
model_knn.fit(X_train,Y_train)


#########################################################
# Step 5 :Model Evaluation
#########################################################

pred_lr = model_lr.predict(X_test)
pred_dt = model_dt.predict(X_test)
pred_knn = model_knn.predict(X_test)

acc_lr = accuracy_score(Y_test, pred_lr)*100
acc_dt = accuracy_score(Y_test, pred_dt)*100
acc_knn = accuracy_score(Y_test, pred_knn)*100

print("Indivisual Model Accuracy :")
print("Logistic Regression :",acc_lr)
print("Decision Tree : ",acc_dt)
print("KNN :",acc_knn)


#confusion martrix for lr
cm = confusion_matrix(Y_test,pred_lr)
print("Confusion matrix for lr : ")
print(cm)

data = ConfusionMatrixDisplay(confusion_matrix=cm,display_labels=model_lr.classes_)
data.plot()

plt.title("Confusion matrix for lr diabetes dataset")
plt.show()

#confusion martrix for dt
cm = confusion_matrix(Y_test,pred_dt)
print("Confusion matrix for dt : ")
print(cm)

data = ConfusionMatrixDisplay(confusion_matrix=cm,display_labels=model_dt.classes_)
data.plot()

plt.title("Confusion matrix for dt diabetes dataset")
plt.show()

#confusion martrix for knn
cm = confusion_matrix(Y_test,pred_knn)
print("Confusion matrix for knn : ")
print(cm)

data = ConfusionMatrixDisplay(confusion_matrix=cm,display_labels=model_knn.classes_)
data.plot()

plt.title("Confusion matrix for knn diabetes dataset")
plt.show()

#precision for all models

precision = precision_score(Y_test, pred_lr)
print("Precision for lr:", precision)

precision = precision_score(Y_test, pred_dt)
print("Precision:", precision)

precision = precision_score(Y_test, pred_knn)
print("Precision:", precision)

#recall for all models

recall = recall_score(Y_test, pred_lr)
print("Recall for lr:", recall)

recall = recall_score(Y_test, pred_dt)
print("Recall for dt:", recall)

recall = recall_score(Y_test, pred_knn)
print("Recall for knn:", recall)

#f1_score for all models

f1 = f1_score(Y_test, pred_lr)
print("F1 Score for lr:", f1)

f1 = f1_score(Y_test, pred_dt)
print("F1 Score for dt:", f1)

f1 = f1_score(Y_test, pred_knn)
print("F1 Score for knn:", f1)

#########################################################
# Step 6 :Final Output
#########################################################

#Display predictions

predictions = model_lr.predict(X_test)
print("Predictions:",predictions)

predictions = model_dt.predict(X_test)
print("Predictions:",predictions)

predictions = model_knn.predict(X_test)
print("Predictions:",predictions)


#save them in a CSV file

result = pd.DataFrame({
    "Actual": Y_test,
    "Logistic_Pred": pred_lr,
    "DecisionTree_Pred": pred_dt,
    "KNN_Pred": pred_knn
})

result.to_csv("diabetes_predictions.csv", index=False)

print("Predictions saved to CSV file successfully!")