# Part 4
import streamlit as st
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = sns.load_dataset("iris")

st.title("🌸 Iris Data Explorer")
st.write("Simple exploration of the famous Iris dataset")

# Sidebar filters
species = st.sidebar.multiselect("Select species", options=df["species"].unique(), default=df["species"].unique())
filtered_df = df[df["species"].isin(species)]

# Show dataset
st.subheader("Dataset Sample")
st.write(filtered_df.head())

# Visualization 1: Count plot
st.subheader("Count of Samples per Species")
fig, ax = plt.subplots()
sns.countplot(x="species", data=filtered_df, ax=ax)
st.pyplot(fig)

# Visualization 2: Scatterplot
st.subheader("Sepal Length vs Sepal Width")
fig, ax = plt.subplots()
sns.scatterplot(x="sepal_length", y="sepal_width", hue="species", data=filtered_df, ax=ax)
st.pyplot(fig)

# Visualization 3: Correlation heatmap
st.subheader("Correlation Heatmap")
fig, ax = plt.subplots(figsize=(6,4))
sns.heatmap(filtered_df.drop(columns="species").corr(), annot=True, cmap="coolwarm", ax=ax)
st.pyplot(fig)
