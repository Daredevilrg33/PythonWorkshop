#%% Change working directory from the workspace root to the ipynb file location. Turn this addition off with the DataSciece.changeDirOnImportExport setting
import os
try:
	os.chdir(os.path.join(os.getcwd(), 'day-1'))
	print(os.getcwd())
except:
	pass

#%%
word = "ROHIT GUPTA"
letter = word[3]
length = len(word)
tCount = word.count('T')
gIndex = word.index('G')
findZ = word.find('T')
print('Hello World!!!')
print(word)
print(letter)
print(length)
print(tCount)
print(gIndex)
print(findZ)
print(word[0])
print(word[0:1])
print(word[0:3])
print(word[:3])
print(word[-3:])
print(word[3:])
print(word[:-3])


#%%
str = "Rohit's"
print(str)
complex(99 +1j)
a= 9.98
type(a)


#%%
c= False
type(c)


#%%
z= 'I\'m walking'
print(z)
z.upper()


#%%
z.title()


#%%
a = [1,2,3,4,6,"help" , True]
type(a)


#%%
a[6]


#%%
a[0]


#%%
a[5]


#%%
a[0:6]


#%%
a[:3]


#%%
a[:-3]


#%%
a[:]


#%%
a[::-1]


#%%
p="Rohit Gupta"
p[::2]


#%%
p[::-1]


#%%
a[2::-1]


#%%
a.index('help')


#%%
a


#%%
a.index(True)


#%%
a.index(1)


#%%
e="xywz"


#%%
s="abcd"


#%%
i = s.find('b')
e[i]


#%%
if True:
    print('hello inside true block')
else:
    print('else block')


#%%
s = 'hello'
if s=="heo":
    print('hello inside true block')
else:
    print('else block')


#%%

if i!=-1:
    print('hello inside true block')
else:
    print('else block')


#%%
a = ["a","helllo", 'c']


#%%
for item1 in a:
    print(item1)


#%%
s1 = 'abcd'
e='xywz'
user_list = 'ba'


#%%
for user in user_list:
    user_index = s1.find(user)
    if user_index !=-1:
        print(e[user_index])
    else:
        print("not found")


#%%
def encoder (user_list):
    str='';
    for user in user_list:
        user_index = s1.find(user)
        if user_index !=-1:
            str = str+e[user_index]
        else:
            print("not found")
    return str


#%%
def my_sum(s1,s2):
    return s1+s2


#%%
my_sum(123,12)


#%%
my_sum("hell0","world")


#%%
print(encoder("babb"))


#%%
d={'a':1,'b':2,'c': "Hello world",'marks': [1,2,3,4,5],4:"helo"}
type(d)


#%%
d['marks']


#%%
d[4]


#%%
type(d['marks'])


#%%
for item in d:
    print(item) # print keys
    print(d[item]) # print values
    


#%%
import pandas


#%%
df = pandas.DataFrame({'a':[1,2],'b':[3,4]})


#%%
type(df)


#%%
len(df)


#%%
df


#%%
import pandas as pd


#%%
df = pd.read_csv("physician_rx.csv")


#%%
len(df)


#%%
df.head(n=10)


#%%
df.tail(10)


#%%
df.shape


#%%
df.columns


#%%
df.dtypes


#%%
df["PHYSICIAN"]


#%%
df[["PHYSICIAN","AllergyMax_RX"]]


#%%
type(9090909*9999999*6755658889894545)


#%%
df[["PHYSICIAN","AllergyMax_RX"]][0:4]


#%%
df[["PHYSICIAN","AllergyMax_RX"]][::-9]


#%%
type(231)


#%%
type(231)


#%%
df.loc[0:4,"PHYSICIAN":"AllergyMax_RX"]


#%%
df.iloc[0:4,0:3]


#%%
# import pandas alias pd


#%%
import pandas as pd


#%%
df = pd.read_csv("physician_rx.csv")


#%%
len(df)


