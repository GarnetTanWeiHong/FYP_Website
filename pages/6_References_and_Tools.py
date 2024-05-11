import streamlit as st

def main():
    st.set_page_config(page_title="References and Tools", page_icon="🧰")

    st.write("# References and Tools")
    st.sidebar.header("References and Tools")
    st.write(
        """This page showcases the references and tools that we used to create this product."""
    )
    st.write("## Main Tools")

    st.write("""Python  
                Tensorflow (TRIQ)  
                Pytorch (Detectron2)   
                Numpy  
                Pandas  
                Streamlit  
                Matplotlib  
                PIL  
                OpenCV  
                Localtunnel  
                Tensorflow Board  
                Tensorflow Addons""")

    st.write("## Platforms and Development Environment")

    st.write("""Dataspell (Ubuntu)  
                Google Colab  
                Google Drive  
                Github""")

    st.write("## References")

    st.write("""
    You, J., & Korhonen, J. (2021, January 8). Transformer for Image Quality Assessment. arXiv.org. Retrieved September 18, 2022, from https://arxiv.org/abs/2101.01097

Yuxin Wu, Alexander Kirillov, Francisco Massa, Wan-Yen Lo, & Ross Girshick. (2019). Detectron2.

JCharis, J. (2020, August 18). How to run streamlit apps from colab. Medium. Retrieved September 18, 2022, from https://medium.com/@jcharistech/how-to-run-streamlit-apps-from-colab-29b969a1bdfc

Frumkin, A. (2022, February 21). Demo your model with Streamlit. Medium. Retrieved September 18, 2022, from https://towardsdatascience.com/demo-your-model-with-streamlit-a76011467dfb

Lin, H., Hosu, V., & Saupe, D. (2019). KADID-10k: A Large-scale Artificially Distorted IQA Database. In 2019 Tenth International Conference on Quality of Multimedia Experience (QoMEX) (pp. 1–3).

Lin, H., Hosu, V., & Saupe, D. (2020). DeepFL-IQA: Weak Supervision for Deep IQA Feature Learning. arXiv preprint arXiv:2001.08113.

V. Hosu, H. Lin, T. Sziranyi, & D. Saupe (2020). KonIQ-10k: An Ecologically Valid Database for Deep Learning of Blind Image Quality Assessment. IEEE Transactions on Image Processing, 29, 4041-4056.

Z. Sinno and A.C. Bovik, "Large-Scale Study of Perceptual Video Quality,” IEEE Transactions on Image Processing, vol. 28, no. 2, pp. 612-627, February 2019.

Z. Sinno and A.C. Bovik, "Large Scale Subjective Video Quality Study,” 2018 IEEE International Conference on Image Processing, Athens, Greece, October 2018.

Z. Sinno and A.C. Bovik, "LIVE Video Quality Challenge Database", Online: http://live.ece.utexas.edu/research/LIVEVQC/index.html, 2018.

Ponomarenko, N., Jin, L., Ieremeiev, O., Lukin, V., Egiazarian, K., Astola, J., Vozel, B., Chehdi, K., Carli, M., Battisti, F., & Jay Kuo, C.-C. (2015). Image database TID2013: Peculiarities, results and perspectives. Signal Processing: Image Communication, 30, 57–77. https://doi.org/10.1016/j.image.2014.10.009
    """)

if __name__ == '__main__':
    main()