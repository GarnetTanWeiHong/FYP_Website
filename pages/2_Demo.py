

import streamlit as st

from PIL import Image

from ultralytics import YOLO

# Mount Google Drive (assuming you've already done this in a separate Colab cell)
# from google.colab import drive
# drive.mount('/content/drive')

# Specify the path to your YOLOv8 model file in Google Drive
v4_model_path = "./Model Source/v4_best.pt"  # Replace with your actual path

v8_model_path = "./Model Source/v8_best.pt"
v9_model_path = "./Model Source/v9_best.pt"
# Load the YOLOv8 model
v4_model = YOLO(v4_model_path)
v8_model = YOLO(v8_model_path)
v9_model = YOLO(v9_model_path)
# Define the image prediction function
def predict_image(image, model, msg):
    # No image preprocessing needed in this case

    # Make predictions using the YOLOv8 model
    results = model(image)

    # Process the predictions (e.g., convert tensors to images)
    for result in results:
        result.save(filename='result.jpg') # display to screen
        st.image("./Images Source/result.jpg", use_column_width=True,caption=msg)
    return results

# Define the Streamlit subpage
def image_prediction_subpage(uploaded_file):
    # st.title("Image Prediction with YOLOv8")

    # uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "png", "jpeg"])

    if uploaded_file is not None:
        image = Image.open(uploaded_file)

        col1, col2, col3, col4  = st.columns(4)

        with col1: 
          st.image(image, caption="Uploaded Image", use_column_width=True)

        with col2:
          msg = "Prediction Result with v4"
          prediction = predict_image(image, v4_model, msg)
        
        with col3:
          msg = "Prediction Result with v8"
          prediction = predict_image(image, v8_model,msg)

        with col4:
          msg = "Prediction Result with v9"
          prediction = predict_image(image, v9_model,msg)
        st.write("")

        return True

        
         
        

def main():
    st.set_page_config(page_title="Demo", page_icon="📈")
    st.title("Image Prediction with YOLOv8")

    uploaded_file = st.file_uploader("Choose image...", type=["jpg", "png", "jpeg"], accept_multiple_files=True)

    result = st.button('Start Evaluation')
    if result:
      st.markdown("<h1 style='text-align: center;'>Starting Evaluation Process</h1>", unsafe_allow_html=True)
      iterate = 1 
      if uploaded_file is None:
        st.write("""Please provide at least one image""") 
      for each_uploaded_file in uploaded_file: 
        centered_text = st.container()
        centered_text.markdown("""<h1 style="text-align: center; font-size: 1rem"> --- Iterate of Image: """ + str(iterate) + " --- </h1>", unsafe_allow_html=True)
        predict = image_prediction_subpage(each_uploaded_file)
        iterate +=1
      if predict is not None:
        st.write("""The image is done process """)
      else:
        st.write("""Error!!!""")


if __name__ == '__main__':
    main()