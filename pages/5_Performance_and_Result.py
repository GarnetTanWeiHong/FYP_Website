import streamlit as st

def main():
    # Set the page configuration with a title and an icon
    st.set_page_config(page_title="Performance and Result", page_icon="📊")

    # Display the main header for the page
    st.write("# Performance and Result")

    # Display the header in the sidebar
    st.sidebar.header("Performance and Result")

    # Provide an introductory description of the page
    st.write(
        """This page showcases the performance and result that we gained from all the models that we examined."""
    )

    # List the metrics used to measure the model performance
    st.write("### Metric to measure the model")
    st.write("1. Accuracy")
    st.write("2. Good Unit Test")
    st.write("3. Defect Ability")
    st.write("4. Over-rejection Test")

    # Display the results of the metrics on the three models
    st.write("### The result of 4 metrics on 3 models")
    st.image("./Images Source/table_of_result.jpg")

    # Placeholder for box plots for each defect type
    st.write("### Box Plot for each Defect Type")
    st.write("Here will be 6 boxplots")

    # Display line chart for training epoch (Precision)
    st.write("### Line Chart for training epoch (maybe Precision)")
    st.image("./Images Source/Precision Training Path.png")
    
    # Display line chart for training epoch (Loss)
    st.write("### Line Chart for training epoch (Loss)")
    st.image("./Images Source/Seg_loss.png")

    # Display progress line for defect coverage
    st.write("### Progress line for defect coverage")
    st.image("./Images Source/Defect Type Completion Progress.png")

# Run the main function when the script is executed
if __name__ == '__main__':
    main()
