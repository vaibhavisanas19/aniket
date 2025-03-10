import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Streamlit App Title
st.title("Graph Plotter from Uploaded File")

# File Upload
uploaded_file = st.file_uploader("Upload a file (TXT/CSV with numerical data)", type=["txt", "csv"])

if uploaded_file is not None:
    try:
        # Read file as a DataFrame (detecting delimiter automatically)
        df = pd.read_csv(uploaded_file, sep=None, engine="python")

        # Show preview of uploaded data
        st.write("Preview of uploaded data:")
        st.dataframe(df.head())

        # Ensure the file has at least two numerical columns
        if df.shape[1] < 2:
            st.error("Error: The file must contain at least two numerical columns.")
            st.stop()

        # Let the user select columns for X and Y axes
        x_col = st.selectbox("Select X-axis column", df.columns, index=0)
        y_col = st.selectbox("Select Y-axis column", df.columns, index=1)

        # Plot Graph
        fig, ax = plt.subplots(figsize=(8, 6))
        ax.plot(df[x_col], df[y_col], marker="o", linestyle="-", color="b", label=f"{y_col} vs {x_col}")
        ax.set_xlabel(x_col)
        ax.set_ylabel(y_col)
        ax.set_title("Graph from Uploaded File")
        ax.legend()
        ax.grid(True)

        # Display graph in Streamlit
        st.pyplot(fig)

    except Exception as e:
        st.error(f"Error processing file: {e}")
