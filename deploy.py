import streamlit as st
import os
import subprocess

EXECUTABLE="translator/test_res"
INPUT="tmp/in.txt"
OUTPUT="tmp/out.txt"

def make_result(line):
    res = st.empty()
    res.info(line)

args = (EXECUTABLE, "<", INPUT, ">", OUTPUT)
cmd = " ".join(args)

st.set_page_config(
    page_title="hs094's Query Optimizer",
    page_icon="😎",
    layout="wide"
)

st.title('Query Optimizer')
st.header('Compiling queries')

sb = st.sidebar

with sb:
    st.subheader("How It Works")
    st.write("""
    1. **Input Query**: Enter your query in the text input box or upload a query file.
    2. **Compilation**: The query is compiled using a C++ backend.
    3. **Optimization**: Various optimization techniques are applied to enhance query performance.
    4. **Execution**: The optimized query is executed, and results are generated.
    5. **Results**: View the results directly in the application.
    """)

col1, col2 = st.columns(2)

with col1:
    custom_query = st.text_input("Enter Query")

with col2:
    file_upload = st.file_uploader("Upload query file")


compile = st.button("Optimize query")

results = st.empty()

if compile:

    custom_query = custom_query.strip()
    print("custom =", custom_query)

    if file_upload is not None:
        custom_query = file_upload.getvalue().decode("utf-8")
        results.warning("Query uploaded from file.")

    with open(INPUT, "w") as f:
        f.write(custom_query)

    subprocess.run(["python", "call.py"])

    with open(OUTPUT, "r") as f:
        for line in f:
            if line != '\n':
                make_result(line)
