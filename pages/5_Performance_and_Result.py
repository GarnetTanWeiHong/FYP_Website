from os import write
from IPython.utils.contexts import NoOpContext
import streamlit as st
from streamlit.elements import image

def main():
    st.set_page_config(page_title="Performance and Result", page_icon="📊")

    st.write("# Performance and Result")
    st.sidebar.header("Performance and Result")
    st.write(
        """This page showcases the performance and result that we gained from the all the model that we examined."""
    )

    st.write("### Metric to measure the model")
    st.write("1. Accuracy")
    st.write("2. Good Unit Test")
    st.write("3. Defect Ability")
    st.write("4. Over-rejection Test")

    st.write("### The result of 4 metric on 3 model ")
    st.image("/content/drive/MyDrive/Dashboard Code and Screenshots/Images Source/table_of_result.jpg")

    st.write("### Box Plot for each Defect Type")
    st.write("Here will be 6 boxplot")

    st.write("### Line Chart for training epoch (maybe Precision)")
    st.image("/content/drive/MyDrive/Dashboard Code and Screenshots/Images Source/Precision Training Path.png")
    
    
    st.write("### Line Chart for training epoch (Loss)")
    st.image("/content/drive/MyDrive/Dashboard Code and Screenshots/Images Source/Seg_loss.png")

    st.write("### Progress line for defect coverage")
    st.image("/content/drive/MyDrive/Dashboard Code and Screenshots/Images Source/Defect Type Completion Progress.png")
    
    



if __name__ == '__main__':
    main()