import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load sample dataset
@st.cache_data
def load_data():
    return sns.load_dataset("iris")  # built-in dataset

df = load_data()

st.title("📊 Visualization Explorer")

# Step 1: Dimension selection
dim_choice = st.sidebar.selectbox(
    "Select Dimension Type",
    ["One Dimensional", "Two Dimensional", "Multi Dimensional"]
)

# Step 2: Visualization options based on dimension
if dim_choice == "One Dimensional":
    viz_choice = st.sidebar.selectbox(
        "Select Visualization Technique",
        ["Histogram", "Boxplot", "Countplot"]
    )

    col = st.selectbox("Select a Column", df.columns)

    if viz_choice == "Histogram":
        fig, ax = plt.subplots()
        ax.hist(df[col], bins=20, color="skyblue", edgecolor="black")
        ax.set_title(f"Histogram of {col}")
        st.pyplot(fig)

    elif viz_choice == "Boxplot":
        fig, ax = plt.subplots()
        sns.boxplot(x=df[col], ax=ax, color="lightgreen")
        ax.set_title(f"Boxplot of {col}")
        st.pyplot(fig)

    elif viz_choice == "Countplot":
        fig, ax = plt.subplots()
        sns.countplot(x=df[col], ax=ax, palette="Set2")
        ax.set_title(f"Countplot of {col}")
        st.pyplot(fig)

elif dim_choice == "Two Dimensional":
    viz_choice = st.sidebar.selectbox(
        "Select Visualization Technique",
        ["Scatterplot", "Lineplot", "Barplot"]
    )

    x_col = st.selectbox("Select X-axis Column", df.columns)
    y_col = st.selectbox("Select Y-axis Column", df.columns)

    if viz_choice == "Scatterplot":
        fig, ax = plt.subplots()
        sns.scatterplot(x=df[x_col], y=df[y_col], hue=df["species"], ax=ax)
        ax.set_title(f"Scatterplot of {x_col} vs {y_col}")
        st.pyplot(fig)

    elif viz_choice == "Lineplot":
        fig, ax = plt.subplots()
        sns.lineplot(x=df[x_col], y=df[y_col], ax=ax)
        ax.set_title(f"Lineplot of {x_col} vs {y_col}")
        st.pyplot(fig)

    elif viz_choice == "Barplot":
        fig, ax = plt.subplots()
        sns.barplot(x=df[x_col], y=df[y_col], ax=ax)
        ax.set_title(f"Barplot of {x_col} vs {y_col}")
        st.pyplot(fig)

elif dim_choice == "Multi Dimensional":
    viz_choice = st.sidebar.selectbox(
        "Select Visualization Technique",
        ["Pairplot", "Heatmap"]
    )

    if viz_choice == "Pairplot":
        st.write("Pairplot of all numerical columns")
        fig = sns.pairplot(df, hue="species")
        st.pyplot(fig)

    elif viz_choice == "Heatmap":
        st.write("Heatmap of Correlation Matrix")
        fig, ax = plt.subplots()
        sns.heatmap(df.corr(), annot=True, cmap="coolwarm", ax=ax)
        st.pyplot(fig)
