import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier

wine = pd.read_csv('https://bit.ly/wine_csv_data')



'''
pandas 라이브러리는 csv 파일을 읽으면 데이터 프레임 객체로 반환을 해 준다.
'''
print(wine.head())
print(wine.info())
print(wine.describe())

data = wine[['alcohol', 'sugar', 'pH']].to_numpy()
target = wine['class'].to_numpy()

'''
지도 학습:머신러닝 5장, 비지도 학습:머신러닝 6장

'''
train_input,test_input,train_traget,test_target = train_test_split(data,target, random_state=42)


ss = StandardScaler()
ss.fit(train_input)

train_scaled = ss.transform(train_input)
test_scaled = ss.transform(test_input)

lr=LogisticRegression()
lr.fit(train_scaled,train_traget)

train_score = lr.score(train_scaled,train_traget)
test_score = lr.score(test_scaled,test_target)

print('훈련점수',train_score,'테스트점수',test_score)

# 9.4,1.9,3.51 ->0

preclass = lr.predict(
    ss.transform(
    [[9.4,1.9,3.51],[9.9,1.6,3.58],[12.2,4.45,3.25]]
    )
)
print('예측값', preclass)


dtclf= DecisionTreeClassifier();
preclass2 = dtclf.predict(
    ss.transform(
    [[9.4,1.9,3.51],[9.9,1.6,3.58],[12.2,4.45,3.25]]
    )
)
print('예측값', preclass2)

import matplotlib.pyplot as plt
from sklearn.tree import plot_tree

'''
plt.figure(figsize=(10,7),dpi=50)
plot_tree(dtclf)
plt.show()
'''