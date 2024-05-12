import streamlit as st

st.set_page_config(
    page_title="Main Page",
    page_icon="👋",
)

st.write("# Welcome to MDS16 Dashboard Demo! 👋")

st.sidebar.success("Select a page that you would like to view.")

st.markdown(
"""
This is a demo for the Data Science Final Year Project by MDS16

**Team**: MDS 16  
**Project Manager**: Lo Kai Hong [[kloo0012@student.monash.edu]](mailto:kloo0012@student.monash.edu)  
**Tech Lead**: Garnet Tan Wei Hong [[gtan0033@student.monash.edu]](mailto:gtan0033@student.monash.edu)  
**Quality Assurance**: Soon Zhen Xu [[zsoo0009@student.monash.edu]](mailto:zsoo0009@student.monash.edu)  

**Project Supervisor**: Dr. Tan Chee Keong [[tan.cheekeong@monash.edu]](mailto:tan.cheekeong@monash.edu)  
**Project Industry Colaborator**: ASPL 

The objective of this project is to overcome the issue of over-rejection rates prevalent in the PCB manufacturing industry.

The purpose of this website is to present our product and provide an explanation of its methodology. 
"""
)