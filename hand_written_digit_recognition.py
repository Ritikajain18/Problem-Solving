import matplotlib.pyplot as plt
%matplotlib inline
from sklearn.datasets import load_digits
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix
import seaborn as sn

digits = load_digits()
X_train,X_test, y_train, y_test = train_test_split(digits.data, digits.target, train_size = 0.8)

model = LogisticRegression()
model.fit(X_train, y_train)

model.score(X_test, y_test)

y_predicted = model.predict(X_test)
cm = confusion_matrix(y_test, y_predicted)
plt.figure(figsize = (10,7))
sn.heatmap(cm, annot = True)
plt.xlabel("prediction")
plt.ylabel('truth')
