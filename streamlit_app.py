import streamlit as st
import pandas as pd
from sklearn.model_selection import  train_test_split
from sklearn.metrics import accuracy_score
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
import category_encoders as ce
import ploty.express as px

st.set_page_config(page_title="🐧 Penguin Classifier", layout="wide")
st.title('🐧 Penguin Classifier - Обучение и предсказивание')
st.write("## Работа с датасетом пингвинов")

df = pd.read_csv("")
