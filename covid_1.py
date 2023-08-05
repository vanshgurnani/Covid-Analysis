# -*- coding: utf-8 -*-
"""COVID_1.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/144I-f5_CJxfeowl3K8Sv5h_2FtPXuAJd
"""

import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

df=pd.read_csv('/content/COVID - COVID.csv',encoding='latin').drop([0], axis=0)
df.head(3)

df=df.dropna()

df=df.drop(['NAME OF THE PATIENT','HOSPITAL NAME','SR NO','REG NO','COMPLAINTS','DIRECT BILIRUBIN',
            'HYPOTHYROIDISM','TOCI DAY from Admission','COVID19 POSITIVE NEGATIVE','PROCAL',
            'DIRECT BILIRUBIN','BAROTRUMA','barotrauma INCIDENCE','Toci Day from COVID symptoms','CKD','MALIGNANCY',
            'TOCI','RESPIRATORY DISORDERS','TYPE OF BAROTRAUMA','LMWH Heparin','INTUBATION Required','INTUBATION ON day from admission','HFNC NIV CPAP'
            ,'WAVE','Inhospital outcome','Outcome in ICU'],axis=1)

df['hb']=df['Hb'].replace(['MISSING'],0)
df['tlc']=df['TLC'].replace(['MISSING'],0)
df['crp']=df['CRP'].replace(['MISSING'],0)
df['d dimer']=df['D DIMER'].replace(['MISSING'],0)
df['creatinine']=df['CREATININE'].replace(['MISSING'],0)

df['il6']=df['IL6'].replace(['MISSING'],0)
df['ldh']=df['LDH'].replace(['MISSING'],0)
df['ferritin']=df['FERRITIN'].replace(['MISSING'],0)
df['total bilirubin']=df['Total Bilirubin'].replace(['MISSING'],0)
df['alt']=df['ALT'].replace(['MISSING'],0)
df['ast']=df['AST'].replace(['MISSING'],0)
df['albumin']=df['ALBUMIN'].replace(['MISSING'],0)

df=df.drop(['Hb','TLC','CRP','D DIMER','CREATININE','IL6','LDH','FERRITIN','Total Bilirubin','ALT','AST','ALBUMIN'],axis=1)

df['hb']=df['hb'].astype(str).astype(float)
df['tlc']=df['tlc'].astype(str).astype(float)
df['crp']=df['crp'].astype(str).astype(float)
df['d dimer']=df['d dimer'].astype(str).astype(float)
df['creatinine']=df['creatinine'].astype(str).astype(float)

df['il6']=df['il6'].astype(str).astype(float)
df['ldh']=df['ldh'].astype(str).astype(float)
df['ferritin']=df['ferritin'].astype(str).astype(float)
df['total bilirubin']=df['total bilirubin'].astype(str).astype(float)
df['alt']=df['alt'].astype(str).astype(float)
df['ast']=df['ast'].astype(str).astype(float)
df['albumin']=df['albumin'].astype(str).astype(float)

df['hb'].mean()
df['hb'] = df['hb'].replace([0],df['hb'].mean())

df['tlc'].mean()
df['tlc'] = df['tlc'].replace([0],df['tlc'].mean())

df['crp'].mean()
df['crp'] = df['crp'].replace([0],df['crp'].mean())

df['d dimer'].mean()
df['d dimer'] = df['d dimer'].replace([0],df['d dimer'].mean())

df['creatinine'].mean()
df['creatinine'] = df['creatinine'].replace([0],df['creatinine'].mean())

df['il6'].mean()
df['il6'] = df['il6'].replace([0],df['il6'].mean())

df['ldh'].mean()
df['ldh'] = df['ldh'].replace([0],df['ldh'].mean())

df['ferritin'].mean()
df['ferritin'] = df['ferritin'].replace([0],df['ferritin'].mean())

df['total bilirubin'].mean()
df['total bilirubin'] = df['total bilirubin'].replace([0],df['total bilirubin'].mean())


df['alt'].mean()
df['alt'] = df['alt'].replace([0],df['alt'].mean())

