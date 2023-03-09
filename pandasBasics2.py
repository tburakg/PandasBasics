import pandas as pd
import numpy as np
import seaborn as sns


### 1
df = pd.read_csv("...")

### 2-1

def check_df(dataframe, head = 5):
    print("########### SHAPE ###########")
    print(dataframe.shape)
    print("########### TYPES ###########")
    print(dataframe.dtypes)
    print("########### HEAD ###########")
    print(dataframe.head(head))
    print("########### TAIL ###########")
    print(dataframe.tail(head))
    print("########### NA ###########")
    print(dataframe.isnull().sum())
    print("########### QUENTILES ###########")
    print(dataframe.describe([0, 0.05, 0.5, 0.95, 0.99, 1]).T)

check_df(df)


### 2-2
df["num_gender"] = ["0" if df.gender[i] == "Male" else "1" for i in df.index]
df.loc[:, ["gender", "num_gender"]].head()

### 3

df["NEW_PaperlessBilling"] = df["PaperlessBilling"].apply(lambda x: "Evt" if x == "Yes" else "Hyr")
df.loc[:, ["PaperlessBilling", "NEW_PaperlessBilling"]]

### 4

df["OnlineBackup"].head(12)


def checkConnection(x):
    if x == "Yes":
        return "Evet"
    elif x == "No":
        return "Hayır"
    else:
        return "Interneti_yok"


df["OnlineSecurity"], df["OnlineBackup"] = [df[col].apply(checkConnection) for col in df.columns if 'Online' in col]
df.loc[:, ["OnlineBackup", "OnlineSecurity"]].head(12)

### 5

# TotalCharges kolonu object tipinde olduğu için df[df["TotalCharges"] < 30] şeklinde bir sorgu gönderirsek hata
# alıyoruz Numerik veri tipinde olması gerekiyor

#Fakat direk numerik dğeişkene de çeviremiyoruz çünkü sayısal karşılığı olmayan değerler var örnek -> " " gibi
#öne bu sayısal karşılığı olmayan değerlere string 0 değeri atıyıp ardından hepsini numerik yapıp en sonda ise
#0 olan değerlere ortalama değerleri atıyorum ki veri setimize minimum derecede negatif etki olsun

for index, value in enumerate(df["TotalCharges"]):
    if " " in value:
        df['TotalCharges'][index] = "0"

for index, value in enumerate(df["TotalCharges"]):
    if " " in value:
        print(value)

df["TotalCharges"] = df["TotalCharges"].astype(float)
df[df["TotalCharges"] < 30]

# 0 değerimiz var mı diye son kontrol
for i in df["TotalCharges"]:
    if i == 0:
        print(i)

# Yukarıda bahsettiğim ortalama değer ataması
df["TotalCharges"].mean()
df["TotalCharges"] = [df["TotalCharges"].mean() if df["TotalCharges"][i] == 0 else df["TotalCharges"][i] for i in df.index]
df[df["TotalCharges"] < 30]


### 6
df[df["PaymentMethod"] == "Electronic check"]["MonthlyCharges"].mean()

### 7
df[(df["gender"] == "Female") & ((df["InternetService"] == "Fiber optic") | (df["InternetService"] == "DSL"))]["MonthlyCharges"].sum()

### 8

df["Churn"] = df["Churn"].apply(lambda x: "1" if x == "Yes" else "0")


### 9
df["Churn"] = df["Churn"].astype(float)
df.groupby(["Contract", "PhoneService"])["Churn"].mean()

### 10 pivot table

### 11 cut label ile qcut q ile