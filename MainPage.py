import streamlit as st

st.set_page_config(
    page_title="Main Page",
    page_icon="👋",
)

st.write("# Welcome to MDS16 Dashboard Demo! 👋")

st.sidebar.success("Select a page that you would like to view.")

st.markdown(
    """
This project is built for Monash Data Science Project. 

Team: MDS 16  
Project Manager: Lo Kai Hong  
Tech Lead: Garnet Tan Wei Hong  
Quality Assurance: Soon Zhen Xu  

Project Supervisor: Dr. Tan Chee Keong  
Project Industry Colaborator: ASPL 

The objective of this project is to overcome the issue of over-rejection rates prevalent in the PCB manufacturing industry.

The purpose of this website is to present our product and provide an explanation of its methodology. 
"""
)