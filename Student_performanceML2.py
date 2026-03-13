import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.model_selection import train_test_split

from sklearn.tree import DecisionTreeClassifier,plot_tree

from sklearn.metrics import (
    accuracy_score,
    confusion_matrix,
    classification_report,
    ConfusionMatrixDisplay
)


Border = "-"*40

print(Border)
print("Load the Dataset")
print(Border)

Dataset = "student_performance_ml.csv"

df = pd.read_csv(Dataset)


#########################################################################
#Decide independent and dependent variables
#########################################################################

print(Border)
print("Decide independent and dependent variables")
print(Border)

#x : Independent variables or features
#y : dependent variable or labels

feature_cals =[
    "StudyHours",
    "Attendance",
    "PreviousScore",
    "AssignmentsCompleted",
    "SleepHours"
] 

X = df[feature_cals]
Y = df["FinalResult"]

print("X shape : ",X.shape)
print("Y shape : ",Y.shape)


#########################################################################
# Split the dataset for training and testing
#########################################################################

X_train, X_test, Y_train, Y_test = train_test_split(
    X,
    Y,
    test_size = 0.5,
    random_state = 42     #shuffel the data using this variable  

)


print("Data splitting activity done :")

print("X :",X.shape)    #(30,5)
print("y ",Y.shape)     #(30,1)

print("X_train : ",X_train.shape)   #(15,5)
print("X_test : ",X_test.shape)     #(15,5)
print("Y_train : ",Y_train.shape)   #(15,1)
print("Y_test : ",Y_test.shape)    #(15,1)


#########################################################################
# Build the model
#########################################################################

print(Border)
print("Build the model")
print(Border)

print("We are going to use DecisionTreeClassifier")

model = DecisionTreeClassifier(
    criterion="gini",
    max_depth=5,
    random_state=42
)

print("Model Succefully Create :",model)

#########################################################################
# Train the model
#########################################################################

print(Border)
print("Train the model")
print(Border)

model.fit(X_train,Y_train)

print("Model training completed")

#########################################################################
#Evalute the model
#########################################################################

print(Border)
print("Evalute the model")
print(Border)

Y_pred = model.predict(X_test)

print("Model Evaluation (testing) Complete")
print(Y_pred.shape)


print("Expected answer : ")
print(Y_test)

print("Predicted answer : ")
print(Y_pred)

#########################################################################
#Evalute the model Performance
#########################################################################

print(Border)
print("Evalute the model Performance")
print(Border)

accuracy = accuracy_score(Y_test,Y_pred)
print("Accuracy of model is ",accuracy*100)

cm = confusion_matrix(Y_test,Y_pred)
print("Confussion Matrix :")
print(cm)

print("Classification report ")
print(classification_report(Y_test,Y_pred))

#########################################################################
#Plot confussion matrix
#########################################################################

print(Border)
print("Plot confussion matrix")
print(Border)

data = ConfusionMatrixDisplay(confusion_matrix=cm,display_labels=model.classes_)
data.plot()
plt.title("Confussion Matrix of Student_performance dataset")
plt.show()


