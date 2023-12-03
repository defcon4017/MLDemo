import streamlit as st
import pandas as pd
import numpy as np
from tensorflow.python.keras.layers import Dense
from tensorflow.python.keras import Sequential

# Build model
model = Sequential()
model.add(Dense(1)) 
model.compile(loss='mse')  

st.write("ML Application")
