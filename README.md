#  Titanic Survival Predictor

This is a simple machine learning project that predicts whether a passenger would have survived the Titanic disaster or not, based on some features like gender, age, and class. This project is built using Python, Streamlit, and scikit-learn.

## Live Demo -[https://basictitanicsurvivalpredictor.streamlit.app/]
## 🔧 What I Did

###  model.py
- Loaded the Titanic dataset (`titanic.csv`)
- Selected useful columns like `Pclass`, `Sex`, `Age`, etc.
- Converted `Sex` column from text to number (male: 1, female: 0)
- Filled missing age values
- Trained a Random Forest Classifier
- Saved the trained model as `model.pkl`

### app.py
- Built a simple UI using Streamlit
- Took user input for `Pclass`, `Sex`, `Age`, `SibSp`, `Parch`, and `Fare`
- Loaded the trained model
- Predicted if the person would survive or not
- Displayed the result
