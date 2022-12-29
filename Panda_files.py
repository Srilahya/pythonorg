
#it is a function used for analysing, cleaning, exploring and manipulating data
#panda refers to panel data and python data analysis
#panda allows us to analyze big data and make conclusions, help to clean messy data sets, make them readable and relavent

# series --
# dataframe --


import pandas as pd
'''
mydataset = {'bikes':["honda","splender","scooty"], 'meilage':[40,50,35]}
mydata =pd.DataFrame(mydataset)
#we can also change the index values
Inder_change = pd.DataFrame(mydataset, index = ['b1','b2','b3'])
print(Inder_change)
print(Inder_change.loc['b2'])

print(mydata)
print(mydata.loc[0])

print(mydata.loc[[0,1]])
#loc - locate is used to print only required things : compare the above two for more understanding

#to check the version of the pandas we can use _version_
print(pd.__version__)

#using pandas Series is used to print the data in column type one by one,[one dimensional array] and it also defines the dtype
a = [1,6,5]
series = pd.Series(a)
print(series)
HAPPY = pd.Series(a, index = [10,20,30])
print(HAPPY) #Lables - it can be used to access a specified value, similiar to our indexes


#we can also locate rows in DataFrames

#comma seperated files
df=pd.read_csv('pandas.txt')
print(df)
#read_csv is used to read the custom document
#read_json is similar csv , json is mainly used when the data is vey big
#to_string is used to print the entire data
#head() function is used to get the topdata of the document
#if we give head() then the 1st five data elements will print automatically
#tail() is opposite to head()
#info() gives more information about the dataset
#non null value indicates there is no value presents, not a 0

print(df.head(2))
print(df.tail(2))
print(df.info())
'''
#series
'''import numpy as np
s = pd.Series([1,2,3,np.nan,6,7])

print(s)
print(s[0])
s1 = pd.Series([1,2,3,6,7])
print(s1)
#creating a DataFrame by passing a Numpy array,with a datetime index using date_range() and labeled columns

dates = pd.date_range("20001015",periods=6)

print(dates)

#random float values

df = pd.DataFrame(np.random.randn(6,4), index=dates,columns=list("ABCD"))
print(df)

df2=pd.DataFrame(
    {
        "A": 1.0,
        "B": pd.Timestamp("20001015"),
        "c": pd.Series(1, index=list(range(4)),dtype="float32"),
        "D": np.array([3] * 4, dtype="int32"),
        "E": pd.Categorical(["test","train","test","train"]),
        "F": "foo",
    }
)


# Boolean Indexing

print(df[df["A"] > 0])
print(df[df > 0])

#is in

df2 = df.copy()
df2 ["E"] = ["one", "one", "two", "three","four","three"]
df2 ["F"] = "1.0"
print(df2)

df2[df2["E"].isin(["two","four"])]'''



import numpy as np

import pandas as pd

# Series - Creating a Series by passing a list of values, letting pandas create a default integer index:

s = pd.Series([1, 3, 5, np.nan, 6, 8])

print(s)
print(s[0])

s1 = pd.Series([1, 3, 5, 6, 8])

print(s1)

# Creating a DataFrame by passing a NumPy array, with a datetime index using date_range() and labeled columns:


dates = pd.date_range("20130101", periods=6)

print(dates)

# random float values
df = pd.DataFrame(np.random.randn(6, 4), index=dates, columns=list("ABCD"))

print(df)

# Creating a DataFrame by passing a dictionary of objects that can be converted into a series-like structure:



df2 = pd.DataFrame(
    {
        "A": 1.0,
        "B": pd.Timestamp("20130102"),
        "C": pd.Series(1, index=list(range(4)), dtype="float32"),
        "D": np.array([3] * 4, dtype="int32"),
        "E": pd.Categorical(["test", "train", "test", "train"]),
        "F": "foo",
    }
)


print(df2)
print(df2.dtypes)


print(df.tail(2))
print("=============")
print(df.head(2))
print("=========")

print(df)


# head and tail
print(df.head(2))

print(df.tail(3))

print(df.index)

print(df.columns)


# while conversion to numpy arrays, compliers omits columns and indexes
print(df.to_numpy())

# with multiple data types,  conversions are expensive

