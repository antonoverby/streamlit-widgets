import streamlit as st
from st_pages import Page, Section, show_pages
from app.utils import page_layout

col1, col2, col3  = st.columns(3)

with col1:
    st.write("")

with col2: 
    st.image("assets/aclogotransparent.png", use_column_width=True)

with col3:
    st.write("")
st.title("Welcome!")
st.text("Here's a place for a homepage")


 # Structure of Pages on the left sidebar. Be careful b/c adjustments may take a server reset. Switching a Page to Section method seems to trigger this
show_pages(
    [
        # Section("Home"),  
        Page("main.py", "Widgets Home"),
        # Section("Vizzes"),
        Page("pages/plotlyviz.py", "Plotly Vizzes"),
        # Section("Components"),
        Page("pages/progressbar.py", "Progress Bar")

    ]
    )


