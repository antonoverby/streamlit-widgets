import streamlit as st
from st_pages import add_page_title, show_pages, Page, Section, add_indentation

'''
Use the page_layout function define things that every page should do. Instead of writing multiple lines of code at the beginning of each page, import and use the page_layout function.
'''

def page_layout():
    st.set_page_config(layout="wide")
    add_page_title()
    add_indentation()
    
   