# DataFrame.to_numpy() does not include the index or column labels in the output.

print(df.describe())

print(df2.describe())
# transpose

print(df)

print(df.T)


# sorting

print( df.sort_index(axis=0, ascending=True))


print( df.sort_values(by="B", ascending=False))

# getting values

print(df["A"])

print(df.A)

print(df.B)

# slicing with data frames

print(df[0:3])


# selection - loc() and at()

print(df.loc[dates[0]])

# multi-axis

print(df.loc[:,["A","B"]])

print(df.loc["20130102":"20130104", ["A", "B"]])

print(df.iloc[3:5, 0:2])

print(df.iloc[[1, 2, 4], [0, 2]])

print(df.iloc[:, 1:3])

# Boolean Indexing

print(df[df["A"] > 0])

print(df[df > 0])

print(df)



# is in
df2 = df.copy()

df2["E"] = ["one", "one", "two", "three", "four", "three"]

df2["F"] = "1.0"
print( df2 )




df2[df2["E"].isin(["two", "four"])]


# automatic alignment

print(df)

s1 = pd.Series([1, 2, 3, 4, 5, 6], index=pd.date_range("20130102", periods=6))

print(s1)


df["F"] = s1

print(s1)
print(df)

#Operations

print(df)
print(df.mean())

print (df.mean(1))

s = pd.Series([1, 3, 5, np.nan, 6, 8], index=dates).shift(2)
s
df.sub(s, axis="index")
print(s)

# STRING OPERATIONS

s = pd.Series(["A", "B", "C", "Aaba", "Baca", np.nan, "CABA", "dog", "cat"])
print( s.str.lower())

# concat

df_r = pd.DataFrame(np.random.randn(10, 4))

print(df_r)
print(df_r[:3], df_r[3:7])
print(df_r[7:])

pieces = [df[:3], df[3:7], df[7:]]

pd.concat(pieces)

# join -- works just like sql join

left = pd.DataFrame({"key": ["foo", "foo"], "lval": [1, 2]})

right = pd.DataFrame({"key": ["foo", "foo"], "rval": [4, 5]})
print(left)
print(right)

pd.merge(left, right, on="key")

# Grouping
# Splitting the data into groups based on some criteria
# Applying a function to each group independently
# Combining the results into a data structure

df = pd.DataFrame(
    {
        "A": ["foo", "bar", "foo", "bar", "foo", "bar", "foo", "foo"],
        "B": ["one", "one", "two", "three", "two", "two", "one", "three"],
        "C": np.random.randn(8),
"D": np.random.randn(8),
    }
)

print(df)

df.groupby("A")[["C", "D"]].sum()


print(df.groupby(["A", "B"]).sum())


tuples = list(
    zip(
        ["bar", "bar", "baz", "baz", "foo", "foo", "qux", "qux"],
        ["one", "two", "one", "two", "one", "two", "one", "two"],
    )
)


index = pd.MultiIndex.from_tuples(tuples, names=["first", "second"])

df = pd.DataFrame(np.random.randn(8, 2), index=index, columns=["A", "B"])

df2 = df[:4]

df2

import pandas as pd
import numpy as np

df = pd.DataFrame(
    {
        "A": ["one", "one", "two", "three"] * 3,
        "B": ["A", "B", "C"] * 4,
        "C": ["foo", "foo", "foo", "bar", "bar", "bar"] * 2,
        "D": np.random.randn(12),
        "E": np.random.randn(12),
    }
)

print(df)

# another complex data
print(pd.pivot_table(df, values="D", index=["A", "B"], columns=["C"]))


# time series

rng = pd.date_range("1/1/2012", periods=100, freq="S")

ts = pd.Series(np.random.randint(0, 500, len(rng)), index=rng)

print(ts)

ts.resample("5Min").sum()


import matplotlib.pyplot as plt

plt.close("all")


ts = pd.Series(np.random.randn(1000), index=pd.date_range("1/1/2000", periods=1000))

ts = ts.cumsum()

print(ts)

ts.plot();


df = pd.DataFrame(
    np.random.randn(1000, 4), index=ts.index, columns=["A", "B", "C", "D"]
)

df = df.cumsum()

print(df)

plt.figure();

df.plot();

plt.legend(loc='best');