import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


Border = "-"*40

print(Border)
print("Load the Dataset")
print(Border)

Dataset = "student_performance_ml.csv"

df = pd.read_csv(Dataset)

print(Border)
print("First 5 records")
print(Border)
    
print("Dataset gets loaded successfully....")
print("Intial entries  form dataset:")
print(df.head())

print(Border)
print("Last 5 records")
print(Border)

print("last 5 entries  form dataset:")
print(df.tail())


print(Border)
print("Total Number of rows and columns")
print(Border)

print("Total rows and columns : ",df.shape)     

print(Border)
print("List of Column names")
print(Border)

print("Column Names :",list(df.columns))    

print(Border)
print("Data types of columns")
print(Border)   

print("Data types : ",df.dtypes)


print(Border)
print("Total Number of student in the dataset")
print(Border)   

Total = len(df)
print(f"Number of Student is : {Total}")


print(Border)
print("Count how many student Passed and Failed")
print(Border)   

print("Count how many student Passed and Failed")
print(df["FinalResult"].value_counts())     

print(Border)
print("Average Study Hors")
print(Border)   
             
print("Average Study Hors")
print(df["StudyHours"].mean())   

print(Border)
print("Average Attendance")
print(Border)   

print("Average Attendance")
print(df["Attendance"].mean())   

print(Border)
print("Maximum Previous Score")
print(Border)   

print("Maximum Previous Score")
print(df["PreviousScore"].max())   

print(Border)
print("Minimum SleepHours")
print(Border)   

print("Minimum SleepHours")
print(df["SleepHours"].min())   

print(Border)
print("Caluculate the percentage of Pass and Fail Students")
print(Border)   

print("FinalResult count")
print(df["FinalResult"].value_counts(normalize=True)*100)    

              
#----------------------------------------------
#Plot a Histrograme of Study Hours
#---------------------------------------------
sns.histplot(df["StudyHours"])

plt.title("Histogram of Study Hours")
plt.xlabel("Study Hours")
plt.ylabel("Number of Students")
plt.show()

#----------------------------------------------
#Scatter plot of StudyHours vs PreviousScore
#---------------------------------------------

sns.scatterplot(x= df["StudyHours"], y=df["PreviousScore"])

plt.title("Scatter plot of StudyHours vs PreviousScore")
plt.xlabel("Study Hours")
plt.ylabel("PreviousScore")
plt.show()

#----------------------------------------------
#Boxplot for Attendance any outlier are present
#---------------------------------------------

sns.boxplot(x= df["Attendance"])
plt.title("Boxplot for Attendance")

plt.show()

#----------------------------------------------
#Plot showing relationship bet Assignments Complete and Final Result
#---------------------------------------------

sns.scatterplot( x=df["AssignmentsCompleted"], y=df["FinalResult"])

plt.title("Assignments Completed vs Final Result")
plt.xlabel("Assignments Completed")
plt.ylabel("Final Result")

plt.show()

#----------------------------------------------
#Plot Sleep Hours against Final Result
#---------------------------------------------

sns.scatterplot( x=df["SleepHours"], y=df["FinalResult"])

plt.title("Sleep Hours vs Final Result")
plt.xlabel("Sleep Hours")
plt.ylabel("Final Result")

plt.show()
