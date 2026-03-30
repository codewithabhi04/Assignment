import pandas as pd 
import seaborn as sns
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import StandardScaler,MinMaxScaler

from sklearn.metrics import (
    accuracy_score,
    confusion_matrix,
    ConfusionMatrixDisplay,
    classification_report,
)



# Load the dataset


DatasetPath = "Bank_Marketing.csv"

df = pd.read_csv(DatasetPath)

print("Dataset gets loaded succesfully...")
print("Initial entries from dataset :")
print(df.head())


print("Missing values (Per Column)")
print(df.isnull().sum())

print("Statical Summery : ")
print(df.describe())

#countplot

sns.countplot(x="y", data=df)
plt.title("Distribution of Y")
plt.show()

#pie chart

df['y'].value_counts().plot(kind='pie', autopct='%1.1f%%')

plt.title("Class Distribution")
plt.ylabel("")
plt.show()

#Value count

print("Class Distribution (Y count)")
print(df["y"].value_counts())

#label encoding

df['y'] = df['y'].map({'yes': 1, 'no': 0})
print(df.head())

#Split the dataset
feture_cols = [
    "age",
    "job",
    "marital",
    "education",
    "default",
    "balance",
    "housing",
    "loan",
    "contact",
    "day",
    "month",
    "duration",
    "campaign",
    "previous",
    "poutcome"
]

X = df[feture_cols]
Y = df["y"]

print("X shape : ",X.shape)
print("Y shape : ",Y.shape)

X = pd.get_dummies(X, drop_first=True)

X_train, X_test, Y_train, Y_test = train_test_split( X,Y,test_size=0.5,random_state=42)

model_lr =LogisticRegression(max_iter=100)
model_knn =KNeighborsClassifier(n_neighbors=5)
model_rf = RandomForestClassifier(random_state=42,n_estimators=10)

model_lr.fit(X_train,Y_train)
model_knn.fit(X_train,Y_train)
model_rf.fit(X_train,Y_train)



#StandardScaler 
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)
print("StandardScaler is :",X_scaled)

#MinMaxScaler 
scaler = MinMaxScaler()
X_scaled = scaler.fit_transform(X)
print("MinMaxScaler is :",X_scaled)


# Model Evaluation

pred_lr = model_lr.predict(X_test)
pred_knn = model_knn.predict(X_test)
pred_rf = model_rf.predict(X_test)


acc_lr = accuracy_score(Y_test, pred_lr)*100
acc_knn = accuracy_score(Y_test, pred_knn)*100
acc_rf = accuracy_score(Y_test, pred_rf)*100


print("Indivisual Model Accuracy :")
print("Logistic Regression :",acc_lr)
print("KNN :",acc_knn)
print("Decision Tree : ",acc_rf)


#confusion martrix for lr
cm = confusion_matrix(Y_test,pred_lr)
print("Confusion matrix for lr : ")
print(cm)

data = ConfusionMatrixDisplay(confusion_matrix=cm,display_labels=model_lr.classes_)
data.plot()

plt.title("Confusion matrix for lr diabetes dataset")
plt.show()


#confusion martrix for knn
cm = confusion_matrix(Y_test,pred_knn)
print("Confusion matrix for knn : ")
print(cm)

data = ConfusionMatrixDisplay(confusion_matrix=cm,display_labels=model_knn.classes_)
data.plot()

plt.title("Confusion matrix for knn diabetes dataset")
plt.show()


#confusion martrix for rf
cm = confusion_matrix(Y_test,pred_rf)
print("Confusion matrix for rf : ")
print(cm)

data = ConfusionMatrixDisplay(confusion_matrix=cm,display_labels=model_rf.classes_)
data.plot()

plt.title("Confusion matrix for rf diabetes dataset")
plt.show()

#Classification report

print("Classification Report for lr")
print(classification_report(Y_test,pred_lr))

print("Classification Report for knn")
print(classification_report(Y_test,pred_knn))

print("Classification Report for rf")
print(classification_report(Y_test,pred_rf))






