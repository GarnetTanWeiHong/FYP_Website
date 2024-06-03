import streamlit as st

def main():
    # Set the page configuration with a title and an icon
    st.set_page_config(page_title="References and Tools", page_icon="🧰")

    # Display the main header for the page
    st.write("# References and Tools")

    # Display the header in the sidebar
    st.sidebar.header("References and Tools")

    # Provide an introductory description of the page
    st.write(
        """This page showcases the references and tools that we used to create this product."""
    )

    # List the software tools used in the project
    st.write("## Software Tools")
    st.write("""Python (Programming Language)  
                Ultralytics  
                NumPy  
                PyTorch  
                TensorFlow  
                OpenCV  
                Streamlit  
                Matplotlib  
                Pillow  
                Pandas  
                Roboflow (Data Annotation)  
             """)
    
    # List the hardware tools used in the project
    st.write("## Hardware Tools")
    st.write("""
             Automated Optical Inspection Camera (Capture PCB Images)
             """)

    # List the platforms and development environments used in the project
    st.write("## Platforms and Development Environment")
    st.write("""Google Colab (Model Development)  
                Google Drive (Cloud Storage)  
                GitHub (Version Control System)  
                Jira (Project Tracking)  
            """)

    # List the references used in the project
    st.write("## References")
    st.write("""
             - Adibhatla, V. A., Chih, H., Hsu, C., Cheng, J., Abbod, M. F., & Shieh, J. (2021). Applying deep learning to defect detection in printed circuit boards via a newest model of you-only-look-once. Mathematical Biosciences and Engineering, 18(4), 4411–4428. https://doi.org/10.3934/mbe.2021223  
             - Analog Devices. (n.d.). Printed Circuit Board. https://www.analog.com/en/design-center/glossary/printed-circuit.html#:~:text=A%20printed%20circuit%20board%2C%20or,a%20working%20circuit%20or%20assembly  
             - Khosla, C., & Baljit Singh Saini. (2020, June 1). Enhancing Performance of Deep Learning Models with different Data Augmentation Techniques: A Survey. IEEE Conference Publication | IEEE Xplore. https://ieeexplore.ieee.org/abstract/document/9160048  
             - Ultralytics. (n.d.). Brief summary of YOLOv8 model structure · Issue #189 · ultralytics/ultralytics. GitHub. https://github.com/ultralytics/ultralytics/issues/189  
    """)

# Run the main function when the script is executed
if __name__ == '__main__':
    main()