df['ast'].mean()
df['ast'] = df['ast'].replace([0],df['ast'].mean())

df['albumin'].mean()
df['albumin'] = df['albumin'].replace([0],df['albumin'].mean())

# df['HRCT_score']=df['HRCT_score'].apply(lambda x:)

df['hrct']=df['HRCT_score'].replace(['MISSING'],0)

df['hrct']=df['hrct'].apply(lambda x:str(x)[-2:])

df['hrct']=df['hrct'].replace(['ne'],0)

df['hrct']=df['hrct'].astype(str).astype(int)

df=df.drop(['HRCT_score'],axis=1)

df['doa']=pd.to_datetime(df['DATE OF ADMISSION'])
df['dod']=pd.to_datetime(df['DATE OF DISCHARGE'])

df['doam']=df['doa'].apply(lambda time:time.month)
df['doadw']=df['doa'].apply(lambda time:time.dayofweek)

df['dodm']=df['dod'].apply(lambda time:time.month)
df['doddw']=df['dod'].apply(lambda time:time.dayofweek)

print(df['doam'].value_counts())
print(df['doadw'].value_counts())
print(df['dodm'].value_counts())
print(df['doddw'].value_counts())

sns.countplot(x='doadw',data=df)

sns.countplot(x='doddw',data=df)

df=df.drop(['DATE OF ADMISSION','DATE OF DISCHARGE'],axis=1)

df['swab']=pd.to_datetime(df['SWAB SENT ON'])
df['swabm']=df['swab'].apply(lambda time:time.month)
df['swabdw']=df['swab'].apply(lambda time:time.dayofweek)
df=df.drop(['SWAB SENT ON'],axis=1)

print(df['swabm'].value_counts())
print(df['swabdw'].value_counts())

sns.countplot(x='swabdw',data=df)

df['Fever']=df['Fever'].replace(['MISSING'],'NO')

print(df['Fever'].value_counts())
print(df['Cough'].value_counts())
print(df['Sore throat'].value_counts())
print(df['Myalgia bodyache'].value_counts())
print(df['Breathlessness'].value_counts())

df['Other symptoms'].value_counts()

df['DM']=df['DM'].replace(['MISSING'],'NO')
df['DM'].value_counts()

print(df['HTN'].value_counts())
df['IHD']=df['IHD'].replace(['MISSING'],'NO')
print(df['IHD'].value_counts())

df['lenICUstay']=df['Length of ICU stay in days'].replace(['NO','no','No'],0)
df=df.drop(['Length of ICU stay in days'],axis=1)

df['lenHOSstay']=df['Length of Hospital stay in days'].replace(['MISSING'],0)
df=df.drop(['Length of Hospital stay in days'],axis=1)

df['std']=df['Steroid Total Duration'].apply(lambda x:str(x).split('DAYS')[:1])

df['std']=df['std'].apply(lambda x:str(x).join(x))

df['std']=df['std'].replace(['NO'],0).replace(['09 days'],9)

df=df.drop(['Steroid Total Duration'],axis=1)

df['steroidtype']=df['Steroid Type'].replace(['MISSING'],'NO')
df=df.drop(['Steroid Type'],axis=1)

df['steroidtype'].value_counts()

sns.countplot(df['lenICUstay'],data=df)

df['Steroid']=df['Steroid'].replace(['Y','INJDEXA 6MG OD'],'YES')

df['Steroid'].value_counts()

df=df.drop(['Steoid dose  day','Steroid started on Day'],axis=1)

df['COVID symptom start time before admission']=df['COVID symptom start time before admission'].replace(['MISSING'],'23.09.2020')

df['COVID symptom start time before admission']=pd.to_datetime(df['COVID symptom start time before admission'])

df['covid symp month']=df['COVID symptom start time before admission'].apply(lambda time:time.month)
df['covid symp dw']=df['COVID symptom start time before admission'].apply(lambda time:time.dayofweek)

df=df.drop(['COVID symptom start time before admission'],axis=1)

df['Fever'].value_counts()

df['Cough'].value_counts()

