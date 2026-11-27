21/9/26

import pandas as pd
import numpy as np

list1 = [1,2,3,4,5]
print(list1)

print("Series")
s1 = pd.Series(list1)
print(s1)

s2=pd.Series(['Lawal', 'Jethro', 'Tracy'])
print(s2)

s3=pd.Series(list1, index=['P', 'Q', 'R', 'S', 'T'])
print(s3)

s4=pd.Series(['Lawal','Jethro','Tracy'], index = [3,1,2])
print(s4)

print()
print("DataFrames")
myList = [[1,2,3], [4,5,6]] # the nexted lists form the rows of the dataframe
print(myList)
df1=pd.DataFrame(myList)
print(df1)

print()
myDict={'A': [1,2,3], 'B':[4,5,6]} #  the lists/keys form the columns respectively
print(myDict)
df2=pd.DataFrame(myDict)
print(df2)

print()
myList2 = [[1,2,3,4,5],[10,20,30,40,50]]
print(myList2)
df3=pd.DataFrame(myList2, index=['A','B'], columns=['1st', '2nd', '3rd', '4th', '5th'])
print(df3)

#reading csv into dataframe
print('\ncsv into dataframe')
classData = pd.read_csv('MachineLearningResources/Datasets/pandasDemo.csv')
print(classData)
print(classData.head(6)) #features are not counted but included
print(classData.tail()) # last five rows
print(classData.describe()) # generate statistical values on numerical features/columns
print()

print("Rename func with re-assignment/implace")
classData = classData.rename(columns={'TA':'Assistant'}, index={0:'Zero', 1:'One'}) # Changing the value of columns and rows
print(classData)
#or
classData.rename(columns={'Assistant':'New_Assistant'}, index={'Zero':'Row Zero', 'One':'Row One'}, inplace = True) # apply the changes to the original object classData
print(classData)
print()

# Slicing features/columns
print('slicing dataframe to series:')
x1=classData['ModuleID']
print(x1)
print(type(x1))
print()

print('slicing into smaller dataframe:')
x2=classData[['ModuleID']]
print(x2)
print(type(x2))

x3= classData[['ModuleID', 'Instructor']] # df[feature(s)]
print(x3)
print(type(x3))
print()

# Selecting rows satisfying a condition in two steps
print("Creating the boolean array which is used to select rows")
arr1=classData['ModuleID'] == 'CS101' # arr1 is a boolean mask
print(arr1)

print("\nThen selecting the rows:\n")

print(classData[arr1]) # targeting the rows respecting the boolean mask arr1
print()

# 25/09/2026
# Revision

print('Combining two conditions with lorgical operator &...|')
arr2=classData['Instructor'] == 'Aaron' # df[feature(s)] == value
print(arr2) 

print("\n")
arr3 = classData[arr1 & arr2] # row(s) satisfying both conditions
arr4 = classData[arr1 | arr2] # row(s) satisfying either of the conditons
print(arr3)
print(arr4)
print()

# without using boolean variable
arr5 = classData[(classData['ModuleID']=='CS101') & (classData['Instructor']=='Aaron')]
print(arr5)
print()

# Selecting rows with .loc[0] & .iloc['Row One'], locates only rows
print(".iloc works with indices; 0,1,2,3 etc. While .loc works with labels, locates only rows")
print(classData.iloc[0]) # row 0 in series
print(classData.iloc[[0]]) # row 0 in dataframe
print(classData.loc['Row One']) # Row One in series
print(classData.loc[['Row One']]) # Row One in dataframe

# Slicing throw rows 
print(classData.iloc[[0,3,4]])
print(classData.iloc[0:3])
print(classData.iloc[6:8]) # when its 2 or more rows (2 dimensional) selected, even if its one square bracket it comes out as a df

# 02/10/2026

# Revision with loc & iloc
print(classData.iloc[0:5,0:2] )# targeting both dimensions [row,column] (contiguous)
# print(classData.iloc[[1,3,7],[1,3,5]]) # targeting both dimensions [row,column] (Specific)

# Adding a new column and correspondiong values to a dataframe
classData['AverageGPA']=[44,46,47,41,45,49,40,41,45,48,42]
print(classData)

# Manipulating the values of all a column
classData['AverageGPA']=classData['AverageGPA']*0.1
print(classData)

# Sorting (.sort_values() does not modify the original dataframe)
# argument implace=True to modify the original classData
print(classData.sort_values(['Rating','AverageGPA'])) #it takes the first specified column (Rating into consideration
print(classData.sort_values(['Rating','AverageGPA'], ascending=False)) #ascending is true by default

# .isnull() (returns False for not-missing value and True for missing values(e.g. None(Absence of value) & NaN(Undefined value)))
print(classData.isnull())
print(".isnull().sum()")
print(classData.isnull().sum()) # to count the missing elements/values by columns because axis=0 by default
print()
data= pd.DataFrame([[None], [np.nan], [''], [0], ['Apple']], columns=['A'])
print(data)
print(data.isnull())
print(".isnull().sum()")
print(data.isnull().sum()) # to count the missing elements/values by columns
print()

# .dropna() (dropping the whole rows/columns with missing values)
print(classData.dropna()) # rows
print(classData)
print(classData.dropna(axis=1)) # columns
print(classData)
print(data.dropna(inplace=True))
print(data)
print()

# Converting from panda series/dataframe to numpy array
data1=pd.DataFrame([[1,2],[3,4]], columns=['A','B'])
print(data1)
arr15 = data1.to_numpy()
print(arr15)
print(type(data1), type(arr15))

# correlation between two columns (-1,0,1)
data2=pd.DataFrame({'A':[1,4,7,10], 'B':[1,2,3,4], 'C':[2,12,1,5]})
print(data2)
print(data2.corr())
