import streamlit as st
import tensorflow as tf
import numpy as np
from PIL import Image

st.title("🧠 Handwritten Digit Classifier")

model = tf.keras.models.load_model("mnist_model.h5")

uploaded_file = st.file_uploader("Upload a digit image (28x28)", type=["png", "jpg", "jpeg"])
if uploaded_file:
    image = Image.open(uploaded_file).convert("L").resize((28,28))
    img_array = np.array(image).reshape(1,28,28,1) / 255.0
    prediction = np.argmax(model.predict(img_array))
    st.write(f"Predicted Digit: **{prediction}**")