df['Sore throat'].value_counts()

df['Myalgia bodyache'].value_counts()

df['Breathlessness'].value_counts()

df['Other symptoms']=df['Other symptoms'].replace(['HEADACHE','GIDDINESS','ALTERED TASTE','ALTERTED TASTE','LOSS OF TASTE','WEAKNESS,LOSS OF APPETITE'],'Y')

df['Other symptoms'].value_counts()

df['DM'].value_counts()

df['HTN'].value_counts()

df['IHD'].value_counts()

df=df.drop(['SpO2 on admission','doa','dod','swab'],axis=1)

df['Oxygen requirement']=df['Oxygen requirement'].replace(['Y','4 Lit.','6LIT','8 LIT','50% FIO2','y'],'YES')

df['Oxygen requirement']=df['Oxygen requirement'].replace(['No'],'NO')

df['Oxygen requirement'].value_counts()

df=df.drop(['Oxygen delivery mode','SEX'],axis=1)

df['Fever']=df['Fever'].replace('YES',1).replace('NO',0)
df['Fever'].value_counts()

df['Cough']=df['Cough'].replace('YES',1).replace('NO',0)
df['Cough'].value_counts()

df['Sore throat']=df['Sore throat'].replace('YES',1).replace('NO',0)
df['Sore throat'].value_counts()

df['Myalgia bodyache']=df['Myalgia bodyache'].replace('YES',1).replace('NO',0)
df['Myalgia bodyache'].value_counts()

df['Breathlessness']=df['Breathlessness'].replace('YES',1).replace('NO',0)
df['Breathlessness'].value_counts()

df['Other symptoms']=df['Other symptoms'].replace('Y',1).replace('N',0)
df['Other symptoms'].value_counts()

df['DM']=df['DM'].replace('YES',1).replace('NO',0)
df['DM'].value_counts()

df['HTN']=df['HTN'].replace('YES',1).replace('NO',0)
df['HTN'].value_counts()

df['IHD']=df['IHD'].replace('YES',1).replace('NO',0)
df['IHD'].value_counts()

df['Oxygen requirement']=df['Oxygen requirement'].replace('YES',1).replace('NO',0)
df['Oxygen requirement'].value_counts()

df['Steroid']=df['Steroid'].replace('YES',1).replace('NO',0)
df['Steroid'].value_counts()

df['std']=df['std'].astype(str).astype(int)

df['lenICUstay']=df['lenICUstay'].astype(str).astype(int)

df['lenHOSstay']=df['lenHOSstay'].astype(str).astype(int)

df=df.drop(['steroidtype'],axis=1)

df.info()

from sklearn.model_selection import train_test_split

X = df.drop('AGE',axis=1).values
y = df['AGE'].values

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.20, random_state=101)

from sklearn.preprocessing import MinMaxScaler

scaler=MinMaxScaler()

X_train = scaler.fit_transform(X_train)

X_test = scaler.transform(X_test)

import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Activation,Dropout
from tensorflow.keras.constraints import max_norm

model=Sequential()

model.add(Dense(78,activation='relu'))
model.add(Dropout(0.2))

model.add(Dense(39,activation='relu'))
model.add(Dropout(0.2))

model.add(Dense(19,activation='relu'))
model.add(Dropout(0.2))

model.add(Dense(units=1,activation='sigmoid'))

model.compile(loss='binary_crossentropy',optimizer='adam')

model.fit(x=X_train, y=y_train, batch_size=256, epochs=25,validation_data=(X_test,y_test))

from tensorflow.keras.models import load_model

model.save('project.h5')

loss=pd.DataFrame(model.history.history)

loss

loss[['loss','val_loss']].plot()

from sklearn.metrics import classification_report,confusion_matrix

predict=model.predict(X_test)
classes=np.argmax(predict,axis=1)

print(confusion_matrix(y_test,classes))

import random
random.seed(101)
random_ind = random.randint(0,len(df))

new = df.drop('AGE',axis=1).iloc[random_ind]
new

model.predict(new.values.reshape(1,36))