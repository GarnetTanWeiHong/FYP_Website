import os

import streamlit as st

from PIL import Image

from ultralytics import YOLO

# Define the paths to your YOLOv8 model files
v4_model_path = "./Model Source/v4_best.pt"  # Replace with your actual path
v8_model_path = "./Model Source/v8_best.pt"
v9_model_path = "./Model Source/v9_best.pt"

# Load the YOLOv8 models
v4_model = YOLO(v4_model_path)
v8_model = YOLO(v8_model_path)
v9_model = YOLO(v9_model_path)

# Open a temporary image
temp_img = Image.open("./Images Source/table_of_result.jpg") 

# Define the image prediction function
def predict_image(image, model, msg):
    # Make predictions using the YOLOv8 model
    results = model(image)
    
    # Process the predictions and save the result image
    for result in results:
        result.save(filename='./Images Source/result.jpg') # display to screen
        st.image("./Images Source/result.jpg", use_column_width=True, caption=msg)
        
    # Save the temporary image to overwrite the result image
    temp_img.save("./Images Source/result.jpg")
    return results

# Define the Streamlit subpage for image prediction
def image_prediction_subpage(uploaded_file):
    # Check if an image file is uploaded
    if uploaded_file is not None:
        # Open the uploaded image
        image = Image.open(uploaded_file)

        # Create columns for displaying images and predictions
        col1, col2, col3, col4 = st.columns(4)

        # Display the uploaded image in the first column
        with col1: 
            st.image(image, caption=uploaded_file.name, use_column_width=True)

        # Display predictions for each model in the respective columns
        with col2:
            msg = "Model A Prediction Result"
            prediction = predict_image(image, v4_model, msg)
        
        with col3:
            msg = "Model B Prediction Result"
            prediction = predict_image(image, v8_model, msg)

        with col4:
            msg = "Model C Prediction Result"
            prediction = predict_image(image, v9_model, msg)
        
        st.write("")  # Add a spacer for readability
        return True  # Return True indicating successful prediction
    return False  # Return False if no file is uploaded

# Define the main function for the Streamlit app
def main():
    # Set the page configuration with a title and an icon
    st.set_page_config(page_title="Predict Your Defect", page_icon="📈")
    
    # Set the title of the page
    st.title("PCB Defect Detection with YOLOv8")

    # Provide descriptions of the models
    st.write("""Model A: Epoxy Overflow, Missing Die, Missing LED, Missing Wire.  
                Model B: Cracking.  
                Model C: Misplacement.""")

    # Allow the user to upload multiple image files
    uploaded_file = st.file_uploader("Choose image...", type=["jpg", "png", "jpeg"], accept_multiple_files=True)
    predict = False  # Initialize the prediction flag
    result = False  # Initialize the result flag

    # Check if files are uploaded and enable the detect button
    if uploaded_file:
        result = st.button('Detect')

    # Perform prediction if the detect button is pressed
    if result:
        # Display a centered starting message
        st.markdown("<h1 style='text-align: center;'>Starting Defect Detection Process</h1>", unsafe_allow_html=True)
        iterate = 1  # Initialize the iteration counter
        
        # Iterate through each uploaded file and perform predictions
        for each_uploaded_file in uploaded_file: 
            centered_text = st.container()
            centered_text.markdown(
                f"""<h1 style="text-align: center; font-size: 1rem"> --- Iteration of Image: {iterate} --- </h1>""", 
                unsafe_allow_html=True
            )
            predict = image_prediction_subpage(each_uploaded_file)
            iterate += 1
        
        # Display the prediction result message
        if predict:
            st.write("Prediction done for image(s)")
        else:
            st.write("There was an error")

        result = False  # Reset the result flag

# Run the main function when the script is executed
if __name__ == '__main__':
    main()
