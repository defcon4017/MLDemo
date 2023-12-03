import streamlit as st
import numpy as np

# Sample data
X = np.array([1000, 1500, 2000]) 
y = np.array([500000, 750000, 1000000])

# Linear regression model
def predict(size, weight, bias):
  return weight * size + bias

# Train parameters  
weight = (np.mean(y) - np.mean(X)) / np.var(X)
bias = np.mean(y) - weight * np.mean(X)

# Streamlit app
size = st.number_input("Size", min_value=100, max_value=5000, value=1000)
price = predict(size, weight, bias) 

st.write(f"Predicted Price: {price}")
