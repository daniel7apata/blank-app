import streamlit as st
import pandas as pd
import openpyxl
import joblib
from sklearn.preprocessing import OneHotEncoder
from sklearn.preprocessing import MinMaxScaler
import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.linear_model import LinearRegression
from sklearn.metrics import roc_auc_score,confusion_matrix,f1_score,accuracy_score,recall_score,precision_score,classification_report
from sklearn.metrics import mean_absolute_error, mean_squared_error,r2_score, mean_absolute_percentage_error

# Título de la aplicación
st.title("Web Scrapping")

url = st.text_input()

