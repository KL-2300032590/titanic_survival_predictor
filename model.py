import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import joblib

data = pd.read_csv("titanic.csv")

data = data[["Pclass","Sex","Age","SibSp","Fare","Survived"]]
data.dropna(inplace=True)

data["Sex"] = data["Sex"].map({"male":0,"female":1})


x = data.drop("Survived",axis=1)
y = data["Survived"]

x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.2,random_state=42)

model = RandomForestClassifier()
model.fit(x_train,y_train)
joblib.dump(model,"model.pkl")
print("Model saved as model.pkl")