#%%
df.loc[0:4,"PHYSICIAN":"AllergyMax_RX"]


#%%
df.iloc[0:4,0:3]


#%%
df["CroMax_RX"] >50


#%%
my_df = df[df["CroMax_RX"] > 50]


#%%
my_df[my_df["GlycoMax_RX"] > 50]


#%%
df[df["CroMax_RX"] > 50]


#%%
my_df[my_df["GlycoMax_RX"] > 50]


#%%
len(df[(df["GlycoMax_RX"] > 50) & (df["CroMax_RX"] > 50)]["PHYSICIAN"])


#%%
(df["GlycoMax_RX"] > 50) & (df["CroMax_RX"] > 50)


#%%
df.loc[0:0,["PHYSICIAN"]]


#%%
df.iloc[0:1,0:1]


#%%
df.iat[0,0]


#%%
df.at[0,"PHYSICIAN"]


#%%
df.isnull().sum()


#%%
df[df["CroMax_RX"].isnull()] # find the null value records for CroMax_RX


#%%
df["CroMax_RX"] = df["CroMax_RX"].fillna(0)


#%%
df.isnull().sum()


#%%
df = df.dropna()


#%%
df.isnull().sum()


#%%
len(df)


#%%
df.columns = ['PHY', 'CroMax_RX', 'GlycoMax_RX', 'AllergyMax_RX', 'FevMax_RX','ColdMax_RX']


#%%
df.head()


#%%
df = df.rename(columns={'PHY':'PHYSICIAN'})


#%%
df.head()


#%%
"hello world".replace("l","z")


#%%
df.columns.str.replace("_",".")


#%%
df["PHYSICIAN"] = df["PHYSICIAN"].str.replace("AP","AB")


#%%
df.head()


#%%
df["bucket"] = "B1"


#%%
df.head()


#%%
my_df = df[(df["GlycoMax_RX"] > 50) & (df["CroMax_RX"] > 50)]


#%%
my_df["bucket"] = "B2"


#%%
my_df.head()


#%%
df = my_df


#%%
df.head()


#%%
df = pd.read_csv("physician_rx.csv")


#%%
df["CroMax_RX"] = df["CroMax_RX"].fillna(0)


#%%
df = df.dropna()


#%%
len(df)


#%%
df[(df["GlycoMax_RX"] > 50) & (df["CroMax_RX"] > 50)]


#%%
df["bucket"] = "B1"


#%%
df


#%%
df[(df["GlycoMax_RX"] > 50) & (df["CroMax_RX"] > 50)]["bucket"] = "B2"


#%%
(df[(df["GlycoMax_RX"] > 50) & (df["CroMax_RX"] > 50)])["bucket"] = "B2"


#%%
df["bucket"] = "B2"


#%%
df.head()


#%%
len(df)


#%%
df.loc[(df["GlycoMax_RX"] > 50) & (df["CroMax_RX"] > 50),"bucket"] = "B1"


#%%
df


#%%
df["new_physician"] = df["bucket"] + "_" + df["PHYSICIAN"]


#%%
df.head()


#%%
df.columns


#%%
df.columns = ['new_physician', 'CroMax_RX', 'GlycoMax_RX', 'AllergyMax_RX', 'FevMax_RX','ColdMax_RX', 'bucket', 'PHYSICIAN']


#%%
df.head()


#%%
df["new_physician"] = df['PHYSICIAN']


#%%
df.head()


#%%
del df["PHYSICIAN"]


#%%
df


#%%
df.columns


#%%
df = df[['new_physician', 'CroMax_RX', 'GlycoMax_RX', 'AllergyMax_RX',
       'FevMax_RX', 'ColdMax_RX']]


#%%
df.head()


#%%
df["new_physician"].str.split("_")


#%%

df["physician"] = df["new_physician"].str.split("_").str[1]
df["bucket"] = df["new_physician"].str.split("_").str[0]


#%%
df.head()


#%%
type(6698736875387538583585385853853)


#%%


#%%



