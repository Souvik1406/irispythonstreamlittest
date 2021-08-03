import pandas as pd
import streamlit as st

from PIL import Image
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split

# Model
df = pd.read_csv("IRIS.csv")

X = df.drop(columns=["species"])
y = df["species"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=42)

rf = RandomForestClassifier()
rf.fit(X_train, y_train)

# Streamlit
st.header("Iris Classification")

image = Image.open("iris.jpg")
st.image(image, use_column_width=True, output_format="jpg")

st.write("Please insert values, to get Iris class prediction")

SepalLengthCm = st.slider('SepalLengthCm:', 2.0, 6.0)
SepalWidthCm = st.slider('SepalWidthCm:', 0.0, 5.0)
PetalLengthCm = st.slider('PetalLengthCm',0.0, 3.0)
PetalWidthCm = st.slider('PetalWidthCm:', 0.0, 2.0)
data = {'SepalLengthCm': SepalLengthCm,
        'SepalWidthCm': SepalWidthCm,
        'PetalLengthCm': PetalLengthCm,
        'PetalWidthCm': PetalWidthCm}

features = pd.DataFrame(data, index=[0])
prediction = rf.predict(features)
percentages = rf.predict_proba(features)

st.subheader("Prediction")
st.write(prediction[0])

st.subheader("Probabilities of all classes")
st.write("Iris-setosa: ", percentages[0][0]*100)
st.write("Iris-versicolor: ", percentages[0][1]*100)
st.write("Iris-virginica: ", percentages[0][2]*100)

st.text("")
st.text("")
st.text("")

st.info('This is a purely informational message. If you click the button below, there will be celebration!')
if st.button('Click for celebration'):
    st.balloons()
    st.balloons()
